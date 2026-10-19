#!/usr/bin/env python3
"""Mandate gate calculator. Rules as arithmetic, not judgment.

Reads state.json (positions, stops, mandate numbers) and optional live overrides, prints PASS/FAIL
for every gate, and can regenerate STATE.md. Never talks to Robinhood: the caller passes live numbers.

Examples
  python3 tools/gates.py                                    # use the numbers stored in state.json
  python3 tools/gates.py --equity 468.77 --mark SOXL=98.675 --mark ETH=2403 --mark BTC=81997 --cash 122.2
  python3 tools/gates.py --premium 50                       # would a $50 option buy still clear the floor-distance gate?
  python3 tools/gates.py --event-stake 35                   # same for an event-contract stake
  python3 tools/gates.py --stop SOXL=3@76 --stop ETH=0.012738@2300   # override stops seen live (coverage check)
  python3 tools/gates.py --save --render                    # persist the marks to state.json and rebuild STATE.md
Exit code 1 if any hard gate FAILs (stop coverage, floor, floor-distance, event cap, PDT).
"""
import argparse, json, sys
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "state.json"
ET = ZoneInfo("America/New_York")
HOLIDAYS = set()  # NYSE closures inside the window; none before the 11/18 deadline (Thanksgiving is 11/26)


def is_bday(d):
    return d.weekday() < 5 and d.isoformat() not in HOLIDAYS


def bdays_between(start, end):
    """Business days after `start` up to and including `end` (0 on the start day)."""
    n, d = 0, start
    while d < end:
        d += timedelta(days=1)
        if is_bday(d):
            n += 1
    return n


def last_n_bdays(end, n):
    out, d = [], end
    while len(out) < n:
        if is_bday(d):
            out.append(d)
        d -= timedelta(days=1)
    return set(out)


def money(x):
    return f"${x:,.2f}"


def load():
    return json.loads(STATE.read_text())


def parse_kv(items, label):
    out = {}
    for it in items or []:
        if "=" not in it:
            sys.exit(f"--{label} expects SYM=value, got {it!r}")
        k, v = it.split("=", 1)
        out[k.upper()] = v
    return out


def compute(st, args):
    m = st["mandate"]
    now = datetime.fromisoformat(args.now).astimezone(ET) if args.now else datetime.now(ET)
    today = now.date()
    marks = parse_kv(args.mark, "mark")
    stops_over = parse_kv(args.stop, "stop")
    for p in st["positions"]:
        if p["sym"] in marks:
            p["mark"] = float(marks[p["sym"]])
        if p["sym"] in stops_over:
            qty, trig = stops_over[p["sym"]].split("@")
            p["backstop_stop"] = {**(p.get("backstop_stop") or {}), "qty": float(qty), "trigger": float(trig)}
    if args.cash is not None:
        st["cash"] = args.cash
    marked = st["cash"] + sum(p["qty"] * p["mark"] for p in st["positions"])
    equity = args.equity if args.equity is not None else st["equity"]
    premium = args.premium if args.premium is not None else st.get("premium_outstanding", 0)
    ev_stake = args.event_stake if args.event_stake is not None else st.get("event_stake_outstanding", 0)

    rows, gap_total = [], 0.0
    for p in st["positions"]:
        value = p["qty"] * p["mark"]
        pnl = value - p["qty"] * p["cost"]
        loss_rule = max(0.0, p["qty"] * (p["mark"] - p["rule_stop"]))
        loss_gap = max(0.0, p["qty"] * (p["mark"] - p["gap_price"]))
        gap_total += loss_gap
        bs = p.get("backstop_stop") or {}
        covered = bs.get("qty", 0) >= p["qty"] - 1e-12 and bs.get("trigger") is not None
        rows.append(dict(p=p, value=value, pnl=pnl, loss_rule=loss_rule, loss_gap=loss_gap, covered=covered))

    gate_level = m["floor_distance_gate"]
    ratchet_on = equity >= m["target_playoffs"]
    if ratchet_on:
        gate_level = max(gate_level, m["ratchet"])
    fd = equity - gap_total - premium - ev_stake

    d_glide = bdays_between(date.fromisoformat(m["glide_start"]), today)
    glide = m["glide_base"] * (1 + m["glide_rate"]) ** d_glide
    rival = st["rival"]["value"]

    pdt_window = last_n_bdays(today, 5)
    pdt_used = sum(1 for s in st.get("day_trades", []) if date.fromisoformat(s) in pdt_window)

    risk_on = sum(r["value"] for r in rows if r["p"].get("risk_on"))
    gates = []  # (name, ok, detail, hard)
    for r in rows:
        bs = r["p"].get("backstop_stop") or {}
        gates.append((f"stop coverage {r['p']['sym']}", r["covered"],
                      f"stop qty {bs.get('qty', 0)} vs position {r['p']['qty']} (trigger {bs.get('trigger')})", True))
    gates.append(("floor (stop trading below)", equity >= m["floor"], f"equity {money(equity)} vs floor {money(m['floor'])}", True))
    gates.append(("floor-distance gate", fd >= gate_level,
                  f"{money(equity)} - gaps {money(gap_total)} - premium {money(premium)} - event stake {money(ev_stake)} = {money(fd)} vs {money(gate_level)}"
                  + (" (ratchet level)" if ratchet_on else ""), True))
    gates.append(("event stake cap", ev_stake <= m["event_stake_cap"], f"{money(ev_stake)} vs cap {money(m['event_stake_cap'])} (Kelly cap {money(m['event_stake_kelly_cap'])} if model-dependent)", True))
    gates.append(("PDT day trades", pdt_used < m["pdt_max"] + 0, f"{pdt_used} used in last 5 business days (max {m['pdt_max']}); {m['pdt_max'] - pdt_used} left", True))
    worst = max(rows, key=lambda r: r["loss_rule"]) if rows else None
    if worst:
        pct = 100 * worst["loss_rule"] / equity
        gates.append(("max loss per trade <= 15%", pct <= m["max_loss_per_trade_pct"],
                      f"{worst['p']['sym']} loss at its rule stop {money(worst['loss_rule'])} = {pct:.1f}% of equity", False))
    gates.append(("mark vs reported equity", abs(marked - equity) <= max(2.0, 0.01 * equity),
                  f"marks+cash {money(marked)} vs equity {money(equity)} (diff {money(marked - equity)}); fix state.json if large", False))
    info = dict(
        today=today.isoformat(), equity=equity, d_glide=d_glide, glide=glide, vs_glide=equity - glide,
        vs_rival=equity - rival, behind=(equity < glide or equity < rival),
        ret_pct=100 * (equity / m["contributed"] - 1),
        to_playoffs=m["target_playoffs"] / equity - 1, to_title=m["target_title"] / equity - 1,
        risk_on_pct=100 * risk_on / equity, gap_total=gap_total, fd=fd, gate_level=gate_level,
        rows=rows, now=now,
    )
    return gates, info


