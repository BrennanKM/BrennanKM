#!/usr/bin/env bash
# Run one of FinceptTerminal's standalone Python data scripts.
# Clones the repo and builds a small venv on first use (the container is ephemeral).
#   tools/fincept.sh yfinance_data.py historical SOXX 2008-01-01 2026-10-17
set -euo pipefail
BASE=/home/user; [ -d /home/user ] || BASE="$HOME"
REPO="$BASE/fincept-corporation/finceptterminal"
VENV="$BASE/fincept-venv"
if [ ! -d "$REPO/.git" ]; then
  mkdir -p "$(dirname "$REPO")"
  GIT_LFS_SKIP_SMUDGE=1 git clone -q --depth 1 https://github.com/Fincept-Corporation/finceptterminal "$REPO" >&2
fi
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV" >&2
  "$VENV/bin/pip" install -q numpy "pandas<3" yfinance==0.2.66 curl_cffi==0.13.0 requests beautifulsoup4 ta==0.11.0 scipy >&2
fi
[ $# -ge 1 ] || { echo "usage: tools/fincept.sh <script.py> [args...]" >&2; exit 2; }
cd "$REPO/fincept-qt/scripts"
exec "$VENV/bin/python" "$@"
