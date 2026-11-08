# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 R027 E016 phase 1 RE-FETCH (B13): the first fetch (run 42500439921) timed out on all CME URLs.
# Same URLs and User-Agent; 120 s timeout, 3 attempts on transport errors only (refusals are final). NO experiment, no price data.
set -euo pipefail
mkdir -p backtests/calendars
python scripts/fetch_cme_settlement.py | tee backtests/calendars/cme_settlement_fetch_log.txt
