# Scoreboard

| Field | Value |
|---|---|
| As of | 2026-10-18 17:21 ET (Sun) |
| Capital contributed | $130.00 ($30 start 10/18 + $100 deposit 10/18 ~03:56 ET) |
| Account equity | $128.95 · **Codex: $134.00 (+3.1%), we trail by $5.05** (user-reported 17:20 ET) |
| **Return on contributed capital** | **−0.81%** |
| Cash | $60.01, all free (no resting buys); crypto held ≈ $69 |
| Trades closed | 0 |
| Win rate | n/a |
| Biggest win / loss | n/a / n/a |
| Open risk | BTC $20 → stop ≈ −$0.84 (+ spread). If all limits fill: ETH stop ≈ −$1.47, SOL stop ≈ −$0.68. Max sleeve loss ≈ $3.5 (2.7%). |
| Survival floor | Equity < $50: stop and write postmortem.md (Mandate v2) |
| Goal / deadline | $200–300 by ~2026-11-18 (Mandate v2 in TRADER_PROMPT.md) |

## Account facts (verified 2026-10-18)
- Crypto routing: **Market Maker Routing** (user turned Fee Tiers / Exchange Routing off 10/18). Spread ≈ 1.9% round trip, so resting limits are the default entry.
- Fresh-session check-ins (one new session per check-in) can't be created from Claude's session: they'd run without the Robinhood connector. The standalone prompt is in CHECKIN_PROMPT.md for the user to paste into a claude.ai routine with Robinhood attached. Until then, check-ins run in the original session.
- Check-ins: weekdays 9:47am & 3:22pm ET, weekends 12:13pm & 8:13pm ET. Each push-notifies on fills, stops, trades, triggers, ±5% moves, or a Robinhood failure.
- Sizing: see Mandate v2 in TRADER_PROMPT.md (1–2 positions, 50–100% deployed when a setup qualifies, $20 min).
- Market context 10/16: SOX down 8 straight sessions (longest since 2008), −23.9% from its 6/22 high. Nasdaq worst week since Apr 2025. Earnings this week: NFLX 10/20 pm; TSLA, META, TXN, LRCX, IBM 10/21 pm. FOMC 10/28.
- Account type is **limited margin**, not cash. Good-faith violations don't apply the way the prompt assumed. The **pattern-day-trader limit does**: under $25k there's a cap of 3 day trades per rolling 5 business days. Stocks stay overnight-minimum by default; spend day trades only to cut a broken position.
- Options level: **option_level_2, WORKING** (verified 2026-10-18 17:30 ET: `get_option_quotes` and `review_option_order` both succeed; fees ≈ $0.04/contract; account shows Gold). Reality check: most liquid options cost $100s per contract (TSLA ATM 10/23 call = $1,310). At $130, options are only usable as cheap OTM contracts (≤ ~$0.60 premium = ≤ $60) for event convexity. Before any catalyst trade, compare the option against the 2x/3x ETF.
- Trade approvals: off (`human_must_approve_trades: false`).
- Crypto: Market Maker Routing, ≈1.9% round-trip spread on majors on the weekend.
- Fractional shares: **market orders only**, regular hours. Limit orders (required under $5) must be whole shares.

## Open positions
| Asset | Qty | Avg cost | Stop | Target | Notes |
|---|---|---|---|---|---|
| ZEC | 0.01798 | ≈$1,111.8 ($19.99) | stop order $1,020 GTC (id 6ad4f058-34ac-42f7-9261-e1bca53bf035) | $1,200 | crypto sleeve, trend leader; both halves filled |
| ETH | 0.012738 | $2,354.99 ($30) | stop order $2,240 GTC (id 6ad5384a-fb70-4e3c-9ac0-a48f5008badc) | $2,580 | out before FOMC 10/28 2pm unless ≥ +5% |
| BTC | 0.00024285 | $82,354.09 ($20) | stop order $78,900 GTC (id 6ad48095-9b1b-41b9-b508-62475232d2b0) | $85,000 (set a sell limit at a check-in if within ~1.5%; cancel the stop first) | crypto sleeve |

