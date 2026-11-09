# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R042 E022 (B19) short EUR/USD 02:00 -> 08:15 NY on dates after a high prior-day range, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-09_E022_vol_state_ecb_fix/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e022_vol_state_ecb.py | tee backtests/validation_reports/E022_results.txt
