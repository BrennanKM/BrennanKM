# Scoreboard

| Field | Value |
|---|---|
| As of | 2026-10-19 18:05 ET (handover reconcile; SOXL closed $98.675, SOXX $502.03) |
| Capital contributed | **$480.00** ($30 + $100 + $200 + $150 on 10/19 ~00:30 ET; Codex gets every deposit too, a standing rule) |
| Account equity | $470.64 · Codex $479 (user report 10/19 PM; we trail by ~$8.36) |
| **Return on contributed capital** | **−1.95%** (−$9.36 on $480) |
| Cash | $122.20 (incl. $19.84 from the ZEC stop); stocks $297.90 (after-hours bid); crypto $50.54 |
| Trades closed | 1 (ZEC, −$0.15) |
| Win rate | n/a |
| Biggest win / loss | n/a / n/a |
| Open risk | Computed by `python3 tools/gates.py` (floor-distance, loss at rule stops, gap losses); see STATE.md |
| Survival floor | Equity < **$185**: stop and write postmortem.md (Mandate v4) |
| Goal / deadline | **$739 (+54%) / $1,109 (+131%)** by ~2026-11-18 (Mandate v4 in TRADER_PROMPT.md) |

## Account facts (verified 2026-10-18)
- Crypto routing: **Market Maker Routing** (user turned Fee Tiers / Exchange Routing off 10/18). Spread ≈ 1.9% round trip, so resting limits are the default entry.
- Check-ins run as scheduled tasks in the Claude desktop app on Brennan's Mac (Pacific time; they run only while the Mac is awake and the app is open). All procedure is in SCHEDULED_RUNBOOK.md. The assistant does not place orders: it writes them to ORDERS.md and push-notifies; Brennan places them.
- Check-ins (cut 10/19 to save usage): weekdays 9:47am & 3:22pm ET, weekends once at 8:13pm ET (Sunday = weekly sweep + strategist). No routine Wednesday strategist pass; pre-trade reviews still run. Extra one-off check-ins: **Wed 10/21 12:37pm** (earnings day: pre-screens the METU put) and **Wed 10/28 1:37pm** (before the 2pm FOMC decision). Each push-notifies on fills, stops, trades, triggers, ±5% moves, or a Robinhood failure.
- Sizing: see Mandate v2 in TRADER_PROMPT.md (1–2 positions, 50–100% deployed when a setup qualifies, $20 min).
- Market context 10/16: SOX down 8 straight sessions (longest since 2008), −23.9% from its 6/22 high. Nasdaq worst week since Apr 2025. Earnings this week: NFLX 10/20 pm; TSLA, META, TXN, LRCX, IBM 10/21 pm. FOMC 10/28.
- Account type is **limited margin**, not cash. Good-faith violations don't apply the way the prompt assumed. The **pattern-day-trader limit does**: under $25k there's a cap of 3 day trades per rolling 5 business days. Stocks stay overnight-minimum by default; spend day trades only to cut a broken position.
- Options level: **option_level_2, WORKING** (verified 2026-10-18 17:30 ET: `get_option_quotes` and `review_option_order` both succeed; fees ≈ $0.04/contract; account shows Gold). Reality check: most liquid options cost $100s per contract (TSLA ATM 10/23 call = $1,310). At $130, options are only usable as cheap OTM contracts (≤ ~$0.60 premium = ≤ $60) for event convexity. Before any catalyst trade, compare the option against the 2x/3x ETF.
- **Options Level 3: user is INELIGIBLE (10/19).** No spreads. The Level 2 toolkit is long calls/puts, two separate long legs (strangle/straddle), covered calls (needs 100 shares) and cash-secured puts (needs strike×100 cash, so strikes ≤ ~$3). Don't plan around spreads.
- Trade approvals: off (`human_must_approve_trades: false`).
- Crypto: Market Maker Routing, ≈1.9% round-trip spread on majors on the weekend.
- Fractional shares: **market orders only**, regular hours. Limit orders (required under $5) must be whole shares.

## Open positions
| Asset | Qty | Avg cost | Stop | Target | Notes |
|---|---|---|---|---|---|
| SOXL | 3 | $102.55 ($307.65) | Rule: daily close < $80 (decided at 3:22). Hard backstop: stop order $76 GTC (id 6ad61fee-3895-47f6-92e9-efcfd94ff88e) | T1 $112 (sell 1, stop → entry), T2 $118 | Bought 10/19 9:49. Time stop: sell 2 by Fri 10/23 3:22 if T1 not hit; all out Mon 10/26 3:22. Alerts: SOXL > $112, SOXX < $495 |
| ETH | 0.012738 | $2,354.99 ($30) | stop order $2,300 GTC (id 6ad56199-5a5d-4192-a7f6-69366deb1b1e) | $2,580 | out before FOMC 10/28 2pm unless ≥ +5% |
| BTC | 0.00024285 | $82,354.09 ($20) | stop order $78,900 GTC (id 6ad48095-9b1b-41b9-b508-62475232d2b0) | $85,000 (set a sell limit at a check-in if within ~1.5%; cancel the stop first) | crypto sleeve |

