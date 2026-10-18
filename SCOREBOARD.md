# Scoreboard

| Field | Value |
|---|---|
| As of | 2026-10-18 03:57 ET (Sun) |
| Capital contributed | $130.00 ($30 start 10/18 + $100 deposit 10/18 ~03:56 ET) |
| Account equity | $130.00 |
| **Return on contributed capital** | **+0.00%** (this is the race number: compare % with Codex, not raw $, unless Codex also got +$100) |
| Cash | $100.00 (ETH $30 + SOL $15 + ZEC $10 limits reserved → ~$45 free; BTC $20 + ZEC $10 held) |
| Trades closed | 0 |
| Win rate | n/a |
| Biggest win / loss | n/a / n/a |
| Open risk | BTC $20 → stop ≈ −$0.84 (+ spread). If all limits fill: ETH stop ≈ −$1.47, SOL stop ≈ −$0.68. Max sleeve loss ≈ $3.5 (2.7%). |
| Survival floor | Equity < $50: stop and write postmortem.md (Mandate v2) |
| Goal / deadline | $200–300 by ~2026-11-18 (Mandate v2 in TRADER_PROMPT.md) |

## Account facts (verified 2026-10-18)
- Sizing: see Mandate v2 in TRADER_PROMPT.md (1–2 positions, 50–100% deployed when a setup qualifies, $20 min).
- Market context 10/16: SOX down 8 straight sessions (longest since 2008), −23.9% from its 6/22 high. Nasdaq worst week since Apr 2025. Earnings this week: NFLX 10/20 pm; TSLA, META, TXN, LRCX, IBM 10/21 pm. FOMC 10/28.
- Account type is **limited margin**, not cash. Good-faith violations don't apply the way the prompt assumed. The **pattern-day-trader limit does**: under $25k there's a cap of 3 day trades per rolling 5 business days. Stocks stay overnight-minimum by default; spend day trades only to cut a broken position.
- Options level: **option_level_2** (approved 2026-10-18). BUT `get_option_quotes` and `review_option_order` both return **403** right after approval. Instrument lookup works. Likely a propagation delay or an unaccepted agreement / agent-options permission in the app. Retry at each check-in; until it works, use the Nasdaq public chain for implied moves and leveraged ETFs for exposure.
- Trade approvals: off (`human_must_approve_trades: false`).
- Crypto: Market Maker Routing, ≈1.9% round-trip spread on majors on the weekend.
- Fractional shares: **market orders only**, regular hours. Limit orders (required under $5) must be whole shares.

## Open positions
| Asset | Qty | Avg cost | Stop | Target | Notes |
|---|---|---|---|---|---|
| ZEC | 0.00881 | $1,134.45 ($10) | stop order $1,020 GTC (id 6ad48150-410b-42e3-b573-e20fdcc2ecb4) | $1,200 | crypto sleeve, trend leader; dip-add limit at $1,090 |
| BTC | 0.00024285 | $82,354.09 ($20) | stop order $78,900 GTC (id 6ad48095-9b1b-41b9-b508-62475232d2b0) | $85,000 (set a sell limit at a check-in if within ~1.5%; cancel the stop first) | crypto sleeve |

## Open orders
| Asset | Side | Type | Size | Price | TIF | Order id |
|---|---|---|---|---|---|---|
| ETH-USD | buy | limit | $30 (0.012738 ETH) | $2,355 | GTC | 6ad47bb7-284d-4f72-b839-148098c268ad |
| SOL-USD | buy | limit | $15 (0.15075 SOL) | $99.50 | GTC | 6ad4808a-abfc-421d-ad10-41034f09ba53 |
| BTC | sell | stop order | 0.00024285 | trigger $78,900 | GTC | 6ad48095-9b1b-41b9-b508-62475232d2b0 |
| ZEC-USD | buy | limit | $10 (0.00917 ZEC) | $1,090 | GTC | 6ad48148-d42f-4e3a-8873-4814655cfda4 |
| ZEC | sell | stop order | 0.00881 | trigger $1,020 | GTC | 6ad48150-410b-42e3-b573-e20fdcc2ecb4 |

