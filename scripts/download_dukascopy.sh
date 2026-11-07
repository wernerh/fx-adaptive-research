#!/usr/bin/env bash
# Download Dukascopy EUR/USD m1 bid+ask, one CSV per year, into data/raw (skips files that exist).
# Usage: FROM_YEAR=2015 TO_DATE=2026-11-01 bash scripts/download_dukascopy.sh
set -euo pipefail
FROM_YEAR="${FROM_YEAR:-2015}"
TO_DATE="${TO_DATE:-2026-11-01}"
command -v dukascopy-node >/dev/null || npm i -g dukascopy-node@1.51.1
CHROME="$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)"
if [ -z "$CHROME" ]; then dukascopy-node --install-browser; fi
mkdir -p data/raw
end_year="${TO_DATE:0:4}"
for year in $(seq "$FROM_YEAR" "$end_year"); do
  from="${year}-01-01"
  if [ "$year" = "$end_year" ]; then to="$TO_DATE"; else to="$((year + 1))-01-01"; fi
  for side in bid ask; do
    name="eurusd-m1-${side}-${year}"
    if [ -s "data/raw/${name}.csv" ]; then echo "cached ${name}"; continue; fi
    dukascopy-node -i eurusd -from "$from" -to "$to" -t m1 -p "$side" -v -f csv \
      -dir data/raw -fn "$name" -bs 10 -bp 1500 -r 5 -rp 2000 -s ${CHROME:+--chrome-path "$CHROME"}
    test -s "data/raw/${name}.csv" || { echo "download failed for ${name}"; exit 1; }
  done
done
