# Scoreboard

| Field | Value |
|---|---|
| As of | 2026-10-18 03:47 ET (Sun) |
| Account equity | $30.00 |
| vs $30 start | +0.00% |
| Cash | $30.00 (QS order cancelled pre-entry after red-team review) |
| Trades closed | 0 |
| Win rate | n/a |
| Biggest win / loss | n/a / n/a |
| Open risk | None. 100% cash. |

## Account facts (verified 2026-10-18)
- Account type is **limited margin**, not cash. Good-faith violations don't apply the way the prompt assumed. The **pattern-day-trader limit does**: under $25k there's a cap of 3 day trades per rolling 5 business days. Stocks stay overnight-minimum by default; spend day trades only to cut a broken position.
- Options level: **none**. No options trades are possible until the user applies for Level 2 in the app.
- Trade approvals: off (`human_must_approve_trades: false`).
- Crypto: Market Maker Routing, ≈1.9% round-trip spread on majors on the weekend.
- Fractional shares: **market orders only**, regular hours. Limit orders (required under $5) must be whole shares.

## Open orders
None.

## Next actions (check-ins read this first)
- **Mon 10/19 open:** QS is dropped. Don't re-enter unless there's a daily close above $4.25 AND the new pricing rule passes (see trades.md post-mortem). Act on the research agents' shortlists in trades.md / research notes. Run the scan below. Every catalyst trade needs the implied move checked first.
- Robinhood option *quotes* return 403 on this account (no options level). Use Nasdaq's public chain to get implied moves.

## Saved scans
- `Sub-$5 catalyst movers` (147a794c-7f10-49f4-a139-9503be836066): stock, $1–5, mkt cap > $50M, 30-day relative volume > 2, 30-day avg volume > 500k. Returns 0 on weekends because relative volume needs a live session. Run Monday after 10:00 ET.