## Open orders
| Asset | Side | Type | Size | Price | TIF | Order id |
|---|---|---|---|---|---|---|
| SOXL | sell | stop order (market) | 3 | trigger $76 | GTC | 6ad61fee-3895-47f6-92e9-efcfd94ff88e |
| ETH | sell | stop order | 0.012738 | trigger $2,300 | GTC | 6ad56199-5a5d-4192-a7f6-69366deb1b1e |
| BTC | sell | stop order | 0.00024285 | trigger $78,900 | GTC | 6ad48095-9b1b-41b9-b508-62475232d2b0 |

## Next actions (live rules only; positions, stops, price rules and the dated calendar are in STATE.md / state.json)
- **Read order for every check-in:** STATE.md, then `python3 tools/gates.py` with live numbers, then the mandate at the bottom of TRADER_PROMPT.md, then only the files today's calendar item needs. History is in ARCHIVE.md.
- **Execution:** the assistant does not place orders. Write the thesis to trades.md, then the exact order (cancel-first ids included) for the user, and PushNotification "ORDER for you: ...". Log every probability used with `tools/track.py cal add`.
- **Keep MANUAL_FALLBACK.md current** whenever a position, stop or exit date changes.
- **Event contracts (Claude picks, user places).** Quotes: `python3 tools/rh_event.py <category>/events/<slug>` (or `--list economics`); use Robinhood's prices, not Kalshi's, and skip any contract flagged NOT TRADABLE ON RH. Gates: behind glide path or Codex, 30-70c, edge >= 5 pts after costs against an independent model, floor-distance gate, strategist review if stake >= 15% of equity. To trade: thesis + exact order in trades.md, PushNotification, set the play to "Place now" in dashboard/plays.json, record the user's fill.
  - **Q3 GDP > 3.5% YES** (Kalshi KXGDP-26OCT30; release Thu 10/29 8:30 ET; RH lists >3.0/3.5/4.0): locked model 50% GDPNow / 25% NY Fed / 25% bank trackers, sigma 1.1 (1.0 on the final day). Max price = model P - 0.07. Stake ~ $25, cap $35. Fees ~ $0.02/contract. 10/19 PM RH 39/42c vs model ~41%: no edge. Re-screen Tue 10/27 3:22pm; final go/no-go Wed 10/28 1:37pm (3:22pm if GDPNow hasn't updated after the 8:30 trade/inventories data).
  - **Sept core PCE > 0.3 (Rothera ECPCE-26SEPCORE; YES needs a printed 0.4+)**: center 0.33, sigma 0.04, P(YES) 0.31. Pass lines: center <= 0.325 -> buy NO, limit <= 65c; center >= 0.345 -> buy YES, limit <= 37c. Stake ~ $30, limit orders only (OI 35), partial fills OK. Re-screen Fri 10/23 3:22pm; final 10/28 1:37pm.
  - **Fed Oct 28:** no bet (hike 14/15c vs futures 16%).
  - Combined event stake: <= $72 cap, <= $50 when the edge is model-dependent (Kelly cap).
- **METU 10/23 put (Wed 10/21 3:22pm decision; midday pre-screen at 12:37).** 1 contract. Limit = lowest of mid, the replay price cap (recompute live; ~$0.60 for the 25P at METU $29.00, ~$0.47 at $29.50) and $0.50. Re-pick the strike so the spread is <= 40% of mid and OI >= 100; skip if the 10/23 META straddle is > 9.5% of price. Must clear the floor-distance gate (`gates.py --premium 50`). Exit Thu 10/22 9:47, win or lose.
- **Options:** Level 2 only. Every buy passes the four-test screen in STRATEGY.md; CSPs and covered calls are banned until equity >= $508. Directional bets use leveraged ETFs, not calls.
- **Crypto sleeve (user unfroze it 10/19):** any new entry needs a written level, a target >= 6% away (3x the 1.9% spread) and a full-quantity stop placed at the fill. New crypto money never takes cash needed for SOXL or the METU put. Trail stops ~1.5x the daily range. **No resting buys** whose fill could sit unprotected for more than ~12 hours.
- **Alerts at Robinhood** (phone only, they do not wake the assistant): SOXL > $112, SOXX < $495, plus the crypto levels in trades.md (10/18). Update them whenever a stop or target moves.
- **SOXL mechanics:** the $76 stop holds all 3 shares, so any sell means cancel the stop first, sell, then re-place a stop on what remains.
- **Dashboard (Rip City Ledger)**, rival updates and the plays card: procedure in SCHEDULED_RUNBOOK.md.
- **Read WATCHLIST.md** before hunting; discipline: fewer, bigger, better trades; no new crypto trade without a level.
- **Rival:** when the user reports Codex's value, run `gates.py --rival <value> --save --render` and update dashboard/rival.json. Codex's holdings are not available (user decision 10/19); its value is the only information.

## Data tools
- `tools/rh_event.py`: Robinhood event-contract quotes.
- `tools/fincept.sh`: FinceptTerminal's Python data scripts (Yahoo quotes and 18-year daily history for backtests, VIX, Treasury rates). See tools/FINCEPT.md. Robinhood stays the source of truth for anything traded.

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
