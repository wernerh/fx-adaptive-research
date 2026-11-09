# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R053 E027 (B22) London-open intraday momentum: sign(08:00 -> 08:30 London) held 15:25 -> 15:55 London
# on every valid date, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-09_E027_london_momentum/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e027_london_momentum.py | tee backtests/validation_reports/E027_results.txt
