# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-13 R154 E048 (B58) 1h swing-level breakout (24 clock-hour high/low, close 07:00 London - 12:00 NY) with 5m
# break-and-retest entry, 60-min hold, DEV block only, 1 trial, trading-date cluster bootstrap, p < 0.05, mean > 1 pip, < 300 NONE.
# Pre-registered in experiments/2026-11-13_E048_breakout_retest/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e048_breakout_retest.py | tee backtests/validation_reports/E048_results.txt
