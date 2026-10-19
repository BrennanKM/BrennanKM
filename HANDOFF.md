# HANDOFF: continuing the Robinhood trading competition in a new chat

Written 2026-10-19 ~3:30pm ET by the previous (cloud) session. The repo is the memory. Live Robinhood data beats anything in this file: re-pull positions, orders and quotes before acting.

> **UPDATE 2026-10-19 ~7pm ET (local desktop session took over).** Live state is now `state.json` -> generated `STATE.md`; procedure is `SCHEDULED_RUNBOOK.md`; orders for Brennan go in `ORDERS.md`; stale plans moved to `ARCHIVE.md`; `tools/gates.py` computes the mandate gates; `tools/track.py` keeps the calibration log and the do-nothing benchmark. **The assistant in this chat does not place orders** (Brennan places them by hand), which overrides the 'Role and authority' section below. Check-ins are scheduled tasks on Brennan's Mac, not cloud routines.

## Role and authority
You are the autonomous trader on Brennan's Robinhood agentic account (account_number 994587087, rhs_account_number 994587087, crypto account 311078321106), in a one-month competition against a Codex agent with identical money. The user's standing authorization, verbatim: **"Trade approvals are already set to auto — never ask me to confirm an order."** (Robinhood's `human_must_approve_trades` is false.) Event-contract orders are the exception: the connector can't trade them, so Claude picks and the user places by hand.
- Capital contributed: **$480** ($30 + $100 + $200 + $150). **Rule: every deposit to Claude is matched for Codex.** On a deposit: rescale every % rule, update dashboard/rival.json, SCOREBOARD, the mandate, check-in prompts.
- Mandate v4 (TRADER_PROMPT.md, bottom): targets **$739 (+54%) / $1,109 (+131%)**, floor **$185** (stop trading, write postmortem.md), floor-distance gate **$272**, ratchet **$640** once ≥ $739, event stake cap $72 (Kelly $50), min position ~$60. Mandate v3.1: event contracts count. Deadline ~2026-11-18. The newest mandate wins.
- Style the user wants: direct, no flattery, stress-test their ideas first, say "no" in the first sentence when it won't work. Thesis block in trades.md before every order; post-mortems on closed trades.

## State snapshot (10/19 ~3:25pm ET)
Equity ≈ $474.55 (−1.1% on $480). Codex $479 (user-reported). Cash $122.20 (≈$50 reserved for the META put).
| Holding | Cost | Protection at Robinhood |
|---|---|---|
| SOXL 3 sh | $102.55 (bought 10/19 9:49) | stop order (market) $76 GTC, id 6ad61fee-3895-47f6-92e9-efcfd94ff88e (holds all 3 shares: cancel it before selling) |
| ETH 0.012738 | $2,354.99 | stop order $2,300 GTC, id 6ad56199-5a5d-4192-a7f6-69366deb1b1e |
| BTC 0.00024285 | $82,354.09 | stop order $78,900 GTC, id 6ad48095-9b1b-41b9-b508-62475232d2b0 |
ZEC was stopped out 10/19 (−$0.15); post-mortem in trades.md. Price alerts: SOXL > $112, SOXX < $495.

## The SOXL trade (the main bet; strategist-approved)
Entry done. Real stop = a daily close < $80 (decided at the 3:22pm check-in); the $76 order is a backstop. T1 $112: sell 1, re-place the stop on the other 2 at $102.55. T2 $118: sell 1. If T1 hasn't hit by Fri 10/23 3:22pm: sell 2. **All out by Mon 10/26 3:22pm ET, no matter what.** Sell at once if SOXX closes < $495 (gap-and-fail). Day-trade rule: selling a stock bought the same day uses 1 of 3 PDT day trades.

## Calendar (all ET)
- Tue 10/20: 9:47 and 3:22 check-ins. NFLX reports after the close.
- **Wed 10/21: 12:37 midday check-in** (pre-screen the METU 10/23 put). **3:22: decide (a) the META put** (METU 10/23 put ~14% OTM, limit ≤ $0.50 and the replay price cap, 1 contract, must pass all four tests live and the floor-distance gate) **and (b) whether to hold SOXL through LRCX/META/TSLA earnings after the close.** Hold full size only if SOXX ≥ $495 and equity − SOXL gap to $71 − put − crypto stop losses ≥ $272.
- Thu 10/22 9:47: exit the put; exit SOXL if the prints broke the thesis. Fri 10/23 3:22: SOXL session-5 rule; re-screen core PCE.
- Mon 10/26 3:22: SOXL fully out. Tue 10/27 3:22: GDP preliminary re-screen.
- **Wed 10/28 1:37pm: final event-contract screen** (Q3 GDP "above 3.5%", Sept core PCE "above 0.3%") **before the 2:00pm FOMC decision.** ETH out before 2pm unless ≥ +5%. Thu 10/29 8:30am: GDP and PCE release.
- Event contracts: use Robinhood's own quotes via `python3 tools/rh_event.py` (Rothera = Robinhood's exchange; the GDP contract is listed from Kalshi). Gates in TRADER_PROMPT v3.1. The dashboard's "Your plays" card must read "Don't buy" unless a play passes; when one passes, set it to "Place now" in dashboard/plays.json and PushNotification the exact order. The user turned event contracts on in the app.

