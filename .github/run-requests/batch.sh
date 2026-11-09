# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R048 E025 (B20v) val confirmation of E024: long EUR/USD 11:05 -> 16:00 NY after a high prior-day range,
# VAL block only (bars >= 2023-07-01 UTC dropped first), 1 trial.
# Pre-registered in experiments/2026-11-09_E025_vol_state_london_fix_val/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e025_vol_state_london_val.py | tee backtests/validation_reports/E025_results.txt
