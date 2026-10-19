# STATE (generated: do not edit; edit state.json, then `python3 tools/gates.py --render`)
As of Mon 2026-10-19 19:00 ET · mandate v4 (+v3.1 events) · deadline 2026-11-18

**Equity $470.64** (-1.95% on $480.00) · cash $122.20 · glide $482.00 (behind $11.36) · Codex $479.00 (behind $8.36, as of 2026-10-19 PM (user report))
Targets $739.00 / $1,109.00 · floor $185.00 · floor-distance gate $272.00 · ratchet $640.00 once >= target 1 · event stake <= $72.00 ($50.00 if model-dependent)

## Positions and protection
| Holding | Qty | Cost | Mark | P&L | Rule stop | Order at Robinhood | Notes |
|---|---|---|---|---|---|---|---|
| SOXL | 3 | 102.55 | 99.30 | -9.75 | daily CLOSE < $80 (decided at the 3:22pm check-in) | stop market 76 x3 GTC `6ad61fee-3895-47f6-92e9-efcfd94ff88e` | Stop order holds all 3 shares: cancel it before any sell, then re-place on what remains. |
| ETH | 0.012738 | 2,354.99 | 2,403.49 | +0.62 | stop order $2,300 | stop 2300 x0.012738 GTC `6ad56199-5a5d-4192-a7f6-69366deb1b1e` | Target $2,580. Out before 2pm ET Wed 10/28 unless >= +5% ($2,473). |
| BTC | 0.00024285 | 82,354.09 | 81,997.04 | -0.09 | stop order $78,900 | stop 78900 x0.00024285 GTC `6ad48095-9b1b-41b9-b508-62475232d2b0` | Target $85,000: at BTC >= $84,600 cancel the stop and place a sell limit at $85,000. |

## Price and time rules
- SOXL >= $112 (T1): cancel stop 6ad61fee, sell 1 share, re-place a stop on the other 2 at $102.55.
- SOXL >= $118 (T2): sell 1 more share.
- SOXL daily CLOSE < $80 (judged at 3:22pm): cancel the stop, sell all.
- SOXX daily CLOSE < $495 (gap-and-fail): sell all SOXL.
- SOXL not at T1 by Fri 10/23 3:22pm: sell 2 shares. ALL out by Mon 10/26 3:22pm ET regardless.
- Day-trade rule: selling a stock bought the same day uses 1 of 3 PDT day trades; spend them only on emergency exits.

## Gates (from tools/gates.py)
- **PASS** stop coverage SOXL: stop qty 3 vs position 3 (trigger 76)
- **PASS** stop coverage ETH: stop qty 0.012738 vs position 0.012738 (trigger 2300)
- **PASS** stop coverage BTC: stop qty 0.00024285 vs position 0.00024285 (trigger 78900)
- **PASS** floor (stop trading below): equity $470.64 vs floor $185.00
- **PASS** floor-distance gate: $470.64 - gaps $89.39 - premium $0.00 - event stake $0.00 = $381.25 vs $272.00
- **PASS** event stake cap: $0.00 vs cap $72.00 (Kelly cap $50.00 if model-dependent)
- **PASS** PDT day trades: 0 used in last 5 business days (max 3); 3 left
- **PASS** max loss per trade <= 15%: SOXL loss at its rule stop $57.90 = 12.3% of equity
- **PASS** mark vs reported equity: marks+cash $470.63 vs equity $470.64 (diff $-0.01); fix state.json if large

## Next dated actions (ET)
- Tue 10/20 09:47: OPEN check-in. Re-test SOXL/SOXX vs rules; first run of the new schedule and gates.py.
- Tue 10/20 15:22: CLOSE check-in. SOXL close rule (<$80) and SOXX < $495 rule. NFLX reports after the close.
- Wed 10/21 12:37: MIDDAY. Pre-screen the METU 10/23 put (four tests, spread <= 40% of mid, OI >= 100, META straddle <= 9.5%).
- Wed 10/21 15:22: DECIDE (a) METU 10/23 put, 1 contract, limit <= min(mid, replay cap, $0.50), gate >= $272; (b) hold SOXL through LRCX/META/TSLA/TXN/IBM earnings only if SOXX >= $495 AND floor-distance gate passes with SOXL gapping to $71 (plus put premium).
- Thu 10/22 09:47: Exit the put (win or lose). Exit SOXL if the prints broke the thesis. A 4th SOXL share only if SOXL >= +10% over fill, funded by put proceeds/spare cash.
- Fri 10/23 15:22: SOXL session-5 rule: sell 2 if T1 ($112) not hit. Re-screen core PCE >0.3 (Rothera ECPCE-26SEPCORE).
- Mon 10/26 15:22: SOXL fully out, no matter what.
- Tue 10/27 15:22: Re-screen Q3 GDP >3.5 (KXGDP-26OCT30) with latest GDPNow / NY Fed.
- Wed 10/28 13:37: FINAL event screen (GDP >3.5, core PCE >0.3). ETH out before 2:00pm FOMC unless >= +5%.
- Thu 10/29 08:30: GDP advance + Sept PCE release. Event contracts close 8:29am.

## Event plays (user places by hand)
- Q3 GDP > 3.5% YES: **No bet**. RH 39/42c on 10/19 PM; locked model ~41%: no edge. Final screen 10/28 13:37.
- Sept core PCE > 0.3% (printed >= 0.4): **No bet**. RH 32/33c, OI 35; model P(YES) 0.31. NO passes if center <= 0.325; YES if >= 0.345.
- Fed Oct 28: **No bet**. Hike 14/15c vs futures 16%: fair.

## Standing rules
- Execution: the assistant does NOT place/cancel/modify orders. It writes the exact order into ORDERS.md (and the thesis into trades.md) and PushNotifications 'ORDER for you: ...'; the user places it in the app.
- Thesis block in trades.md BEFORE any order is recommended; post-mortem when a trade closes.
- Every holding has a full-quantity stop at Robinhood at all times (gates.py checks coverage).
- Options: Level 2 only, four-test screen in STRATEGY.md; CSPs/covered calls banned until equity >= $508.
- Crypto: new entries need a written level, target >= 6% away (3x the 1.9% spread) and a stop at the fill. No resting buys that could fill unprotected for > 12h.
- Events: Claude picks, the user places by hand. Gates in TRADER_PROMPT v3.1; stake <= $72 total, <= $50 when model-dependent.
- Floor: equity < $185 -> stop recommending trades, write postmortem.md. Ratchet: at >= $739 never risk below $640.
- Log every probability used in a decision with `python3 tools/track.py cal add ...`; log the benchmark row at every CLOSE check-in.

## Open items
- FRED_API_KEY: not set in the assistant's shell on 10/19; confirm it is available to scheduled runs, then delete this line.
- Codex holdings unknown (only its value is reported); ask the user for positions daily.
- Pending deposit of $200 still displays in Robinhood but is not in total_value; cash + holdings already reconcile to $480 contributed.
