# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-11 R103 E045 (B52) take-profit reversal at round numbers: fade the first rejected touch of a 00/50 level per
# trading date, entry t+1 min, 60-min hold, DEV block only, 1 trial, date-cluster bootstrap, p < 0.05, < 300 events NONE.
# Pre-registered in experiments/2026-11-11_E045_round_touch_reversal/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e045_round_touch.py | tee backtests/validation_reports/E045_results.txt
