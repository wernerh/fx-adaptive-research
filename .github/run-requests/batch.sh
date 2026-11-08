# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 R021 E014 (B11v): FOMC statement-day long EUR/USD, VAL ONLY, 1 trial (confirmation of E013 dev SIGNAL).
# Bars truncated to 2021-01-01..2023-06-30 inside the script; OOS never read.
set -euo pipefail
python scripts/run_e014_fomc_day_val.py | tee backtests/validation_reports/E014_results.txt
