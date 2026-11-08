# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 R026 E016 phase 1 (B13): fetch official CME Group pages with the FX futures daily settlement window;
# NO experiment, no price data used. Outputs go to backtests/calendars/ for review before E016 phase 2 is queued.
set -euo pipefail
mkdir -p backtests/calendars
python scripts/fetch_cme_settlement.py | tee backtests/calendars/cme_settlement_fetch_log.txt
