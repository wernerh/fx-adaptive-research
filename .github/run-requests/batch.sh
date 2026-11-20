# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-20 R308 E052 (B64) lagged daily Bitcoin return -> next-day EUR/USD, s = sign(ln BTC mid 16:00 NY D / previous
# trading date), EUR/USD 16:00 NY D -> 16:00 NY next date, dev dates 2017-05-09..2020-12-31, DEV block only, 1 trial, block-20
# bootstrap, p < 0.05, mean > 1 pip, >= 500 dates. Pre-registered in experiments/2026-11-20_E052_btc_lag/. No val, no OOS.
# Phase 1 downloads Dukascopy btcusd m1 bid/ask 2017-05-07..2021-01-01 only (dev). A download failure is recorded by the data gate.
set -euo pipefail
mkdir -p backtests/validation_reports
bash scripts/download_dukascopy_btc.sh 2>&1 | tee backtests/validation_reports/E052_download.txt || echo "BTC download failed; E052 data gate decides"
python scripts/run_e052_btc_lag.py | tee backtests/validation_reports/E052_results.txt
