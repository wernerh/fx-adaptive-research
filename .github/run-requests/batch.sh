# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-11 R094 E042 (B46) lagged daily gold return -> next-day EUR/USD: position -sign(ln XAU/USD 16:00 London D /
# previous date), hold 16:05 London D -> 16:00 London next date, DEV block only, 1 trial, p < 0.05.
# Pre-registered in experiments/2026-11-11_E042_gold_lag/. No val, no OOS.
# The gold download (dev dates only) may fail without failing the job: the E042 data gate then records BLOCKED (0 trials).
set -euo pipefail
mkdir -p backtests/validation_reports
bash scripts/download_dukascopy_gold.sh 2>&1 | tee backtests/validation_reports/E042_gold_download.log \
  || echo "GOLD DOWNLOAD FAILED (E042 data gate will record BLOCKED)" | tee -a backtests/validation_reports/E042_gold_download.log
python scripts/run_e042_gold_lag.py | tee backtests/validation_reports/E042_results.txt
