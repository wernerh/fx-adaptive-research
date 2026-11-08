# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 E013 phase 1 (B11): fetch + parse official FOMC dates; NO experiment, no price data used.
# Outputs go to backtests/calendars/ for review by the next run before E013 phase 2 is queued.
set -euo pipefail
python scripts/fetch_fomc_dates.py --years 2015-2023 | tee backtests/calendars_fetch_log.txt
