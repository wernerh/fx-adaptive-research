# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 R019 E013 phase 2 (B11): FOMC statement-day long EUR/USD, DEV ONLY, 1 trial.
# Date file reviewed and promoted to data/calendars/fomc_dates.csv (47 dev statement days).
set -euo pipefail
python scripts/run_e013_fomc_day.py | tee backtests/validation_reports/E013_results.txt