def upcoming(st, now, hours=72, minimum=3):
    items = []
    for c in st["calendar"]:
        t = datetime.fromisoformat(f"{c['date']}T{c['time']}").replace(tzinfo=ET)
        items.append((t, c))
    items.sort(key=lambda x: x[0])
    fut = [(t, c) for t, c in items if t >= now - timedelta(hours=1)]
    near = [(t, c) for t, c in fut if t <= now + timedelta(hours=hours)]
    return near if len(near) >= minimum else fut[:minimum]


def report(st, gates, info):
    out = []
    pr = lambda s="": out.append(s)
    pr(f"GATES  {info['now'].strftime('%a %Y-%m-%d %H:%M ET')}  (trading day {info['d_glide']} of the glide path)")
    pr(f"Equity {money(info['equity'])}  return {info['ret_pct']:+.2f}% on {money(st['mandate']['contributed'])}  "
       f"| glide {money(info['glide'])} ({'BEHIND' if info['vs_glide'] < 0 else 'ahead'} {money(abs(info['vs_glide']))}) "
       f"| Codex {money(st['rival']['value'])} ({'BEHIND' if info['vs_rival'] < 0 else 'ahead'} {money(abs(info['vs_rival']))})")
    need = lambda x, tgt: f"+{100 * x:.0f}% to {money(tgt)}" if x > 0 else f"at/above {money(tgt)}"
    pr(f"Needs {need(info['to_playoffs'], st['mandate']['target_playoffs'])}, {need(info['to_title'], st['mandate']['target_title'])}. "
       f"Risk-on exposure (one correlated bet): {info['risk_on_pct']:.0f}% of equity. Event gate #1 'behind': {'YES' if info['behind'] else 'NO (ahead of both: protect the lead, no event bets)'}")
    pr("")
    pr(f"{'Position':8} {'qty':>12} {'mark':>11} {'value':>9} {'P&L':>8} {'rule-stop loss':>15} {'gap loss':>9}  stop")
    for r in info["rows"]:
        p = r["p"]
        bs = p.get("backstop_stop") or {}
        pr(f"{p['sym']:8} {p['qty']:>12g} {p['mark']:>11,.2f} {r['value']:>9.2f} {r['pnl']:>+8.2f} {r['loss_rule']:>15.2f} {r['loss_gap']:>9.2f}  "
           f"{bs.get('trigger')} x{bs.get('qty')} ({'covered' if r['covered'] else 'NOT COVERED'})")
    pr(f"{'Cash':8} {'':>12} {'':>11} {st['cash']:>9.2f}")
    pr("")
    bad = False
    for name, ok, detail, hard in gates:
        flag = "PASS" if ok else ("FAIL" if hard else "WARN")
        bad |= (not ok) and hard
        pr(f"[{flag}] {name}: {detail}")
    pr("")
    pr("Next dated actions:")
    for t, c in upcoming(st, info["now"]):
        pr(f"  {t.strftime('%a %m/%d %H:%M')} ET  {c['what']}")
    return "\n".join(out), bad


