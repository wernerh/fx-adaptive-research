# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-12 R125 E047 (B56) pivot-point R1/S1 first touch per UTC date, continuation (long R1, short S1), entry t+1 min,
# 120-min hold, DEV block only, 1 trial, UTC-date cluster bootstrap, p < 0.05, mean > 1 pip, < 300 events NONE.
# Pre-registered in experiments/2026-11-12_E047_pivot_touch/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e047_pivot_touch.py | tee backtests/validation_reports/E047_results.txt
