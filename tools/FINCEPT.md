# FinceptTerminal data scripts

[FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) (AGPL-3.0) is a C++/Qt desktop app; the GUI can't run here. Its `fincept-qt/scripts/*.py` are standalone CLI data fetchers that print JSON, and those we use. `tools/fincept.sh` clones the repo and builds a venv on first use (~1 min), then runs a script. Not vendored into this repo.

Output is third-party data: check it against Robinhood before trading on it. Robinhood stays the source of truth for prices, positions and orders.

## Tested 2026-10-19 (work with no API key)
| Need | Command |
|---|---|
| Quote (Yahoo) | `tools/fincept.sh yfinance_data.py quote SOXX` |
| **Long daily history for backtests** (SOXX back to 2008, 4,728 bars) | `tools/fincept.sh yfinance_data.py historical SOXX 2008-01-01 2026-10-17` |
| VIX latest | `tools/fincept.sh cboe_vix_data.py current` |
| VIX history / futures term structure | `tools/fincept.sh cboe_vix_data.py history VIX` · `... term_structure` |
| Treasury average rates | `tools/fincept.sh treasury_data.py interest_rates "Treasury Bills" 2026-09-01 2026-10-17` |

`yfinance_data.py` also has: batch_quotes, info, financials, company_profile, financial_ratios, historical_period, search, news (news returned empty in testing).

## Available but need a key or extra installs (untested)
fred_data.py / fred_economic_data.py (FRED key), bea_data.py (BEA key), polygon_io_data.py, tiingo_data.py, finnhub_data.py, alphavantage_data.py (keys); prediction_kalshi.py (Kalshi API key, mostly order commands); cftc_data.py (COT positioning), cboe_data.py, derivatives_pricing.py (option/bond pricing; argparse subcommands), quantstats_analysis.py (needs quantstats), Analytics/backtesting/* (vectorbt, backtesting.py; heavy installs). economic_calendar.py needs Selenium + Chrome: skip it.

## Who uses it
- The Trader and research subagents (they have Bash).
- The strategist has no Bash by design (read-only). For long-history backtests it asks a research subagent to run these commands.
