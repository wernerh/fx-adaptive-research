# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-16 R212 E051 (B62) random forest (51 trees, random_state 0, defaults) on 10 lagged daily 16:00 NY returns,
# next-day direction, walk-forward (first fit to 2015-12-31, refit every 21 trading dates), 16:00 NY daily hold, DEV block only,
# 1 trial, block-20 bootstrap, p < 0.05, mean > 1 pip. Pre-registered in experiments/2026-11-16_E051_rf_lags/. No val, no OOS.
# No external data download (scikit-learn==1.9.1 via pyproject).
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e051_rf_lags.py | tee backtests/validation_reports/E051_results.txt
