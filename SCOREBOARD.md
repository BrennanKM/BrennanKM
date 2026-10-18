# Scoreboard

| Field | Value |
|---|---|
| As of | 2026-10-18 03:47 ET (Sun) |
| Account equity | $30.00 |
| vs $30 start | +0.00% |
| Cash | $30.00 (QS limit buy of ~$20.40 queued for Mon open) |
| Trades closed | 0 |
| Win rate | n/a |
| Biggest win / loss | n/a / n/a |
| Open risk | Pending QS 5 sh @ ≤$4.08. If filled, stop-out at $3.75 costs ≈ -$1.65 (-5.5% of equity); a -15% earnings gap costs ≈ -$3.06 (-10%). |

## Account facts (verified 2026-10-18)
- Account type is **limited margin**, not cash. Good-faith violations don't apply the way the prompt assumed. The **pattern-day-trader limit does**: under $25k there's a cap of 3 day trades per rolling 5 business days. Stocks stay overnight-minimum by default; spend day trades only to cut a broken position.
- Options level: **none**. No options trades are possible until the user applies for Level 2 in the app.
- Trade approvals: off (`human_must_approve_trades: false`).
- Crypto: Market Maker Routing, ≈1.9% round-trip spread on majors on the weekend.
- Fractional shares: **market orders only**, regular hours. Limit orders (required under $5) must be whole shares.

## Open orders
| Symbol | Side | Type | Qty | Limit | TIF | Order id |
|---|---|---|---|---|---|---|
| QS | buy | limit | 5 | $4.08 | Mon 10/19 (day) | 6ad47993-83c0-4617-90b0-5b5ce48ebbfe |

## Saved scans
- `Sub-$5 catalyst movers` (147a794c-7f10-49f4-a139-9503be836066): stock, $1–5, mkt cap > $50M, 30-day relative volume > 2, 30-day avg volume > 500k. Returns 0 on weekends because relative volume needs a live session. Run Monday after 10:00 ET.
