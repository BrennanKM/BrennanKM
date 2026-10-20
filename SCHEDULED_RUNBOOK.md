# Scheduled check-in runbook (single source for every scheduled run)

Each scheduled task passes only its TYPE (OPEN, CLOSE, MIDDAY, WEEKEND, PRE-FOMC) and points here. If this file and a task prompt disagree, this file wins. Repo: `/Users/Brenn/Developer/BrennanKM`, branch `claude/new-session-z2huzr`. Robinhood account 994587087 (crypto calls take `rhs_account_number` 994587087).

## 0. Hard limits (read first)
- **The assistant does not place, cancel or modify orders** (buy, sell, stop, limit, options, crypto). It writes the exact order into `ORDERS.md` and sends a PushNotification `ORDER for you: <order>`; Brennan places it in the Robinhood app. Existing GTC stops at Robinhood keep protecting the account. Lifted only if Brennan says so in chat.
- Event contracts: Claude picks, Brennan places (unchanged).
- No thesis block in `trades.md`, no recommended order. Post-mortem when a trade closes.
- Floor: equity < $185 -> recommend nothing new, write `postmortem.md`, notify.

## 1. Bootstrap
1. `cd /Users/Brenn/Developer/BrennanKM` (clone `https://github.com/BrennanKM/BrennanKM` there if missing), then `git fetch origin claude/new-session-z2huzr && git checkout claude/new-session-z2huzr && git pull`.
2. Double-run guard: if `git log -3 --format='%an %cr'` shows a commit from the last 10 minutes that is not yours, another check-in is running. Stop and PushNotification instead of duplicating.
3. Robinhood tools come from the Robinhood connector (load via ToolSearch if deferred). If it cannot be reached after one retry: note it at the top of `SCOREBOARD.md`, commit and push, PushNotification "Check-in could not reach Robinhood; stops at Robinhood still active", stop.

## 2. Read (in this order, nothing else unless needed)
`STATE.md` -> `ORDERS.md` -> `SCOREBOARD.md` "Next actions" -> the mandate at the bottom of `TRADER_PROMPT.md` (newest wins). Open `trades.md` (tail ~80 lines), `STRATEGY.md`, `WATCHLIST.md` only when today's calendar item needs them. `ARCHIVE.md` is history; do not read it for instructions.

## 3. Reconcile with Robinhood
Pull portfolio, equity/crypto/option positions and all open orders (equity, crypto, option). Compare with `state.json`:
- Positions, quantities, and every stop (id, trigger, quantity) must match. A fill, a triggered stop, a partial fill or a cancelled order is the headline: update `state.json` first, write a line in `trades.md` (post-mortem if a trade closed), and notify.
- Then run, with live numbers (equity from `total_value`, marks from quotes/mark price, cash, and each live stop as `SYM=qty@trigger`):
  `python3 tools/gates.py --equity <E> --cash <C> --mark SOXL=<px> --mark ETH=<px> --mark BTC=<px> --stop SOXL=3@76 --stop ETH=<q>@<t> --stop BTC=<q>@<t> --save --render`
  Any FAIL (stop coverage, floor, floor-distance, event cap, PDT) is the first item in the notification and in `ORDERS.md`.
- When you move a stop or change a position, update `rule_stop`, `gap_price`, `backstop_stop`, `price_rules` and `calendar` in `state.json` and re-render. `STATE.md` is generated; never hand-edit it.

- Alerts: `get_alerts` must still contain the levels listed under `alerts` in state.json; if a rule level moves (stop, target), add the matching alert and update state.json.
- FRED: if `open_items` still has the FRED line, run `python3 tools/fred.py --check` and report one line.

## 4. Apply the rules
- Re-test every holding against its invalidation (`state.json` price_rules, `SCOREBOARD.md`, `trades.md`). Daily-close rules are judged at the CLOSE check-in using the live price at 3:22pm ET, before the 4pm close; send the order notification as early in the run as possible.
- Execute nothing yourself. For each rule that fires, add a block to `ORDERS.md` (status PENDING): symbol, side, quantity, type, price, TIF, the existing order id to cancel first, why, and the deadline. PushNotification it.
- Do what today's `calendar` entry says (state.json lists the next dated actions).
- Hunt only if warranted; discipline in `SCOREBOARD.md` Next actions. Every idea needs a full thesis block in `trades.md` first. Strategist gate (position >= 25% of equity or event stake >= 15%): spawn a subagent told to read `.claude/agents/strategist.md` in mode 2 and follow APPROVE/RESIZE/REJECT; log the verdict.
- Event contracts: refresh quotes with `python3 tools/rh_event.py <path>`, run any screen the calendar schedules today. A play that passes every gate becomes "Place now" in `dashboard/plays.json` and a PushNotification `EVENT ORDER for you: <contract> <side> <qty> @ <= <price>`.

