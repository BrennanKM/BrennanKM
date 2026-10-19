#!/usr/bin/env python3
"""Calibration log + do-nothing benchmark.

Why: our edges are thin and model-based (n=15 backtests, blended nowcasts). If we never score our own
probabilities we are guessing with confident language. And if active management can't beat simply
holding the book, the check-ins are noise.

Calibration (calibration.csv)
  python3 tools/track.py cal add --id GDP35 --claim "Q3 GDP advance > 3.5%" --p 0.41 --market 0.42 \\
        --resolve-by 2026-10-29 --src STRATEGY.md
  python3 tools/track.py cal resolve --id GDP35 --outcome 1          # 1 = claim came true, 0 = it didn't
  python3 tools/track.py cal report
  p = OUR probability the claim is true. market = price/implied probability of the same claim (optional).
  Brier = (p - outcome)^2; always-50% scores 0.25, so lower than 0.25 means signal. Compare against market.

Benchmark (benchmark.csv): log one row at every CLOSE check-in (regular-session closes).
  python3 tools/track.py bench log --date 2026-10-20 --equity 470.6 --spy 770 --qqq 720 --soxl 101 --eth 2400 --btc 82000
  python3 tools/track.py bench report
  Compares the account against: SPY buy-and-hold, SOXL buy-and-hold, and the FROZEN BOOK (the 10/19-close
  holdings with no further decisions and no stops). Frozen book minus account = what our decisions added.
"""
import argparse, csv, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAL = ROOT / "calibration.csv"
BEN = ROOT / "benchmark.csv"
CAL_FIELDS = ["id", "logged", "claim", "p", "market", "resolve_by", "src", "outcome", "brier", "market_brier"]
BEN_FIELDS = ["date", "equity", "spy", "qqq", "soxl", "eth", "btc"]
# Holdings frozen at the 10/19 close (cash $122.20). Edit only if we deliberately re-base the benchmark.
FROZEN = {"cash": 122.20, "soxl": 3, "eth": 0.012738, "btc": 0.00024285}


def read(path):
    if not path.exists():
        return []
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def write(path, fields, rows):
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(rows)


# ---------- calibration ----------
def cal_add(a):
    rows = read(CAL)
    if any(r["id"] == a.id for r in rows):
        sys.exit(f"id {a.id} already exists; pick a new id (e.g. {a.id}-2) so history is never overwritten")
    if not 0 < a.p < 1:
        sys.exit("--p must be strictly between 0 and 1")
    rows.append(dict(id=a.id, logged=date.today().isoformat(), claim=a.claim, p=a.p, market=a.market if a.market is not None else "",
                     resolve_by=a.resolve_by or "", src=a.src or "", outcome="", brier="", market_brier=""))
    write(CAL, CAL_FIELDS, rows)
    print(f"logged {a.id}: p={a.p}")


def cal_resolve(a):
    rows = read(CAL)
    for r in rows:
        if r["id"] == a.id:
            if r["outcome"] != "":
                sys.exit(f"{a.id} already resolved ({r['outcome']}); not overwriting")
            o = int(a.outcome)
            r["outcome"] = o
            r["brier"] = round((float(r["p"]) - o) ** 2, 4)
            if r["market"] != "":
                r["market_brier"] = round((float(r["market"]) - o) ** 2, 4)
            write(CAL, CAL_FIELDS, rows)
            print(f"{a.id}: outcome {o}, Brier {r['brier']}" + (f" (market {r['market_brier']})" if r["market_brier"] != "" else ""))
            return
    sys.exit(f"no such id {a.id}")


