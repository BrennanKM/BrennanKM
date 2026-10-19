# Scoreboard

| Field | Value |
|---|---|
| As of | 2026-10-18 20:14 ET (Sun evening check-in) |
| Capital contributed | **$330.00** ($30 start + $100 on 10/18 ~03:56 ET + $200 on 10/18 ~21:30 ET; Codex got the same) |
| Account equity | $331.75 · Codex est. $336 (last report $136 + $200 deposit) |
| **Return on contributed capital** | **+0.53%** ($1.75 on $330) |
| Cash | $260.01 free (incl. the $200 deposit, instantly spendable); crypto held ≈ $72 |
| Trades closed | 0 |
| Win rate | n/a |
| Biggest win / loss | n/a / n/a |
| Open risk | BTC $20 → stop ≈ −$0.84 (+ spread). If all limits fill: ETH stop ≈ −$1.47, SOL stop ≈ −$0.68. Max sleeve loss ≈ $3.5 (2.7%). |
| Survival floor | Equity < **$127**: stop and write postmortem.md (Mandate v3) |
| Goal / deadline | **$508 (+54%) / $762 (+131%)** by ~2026-11-18 (Mandate v3 in TRADER_PROMPT.md) |

## Account facts (verified 2026-10-18)
- Crypto routing: **Market Maker Routing** (user turned Fee Tiers / Exchange Routing off 10/18). Spread ≈ 1.9% round trip, so resting limits are the default entry.
- Fresh-session check-ins (one new session per check-in) can't be created from Claude's session: they'd run without the Robinhood connector. The standalone prompt is in CHECKIN_PROMPT.md for the user to paste into a claude.ai routine with Robinhood attached. Until then, check-ins run in the original session.
- Check-ins: weekdays 9:47am & 3:22pm ET, weekends 12:13pm & 8:13pm ET. Extra one-off check-ins: **Wed 10/21 12:37pm** (earnings day: pre-screens the METU put) and **Wed 10/28 1:37pm** (before the 2pm FOMC decision). Each push-notifies on fills, stops, trades, triggers, ±5% moves, or a Robinhood failure.
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
| ZEC | 0.01798 | ≈$1,111.8 ($19.99) | stop order $1,105 GTC (id 6ad57e63-debf-42fb-a2e1-43415066ed5a) | $1,200 | crypto sleeve, trend leader; both halves filled |
| ETH | 0.012738 | $2,354.99 ($30) | stop order $2,300 GTC (id 6ad56199-5a5d-4192-a7f6-69366deb1b1e) | $2,580 | out before FOMC 10/28 2pm unless ≥ +5% |
| BTC | 0.00024285 | $82,354.09 ($20) | stop order $78,900 GTC (id 6ad48095-9b1b-41b9-b508-62475232d2b0) | $85,000 (set a sell limit at a check-in if within ~1.5%; cancel the stop first) | crypto sleeve |

## Open orders
| Asset | Side | Type | Size | Price | TIF | Order id |
|---|---|---|---|---|---|---|
| ETH | sell | stop order | 0.012738 | trigger $2,300 | GTC | 6ad56199-5a5d-4192-a7f6-69366deb1b1e |
| BTC | sell | stop order | 0.00024285 | trigger $78,900 | GTC | 6ad48095-9b1b-41b9-b508-62475232d2b0 |
| ZEC | sell | stop order | 0.01798 | trigger $1,105 | GTC | 6ad57e63-debf-42fb-a2e1-43415066ed5a |

