# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R080 E037 (B35 + B36) relative equity performance -> next-day EUR/USD (Hau-Rey, lagged): position
# -sign(EU50 minus US500 log return, 16:00 London prev -> D (B35) or over 20 dates (B36)), hold 16:05 London D -> 16:00 London next
# date, DEV block only, 2 trials. Pre-registered in experiments/2026-11-10_E037_relative_equity/. No val, no OOS.
# The index download (dev dates only) may fail without failing the job: the E037 data gate then records BLOCKED (0 trials).
set -euo pipefail
mkdir -p backtests/validation_reports
bash scripts/download_dukascopy_index.sh 2>&1 | tee backtests/validation_reports/E037_index_download.log \
  || echo "INDEX DOWNLOAD FAILED (E037 data gate will record BLOCKED)" | tee -a backtests/validation_reports/E037_index_download.log
python scripts/run_e037_relative_equity.py | tee backtests/validation_reports/E037_results.txt
