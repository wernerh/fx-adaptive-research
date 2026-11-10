#!/usr/bin/env bash
# E034 (B30): download Dukascopy index CFD m1 bid+ask for the DEV block only, one CSV per year, into data/raw_index
# (skips files that exist). Instruments: eusidxeur (EU Stocks 50, EUR), usa500idxusd (US 500, USD); dukascopy-node 1.51.1.
# Kept out of data/raw so the EUR/USD ingest (glob *bid*/*ask* in data/raw) never sees these files.
# Usage: IDX_FROM_YEAR=2015 IDX_TO_DATE=2021-01-01 bash scripts/download_dukascopy_index.sh
set -euo pipefail
IDX_FROM_YEAR="${IDX_FROM_YEAR:-2015}"
IDX_TO_DATE="${IDX_TO_DATE:-2021-01-01}"
command -v dukascopy-node >/dev/null || npm i -g dukascopy-node@1.51.1
CHROME="$(command -v google-chrome || command -v chromium || command -v chromium-browser || true)"
if [ -z "$CHROME" ]; then dukascopy-node --install-browser; fi
mkdir -p data/raw_index
end_year="${IDX_TO_DATE:0:4}"
for inst in eusidxeur usa500idxusd; do
  for year in $(seq "$IDX_FROM_YEAR" "$end_year"); do
    from="${year}-01-01"
    if [ "$year" = "$end_year" ]; then to="$IDX_TO_DATE"; else to="$((year + 1))-01-01"; fi
    [ "$from" = "$to" ] && continue
    for side in bid ask; do
      name="${inst}-m1-${side}-${year}"
      if [ -s "data/raw_index/${name}.csv" ]; then echo "cached ${name}"; continue; fi
      dukascopy-node -i "$inst" -from "$from" -to "$to" -t m1 -p "$side" -f csv \
        -dir data/raw_index -fn "$name" -bs 10 -bp 1500 -r 5 -rp 2000 -s ${CHROME:+--chrome-path "$CHROME"}
      test -s "data/raw_index/${name}.csv" || { echo "download failed for ${name}"; exit 1; }
      echo "downloaded ${name}: $(wc -l < "data/raw_index/${name}.csv") lines; head: $(sed -n 2p "data/raw_index/${name}.csv")"
    done
  done
done