## Next actions (check-ins read this first)
- **MON 10/19 9:47: SOXL ENTRY (strategist-approved; supersedes all earlier SOXL rules below).** SOXX $495–512 → buy 2 SOXL, marketable limit cap $104. SOXX > $512 → 1 now, 2nd at 3:22 if holding above the open. SOXX < $495 → wait to 3:22, buy 2 only if $492.83 is intact. No entry if SOXX breaks $492.83 first. Stop: close < $80. T1 $112 (sell 1), T2 $118. Half out by session 5, all out by Mon 10/26 3:22. Exit Thu 9:47 if the Wed prints break the thesis. The weekly pass counts as the pre-trade review for this exact entry; re-review only if conditions differ.
- **Crypto sleeve UNFROZEN by the user 10/19 ("keep trading crypto as much as you want"; overrides strategist #4).** Trader's rules: (1) crypto never takes cash needed for SOXL (≤ $208 Mon) or the Wed METU put; until SOXL fills, new crypto money ≤ $40. (2) Every entry needs a written level and a target ≥ 3× the 1.9% spread (≥ ~6%) away. (3) Full-quantity stop placed in the same check-in as the fill; resting buys only if the stop can be placed at the next check-in and the gap is written down. (4) Trail stops on winners: ZEC was ratcheted to $1,105 (≈ breakeven after spread) on 10/18 22:20 ET at mark $1,181. (5) Check crypto at every check-in, weekends included, since it's the only market open nights and weekends.
- **SOXL size stays 2 shares (strategist pre-trade review 10/19: KEEP 2, accepted).** 3 shares would fail the $187 floor gate together with the METU put, and the Monday 3:22 pyramid is rejected. **The only allowed add:** Thu 10/22 9:47, if the Wed prints are clean AND SOXL ≥ +10% over the fill. Add 1 share funded by METU put proceeds or the unspent put cash, and move the original stop to the entry price.
- **Options = Level 2 playbook in STRATEGY.md (adopted 10/19).** Every option buy must pass the four-test screen (R ≥ 1.20, replay price cap, liquidity, skew/IV); otherwise no trade. Cash-secured puts and covered calls are banned until equity ≥ $508. Directional bets use leveraged ETFs, not calls.
- **EVENT PRICES = ROBINHOOD'S OWN (user 10/19).** Run `python3 tools/rh_event.py <category>/events/<slug>` (or `--list economics`) for the contract symbol, listing exchange (KALSHI or ROTHERA, Robinhood's exchange), whether Robinhood lets you trade it, YES/NO bid/ask and OI, all from robinhood.com's public pages. Use those numbers, not Kalshi's, for every screen and order. Contracts flagged NOT TRADABLE ON RH are out. 10/19 facts: Q3 GDP = Kalshi KXGDP-26OCT30, tradable on RH only at >3.0/>3.5/>4.0 (and 0.0/0.5); Fed Oct (ECUSFED-26OCT) and Sept Core PCE (ECPCE-26SEPCORE, release 10/29) are on ROTHERA.
- **Event contracts ENABLED in the user's Robinhood app (10/19).**
- **EVENT CONTRACTS COUNT (Mandate v3.1, 10/19).** Claude picks; the user places them in the app. Gates: behind the glide path or Codex · 30–70¢ · edge ≥ 5 pts after costs vs an independent model · stake ≤ 25% of equity · $187 floor gate · strategist review if ≥ 15%. To trade: write the thesis + exact order in trades.md, PushNotification "EVENT ORDER for you: <contract> <side> <qty> @ ≤ <price>", and record the user's fill when they report it.
- **Q3 GDP contract (release Thu 10/29 8:30am ET; Kalshi KXGDP-26OCT30, trading closes 8:29am release day):** first screen 10/19 = NO BET YET. Only candidate: **>3.5% YES** (0.29/0.32), +6.7 pts net on the locked blend (50% GDPNow / 25% NY Fed / 25% bank trackers, σ 1.1), but fragile (only +3.5 equal-weight). Max price = model prob − 0.07. Size ≈ $25, cap **$35** (Kelly cap, accepted). Funded from SOXL proceeds after the 10/26 time stop. **Fees verified by web 10/19: $0.02/contract all-in** ($0.01 Robinhood + $0.01 exchange; GDP is a listed Robinhood economics category). Data is pulled by agents (Kalshi public API, GDPNow, NY Fed); the user only needs the Derivatives account enabled and to place the order. If Robinhood's price for the strike differs from Kalshi's, the limit price in the order protects us. The **final go/no-go is 10/28 1:37pm, or 3:22pm if GDPNow hasn't updated after the 8:30 trade/inventories data.** **Re-screen at Tue 10/27 3:22pm and Wed 10/28 1:37pm** with the latest GDPNow / NY Fed nowcast and live Kalshi prices. If it passes the gates at 10/28 1:37pm, send the order to the user then (before the market closes for the release).
- **Sept Core PCE (ECPCE-26SEPCORE, Rothera; release Thu 10/29 8:30am ET), strategist screen 10/19: NO BET YET.** YES needs a printed ≥ 0.4 (strictly above 0.3, one decimal). Locked center 0.33, σ 0.04 → P(YES) 0.31. Pass lines: center ≤ 0.325 → buy NO, limit ≤ 65¢; center ≥ 0.345 → buy YES, limit ≤ 37¢. Stake ≈ $30. OI 35: limit orders only, partial fill OK. Re-screen Fri 10/23 3:22pm; final Wed 10/28 1:37pm together with GDP.
- **Fed Oct 28: NO BET** (futures 16% hike ≈ RH 15¢; all strikes outside the band).
- **Event stake cap (accepted 10/19): total event stake across PCE + GDP ≤ $50 (15% of equity).**
- **METU put Wed:** limit = the lowest of mid, the replay price cap (≈ $0.60 for the 25p at METU $29.00 / $0.47 at $29.50; recompute live) and $0.50. Must pass the liquidity test live, or skip. gate = equity − all gaps through stops − premium ≥ $187. 1 contract; re-pick the strike so the spread is ≤ 60% of mid.
- **Capital now $330 (10/18 21:30 ET).** Re-size every plan in % terms: SOXL 35% stage ≈ $115 (1 sh), 70% ≈ $230 (2–3 sh). METU put cap stays ≤ ~$50 (now 15%), and 1–2 contracts are OK if the quote qualifies. TMF ≤ 15% ≈ $50. FAS 1 share ≈ $160 = 48%, still too big for a side bet: skip.
- **Read WATCHLIST.md** (weekly playbook from the 10/18 sweep) before hunting.
- **Strategy discipline (10/18 review):** fewer, bigger, better trades. Each small crypto round trip costs ~1.9% (≈ $0.40 on $20), so no new crypto trade unless it clears 3x spread with a defined level. Capital goes to the dated catalysts (SOXL trigger, META 10/21, the Sunday-sweep picks).
- **Dashboard "Rip City Ledger" (Trail Blazers theme; was The Iron Ledger)** (https://claude.ai/artifact/QXgQDxzX7dvyhKdskrY7j1): positions, orders, quotes and account value are live Robinhood queries. At EVERY check-in: (1) append `{at, equity, contributed, note}` to `dashboard/curve.json` from get_portfolio; (2) sync `dashboard/ledger.json` with trades.md (status, fills, lessons; the "house" field is unused by the page now, so any value is fine); (3) upload both with Artifact publish `asset:true` to that url, then ArtifactData `update` datasets/curve and datasets/ledger with the new `source.url` and `updated:{at,by:"Claude"}`. Also read data/users/me/check once and fix any page error it names. **(4) Your plays card:** keep `dashboard/plays.json` in sync with every event-contract play (status: Place now / Placed / Filled / On deck / Screening / Won / Lost / No bet; contract, side, qty, max_price, stake_usd, pays_usd, place_by, next_screen, quote from tools/rh_event.py, model_prob, edge_pts, why, result, **decide_at** (when the final go/no-go happens), **instruction** (one plain sentence telling the user exactly what to do, e.g. "Don't buy this…")). For a "Place now" play, side, qty, max_price, stake_usd and place_by are REQUIRED: the card builds the step-by-step order from them. Upload it with `asset:true`, then update datasets/plays `source.url`. A play the user must place now = status "Place now" + PushNotification.
- **No resting buys** (SOL and the BTC add were cancelled 10/18 to close unprotected-fill gaps). Cash $60 is earmarked for SOXL (needs ~$90; sell crypto to top up if it triggers).
- **Alerts:** Robinhood price alerts are live (see trades.md, 10/18 17:25). Update or delete them when stops or targets change.
- **Crypto sleeve:** ZEC fully filled with the stop re-sized (done 10/18 12:14). If SOL fills, place a GTC stop order at $95. Weekend/weekday checks: BTC ≥ $84,600 → cancel the stop and place a sell limit at $85,000. **If SOXL triggers and cash is < $90, sell sleeve positions first.**
- ~~SUPERSEDED by the MON 10/19 entry at the top~~ **SOXL revision 10/18 (see trades.md):** trigger (b) = SOXX close ≥ **$503.26** AND above that day's open. **Staged:** 35% of equity if it fires Mon/Tue (before Wed's LRCX/META binary), add to 70% only if SOXX holds above that day's low through Thu. Full 70% if it fires Thu after good prints.
- ~~SUPERSEDED by the MON 10/19 entry at the top~~ **(old) SOXL reversal trigger, checked at EVERY 3:22pm check-in from Mon 10/19.** Get SOXX/SOXL quotes vs prior close (SOX proxy: SOXX; 11,100 ≈ SOXX $490). Trigger = (a) the session traded below 11,100 / SOXX $490 and is now green, OR (b) SOX/SOXX ≥ +2% on the day after 8 down sessions. If triggered and SOXL is in $85–95: write the fill into trades.md and buy ~70% of equity with a marketable limit. Then set the stop rule (daily close < $80) and the T1 sell-half at $110. No trigger means no trade. (Old rule; the strategist backtest overrode it: buy at the 9:47 open per the top entry.)
- **Wed 10/21 3:22pm:** META earnings: decide the **METU 10/23 put** (~14% OTM, limit ≤ $0.50, 1 contract, ≤ $50) per WATCHLIST.md #2. It replaces the METU-shares bet. Skip if ask > $0.60 or total risk incl. SOXL > ~25% of equity at stops. Exit Thu 10/22 9:47 check-in.
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
