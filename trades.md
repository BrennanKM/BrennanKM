# Trade Log

Account: MCP (limited margin, agentic). Start: $30.00 on 2026-10-18.

---

## 2026-10-18 CRYPTO (all pairs) — NO TRADE
Decision: stay flat on crypto this session.
Evidence:
- `get_crypto_quotes` (03:45 ET Sun): BTC bid 80,816.91 / ask 82,358.87 → 1.89% spread; ETH 1.89%, SOL 1.90%, DOGE 1.90%, XRP 1.90%, HYPE 1.90%, PEPE 2.1%.
- `preview_crypto_order` $10 BTC market buy priced at 82,352.07 vs mark 81,587.89 → +0.94% paid on entry alone; round trip ≈1.9%, above the 1.5% ceiling. A trade would need a ≥5.7% move just to clear 3x spread.
- Web: BTC -2.6%, ETH -4.5%, SOL -6.2% over 5 sessions; Ledger hardware-wallet breach (~$90M) in the weekend news flow. Weak tape, no dated catalyst.
Why: paying ~2% to make a weekend directional bet with no catalyst is donating to the market maker. Revisit if the user switches crypto to Exchange Routing (Settings → Crypto → Fee Tiers), which should tighten the effective spread.

---

## 2026-10-18 QS LONG
Catalyst: Q3 2026 earnings Wed 2026-10-21 after close (verified, `get_earnings_results`). Est EPS -0.17; beat or matched in each of the last 6 quarters.
Evidence:
- `get_earnings_calendar` / `get_earnings_results`: report 10/21 pm, verified.
- `get_equity_historicals` (daily, Jul–Oct 2026): steady downtrend $7.61 → $4.01. Made a 52-week low of $3.80 on 10/15, then a +7.6% reversal day (3.81 → 4.23) on above-average volume (16.8M vs 13.5M 30-day average). $3.60–3.95 was also the April 2025 base, before the 2025 run to $18.56.
- `get_equity_technical_indicators`: 14-day RSI 21.8 on 10/14, 30.8 on 10/16. Deeply oversold.
- History of violent two-sided reactions around earnings (weekly bars): Apr-2026 week high $9.66 off a $6.87 low (+40% intraday wick); Jun-2025 week +54%; Feb-2026 week -18%; Jul-2026 -13% (PowerCo payment cut from $131M to $75M).
- Dilution check (`get_sec_filing_index` since 2026-06-01): no S-3/424B5 filed; only Form 4s and the July 8-K/10-Q. Web: $859M cash at 6/30/26, ATM use in 2026 ≈$0.9M (negligible), runway guided into 2029. A raise before 10/21 is unlikely.
- Web: new solid-state architecture for AI data-center racks announced recently. Negative: CTO sold 120k shares under a 10b5-1 plan.
Entry: limit buy 5 sh @ $4.08, regular hours, good for day (Mon 10/19). Fri close $4.01. If it gaps above $4.08 there's no fill and no chase.
Target: $4.70 (+15%) into or after the print; trim half at $4.45 (+9%) if the stock runs up before earnings. Spread is about $0.01 on $4 (0.25%), so the target is far above 3x costs.
Invalidation: daily close < $3.75 (loses the 52w-low/April-2025 base), OR a dilution filing (S-3/424B) before the print. Exit immediately, no averaging down.
Size: 5 sh ≈ $20.40 = 68% of equity. All-in is allowed (catalyst ≤5 trading days), but I'm holding ~$9.60 back for a scanner setup Monday since the sub-$5 scan can't read weekend volume. Gap risk: a -15% earnings gap costs ≈$3. That's survivable and nowhere near the $10 floor.
Hold: 1–3 trading days. Decide by Wed 10/21 3:30pm ET whether to hold through the print (hold if ≥ entry and no filing; sell if below entry, so I don't double down on a broken trade with binary gap risk).
Edge over Codex: a generic agent screens "sub-$5 + earnings this week" and either skips QS as a falling knife or buys it blind. The edge here is (1) confirming there's no live shelf/ATM overhang before the print, which kills most pre-earnings longs in cash-burning small caps, and (2) entry at a multi-year base with a defined 8% stop, not a chase.
Known weaknesses: the trend is still down; the last earnings sold off; and "oversold" isn't a catalyst by itself. This is a ~45/55 trade on direction, taken for its convex payoff (QS has repeatedly made +30–50% moves on news), not because I expect it to go up.

### QS: CANCELLED before entry (2026-10-18, 04:05 ET Sun)
The red-team review (read-only research agent) knocked the thesis out:
- **Implied move:** the 10/23 ATM straddle is ≈ ±11.7% ($3.54–$4.48). My $3.75 stop was **inside** that range and my $4.70 target was **outside** it. I'd have paid for noise to stop me out, and the target needed a move bigger than the market is pricing.
- **The "convexity" was a mirage:** day after earnings, closes were −0.5, −1.6, +8.0, −12.0, +1.4, −12.9%. Four of six red, and 0/6 hit +15%. April's +32% open faded to +1.4% by the close.
- **The reversal had already failed:** 10/16 closed −5.2% at the low of the day, giving back the 10/15 reversal. The $4.08 limit sat above the last trade, so it would have bought the open without any confirmation.
- **Context:** short interest is 112M shares (~18% of float, 9.1 days to cover) and *rising* into the print. Analysts are 0 Buy / 6 Hold / 2 Sell. Insiders were all selling, none buying.

Post-mortem: I treated "oversold + dated catalyst + clean balance sheet" as an edge without pricing the event. **Rule change:** before any earnings or catalyst trade, get the implied move (from the option chain, or Nasdaq's if Robinhood option quotes 403). The stop must sit outside ~1x the implied move, or the position must be sized so a full gap through the stop is acceptable. The target has to be reachable inside the implied range, or the thesis has to explain why the market is underpricing the move.

---

## 2026-10-18 ETH-USD LONG (resting limit, not filled yet)
Catalyst: retest of the 10/15 leverage-flush low (~$286M of ETH longs liquidated; ETH −6.4% to $2,356). Secondary: the Glamsterdam upgrade goes live on the Hoodi testnet 10/26. Hard time-stop: the 10/28 FOMC decision (2pm ET), where hike risk was ~20% priced earlier this month.
Evidence:
- `get_crypto_quotes` 03:45 ET: ETH mark $2,407, bid $2,384.30, ask $2,429.78 (1.89% spread). `get_currency_pairs` sweep by research agent: no non-stable pair is under 1.88%.
- Web (CoinDesk 10/15): the $2,356 flush low on ~$1B of liquidations market-wide. Funding still above its monthly average, so another flush into that level is plausible, and that's where I want to be a buyer, not at $2,407.
- Web (bgeometrics weekly): BTC ranging 75.7K–85.8K for 4 weeks, so mean reversion inside a range is the regime, not a trend.
- Robinhood fee schedule (2026-06-22): Exchange Routing at the $0–10K tier is 0.50% maker / 0.95% taker. On Market Maker Routing a resting limit buy only fills once the *ask* trades down to it, so the spread is paid in *where* it triggers, not on top of the fill price.
Entry: limit buy $10.00 of ETH at $2,355 (GTC). This fills only if the ask reaches $2,355, i.e. mid ≈ $2,333, a full retest of the flush low.
Target: limit sell at $2,580 (+9.6% from fill). At ≈1.9% round-trip spread that's ~5x costs.
Invalidation: daily close < $2,240 (−4.9% from fill). Breaking below the liquidation low means the flush wasn't the low. Also exit before 2pm ET 10/28 (FOMC) unless the position is already ≥ +5%.
Size: $10 = 33% of equity. That's the minimum meaningful size: a crypto mean-reversion trade has no dated catalyst, so per the rules it doesn't earn concentration. The remaining $20 is reserved for an equity catalyst trade.
Hold: 2–10 days.
Edge over Codex: a generic agent buys ETH at market and pays ~0.95% on entry. Here the entry sits at a defined liquidity level and only triggers on a real retest. If ETH never comes back, there's no fill, no cost, and no regret.
Weakness: check-ins only run on weekdays, so a weekend fill followed by a breakdown below $2,240 won't be caught until Monday 9:47 ET. Positive funding + ETF outflows + a hawkish Fed is a real path down to ~$2,150.

**Resize (2026-10-18 03:56 ET):** the user deposited $100, taking equity to $130. I cancelled the $10 order (0 filled) and replaced it with a **$30** GTC limit at the same $2,355, order 6ad47bb7-284d-4f72-b839-148098c268ad. Same thesis, same stop and target. $30 is 23% of equity, under my ~25–33% cap for a trade without a dated catalyst. Loss at the stop ≈ $1.47 (1.1% of equity).

---

## PLANNED (conditional; no order until trigger): SOXL LONG, semis capitulation bounce
Catalyst: SOX down 8 straight sessions (longest since 2008), −11.4% on the week, −23.9% from its 6/22 record. Decisive event: **Tue 10/21 after close: LRCX (memory/capex), META (hyperscaler AI capex), TXN.** Time-stop: FOMC 10/28 2pm.
Evidence (research agent, 2026-10-18; Yahoo SOX daily 1994–2026, Robinhood quotes/earnings, Nasdaq chains):
- Analog screen "week ≤ −10% and 15–35% below 52-week high" (n=29): SOX forward 5 days +3.1% mean, 76% win (baseline 55%). SOXL forward 5 days +11.7% mean, 88% win (n=16). By 20 days it's a coin flip, and 38% of cases fell another 10%+ (≈ −30% SOXL) first.
- Pure 8+ day streaks are bearish (n=6, 4 failed), but every one came deep in a bear market (SOX 47–82% below its record). Today's −24% matches the correction set.
- Friday closed at the low (11,137) on the 9/14 low (11,131). RSI 31.8, not washed out. ASML/TSM beats got sold, so good news isn't being rewarded yet. **No reversal signal → no entry at the open.**
Trigger (must happen first): (a) SOX trades below 11,100 (SOXX ≈ $490), then closes green; OR (b) the first SOX close ≥ +2% that breaks the streak (best case: after LRCX/META on 10/22). Judged at the 3:22pm ET check-in from price vs prior close. Enter with a marketable limit before 4pm, or at the next open if confirmed after hours.
Entry: SOXL $85–95. Whole-share marketable limit at ask + $0.05.
Target: T1 $110–112 (SOX ≈ 11,900): sell half and trail the stop to entry. T2 $117 (SOX 50-day ≈ 12,063).
Invalidation: SOXL **daily close < $80** (SOX ≈ 10,600, the 200-day). Max loss ≈ −12% to −15% of the position.
Size: **~70% of equity (~$90, ~1 sh at $90 or fractional market).** That's above the agent's 45% on purpose: under Mandate v2, P(reaching $200) requires concentration in the best setup of the month. A stop-out at $80 from a $91 entry ≈ −$11 (−8.5% of equity), within the 15% per-trade cap.
Hold: 3–7 trading days. Trim to ≤ 35% of equity before 10/28 2pm (FOMC + MSFT/GOOGL capex that night) unless T1 is already hit and the stop trails.
Edge over Codex: a generic aggressive agent either buys SOXL Monday morning into a falling knife or avoids it entirely. Here entry waits for a reversal *close* and is sized on base rates from 29 analog episodes. Decay is accounted for: ~0.14%/day at 34% vol.
Weakness: n is small (16 SOXL episodes). Jul 2026 and Feb 2020 analogs both bounced and then broke down. 3x decay hurts in chop. A hot macro print or a hawkish Fed can override the bounce.

## PLANNED (conditional, variance bet): METU through META earnings (10/21 pm)
Evidence: META's implied move (10/23 straddle) is 7.3% vs a last-8 median realized move of 8.3%, and its last 5 moves were all ≥ 8%. It's the only one of NFLX/TSLA/META that's underpriced. Recent tilt is down (3 of the last 4). No drift after day 1.
Condition: only if META ≥ ~$700 and SOX isn't making new lows on 10/21.
Entry: Wed 10/21 by 3:50pm ET, limit order, ~$22–26 (15–20% of equity). Exit: Thu 10/22 at the open or within the first 30 minutes, whatever the outcome. This is a planned overnight hold, not a day trade.
Expected: METU ±15–20% → ±$4–5. ~45–50% up. **No directional edge.** It's taken only because Mandate v2's threshold goal rewards variance at small size. Skip it if SOXL is already on at ≥ 70% and losing.
Skipped: NFXL (implied move rich vs realized, illiquid), TSLL through earnings (fairly priced, no edge).

---

# CRYPTO SLEEVE: small "learn by trading" positions (user request 2026-10-18)
Budget: ≤ $65 total including the resting ETH order. **SOXL has priority:** if the SOXL trigger fires and cash is short, sell sleeve positions to fund it.
Known cost: Market Maker Routing ≈ 0.95% per side (measured), so every round trip starts −1.9%. These trades are partly tuition. The lesson I'm testing: do range-edge entries with hard stops beat a 1.9% toll?

## 2026-10-18 BTC-USD LONG (market, live)
Catalyst: no dated catalyst. Range-bottom mean reversion, and the US ETF-flow window reopens Mon 10/19.
Evidence:
- `get_equity_historicals` IBIT daily 9/18–10/16: 4-week range $45.11 (10/15 low) to $49.39 (10/2 high) ≈ BTC $79.8K–$87.3K (IBIT×1,768). IBIT closed 10/16 at $46.15 ≈ $81.6K, lower third of the range. The 10/15 flush low was bought: IBIT closed $46.59 off a $45.11 low.
- `get_crypto_quotes` 04:16 ET: BTC mark $81,579, bid $80,808 / ask $82,350 (1.89%).
- Web (research agent): ETF net outflows ≈ $228M 10/12–16, Fear & Greed 53 (down from 71). Sentiment has cooled, but there's no capitulation.
Entry: market buy $20 (expect ≈ $82,350 = ask).
Target: $85,000 (+3.2% from fill, upper-middle of the range). Sell limit is set at check-ins; it can't sit alongside the stop on the same coins.
Invalidation: **GTC stop order (sell) at $78,900**, below the 10/15 range low with a buffer: −4.2% from fill ≈ −$0.84.
Size: $20 = 15% of equity.
Hold: 1–5 days. Must not block SOXL capital.
Lesson being tested: buying the range bottom on market-maker routing. If it's stopped out, the range broke and I paid ~1% extra to learn the spread on top.

## 2026-10-18 SOL-USD LONG (resting limit: stop-hunt buy)
Catalyst: none dated. A sweep of the 10/15 low / $100 round number.
Evidence:
- `get_equity_historicals` BSOL daily: lower highs since 10/2 ($17.03 → $14.70); 10/15 low $13.91 ≈ SOL $100.4 (BSOL×7.22); now $14.28 ≈ $103. Weakest of BTC/ETH/SOL (−6.2% over 5 sessions).
- `get_crypto_quotes` 04:16 ET: SOL mark $103.10, bid $102.12 / ask $104.08.
Entry: limit buy $15 at **$99.50** (GTC). It only fills if the ask trades below the 10/15 low and $100, i.e. a liquidity sweep where weak longs get stopped.
Target: $108 (+8.5%).
Invalidation: $95 (−4.5%). Below that the sweep became a breakdown.
Size: $15 (11.5%).
Lesson being tested: does a sweep-of-the-low limit buy beat buying now? Compare with the BTC market entry.

**BTC fill (04:17 ET):** 0.00024285 BTC @ **$82,354.09** ($20.00). The mark was $81,579, so I paid +0.95% over mid. At the bid the position is worth ≈ $19.62 (−1.9%) the moment it fills.
Lesson 1 (immediate): a market buy on MM routing is a guaranteed −1.9% mark-to-bid. The "price" field on a market order ($83,175.91) is the +1% collar ceiling, not the fill.
Stop order placed: sell 0.00024285 BTC, trigger $78,900, GTC, order 6ad48095-9b1b-41b9-b508-62475232d2b0. Worst-case fill floor shown is $74,955 (−5% collar). A stop triggered on a fast weekend wick can fill well below $78,900.
SOL limit placed: buy $15 (0.15075 SOL) @ $99.50 GTC, order 6ad4808a-abfc-421d-ad10-41034f09ba53.

## 2026-10-18 ZEC-USD LONG (trend leader, scale-in: half market + half dip limit)
Catalyst: none dated. Momentum: buy the strongest trend in crypto on a pullback day.
Evidence:
- Web (delta.app / The Block): ZEC ≈ $488–493 in early/mid Aug 2026. `get_crypto_quotes` 04:19 ET: mark $1,122.61. That's **+128% in ~2 months**, the strongest trend of any pair I've checked.
- `get_crypto_quotes`: ZEC −2.5% on the day (open $1,151), the biggest daily dip among 20 pairs scanned, so it's a pullback inside the trend. Spread 1.89%, the tightest on Robinhood.
Entry: (1) market buy $10 now (≈ ask $1,133); (2) limit buy $10 at **$1,090** GTC (fills when the ask reaches $1,090, mid ≈ $1,080, −3.8%).
Target: $1,200 (+6–10% depending on fills).
Invalidation: $1,020 (−9% from the market fill). A parabolic leader needs room: the stop sits below a ~10% pullback, and size is kept small to pay for that room. GTC stop order on the market-fill coins now; add the dip-fill coins to it if that order fills.
Size: $20 total (15% of equity).
Lesson being tested: **leader vs. laggard.** ZEC (strongest trend, bought on a dip) vs SOL (weakest, bought on a sweep) vs BTC (range bottom, market).

**ZEC fill (04:20 ET):** 0.00881 ZEC @ **$1,134.45** ($10.00). Mark was $1,122.61, so +1.05% over mid (slightly worse than BTC). Stop order: sell 0.00881 @ trigger $1,020 GTC, id 6ad48150-410b-42e3-b573-e20fdcc2ecb4 (collar floor $969). Dip limit: buy 0.00917 ZEC @ $1,090 GTC, id 6ad48148-d42f-4e3a-8873-4814655cfda4.

### Weekend check-in 2026-10-18 12:14 ET
- **ZEC dip limit FILLED** at 11:40 ET: 0.00917 @ $1,088.68 ($9.99). Position is now 0.01798 ZEC, cost $19.99, avg ≈ $1,111.8. Mark $1,081 (−2.8%). ZEC fell from $1,151 to ~$1,070, so the "leader on a dip" kept dipping.
- Old ZEC stop (0.00881) cancelled. **New stop order: sell 0.01798 ZEC @ trigger $1,020 GTC**, id 6ad4f058-34ac-42f7-9261-e1bca53bf035. Risk at the stop ≈ −$1.65 plus spread.
- BTC mark $81,066 (−1.6% vs fill); stop at $78,900 untouched. ETH ask $2,392.77 vs my $2,355 limit: not filled, ~1.6% away. SOL ask $102.93 vs the $99.50 limit: not filled.
- Equity $129.13 (−0.67% on $130). No invalidation hit. Floor $50 nowhere near.
- Early lesson, ZEC: the dip-buy limit filled 4% below the market entry, so scaling in beat buying all at once. The dip was still a falling price, though; the stop decides whether it was a buy.

## 2026-10-18 15:25 ET BTC ADD (resting limit at range low), user asked to deploy extra cash today
Catalyst: none dated. Planned scale-in at the 4-week range floor. This is the one allowed average-down, and the range thesis is intact: no close below $79.8K.
Evidence:
- `get_crypto_quotes` 15:24 ET: BTC is the strongest major on the day (−1.1% vs ETH −2.6%, SOL −2.5%, AVAX −3.8%, UNI −5.0%, ZEC −7.3%). Leadership in a broad drift.
- IBIT daily (from earlier): range floor 10/15 at $45.11 ≈ BTC $79.8K. Mark now $80,978.
- Web: ETF outflows and CPI/Fed fears drove the 10/15 flush (CoinDesk, Cryptotimes). No new negative catalyst found for this weekend.
Entry: limit buy **$25 at $80,550** GTC. Fills when the ask reaches $80,550, i.e. mid ≈ $79.8K, the range floor.
Target: $85,000 (+5.5% from fill). Combined position avg ≈ $81.3K if filled.
Invalidation: existing stop at $78,900 (≈ −2% from fill), to be resized to the full quantity on fill.
Size: $25 (19% of equity). If it fills, BTC is ≈ $45 total = 35%.
Not done: the other $20 stays in cash for SOXL. A market buy now ($81,744 ask) was rejected: ~1:1 reward:risk after spread vs ~2.7:1 at the floor.
Weakness: if BTC never revisits $79.8K there's no trade. If it does, it may be on the way through the floor; the tight stop then costs ≈ $0.50 plus spread.

### 2026-10-18 17:21 ET: ETH filled; rival update
- **ETH limit FILLED** 15:40 ET: 0.012738 ETH @ **$2,354.99** ($30). Stop order: sell 0.012738 @ trigger **$2,240** GTC, id 6ad5384a-fb70-4e3c-9ac0-a48f5008badc (collar floor $2,128). Target $2,580; exit before FOMC 10/28 2pm unless ≥ +5%.
- **Codex reported at $134.00 (+3.1% on $130)** vs me $128.95 (−0.8%). Gap: −$5.05.
- Read: everything I track is down today (BTC −1.1%, ETH −2.6%, ZEC −7%), and Codex is *up*. So Codex is probably not long crypto, or made a lucky stock/crypto trade before the drift. My crypto book is already different from Codex's, and different is what a trailing player needs. **I will not chase Codex's +3%.** A $5 gap is noise against a $200 target. What closes it is the planned SOXL/METU catalysts, not more weekend crypto.
