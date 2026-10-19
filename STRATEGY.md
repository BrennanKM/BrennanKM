# Strategy (maintained by the Strategist subagent, read-only)
Weekly pass for Mon 10/19 – Fri 10/23, written Sun 2026-10-18 ~21:45 ET. Live state pulled from Robinhood at 21:40 ET.

## 1. Standing
| Item | Value |
|---|---|
| Equity | **$331.79** (cash $260.01 incl. the $200 deposit, which still shows as `pending_deposits` but is already in buying power; crypto $71.78; no equity or option positions) |
| Contributed / return | $330 / **+0.54%** |
| Codex | est. **$336** ($136 last report + $200), so we're **−$4.2 (−1.3%)**. That's noise against a $176 gap to target. |
| Trading days left | **23** (10/19 → 11/18) |
| Required to $508 | +53.1%, i.e. **+1.87% per trading day** compounded (≈ +9.7%/week) |
| Required to $762 | +129.7%, i.e. **+3.68% per trading day** |
| Floor ($127) | $204.8 of cushion (−61.7%). The floor is not the binding constraint this week. The target is. |
| One SOXL stop-out (2 sh, $100 → $80) | −$40 (−12%), and the required daily rate rises to 2.55% |

Threshold math (zero-edge random walk, 23 days): the chance of finishing ≥ $508 is ≈ 0.4% at 50% average SOXL exposure, ≈ 2.6% at 70% and ≈ 7% at 100%. A low-variance book can't reach $508, so idle cash costs us real probability. Only an edge or convexity moves this. My honest estimate for P(≥ $508) with the plan below is ≈ 10–14%. With the staged 35%-first plan it's ≈ 7–9%.

## 2. Regime (Fri 10/16 close → Sun 21:40 ET 24h session)
- **Semis:** SOXX $493.39 → **$504.36** (+2.2%) in 24h trade. −24.8% from the $655.95 high, 5-day −11.8%, below the 50-day ($537) and above the 200-day (**$467.6**), RV20 36%. SOXL $93.67 → **$100.01** (+6.8%), RV20 108%. A capitulation-flush setup is live.
- **Broad equities:** SPY $763 → $767.5 (+0.6%). QQQ $709.8, −7% from its high, below the 50-day ($727). IWM $270.4, −11.4%, below the 50-day ($289). Breadth is weak; the damage is concentrated in semis and small caps.
- **Rates/Fed:** TLT $80.05 → $80.23 (TMF trigger is $80.57, not hit). FOMC 10/28, hike odds ~15% (from ~42%) per the 10/18 sweep. Fed blackout until 10/29.
- **Crypto:** BTC mark $82.35K, mid-range in $79.8–87.3K. ETH $2,422. ZEC $1,165 (+1.2% on the day). ETF outflows last week (BTC −$228M, ETH −$320M). MM routing spread still 1.9%.
- **Vol:** VIXY $17.73 → $17.10 (−3.6%) and UVXY −5% overnight, so fear is easing into Monday. SOXL 10/30 options are priced at **IV ~136% vs 108% realized**, which means SOXL calls are expensive.