def cal_report(_):
    rows = read(CAL)
    if not rows:
        print("calibration.csv is empty")
        return
    done = [r for r in rows if r["outcome"] != ""]
    print(f"{'id':12} {'p':>5} {'mkt':>5} {'resolve_by':>11} {'out':>4} {'brier':>6}  claim")
    for r in rows:
        print(f"{r['id']:12} {float(r['p']):>5.2f} {(r['market'] or '-'):>5} {r['resolve_by']:>11} {(r['outcome'] or '-'):>4} {(r['brier'] or '-'):>6}  {r['claim']}")
    print(f"\n{len(done)} resolved of {len(rows)} logged.")
    if done:
        mb = sum(float(r["brier"]) for r in done) / len(done)
        print(f"Mean Brier (ours): {mb:.3f}   [always-50%: 0.250; lower is better]")
        both = [r for r in done if r["market_brier"] != ""]
        if both:
            ours = sum(float(r["brier"]) for r in both) / len(both)
            mk = sum(float(r["market_brier"]) for r in both) / len(both)
            print(f"On the {len(both)} claims that have a market price: ours {ours:.3f} vs market {mk:.3f} -> "
                  + ("we beat the market" if ours < mk else "the market was better; our 'edge' is not showing up"))
        if len(done) < 10:
            print("n < 10: treat all of this as noise; do not claim calibration yet.")
    pend = [r for r in rows if r["outcome"] == "" and r["resolve_by"] and r["resolve_by"] <= date.today().isoformat()]
    if pend:
        print("\nDUE to resolve: " + ", ".join(r["id"] for r in pend))


# ---------- benchmark ----------
def frozen_value(r):
    return FROZEN["cash"] + FROZEN["soxl"] * float(r["soxl"]) + FROZEN["eth"] * float(r["eth"]) + FROZEN["btc"] * float(r["btc"])


def bench_log(a):
    rows = read(BEN)
    d = a.date or date.today().isoformat()
    rows = [r for r in rows if r["date"] != d]  # one row per date; re-logging a date replaces it
    rows.append(dict(date=d, equity=a.equity, spy=a.spy, qqq=a.qqq, soxl=a.soxl, eth=a.eth, btc=a.btc))
    rows.sort(key=lambda r: r["date"])
    write(BEN, BEN_FIELDS, rows)
    print(f"logged {d}")


def bench_report(_):
    rows = read(BEN)
    if len(rows) < 1:
        print("benchmark.csv is empty")
        return
    base = rows[0]
    e0 = float(base["equity"])
    print(f"Base {base['date']} (regular close): account {e0:.2f}. Benchmarks are scaled to the same start.")
    print(f"{'date':11} {'account':>9} {'frozen book':>12} {'SPY hold':>9} {'SOXL hold':>10}  {'decisions added':>16}")
    for r in rows:
        acct = float(r["equity"])
        frozen = frozen_value(r) * e0 / frozen_value(base)
        spy = e0 * float(r["spy"]) / float(base["spy"])
        soxl = e0 * float(r["soxl"]) / float(base["soxl"])
        print(f"{r['date']:11} {acct:>9.2f} {frozen:>12.2f} {spy:>9.2f} {soxl:>10.2f}  {acct - frozen:>+16.2f}")
    last = rows[-1]
    acct = float(last["equity"])
    frozen = frozen_value(last) * e0 / frozen_value(base)
    print(f"\nSince {base['date']}: decisions added {acct - frozen:+.2f} vs doing nothing; "
          f"vs SPY {acct - e0 * float(last['spy']) / float(base['spy']):+.2f}.")
    if len(rows) < 5:
        print("Fewer than 5 observations: this is noise, not a verdict.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="grp", required=True)
    c = sub.add_parser("cal").add_subparsers(dest="cmd", required=True)
    p = c.add_parser("add"); p.add_argument("--id", required=True); p.add_argument("--claim", required=True)
    p.add_argument("--p", type=float, required=True); p.add_argument("--market", type=float)
    p.add_argument("--resolve-by", dest="resolve_by"); p.add_argument("--src"); p.set_defaults(fn=cal_add)
    p = c.add_parser("resolve"); p.add_argument("--id", required=True); p.add_argument("--outcome", required=True, choices=["0", "1"]); p.set_defaults(fn=cal_resolve)
    p = c.add_parser("report"); p.set_defaults(fn=cal_report)
    b = sub.add_parser("bench").add_subparsers(dest="cmd", required=True)
    p = b.add_parser("log"); p.add_argument("--date")
    for k in ("equity", "spy", "qqq", "soxl", "eth", "btc"):
        p.add_argument(f"--{k}", type=float, required=True)
    p.set_defaults(fn=bench_log)
    p = b.add_parser("report"); p.set_defaults(fn=bench_report)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
