#!/usr/bin/env bash
# E052 (B64): download Dukascopy BTC/USD (btcusd) m1 bid+ask for the DEV block only (2017-05-07 to 2021-01-01), one CSV per year,
# into data/raw_btc (skips files that exist). Instrument: btcusd (hourly/daily candles and ticks from 2017-05-07 per dukascopy-node
# 1.51.1 metadata, checked R307); dukascopy-node 1.51.1. A failure does not fail the job: the E052 data gate records BLOCKED.
# Kept out of data/raw so the EUR/USD ingest never sees these files.
# Usage: BTC_FROM=2017-05-07 BTC_TO_DATE=2021-01-01 bash scripts/download_dukascopy_btc.sh
set -euo pipefail
BTC_FROM="${BTC_FROM:-2017-05-07}"
BTC_TO_DATE="${BTC_TO_DATE:-2021-01-01}"
command -v dukascopy-node >/dev/null || npm i -g dukascopy-node@1.51.1
CHROME="$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)"
if [ -z "$CHROME" ]; then dukascopy-node --install-browser; fi
mkdir -p data/raw_btc
start_year="${BTC_FROM:0:4}"
end_year="${BTC_TO_DATE:0:4}"
for inst in btcusd; do
  for year in $(seq "$start_year" "$end_year"); do
    if [ "$year" = "$start_year" ]; then from="$BTC_FROM"; else from="${year}-01-01"; fi
    if [ "$year" = "$end_year" ]; then to="$BTC_TO_DATE"; else to="$((year + 1))-01-01"; fi
    [ "$from" = "$to" ] && continue
    for side in bid ask; do
      name="${inst}-m1-${side}-${year}"
      if [ -s "data/raw_btc/${name}.csv" ]; then echo "cached ${name}"; continue; fi
      dukascopy-node -i "$inst" -from "$from" -to "$to" -t m1 -p "$side" -f csv \
        -dir data/raw_btc -fn "$name" -bs 10 -bp 1500 -r 5 -rp 2000 -s ${CHROME:+--chrome-path "$CHROME"}
      test -s "data/raw_btc/${name}.csv" || { echo "download failed for ${name}"; exit 1; }
      echo "downloaded ${name}: $(wc -l < "data/raw_btc/${name}.csv") lines; head: $(sed -n 2p "data/raw_btc/${name}.csv")"
    done
  done
done