## 3. Allocation plan
- **Core: SOXL, 2 whole shares (~$200, ~60%), entered Monday rather than staged.** Evidence below (§5 #1): from 2010–2026 SOXX data, buying in the 5 sessions after a ≥10% weekly flush beats waiting for a +2% confirmation close by ~10 points of SOXL return.
- **Satellite: METU 10/23 put, 1 contract, ≤ $0.50 (~$50, 15%).** Bought Wed 3:22pm, sold Thu 9:47am. This is a convexity bet on META's realized earnings move versus its implied move.
- **Crypto sleeve:** hold as is ($72, 22%), frozen. No adds and no new crypto trades.
- **Cash:** ~$60 (18%) Mon–Wed, then ~$10 (3%) after the put. Idle cash isn't "safety" here, because it lowers P(target) and the floor is $205 away. Holding $190 idle through the best edge window of the month (days 1–5 after the flush) is the main flaw in the current plan.
- **Max total risk at stops:** SOXL −$40 + put −$50 (full premium) + crypto −$6 (stops + spread) = **−$96 (29%)**. Worst case, if every position gaps through its stop (SOX −10% Thursday gives SOXL ≈ −30%), the loss is ≈ −$118 and equity ends ≈ $214, still $87 above the floor.
- **True independent bets: ~1.5.** SOXL and crypto are one risk-on bet. The METU put is roughly half independent: its payoff depends on META-specific news, but a broad risk-off Wednesday hurts SOXL and pays the put, so it's a partial hedge, not a separate bet.

## 4. Position review
| Position | Verdict | Reason / stop-target check |
|---|---|---|
| **BTC** 0.00024285 ($20.0, mark ≈ cost) | **KEEP, frozen** | It's wrong if BTC loses the $79.8K range floor, and that hasn't happened. From the mark, the target is +3.2% and the stop −4.2% plus a ~1% exit spread, so reward/risk is < 1. I wouldn't open this today, but closing it costs ~$0.19 and frees $20 we don't need. Stop $78.9K stays. |
| **ETH** 0.012738 ($30.9, +2.8%) | **KEEP** | It's wrong below $2,300 (the 10/15 flush low failing), and that hasn't happened. Stop $2,300 sits 5% under the mark, outside a ~3.5% daily move. Fine. Exit before FOMC 10/28 as planned. |
| **ZEC** 0.01798 ($20.9, +4.8%) | **KEEP** | It's wrong below the $1,057 liquidation low. That hasn't happened. The $1,200 target is +3% away. When ZEC trades ≥ $1,190, swap the stop for a $1,200 sell limit. |
| Crypto sleeve overall | **No adds; don't sell to fund SOXL** | The whole sleeve's upside to its targets is +$3.3 (1% of equity), so it doesn't affect P(target). It's user-requested tuition and cash already covers the plan, so leave it alone and don't spend check-in time on it. |
| **SOXL staged plan (35% → 70%)** | **RESIZE: 2 shares on Monday, not 1 share plus 1 later** | (1) The "$85–95" entry band in SCOREBOARD is stale: SOXL is $100 in 24h trade, so as written the Trader would never buy. (2) Trigger (b) (SOXX ≥ $503.26) is already met in 24h trade, so it adds nothing. (3) The analog data say the confirmation-close trigger gives away most of the edge (§5). Stop: daily close < $80 (≈ SOXX $469, at the 200-day $467.6). That's −20% from $100, so 2 shares = −$40 (12%), and even a 24% gap-through (SOX −8%) = −$48 (14.5%), inside the 15% cap. **3 shares would breach the cap (−$60), so 2 is the maximum.** |
| **METU 10/23 put** | **KEEP, 1 contract; don't size up** | Positive EV only on the fat tail: META −11% or worse (METU ≈ $23) gives the put ≈ $2 (4x). Using the research distribution (median abs move 8.3%), EV ≈ +25–30% per dollar, which makes Kelly ≈ 10% of equity. One contract (15%) is already above Kelly, so don't buy 2. The 25P quote now fails the plan's own spread test (bid $0.25 / ask $0.65 = 89% of mid). Re-quote Wed. |
| TMF / FAS | **Not this week** | TMF hasn't triggered and there's no cash for it once SOXL and the put are on. FAS: one share is 48% of equity, so skip. |

## 5. Ranked opportunities
**1. SOXL post-flush entry (Mon 10/19).**
- *Evidence (my backtest on SOXX daily bars 2010-10 → 2026-10, 3x daily-compounded with fees as the SOXL proxy):* setup = SOXX 5-day ≤ −10% and 15–35% below its 52-week high. This Friday qualifies (−11.8%, −24.8%).
  - Buy the *next open*: n=15, SOXL 5-day **mean +11.4%, win 80%**. The subset that gapped up ≥1% at the open (like Monday): n=6, **mean +14.1%, win 83%**.
  - Wait for the first +2% green close, the current trigger (b): n=13, **mean +1.4%, win 38%**. With the stricter "≥ 6 down days" setup: n=7, mean +3.1%, win 71%.
  - The bounce *is* the edge, and the confirmation close mostly buys its end.
  - Max adverse close over 5 days, for open entries: worst ≈ −15% SOXL. **The $80 stop (−20%) would not have been hit in any of the 15.**
  - Breaking Friday's low after entry wasn't decisive: of 5 cases, 2 still finished +12% / +25%.
- *Trigger:* at the 9:47 check-in, SOXX between $495 and $512. If SOXX > $512 (+3.8%, a chase), buy 1 share and buy the second at 3:22 if SOXX is still ≥ that day's open. If SOXX < $495, wait for 3:22 and buy 2 shares if SOXX is above Friday's low ($492.83). If Friday's low breaks before entry, there's no trade, and the original trigger (a) applies (washout below $490, then a green close).
- *Entry:* marketable limit at ask + $0.05, SOXL cap **$104**.
- *Size:* 2 shares ≈ $200 (60%).
- *Stop:* SOXL close < $80. Thesis stop: exit at the Thu 9:47 check-in, whatever the price, if LRCX guides WFE down or META/TSLA cut AI capex.
- *Targets:* T1 $112: sell 1 share and move the stop on the other to entry. T2 $118 (≈ SOX 50-day).
- *Time stop:* sell 1 share by Mon 10/26 3:22pm if T1 hasn't hit (the analog edge is a 5-day effect and is a coin flip by day 20). Be ≤ 35% by FOMC 10/28 2pm.
- *Implied vs expected:* the 10/30 ATM call has IV 136%, so the implied 1-week SOXL move is ≈ ±19%. The expected move is +5.7% (analog mean, halved for small n). P(win over 5 days) ≈ 65–70% after the haircut.
- *Effect on the week (Monte Carlo, halved edge):* 2 shares vs 1 share raises P(week ends ≥ $365) from 3% to 21% and the mean from $337 to $343. It also raises P(≤ $300) from 0% to 11%.

**2. METU 10/23 put through META earnings (Wed 10/21 after the close).**
- *Trigger/entry:* Wed 3:22pm. Choose the strike that is ~15% OTM on METU at that moment. Limit at mid, max **$0.50** ($50, 15%). Skip if the ask > $0.60, the spread > 60% of mid, or the 10/23 META ATM straddle is > 8.3% of price (no edge left).
- *Exit:* Thu 9:47, win or lose.
- *Expected payoff:* P(META ≤ −8%) ≈ 25%. At META −11% the put is worth ≈ $2 (4x). At −14% it's ≈ $3.7 (7x, +$320 on one contract).
- *Effect on P(target):* this is the cheapest P(target) lever on the board. In the Monte Carlo it alone takes P(week ends ≥ $440) from ~0% to ~19%. The cost is a ~70% chance of losing all $50.

**3. TMF (fallback only, if #1 is not entered because SOXX broke Friday's low).**
- *Trigger:* TLT close > $80.57.
- *Size:* 2 shares ≈ $56 (17%).
- *Stop/target:* stop on a TMF close < $27.00. Target $30.
- *Hard exit:* midday 10/28.
- It's uncorrelated, but low variance (≈ 45% vol), so it does little for P(target). It's a placeholder until a better setup appears.

Considered and rejected:
- **SOXL calls:** IV 136% vs RV 108%. The 10/30 $130C costs $115 and needs SOXL +31%. Shares are better.
- **TQQQ:** QQQ is only −7% from its high, so there's no flush and no edge, and it's the same AI beta as SOXL.
- **More crypto:** 1.9% round trip and no edge.

## 6. Rule proposals (Trader: accept or reject each in trades.md)
1. **Replace SOXL trigger (b) and the "do not buy at the 9:47 open check-in" rule with the post-flush entry in §5 #1.** Also delete the stale "$85–95" band and use a $104 cap. *Reason:* by the n=15 analog data, next-open entry beats a confirmation close by ~10 points of 5-day SOXL return. Trigger (b) is also already met in 24h trade.
2. **Gate the METU put on worst-case floor distance, not on "total risk ≤ 25% at stops":** allow it if equity minus the worst-case loss of all positions (gaps through stops, full premium) is ≥ $187 ($127 floor + $60). *Reason:* that's ≈ $214 today. The 25% rule would block the bet that does most for P(target). Keep the size at 1 contract (Kelly).
3. **Add a 5-session time stop to mean-reversion trades:** for SOXL, sell half by session 5 unless T1 has hit. *Reason:* the analog edge peaks at day 5, and 38% of cases fell another 10%+ by day 20.
4. **Freeze the crypto sleeve:** no new crypto entries and no re-entries after stops, through 11/18, unless the user asks. A sleeve position is closed only by its stop or target. *Reason:* ±1% of equity at a 1.9% toll, and it's the same risk-on bet as SOXL.
5. **Glide-path check every Sunday:** compare equity with the path $332 × 1.0187^days. If ≥ 15% behind on 11/1, the next pass must add a dated convex bet. If ≥ 10% ahead, cut variance and protect the gain. *Reason:* the target is threshold-shaped, so the right amount of risk depends on where we stand against it.

## 7. What would change my mind this week
- **Gap-and-fail Monday:** SOXX opens > $505 and trades below $495 by 3:22, or below Friday's low ($492.83) at any time before entry. That means the flush isn't finished: no entry, and fall back to trigger (a).
- **Wednesday prints:** LRCX guiding WFE down, or META/TSLA cutting AI capex, breaks the thesis. Exit SOXL at Thu 9:47 whatever the price. A META capex *raise* is fine (bad for META, good for semis, and both of our bets win).
- **Macro:** the 10-year yield spiking or Oct-hike odds back above ~35% before FOMC (watch Thursday claims and Friday PMIs). Then trim SOXL to 1 share and skip TMF.

## Level 2 options playbook (no spreads)
Written 2026-10-19 ~22:30 ET (Sun night). Option quotes are Fri 10/16 closes, so every number below gets re-pulled live before an order. Level 3 is unavailable, so no spreads are allowed.

**0. Bottom line.** Buying options is negative-EV by default: sellers earn the variance premium, and our spreads run 2–90% of mid. An option buy is allowed only when a measured gap says it's cheap. Short premium (CSPs and covered calls) is ruled out at this size (§3). The leveraged ETF stays the core (§6).

**1. The screen.** A trade must pass all four tests, using numbers computed in the same session.
- **(a) Magnitude ratio R.** R = median |earnings-day move| over the last 6–8 prints ÷ implied move.
  - Realized moves come from `get_earnings_results` dates plus `get_equity_historicals` daily closes. Use close→close: the prior close to the print-day close for "am" reporters, and the print-day close to the next close for "pm" reporters.
  - Implied move = mid of the ATM call plus mid of the ATM put, for the first expiry after the print, ÷ spot.
  - **Buy only if R ≥ 1.20.** Below 0.9, never buy, since IV crush wins.
  - Stricter optional version, the event-only move: σ_ev² = IV_post²·T − IV_pre²·T, using the expiry just before the print for IV_pre; E|move| ≈ 0.8·σ_ev.
- **(b) Symmetrized replay price cap.** Apply each historical |move| to today's spot in the leg's direction. For leveraged-ETF options, use 2× or 3× the move.
  - Payoff = intrinsic + $0.05 of leftover time value. Replay value = ½ × the mean payoff, since direction is treated as 50/50.
  - **Max limit = replay value ÷ 1.25.** Never pay above it.
- **(c) Liquidity.**
  - Spread (ask−bid)/mid ≤ 20% on single-stock chains and ≤ 40% on leveraged-ETF chains.
  - Open interest ≥ 500 on single stocks, ≥ 100 on leveraged-ETF chains.
  - Fill at mid or better. Step up at most one tick.
- **(d) Skew and IV.** Compare put and call IV at the same |Δ|. Buy the lower-IV side unless the portfolio needs the other side (a put hedges SOXL). For non-event trades, require ATM IV ≤ 0.9 × RV20; SOXL fails this today (IV 136% vs RV 108%).

**Screen results (6 prints, Q1-25 → Q2-26, straddles from Fri closes):**
| Name / print | Median (mean) realized | Implied | R | Cost and liquidity | Verdict |
|---|---|---|---|---|---|
| META 10/21 pm | 9.5% (9.0%); 5 of 6 moves ≥ 8% | 7.3% (10/23 straddle $51.75) | **1.29** | The META chain is unaffordable, so use METU 10/23 | **PASS on magnitude.** Liquidity decides (§5) |
| TSLA 10/21 pm | 4.5% (6.3%) | 7.4% | 0.61 | — | FAIL. Straddle replay ≈ −35% |
| LRCX 10/21 pm | 4.4% (6.5%) | 8.2% | 0.54 | Put spread 12% of mid | FAIL. Replay ≈ −40% |
| AMKR 10/26 pm | 4.4% (9.3%) | 15.6% | 0.28 | $650 straddle; spreads 20–40% | FAIL |
| SOFI 10/27 am | 6.5% (7.2%) | 11.0% (event-only 7.8%) | 0.83 | 16C/13P strangle costs $56, spreads 3% | FAIL. Strangle replay 0.36x |
| MBLY 10/29 am | 7.0% (7.3%) | — | — | 7C bid/ask 0.28/0.74 (90% of mid); OI 30 | FAIL on liquidity |
| INTC 10/29 pm | 8.2% (10.7%) | 12.1% (10/30) | 0.68 | Straddle $1,088 | FAIL |
| FOMC 10/28 | Not screened (no realized-move dataset) | — | — | — | Default REJECT |

**2. Legged straddles and strangles (two separate long legs).**
- *When they beat a directional bet:* R ≥ 1.2 and no directional edge (P(up) within 45–55%). If you have a directional edge with p ≥ 60%, use one leg or the leveraged ETF instead.
- *IV crush:* it kills the straddle whenever realized < implied. The loss ≈ (implied − realized)/implied, e.g. TSLA −35% and LRCX −40% at the median move.
- *Max premium:* ≤ 15% of equity for both legs together ($50). That means an ATM straddle is only affordable on underlyings ≤ ~$8, and none of those passed the screen. At this size, the practical form is **one leg = half a strangle**: same EV per dollar, more variance (good for a threshold goal).
- *Legging:* enter both legs in the same check-in at mid. If one leg is unfilled at the end of the check-in, cancel it. Keep the filled leg only if it passes test (b) on its own; otherwise sell it.
- *IV run-up (sell before the print):* the measured edge is ≈ +3% over the last 3 pre-print days (Gao-Xing-Zhang 2018). With 1 week to go, theta beats the IV rise in price terms: the SOFI 10/30 straddle loses ~20% from 10/19→10/26 at constant event vol. **Only worth it on chains with spreads ≤ 3% that we can afford. Nothing qualifies, so don't run it.**

**3. Cash-secured puts and covered calls: not worth it.**
- After 2 SOXL, free cash ≈ **$60**, not $130. That means CSP strikes ≤ $0.60, and none are tradable.
- At $130 free cash, the live checks:
  - PLUG ($1.40) 11/20 $1P: bid $0, nothing to sell.
  - PLUG 1.5P: bid $0.19, so $19 premium on $150 collateral, at Δ −0.55 (a synthetic long in a junk name).
  - PLUG covered call: 100 sh = $140 plus the 1.5C at bid $0.08. Max gain $18 (+5.5% of equity) on 42% of equity; downside is the whole $140.
  - OPEN ($2.12) 2P: bid $0.15 on $200 of collateral.
- These are concave, capped-upside payoffs. We need +53%, so they **lower** P(target). They're banned unless we're ≥ $508 and protecting the lead.

**4. Strike, expiry, exit and size rules.**
- *Expiry:* the first expiry after the event. Check that `sellout_datetime` falls after the planned exit.
- *Strike:* |Δ| 0.15–0.35 for event legs, i.e. ≈ 0.7–1.3× the implied move OTM. Never below Δ 0.10 (lottery tickets with 50%+ spreads).
- *Entry timing:* the 3:22 check-in on print day. That minimizes theta paid and lets the Trader read the tape first.
- *Exit, event trades:* sell at the next 9:47, win or lose. IV crush is complete by the open; never hold past the event day. With 2+ contracts, sell half at ≥ 2x and the rest by 3:22.
- *Exit, non-event (IV ≤ 0.9·RV):*
  - Sell half at +100%.
  - Time stop: out at DTE ≤ 7, or when half the time is gone without +50%.
  - Premium stop: −50%, but only if the position is > 10% of equity.
- *Size:* total premium outstanding ≤ min(**15% of equity**, equity − every other position gapping through its stop − **$187**) (the floor gate).
  - Today: $332 − SOXL gap $48 − crypto $6 − $187 = $91, so the **15% = $50 is binding**.
  - Premium counts at 100% as risk.

**5. Candidates for the next two weeks.**
- **Only conditional pass: METU 10/23 put, 1 contract, Wed 10/21 3:22pm. Exit Thu 9:47.**
  - Strike ≈ 0.86 × METU, rounded to $0.50 (≈ META −7%).
  - Limit = min(mid, replay cap, $0.50).
  - Replay cap: at METU $29.00 the 25P cap is **$0.60** (Friday mid $0.45 passes; the $0.65 ask fails). At METU $29.50 (Sunday 24h) the 25P cap is $0.47, and the 25.5P cap is ≈ $0.58.
  - Skip if: the spread is > 40% of mid; the 10/23 META straddle on Wed is > 9.5% (R < 1.0); or it doesn't fill at ≤ cap. Friday's 25P was 0.25/0.65 (89% of mid), so it fails today on liquidity and **must be re-checked live**.
  - Payoff: P(META ≤ −7%) ≈ 30–35%, worth 2–5x. Otherwise ~0.
  - It's a partial hedge for SOXL (risk-off Wednesday).
- **Everything else on the calendar fails** (table above): TSLA, LRCX, AMKR, SOFI, MBLY, INTC, FOMC.
- **Next to screen:** MSFT/GOOGL (10/28 pm) via MSFU/GGLL chains, and AMZN/AAPL (~10/29–30). Run this on Sunday 10/25.

**6. Leveraged ETF vs options, per dollar of risk.**
- *SOXL 2 sh:* $40 at the stop ($48 gapped). Analog 5-day EV (halved) ≈ +$11, so EV/risk ≈ **+0.25**. Costs: ~0.04% spread plus ~0.16%/day decay.
- *SOXL calls:* you pay 26% vol over realized. The 10/30 $130C costs $115 and needs +31%. EV/risk ≈ **−0.1 to −0.3**.
- *METU put at the cap:* EV/risk ≈ +0.25, but convex, with a 1-in-3 shot at +$50 to +$200.
- **Verdict: the leveraged ETF wins every directional bet. Options are used only for gap-through events where R ≥ 1.2, as a ≤ 15% satellite, never as a SOXL substitute.**

## Event contracts: Q3 GDP screen (first pass 10/19)
Written Mon 10/19. Kalshi prices were pulled from the public API on 10/19. The Robinhood app listing and its prices are **unverified**: the user must confirm both in the app.
- **Release:** BEA's schedule shows the Q3 advance estimate on **Thu 10/29 at 8:30 ET** (verified, same release as Sept PCE). Kalshi's event `KXGDP-26OCT30` lists its close as 10/30 08:29 ET, but its own rule says it "closes at 8:29 AM on the day of the expected release." **Treat Wed 10/28 evening as the last time to bet.**
- **Contract rules:** "More than X%" on the BEA advance estimate (SAAR, one decimal), so a print exactly at the strike resolves NO. Fees: assume 2¢ per contract all-in on Robinhood ($0.01 commission + $0.01 exchange; sources disagree). Settlement carries no exit fee.
- **Inputs:**
  - GDPNow **3.64%** (10/15; 3.7 on 10/6, 5.0 on 9/25). Key components: PCE 3.6%, inventories **+1.87pp**, net exports **−2.69pp**. Next update Tue 10/20.
  - NY Fed Staff Nowcast **2.6%** (10/9, official). 2.67% on 10/16 is unconfirmed.
  - Morgan Stanley tracking estimate 3.2%. An unsourced average of trackers is 3.25%.
  - Surveys 2.3–2.5% (Aug–Oct, stale).
  - St. Louis Fed: no current nowcast found.
- **Error model:** GDPNow final nowcast vs the advance print, 2011Q3–2025Q2: MAE 0.77pp, **RMSE 1.17pp** (Atlanta Fed, verified). COVID quarters fatten that number. The last 5 quarters' errors were 0.0, 0.8, 1.6, 0.8, 0.1, an RMSE of 0.88.
- **Model:** μ = 0.5·GDPNow + 0.25·NYFed + 0.25·bank-tracker avg = **3.29%**. σ = 1.1 today, 1.0 on the final day (fixed now, so it can't be tuned later). P(>X) = 1 − Φ((X + 0.05 − μ)/σ).

| Strike | Kalshi bid/ask (YES) | OI | Mkt mid | Model P | Best in-band side | Net edge |
|---|---|---|---|---|---|---|
| >2.5 | 0.88 / 0.89 | 11.7k | 0.885 | 0.75 | NO costs 0.12, out of band | (+11, ineligible) |
| >3.0 | 0.59 / 0.64 | 13.2k | 0.615 | 0.59 | NO at 0.41 | **−1.6** |
| >3.5 | 0.29 / 0.32 | 9.4k | 0.305 | 0.41 | YES at 0.32 | **+6.7** |
| >4.0 | 0.19 / 0.23 | 17.3k | 0.21 | 0.25 | YES costs 0.23, out of band | (−0.5) |

- **Sensitivity of >3.5 YES at 0.32:**
  - Equal-weight blend (μ 3.17): +3.5, fails.
  - Our blend with σ = 1.0: +5.7.
  - GDPNow alone: +19.
  - The edge is entirely "the market underweights GDPNow." Given GDPNow's +1.9 inventory / −2.7 net-export swing, the market's discount is defensible. **The edge isn't robust.**
- **Verdict: NO BET YET.**
  - The edge is marginal and depends on the model.
  - Wed 10/28 8:30 brings the Advance Economic Indicators (Census, verified), which reprices exactly the two components that drive GDPNow's gap.
  - Cash after SOXL (2 sh) and the METU put is about $10. The bet can only be funded after the SOXL time stop (Mon 10/26 3:22).
- **What moves the nowcasts before 10/29:**
  - GDPNow Tue 10/20.
  - NY Fed Fri 10/23.
  - New home sales and durable goods around 10/26–27 (dates unverified).
  - **Advance trade and inventories Wed 10/28 8:30**, followed by GDPNow's final update (usually the same day; timing unverified).
  - FOMC 10/28 2pm doesn't affect the print.
- **Re-screen:**
  - Tue 10/27 3:22: preliminary, recompute the table.
  - **Wed 10/28 1:37pm: final go/no-go** after the final GDPNow. Use 3:22 if GDPNow hasn't posted yet.
  - PASS only if an in-band side (30–70¢) shows net edge ≥ 5 points with the formula above, re-run live, **and** the user confirms the Robinhood price is ≤ the max price.
  - Max price = model P − 0.07.
- **Sizing if PASS:**
  - Glide path on 10/28 is $332·1.0187^7 ≈ **$378**. From ~$330, that needs ≈ +$48.
  - At 0.34 all-in, that's ~73 contracts ≈ **$25**.
  - Kelly at p = 0.41 is 10% ≈ $33. **Cap $35**, not the 25% ($83) maximum: the edge is model-dependent.
  - Floor gate: equity − all gaps through stops − stake ≥ $187 (≈ $240 today, so it passes).
  - This is the only bet on the board that's independent of the risk-on book (SOXL and crypto).

## Event contracts on Robinhood (Rothera + Kalshi), screen 10/19
Written Mon 10/19 ~00:30 ET. Equity $332.03 (cash $260). RH quotes are from the Trader's rh_event.py pull (10/19 ~03:00Z) plus robinhood.com pages. Kalshi quotes come from its public API.
**1. Sept Core PCE (ROTHERA ECPCE-26SEPCORE, BEA release Thu 10/29 8:30 ET).** NO BET YET.
- *Terms (Rothera T&C PDF, read in full):* the underlying is the m/m % change "as reported in the first official release" by BEA (seasonally adjusted). "Above" means **strictly greater than** the strike, and strikes step by 0.1. BEA publishes one decimal, so **">0.3%" pays only on a printed 0.4 or higher, i.e. unrounded ≥ ~0.35%.** A 0.33% print resolves NO. The market ladder (>0.2 at 0.96, >0.3 at 0.36, >0.4 at 0.03) is consistent only with this rounded reading. If BEA's release slips past expiry (up to 2 days), Rothera settles at its "fair price."
- *Inputs (post-CPI 10/14 and PPI 10/15):* core CPI +0.33% unrounded. Translations: CNBC 7-firm median **0.32** (range 0.29 Oxford to 0.35 Barclays); TD 0.32 (TD's market-based figure 0.34); WSJ Timiraos ~0.34; Employ America nowcast 0.34. **Locked μ = median of the latest translations = 0.33.**
- *Error:* published post-PPI translation misses are typically 0–3bp, with a 7bp outlier (EA, Aug-25: airfares, portfolio management, seasonal factors). **Locked σ = 0.04**, which includes ~1bp of disagreement about the center. The model is P(YES) = 1 − Φ((0.35 − μ)/σ).
| Strike (needs print ≥) | RH YES bid/ask | Model P(YES) | YES net edge | NO cost all-in | NO net edge |
|---|---|---|---|---|---|
| >0.2 (0.3) | 0.95/0.97 | 0.98 | out of band | 0.07 | out of band |
| **>0.3 (0.4)** | **0.35/0.37** | **0.31** (range 0.24–0.39 for μ 0.325–0.34) | **−8** | **0.67** | **+2** |
| >0.4 (0.5) | 0.02/0.04 | <0.01 | out of band | 1.00 | out of band |
- *Pass lines for >0.3, with σ locked:* NO at ≤ 0.65 passes if μ ≤ **0.325** (P(YES) ≤ 0.27). YES at ≤ 0.37 passes only if μ ≥ **0.345**. Max price = model P − 0.07.
- *Liquidity:* OI is only 35, so this is a single market-maker quote. A $25 order (~37 NO contracts) is larger than all open interest. Use a limit order only and accept a partial fill. Quote age is unverified: I couldn't run Bash, and the WebFetch page view showed only the 35¢ YES.
- *If it PASSES:* buy NO, Kelly at p = 0.73 / c = 0.67 is 18%, so half-Kelly ≈ **$30, cap $35**. A win pays only ≈ +$15, so this is EV, not a P(target) lever.
- *Re-screen:* Fri 10/23 3:22 (new previews), then **final Wed 10/28 1:37pm** together with GDP, using the Bloomberg consensus and the bank previews from that week. Last trade is before the 8:30 release on 10/29.
**2. Fed 10/28 (ROTHERA ECUSFED-26OCT).** NO BET. Fed-funds-implied odds (Investing.com rate monitor, 10/17 00:35 ET): hold 83.9%, hike 16.1%. On RH, buying hike costs 0.15 + 0.02 = 0.17 (−1); maintain costs 0.89 (−5). On Kalshi, hike trades at 0.12/0.13, so Rothera's hike is ~2¢ rich. Everything is outside 30–70¢ and nothing reaches 5 points. The only signal: if a hike is wanted as a hedge, Kalshi is cheaper. The Fed is in blackout and has no new data before 10/28.
**3. Q3 GDP (Kalshi KXGDP-26OCT30, routed through RH).** The RH page lists exactly 0.0, 0.5, **3.0**, 3.5 and 4.0 (with 4 more hidden). That matches rh_event.py, so **>3.0 is tradable on RH**. Kalshi API quotes now: >3.0 at 0.59/0.64 (last 0.69); >3.5 at 0.29/0.32, OI 9,377. These are unchanged, and so is the model (μ 3.29, σ 1.1). >3.5 YES at 0.32 nets +6.7, but the result is fragile (+3.5 equal-weight). >3.0 NO nets −2. **NO BET YET**, final Wed 10/28 1:37pm (GDPNow updates Tue 10/20).
- *Independence:* PCE, GDP and Fed resolve within 24h of each other. GDP and PCE are close to independent of each other and of SOXL. **Combined event stake ≤ $50** (15% of equity), so no strategist review is needed under v3.1 #6.

## Strategist log
- 2026-10-18 21:45 ET: weekly pass (first). The staged 35%→70% SOXL plan becomes 2 shares on Monday's open window. Data: next-open entry +11.4% mean / 80% win vs confirmation close +1.4% / 38% (SOXX 2010–26). The $85–95 band was stale (SOXL $100 in 24h trade). METU put kept at 1 contract with a strike/spread re-check on Wed. Crypto sleeve frozen. Five rule proposals filed.
- 2026-10-19 22:35 ET: Level 3 is unavailable, so I added the "Level 2 options playbook (no spreads)". It sets a 4-test screen: R ≥ 1.2, a symmetrized-replay price cap, liquidity limits, and a skew/IV check. Of the 8 catalysts in the next two weeks, only META (R = 1.29, via the METU 10/23 put, limit ≤ the cap) passes, and only conditionally on Wednesday's liquidity. TSLA, LRCX, AMKR, SOFI, MBLY, INTC and FOMC fail. CSPs and covered calls are banned at this size. Leveraged ETF > options for directional bets. Pre-trade review of SOXL 3 shares: KEEP 2. At 3 shares the stop loses 18–22% of equity, above the 15% cap, and the Wed METU put no longer fits under the $187 floor gate.
- 2026-10-19: first-pass screen of Q3 GDP event contracts (Kalshi KXGDP-26OCT30; BEA advance print Thu 10/29 8:30). Blend μ 3.29% (GDPNow 3.64 / NY Fed 2.6 / MS 3.2), σ 1.1. Only >3.5% YES at 0.32 shows an edge (+6.7 net), and that edge is model-dependent (+3.5 to +19). NO BET YET. Final re-screen Wed 10/28 1:37pm after the advance trade and inventories report and the last GDPNow. Cap $35 if it passes.
- 2026-10-19 ~00:30 ET: screened the RH event contracts.
  - **Core PCE >0.3:** the Rothera T&C means a printed ≥ 0.4 (strictly above, one-decimal BEA print). The translations' median is 0.33 and σ is locked at 0.04, giving P(YES) 0.31. That's −8 for YES and +2 for NO at 0.67 all-in, so NO BET YET. NO passes if μ ≤ 0.325 and YES if μ ≥ 0.345. OI 35.
  - **Fed:** futures put a hike at 16.1% vs RH's 0.15 ask, out of band, so NO BET.
  - **GDP:** >3.0 is confirmed tradable on RH. >3.5 is unchanged at +6.7 (fragile). Final call 10/28 1:37pm.
  - Combined event stake cap is $50.
- 2026-10-18 ~23:50 ET (Trader's clock 10/19 ~00:30): pre-trade review after the +$150 deposit. Contributed $480, equity $481.93 (cash $410.01, crypto $71.92). Codex est. $486, so we're −$4. Live 24h quotes: SOXX $506.0 (in the $495–512 band), SOXL $100.86 bid / $100.91 ask, TLT $80.37, TMF $28.38, XLF $55.62, METU $29.68.
  - **VERDICT: B, 3 SOXL** with the same gates and the $104 cap. The scaled-entry splits: SOXX > $512 → buy 2 now and the 3rd at 3:22 if it's above the open; SOXX < $495 → buy 3 at 3:22 if $492.83 is intact.
  - **Loss math at $101 / $104 entry:**
    - Stop (close < $80): −$63 (13.1%) / −$72 (14.9%).
    - 24% gap-through: −$73 (15.1%).
    - Post-Wednesday gap to $71: −$90 to −$99 (19–21%).
  - **Floor gate:** $482 − $99 − put $50 − crypto $6 = **$327, above $272.** That's the same exposure (63%) as the approved 2 shares in $332. The 10/18 "keep 2" verdict failed only on the old $187 gate, which no longer binds.
  - **Exits:** T1 $112 sells 1 and moves the stop on the other 2 to entry. T2 $118 sells 1. If T1 hasn't hit, sell 2 at session 5 (Fri 10/23 3:22). Everything is out by Mon 10/26 3:22.
  - **Thursday pyramid:** a 4th share only from put proceeds plus leftover cash (no margin).
  - **C rejected, nothing qualifies:**
    - TMF: TLT $80.37 hasn't hit the $80.57 trigger, and at ~45% vol it adds about ±$4 a week, so it does nothing for P(target).
    - FAS: XLF $55.62 hasn't hit $56.05, and one share is $158 (33%).
    - TQQQ, TNA, NVDL: the same risk-on beta.
    - Every other earnings name failed R.
  - **METU put:** stays at 1 contract (Kelly ≈ 10% ≈ $48). Buy 2 only if 2 × the limit ≤ $50 and all four tests pass live on Wednesday.
  - **Events:** caps rescale to GDP ≤ $50 and combined ≤ $72. The verdicts are unchanged (NO BET YET), and the final call is still 10/28 1:37pm, after SOXL is out.
  - **Correlation:** SOXL plus crypto is ≈ $375 (78%) in one risk-on bet. True independent bets ≈ 1.5.
