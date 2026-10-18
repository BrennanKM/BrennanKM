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
