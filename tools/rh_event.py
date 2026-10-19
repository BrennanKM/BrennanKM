#!/usr/bin/env python3
"""Pull live Robinhood prediction-market quotes from the public event page (no login).

Usage:
  python3 tools/rh_event.py <event-url-or-path> [--json]
  python3 tools/rh_event.py --list <category>      # list event paths, e.g. economics
Example:
  python3 tools/rh_event.py economics/events/us-real-gdp-growth-in-q3-2026-oct-30-2026

Reads the page's embedded __NEXT_DATA__ JSON (props.pageProps.event): each contract's
symbol, listing exchange (KALSHI or ROTHERA, Robinhood's own exchange), whether Robinhood
lets you trade it, YES/NO bid/ask, open interest and quote time. These are the prices
Robinhood shows in the app.
"""
import json, re, subprocess, sys

BASE = "https://robinhood.com/us/en/prediction-markets/"

def get(url):
    return subprocess.run(["curl", "-sS", "-L", "-m", "30", url],
                          capture_output=True, text=True, check=True).stdout

def next_data(html, url):
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        sys.exit(f"no __NEXT_DATA__ at {url} (page missing or layout changed)")
    return json.loads(m.group(1))

def list_events(category):
    url = BASE + category.strip("/") + "/"
    for path in sorted(set(re.findall(r'href="/us/en/prediction-markets/(' + re.escape(category.strip("/")) + r'/events/[^"]+)"', get(url)))):
        print(path)

def event(path):
    url = path if path.startswith("http") else BASE + path.strip("/") + "/"
    props = next_data(get(url), url)["props"]["pageProps"]
    ev = props["event"]
    quotes = props.get("quotes") or {}
    fund = props.get("fundamentals") or {}
    rows = []
    for c in ev["eventContracts"].values():
        q, f = quotes.get(c["id"], {}), fund.get(c["id"], {})
        rows.append({
            "name": c.get("displayLongName") or c.get("name"),
            "symbol": c.get("symbol"),
            "exchange": (c.get("exchange") or "").replace("EXCHANGE_SOURCE_", ""),
            "tradable_on_robinhood": c.get("tradability") == "EVENT_CONTRACT_TRADABILITY_TRADABLE",
            "yes_bid": q.get("yes_bid_price"), "yes_ask": q.get("yes_ask_price"),
            "no_bid": q.get("no_bid_price"), "no_ask": q.get("no_ask_price"),
            "open_interest": f.get("open_interest"), "volume": f.get("volume"),
            "quote_time": q.get("ask_venue_timestamp") or q.get("bid_venue_timestamp"),
            "expected_expiration": c.get("expectedExpirationTime"),
            "fractional": c.get("isFractionable"),
        })
    return url, rows

def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if sys.argv[1] == "--list":
        return list_events(sys.argv[2])
    url, rows = event(sys.argv[1])
    if "--json" in sys.argv:
        print(json.dumps({"url": url, "contracts": rows}, indent=1))
        return
    print(url)
    for r in rows:
        flag = "" if r["tradable_on_robinhood"] else "  [NOT TRADABLE ON RH]"
        print(f"{r['name']:<24} {r['symbol']:<24} {r['exchange']:<8} YES {r['yes_bid']}/{r['yes_ask']}  "
              f"NO {r['no_bid']}/{r['no_ask']}  OI {r['open_interest']}  @ {r['quote_time']}{flag}")

if __name__ == "__main__":
    main()
