#!/usr/bin/env python3
"""FRED helper. Reads the key from $FRED_API_KEY or from the file ~/.config/fred_api_key (chmod 600).
The key is never printed. Scheduled runs started by the desktop app do not necessarily inherit shell
variables, so the file is the reliable place for it.

  python3 tools/fred.py --check                         # is a key available? (prints yes/no only)
  python3 tools/fred.py GDPNOW --limit 10               # latest observations of a series
  python3 tools/fred.py GDPNOW --vintages --limit 30    # ALFRED vintages: how the nowcast moved (if the series keeps them)
  python3 tools/fred.py PCEPILFE --units pch --limit 6  # core PCE m/m % change (units pch = percent change)
Series ids are unverified until a key exists: `--check` first, then confirm the id by running it once.
"""
import argparse, json, os, sys, urllib.parse, urllib.request
from pathlib import Path

KEYFILE = Path.home() / ".config" / "fred_api_key"


def get_key():
    k = os.environ.get("FRED_API_KEY", "").strip()
    if k:
        return k
    try:
        if KEYFILE.exists():
            if KEYFILE.stat().st_mode & 0o077:
                print(f"warning: {KEYFILE} is readable by others; run: chmod 600 {KEYFILE}", file=sys.stderr)
            return KEYFILE.read_text().strip()
    except OSError:
        pass
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("series", nargs="?")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--units", default="lin")
    ap.add_argument("--start", help="observation_start YYYY-MM-DD")
    ap.add_argument("--vintages", action="store_true", help="realtime window = all vintages (ALFRED)")
    a = ap.parse_args()
    key = get_key()
    if a.check:
        print("FRED key: yes" if key else "FRED key: NO (set $FRED_API_KEY or create ~/.config/fred_api_key with chmod 600)")
        sys.exit(0 if key else 1)
    if not key:
        sys.exit("No FRED key found (env FRED_API_KEY or ~/.config/fred_api_key). Run with --check.")
    if not a.series:
        sys.exit("give a series id, e.g. GDPNOW")
    q = {"series_id": a.series, "api_key": key, "file_type": "json", "sort_order": "desc", "limit": a.limit, "units": a.units}
    if a.start:
        q["observation_start"] = a.start
    if a.vintages:
        q.update(realtime_start="1776-07-04", realtime_end="9999-12-31")
    url = "https://api.stlouisfed.org/fred/series/observations?" + urllib.parse.urlencode(q)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.load(r)
    except Exception as e:  # never echo the URL: it contains the key
        sys.exit(f"FRED request failed: {type(e).__name__}: {getattr(e, 'code', '')} {getattr(e, 'reason', '')}".strip())
    for o in data.get("observations", []):
        extra = f"  (vintage {o['realtime_start']})" if a.vintages else ""
        print(f"{o['date']}  {o['value']}{extra}")


if __name__ == "__main__":
    main()