## Next actions (check-ins read this first)
- **Crypto sleeve:** if the ZEC $1,090 limit fills, cancel the ZEC stop and re-place it for the full quantity at $1,020. If SOL fills, place a GTC stop order at $95. Weekend/weekday checks: BTC ≥ $84,600 → cancel the stop and place a sell limit at $85,000. **If SOXL triggers and cash is < $90, sell sleeve positions first.**
- **PRIMARY: SOXL reversal trigger, checked at EVERY 3:22pm check-in from Mon 10/19.** Get SOXX/SOXL quotes vs prior close (SOX proxy: SOXX; 11,100 ≈ SOXX $490). Trigger = (a) the session traded below 11,100 / SOXX $490 and is now green, OR (b) SOX/SOXX ≥ +2% on the day after 8 down sessions. If triggered and SOXL is in $85–95: write the fill into trades.md and buy ~70% of equity with a marketable limit. Then set the stop rule (daily close < $80) and the T1 sell-half at $110. No trigger means no trade. **Do not buy at the 9:47 open check-in.**
- **Wed 10/21 3:22pm:** METU variance bet per trades.md (only if META ≥ $700 and SOX isn't at new lows). Exit Thu 10/22 at the open.
- **Mon 10/19 open:** QS is dropped. Don't re-enter unless there's a daily close above $4.25 AND the new pricing rule passes (see trades.md post-mortem). Act on the research agents' shortlists in trades.md / research notes. Run the scan below. Every catalyst trade needs the implied move checked first.
- **ETH (spot, resting):** kept as weekend flush coverage only. **Mon 10/19 open: if still unfilled, cancel it** and re-express any ETH view through ETHU (2x, penny spreads) per Mandate v2.
- **ETH:** if filled, place a GTC limit sell of the full quantity at $2,580. Check the daily close vs $2,240 (exit if below). Exit before 2pm ET 10/28 (FOMC) unless ≥ +5%. If unfilled by 10/27, cancel it: the setup is stale into FOMC.
- **Options:** retry `review_option_order` (1 lot, TSLA 10/23 $355C id 1d90fde3-84c7-4b46-97a9-5893cdb900c6, $0.50 limit, review only) to see whether the 403 has cleared. If it still 403s on Mon, tell the user.
- Robinhood option *quotes* return 403 on this account (no options level). Use Nasdaq's public chain to get implied moves.

## Watchlist: earnings setups (research agent, 2026-10-18; no orders yet)
Small-cap tape is risk-off (IWM at a 3-month low, RSI 32). Each name below is clean on dilution (no S-1/S-3/424B since 7/1) and heavily shorted. Two entries are possible: (a) a small position before the print, or (b) a resting limit ~1x the implied move below price to catch a post-print flush. Weight (b) at least equally: SOFI and AMKR won back most of their last earnings drops within 5 days.
| Ticker | Px 10/16 | Catalyst | Implied move | SI % float | Entry (a) | Stop | Target |
|---|---|---|---|---|---|---|---|
| MBLY | $7.22 | Q3, Thu 10/29 before open | ±14% | 26.7% (7.7 days to cover) | 4 sh @ $7.10 | close < $6.15 | $8.30–8.50 |
| SOFI | $14.55 | Q3, Tue 10/27 before open | ±11% | 17% | 2 sh @ $14.35 | $12.85 | $16.50–17.00 |
| AMKR | $41.82 | Q3, Mon 10/26 after close | ±15.6% | 17.7% (2.3 days to cover) | 1 sh @ $41.50 | $35 | $48–50 |
Notes: AMKR is a semi, so don't stack it with a SOXL position. Revisit entries Thu 10/22 to Mon 10/26, after this week's mega-cap prints set the tone. Rejected: INO (sub-$1, raised cash 7/29), IONS (approval ~85% and priced in), IRD (catalyst spent), JBLU/BBAI/ENVX (debt or serial dilution), CLF (reports before Monday's open).

## Saved scans
- `Sub-$5 catalyst movers` (147a794c-7f10-49f4-a139-9503be836066): stock, $1–5, mkt cap > $50M, 30-day relative volume > 2, 30-day avg volume > 500k. Returns 0 on weekends because relative volume needs a live session. Run Monday after 10:00 ET.