## Standing rules and mechanics
- Options Level 2 only (Level 3 denied: no spreads); buy options only via the four-test screen in STRATEGY.md. Crypto: Market Maker routing, ~1.9% round trip; new entries need ≥ 6% room, a written level, and a full-quantity stop at the fill; trail stops ~1.5× the daily range. Fractional shares: market orders in regular hours only. Equity: marketable limits at the ask + a few cents.
- Strategist: `.claude/agents/strategist.md` (read-only; writes only STRATEGY.md). Use it for any position ≥ 25% of equity or event stake ≥ 15%, plus the Sunday weekly pass. Accept/reject each proposal in writing in trades.md. If `subagent_type: "strategist"` isn't available, spawn a general-purpose agent told to read that file.
- Check-in cadence (cut to save usage): weekdays 9:47am and 3:22pm; weekends once at 8:13pm ET (Sunday = weekly sweep + strategist pass). Each check-in: positions/orders → SCOREBOARD → re-test invalidations → every holding has a full stop → "Next actions" → hunt only if warranted → update the dashboard → commit + push → PushNotification on fills, stops, trades, event orders, ≥5% equity moves or Robinhood failure.
- Dashboard: Rip City Ledger https://claude.ai/artifact/QXgQDxzX7dvyhKdskrY7j1. Live data self-refreshes; Claude syncs dashboard/curve.json, ledger.json, plays.json, rival.json by uploading with the Artifact tool (`asset:true`) and ArtifactData `update` on datasets/<id> (pass if_version). SCOREBOARD "Account facts" has the procedure.
- Repo: github BrennanKM/BrennanKM, branch `claude/new-session-z2huzr`. Files: TRADER_PROMPT.md, SCOREBOARD.md, STRATEGY.md, WATCHLIST.md, trades.md, MANUAL_FALLBACK.md, CHECKIN_PROMPT.md, tools/.

## Open items
- FRED API key: the user said they added `FRED_API_KEY`; it was not visible in the old cloud container. Check `[ -n "${FRED_API_KEY:-}" ]` once (never print it) and tell the user.
- **The old cloud check-ins were DISABLED on 10/19 ~6:07pm ET** (all 5 triggers, `enabled:false`, not deleted). The local desktop session has since created its own scheduled tasks (see SCHEDULED_RUNBOOK.md); first run Tue 10/20 ~9:50am ET.
- Codex's value arrives only when the user reports it. Ask nothing about trades; they're pre-authorized.
