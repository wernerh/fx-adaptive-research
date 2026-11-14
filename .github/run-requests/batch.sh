# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-14 R156 E049 (B59) 1h + 30m + 15m EMA20 trend alignment with 5m EMA20-cross trigger (5m close
# 07:00 London - 12:00 NY), 60-min hold, DEV block only, 1 trial, trading-date cluster bootstrap, p < 0.05, mean > 1 pip, < 300 NONE.
# Pre-registered in experiments/2026-11-14_E049_mtf_alignment/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e049_mtf_alignment.py | tee backtests/validation_reports/E049_results.txt
