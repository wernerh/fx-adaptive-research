# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R039 E021 (B18) next-session reversal after a large daily move, 20:00 NY D -> 10:45 NY next date, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-09_E021_daily_reversal/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e021_daily_reversal.py | tee backtests/validation_reports/E021_results.txt