## Open orders
| Asset | Side | Type | Size | Price | TIF | Order id |
|---|---|---|---|---|---|---|
| ETH | sell | stop order | 0.012738 | trigger $2,240 | GTC | 6ad5384a-fb70-4e3c-9ac0-a48f5008badc |
| BTC | sell | stop order | 0.00024285 | trigger $78,900 | GTC | 6ad48095-9b1b-41b9-b508-62475232d2b0 |
| ZEC | sell | stop order | 0.01798 | trigger $1,020 | GTC | 6ad4f058-34ac-42f7-9261-e1bca53bf035 |

## Next actions (check-ins read this first)
- **Strategy discipline (10/18 review):** fewer, bigger, better trades. Each small crypto round trip costs ~1.9% (≈ $0.40 on $20), so no new crypto trade unless it clears 3x spread with a defined level. Capital goes to the dated catalysts (SOXL trigger, META 10/21, the Sunday-sweep picks).
- **Dashboard "The Iron Ledger"** (https://claude.ai/artifact/QXgQDxzX7dvyhKdskrY7j1): positions, orders, quotes and account value are live Robinhood queries. At EVERY check-in: (1) append `{at, equity, contributed, note}` to `dashboard/curve.json` from get_portfolio; (2) sync `dashboard/ledger.json` with trades.md (status, fills, lessons; keep the house names); (3) upload both with Artifact publish `asset:true` to that url, then ArtifactData `update` datasets/curve and datasets/ledger with the new `source.url` and `updated:{at,by:"Claude"}`. Also read data/users/me/check once and fix any page error it names.
- **No resting buys** (SOL and the BTC add were cancelled 10/18 to close unprotected-fill gaps). Cash $60 is earmarked for SOXL (needs ~$90; sell crypto to top up if it triggers).
- **Alerts:** Robinhood price alerts are live (see trades.md, 10/18 17:25). Update or delete them when stops or targets change.
- **Crypto sleeve:** ZEC fully filled with the stop re-sized (done 10/18 12:14). If SOL fills, place a GTC stop order at $95. Weekend/weekday checks: BTC ≥ $84,600 → cancel the stop and place a sell limit at $85,000. **If SOXL triggers and cash is < $90, sell sleeve positions first.**
- **PRIMARY: SOXL reversal trigger, checked at EVERY 3:22pm check-in from Mon 10/19.** Get SOXX/SOXL quotes vs prior close (SOX proxy: SOXX; 11,100 ≈ SOXX $490). Trigger = (a) the session traded below 11,100 / SOXX $490 and is now green, OR (b) SOX/SOXX ≥ +2% on the day after 8 down sessions. If triggered and SOXL is in $85–95: write the fill into trades.md and buy ~70% of equity with a marketable limit. Then set the stop rule (daily close < $80) and the T1 sell-half at $110. No trigger means no trade. **Do not buy at the 9:47 open check-in.**
- **Wed 10/21 3:22pm:** METU variance bet per trades.md (only if META ≥ $700 and SOX isn't at new lows). Exit Thu 10/22 at the open.
- **Mon 10/19 open:** QS is dropped. Don't re-enter unless there's a daily close above $4.25 AND the new pricing rule passes (see trades.md post-mortem). Act on the research agents' shortlists in trades.md / research notes. Run the scan below. Every catalyst trade needs the implied move checked first.
- **ETH:** filled 10/18 15:40 ET with its stop placed. Manage: sell limit at $2,580; exit before FOMC 10/28 2pm unless ≥ +5%.
- **Rival:** when the user reports Codex's value, update dashboard/rival.json, upload it, and update datasets/rival.
- **ETH:** if filled, place a GTC limit sell of the full quantity at $2,580. Check the daily close vs $2,240 (exit if below). Exit before 2pm ET 10/28 (FOMC) unless ≥ +5%. If unfilled by 10/27, cancel it: the setup is stale into FOMC.
- **Options are live.** For the SOXL trigger and the META earnings bet, price a cheap OTM call (≤ $0.60) next to the leveraged ETF and pick whichever gives better payoff per dollar risked. Write both in the thesis block.

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
