# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R037 E020 (B17) weekend-gap reversal, 20:00 NY Sun -> 16:00 NY Mon, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-09_E020_weekend_gap/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e020_weekend_gap.py | tee backtests/validation_reports/E020_results.txt
