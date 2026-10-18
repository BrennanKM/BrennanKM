# Scoreboard

| Field | Value |
|---|---|
| As of | 2026-10-18 03:57 ET (Sun) |
| Capital contributed | $130.00 ($30 start 10/18 + $100 deposit 10/18 ~03:56 ET) |
| Account equity | $130.00 |
| **Return on contributed capital** | **+0.00%** (this is the race number: compare % with Codex, not raw $, unless Codex also got +$100) |
| Cash | $130.00 ($30 reserved by resting ETH limit buy) |
| Trades closed | 0 |
| Win rate | n/a |
| Biggest win / loss | n/a / n/a |
| Open risk | If ETH fills: $30 position, stop at daily close < $2,240 ≈ −$1.47 (−1.1% of equity). |
| Survival floor | Equity < $50: stop and write postmortem.md (Mandate v2) |
| Goal / deadline | $200–300 by ~2026-11-18 (Mandate v2 in TRADER_PROMPT.md) |

## Account facts (verified 2026-10-18)
- Sizing: see Mandate v2 in TRADER_PROMPT.md (1–2 positions, 50–100% deployed when a setup qualifies, $20 min).
- Market context 10/16: SOX down 8 straight sessions (longest since 2008), −23.9% from its 6/22 high. Nasdaq worst week since Apr 2025. Earnings this week: NFLX 10/20 pm; TSLA, META, TXN, LRCX, IBM 10/21 pm. FOMC 10/28.
- Account type is **limited margin**, not cash. Good-faith violations don't apply the way the prompt assumed. The **pattern-day-trader limit does**: under $25k there's a cap of 3 day trades per rolling 5 business days. Stocks stay overnight-minimum by default; spend day trades only to cut a broken position.
- Options level: **none**. No options trades are possible until the user applies for Level 2 in the app.
- Trade approvals: off (`human_must_approve_trades: false`).
- Crypto: Market Maker Routing, ≈1.9% round-trip spread on majors on the weekend.
- Fractional shares: **market orders only**, regular hours. Limit orders (required under $5) must be whole shares.

## Open orders
| Asset | Side | Type | Size | Limit | TIF | Order id |
|---|---|---|---|---|---|---|
| ETH-USD | buy | limit | $30 (0.012738 ETH) | $2,355 | GTC | 6ad47bb7-284d-4f72-b839-148098c268ad |

## Next actions (check-ins read this first)
- **Mon 10/19 open:** QS is dropped. Don't re-enter unless there's a daily close above $4.25 AND the new pricing rule passes (see trades.md post-mortem). Act on the research agents' shortlists in trades.md / research notes. Run the scan below. Every catalyst trade needs the implied move checked first.
- **ETH (spot, resting):** kept as weekend flush coverage only. **Mon 10/19 open: if still unfilled, cancel it** and re-express any ETH view through ETHU (2x, penny spreads) per Mandate v2.
- **ETH:** if filled, place a GTC limit sell of the full quantity at $2,580. Check the daily close vs $2,240 (exit if below). Exit before 2pm ET 10/28 (FOMC) unless ≥ +5%. If unfilled by 10/27, cancel it: the setup is stale into FOMC.
- Robinhood option *quotes* return 403 on this account (no options level). Use Nasdaq's public chain to get implied moves.

## Saved scans
- `Sub-$5 catalyst movers` (147a794c-7f10-49f4-a139-9503be836066): stock, $1–5, mkt cap > $50M, 30-day relative volume > 2, 30-day avg volume > 500k. Returns 0 on weekends because relative volume needs a live session. Run Monday after 10:00 ET.