## 5. Measurement (every run)
- Any probability used in a decision gets logged: `python3 tools/track.py cal add --id <ID> --claim "..." --p <ours> [--market <price>] --resolve-by <date> --src <file>`. Log it BEFORE the outcome is known.
- Resolve due claims: `python3 tools/track.py cal report` lists DUE rows; then `cal resolve --id <ID> --outcome 0|1`.
- **CLOSE check-in only:** log the regular-session closes: `python3 tools/track.py bench log --equity <E> --spy <px> --qqq <px> --soxl <px> --eth <px> --btc <px>`, then `bench report`. One line of the final message states "decisions added vs frozen book: +/-$X".

## 6. Dashboard (Rip City Ledger, https://claude.ai/artifact/QXgQDxzX7dvyhKdskrY7j1)
Live Robinhood data refreshes itself. At every check-in: append `{at, equity, contributed:480, note}` to `dashboard/curve.json`; sync `dashboard/ledger.json` with `trades.md` (status, fills, lessons); sync `dashboard/plays.json`; if Brennan reported Codex's value, `dashboard/rival.json`. Upload each changed file with the Artifact tool (action publish, the url above, `asset:true`, `file_path`), then ArtifactData `update` on collection "datasets", doc_id "curve" / "ledger" / "plays" / "rival" with the new `source:{kind:"file", url:"/_blob/...", name}` and `updated:{at, by:"Claude"}`; read the current version first and pass it as `if_version`. Also read `data/users/me/check` once and fix any page error it names. Plays card: statuses Place now / Placed / Filled / On deck / Screening / Won / Lost / No bet; fields contract, side, qty, max_price, stake_usd, pays_usd, place_by, next_screen, quote, model_prob, edge_pts, why, result, decide_at, instruction. A "Place now" play REQUIRES side, qty, max_price, stake_usd and place_by (the card builds the order steps from them). `instruction` is one plain sentence telling Brennan what to do ("Don't buy this..." when nothing passes).

## 7. Types
- **OPEN (weekday 9:47 ET):** reconcile, gap/overnight review (SOXL vs SOXX vs rules, crypto vs stops), anything the calendar schedules for the morning.
- **CLOSE (weekday 3:22 ET):** daily-close rules and hold-through-catalyst decisions happen HERE. Benchmark row. Update `MANUAL_FALLBACK.md` if any position, stop or exit date changed.
- **MIDDAY (Wed 10/21 12:37 ET):** pre-screen the METU 10/23 put per `SCOREBOARD.md`/`STRATEGY.md`; do not recommend the order until the 3:22 decision unless the quote will not survive.
- **PRE-FOMC (Wed 10/28 13:37 ET):** final event screens and the ETH exit, fast, before the 2:00pm decision.
- **WEEKEND (Sat/Sun 8:13pm ET):** crypto only (stops intact, levels). **Sunday also:** WEEKLY SWEEP: 2-3 read-only research subagents in parallel (earnings Mon-Fri with implied vs realized moves; macro calendar incl. `python3 tools/rh_event.py --list economics`; leveraged-ETF setups with triggers), rewrite `WATCHLIST.md`, then the strategist (mode 1) rewrites `STRATEGY.md`; accept or reject each rule proposal in `trades.md` with a reason; Sunday glide-path check from `gates.py`; ask Brennan for Codex's latest value only (he will not share its holdings).

## 8. Finish
Commit (message ends with `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`) and `git push origin claude/new-session-z2huzr` (retry up to 4 times). PushNotification (one line, under 200 chars) on: a fill, a triggered stop, any order Brennan must place, an event play turning "Place now", a gate FAIL, equity moving >= 5% since the last snapshot, or a Robinhood failure. Final message: first line = one-line summary leading with what matters, e.g. "ORDER for you: ..." or "No change. Equity $474 (-1.1%), decisions added -$X vs frozen book."
