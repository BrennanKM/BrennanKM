# If the check-ins stop (Claude out of usage)

Robinhood keeps protecting the account on its own: every stop order below is a GTC order at Robinhood. What stops is everything that needs judgment: profit-taking, time stops, earnings decisions. Open the Robinhood app and do this yourself.

## Positions as of 2026-10-19 close
| Holding | What's already at Robinhood | What you do by hand |
|---|---|---|
| SOXL, 3 shares @ $102.55 | Stop order sells all 3 at $76 | **Sell all 3 by Mon 10/26 before 4pm ET, whatever the price** (time stop: SOXL is a 3x ETF and decays). Sell earlier if it closes below $80, or sell 1 if it reaches $112. To sell, first cancel the $76 stop order (it holds the shares), then sell. |
| ETH, 0.012738 | Stop order at $2,300 | Sell before 2pm ET Wed 10/28 (Fed decision), unless it's up 5%+ from $2,355. |
| BTC, 0.00024285 | Stop order at $78,900 | Nothing. The stop handles it. |
| Cash | — | Don't buy anything new without a plan. |

## Event contracts
Don't buy any. If the dashboard's Your plays card isn't red, there's no order.

## Restarting
Everything (rules, trades, scoreboard, dashboard data) is in the GitHub repo, branch `claude/new-session-z2huzr`. A new Claude session pointed at the repo can pick up from SCOREBOARD.md "Next actions". CHECKIN_PROMPT.md is a self-contained check-in prompt for a claude.ai routine with the Robinhood connector attached.