def render_state(st, gates, info, text):
    m = st["mandate"]
    L = []
    a = L.append
    a("# STATE (generated: do not edit; edit state.json, then `python3 tools/gates.py --render`)")
    a(f"As of {info['now'].strftime('%a %Y-%m-%d %H:%M ET')} · mandate {m['version']} · deadline {m['deadline']}")
    a("")
    a(f"**Equity {money(info['equity'])}** ({info['ret_pct']:+.2f}% on {money(m['contributed'])}) · cash {money(st['cash'])} · "
      f"glide {money(info['glide'])} ({'behind' if info['vs_glide'] < 0 else 'ahead'} {money(abs(info['vs_glide']))}) · "
      f"Codex {money(st['rival']['value'])} ({'behind' if info['vs_rival'] < 0 else 'ahead'} {money(abs(info['vs_rival']))}, as of {st['rival']['as_of']})")
    a(f"Targets {money(m['target_playoffs'])} / {money(m['target_title'])} · floor {money(m['floor'])} · floor-distance gate {money(m['floor_distance_gate'])} · ratchet {money(m['ratchet'])} once >= target 1 · event stake <= {money(m['event_stake_cap'])} ({money(m['event_stake_kelly_cap'])} if model-dependent)")
    a("")
    a("## Positions and protection")
    a("| Holding | Qty | Cost | Mark | P&L | Rule stop | Order at Robinhood | Notes |")
    a("|---|---|---|---|---|---|---|---|")
    for r in info["rows"]:
        p, bs = r["p"], r["p"].get("backstop_stop") or {}
        a(f"| {p['sym']} | {p['qty']:g} | {p['cost']:,.2f} | {p['mark']:,.2f} | {r['pnl']:+.2f} | {p['rule_stop_desc']} | {bs.get('type')} {bs.get('trigger')} x{bs.get('qty')} {str(bs.get('tif', '')).upper()} `{bs.get('id')}` | {p.get('note', '')} |")
    a("")
    a("## Price and time rules")
    for r in st["price_rules"]:
        a(f"- {r}")
    a("")
    a("## Gates (from tools/gates.py)")
    for name, ok, detail, hard in gates:
        a(f"- **{'PASS' if ok else ('FAIL' if hard else 'WARN')}** {name}: {detail}")
    a("")
    a("## Next dated actions (ET)")
    for t, c in upcoming(st, info["now"], hours=24 * 14, minimum=6):
        a(f"- {t.strftime('%a %m/%d %H:%M')}: {c['what']}")
    a("")
    a("## Event plays (user places by hand)")
    for pl in st["plays"]:
        a(f"- {pl['name']}: **{pl['status']}**. {pl['note']}")
    a("")
    a("## Standing rules")
    for r in st["rules"]:
        a(f"- {r}")
    a("")
    a("## Open items")
    for r in st["open_items"]:
        a(f"- {r}")
    a("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--equity", type=float)
    ap.add_argument("--cash", type=float)
    ap.add_argument("--mark", action="append", help="SYM=price (repeatable)")
    ap.add_argument("--stop", action="append", help="SYM=qty@trigger as seen live at Robinhood (repeatable)")
    ap.add_argument("--premium", type=float, help="option premium at risk (defaults to state.json)")
    ap.add_argument("--event-stake", type=float, dest="event_stake")
    ap.add_argument("--rival", type=float, help="Codex's latest reported value")
    ap.add_argument("--day-trade", action="append", dest="day_trade", help="YYYY-MM-DD of a day trade to record (with --save)")
    ap.add_argument("--now", help="ISO timestamp override for testing")
    ap.add_argument("--save", action="store_true", help="write marks/equity/cash/rival back into state.json")
    ap.add_argument("--render", action="store_true", help="rewrite STATE.md")
    args = ap.parse_args()

    st = load()
    if args.rival is not None:
        st["rival"]["value"] = args.rival
    gates, info = compute(st, args)
    text, bad = report(st, gates, info)
    print(text)
    if args.save:
        if args.equity is not None:
            st["equity"] = args.equity
        if args.day_trade:
            st.setdefault("day_trades", []).extend(args.day_trade)
        st["as_of"] = info["now"].astimezone(ZoneInfo("UTC")).strftime("%Y-%m-%dT%H:%M:%SZ")
        if args.premium is not None:
            st["premium_outstanding"] = args.premium
        if args.event_stake is not None:
            st["event_stake_outstanding"] = args.event_stake
        STATE.write_text(json.dumps(st, indent=2) + "\n")
        print("\nsaved state.json")
    if args.render:
        (ROOT / "STATE.md").write_text(render_state(st, gates, info, text))
        print("wrote STATE.md")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
