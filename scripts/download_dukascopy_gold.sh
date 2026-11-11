#!/usr/bin/env bash
# E042 (B46): download Dukascopy gold spot (xauusd) m1 bid+ask for the DEV block only (2015-2020), one CSV per year, into data/raw_gold
# (skips files that exist). Instrument: xauusd (minute candles from 2003-05-05 per dukascopy-node 1.51.1 metadata, checked R094); dukascopy-node 1.51.1. A failure does not fail the job: the E042 data gate records BLOCKED.
# Kept out of data/raw so the EUR/USD ingest never sees these files.
# Usage: IDX_FROM_YEAR=2015 IDX_TO_DATE=2021-01-01 bash scripts/download_dukascopy_gold.sh
set -euo pipefail
IDX_FROM_YEAR="${IDX_FROM_YEAR:-2015}"
IDX_TO_DATE="${IDX_TO_DATE:-2021-01-01}"
command -v dukascopy-node >/dev/null || npm i -g dukascopy-node@1.51.1
CHROME="$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)"
if [ -z "$CHROME" ]; then dukascopy-node --install-browser; fi
mkdir -p data/raw_gold
end_year="${IDX_TO_DATE:0:4}"
for inst in xauusd; do
  for year in $(seq "$IDX_FROM_YEAR" "$end_year"); do
    from="${year}-01-01"
    if [ "$year" = "$end_year" ]; then to="$IDX_TO_DATE"; else to="$((year + 1))-01-01"; fi
    [ "$from" = "$to" ] && continue
    for side in bid ask; do
      name="${inst}-m1-${side}-${year}"
      if [ -s "data/raw_gold/${name}.csv" ]; then echo "cached ${name}"; continue; fi
      dukascopy-node -i "$inst" -from "$from" -to "$to" -t m1 -p "$side" -f csv \
        -dir data/raw_gold -fn "$name" -bs 10 -bp 1500 -r 5 -rp 2000 -s ${CHROME:+--chrome-path "$CHROME"}
      test -s "data/raw_gold/${name}.csv" || { echo "download failed for ${name}"; exit 1; }
      echo "downloaded ${name}: $(wc -l < "data/raw_gold/${name}.csv") lines; head: $(sed -n 2p "data/raw_gold/${name}.csv")"
    done
  done
done
