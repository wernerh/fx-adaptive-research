# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R034 E019 (B16) 12-month time-series momentum, daily 16:00 NY hold, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-09_E019_tsmom_12m/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e019_tsmom.py | tee backtests/validation_reports/E019_results.txt
