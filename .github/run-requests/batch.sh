# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R072 E034 (B30) month-end pre-fix equity-hedging flow (Melvin-Prins): position -sign(EU50 minus US500
# month-to-date log return), windows 15:00 -> 16:00 London on D and 16:00 London D-1 -> 16:00 London D, DEV block only, 2 trials.
# Pre-registered in experiments/2026-11-10_E034_month_end_hedging/. No val, no OOS.
# The index download may fail without failing the job: the E034 data gate then records BLOCKED (0 trials).
set -euo pipefail
mkdir -p backtests/validation_reports
bash scripts/download_dukascopy_index.sh 2>&1 | tee backtests/validation_reports/E034_index_download.log \
  || echo "INDEX DOWNLOAD FAILED (E034 data gate will record BLOCKED)" | tee -a backtests/validation_reports/E034_index_download.log
python scripts/run_e034_month_end_hedging.py | tee backtests/validation_reports/E034_results.txt
