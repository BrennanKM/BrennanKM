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

## Strategist log
- 2026-10-18 21:45 ET: weekly pass (first). The staged 35%→70% SOXL plan becomes 2 shares on Monday's open window. Data: next-open entry +11.4% mean / 80% win vs confirmation close +1.4% / 38% (SOXX 2010–26). The $85–95 band was stale (SOXL $100 in 24h trade). METU put kept at 1 contract with a strike/spread re-check on Wed. Crypto sleeve frozen. Five rule proposals filed.
