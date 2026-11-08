# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 R023 E015 phase 1 (B12): fetch + parse official BLS Employment Situation release dates;
# NO experiment, no price data used. Outputs go to backtests/calendars/ for review before E015 phase 2 is queued.
set -euo pipefail
python scripts/fetch_nfp_dates.py --years 2015-2023 | tee backtests/calendars/nfp_fetch_log.txt
