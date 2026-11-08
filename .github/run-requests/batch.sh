# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 R029 E017 (B14) home-hours depreciation, VAL block only, 1 trial. Pre-registered in
# experiments/2026-11-08_E017_home_hours_val/. No dev, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e017_home_hours.py | tee backtests/validation_reports/E017_results.txt
