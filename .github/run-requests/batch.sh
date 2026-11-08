# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 R032 E018 (B15) round-number crossing continuation, DEV block only, 1 trial. Pre-registered in
# experiments/2026-11-08_E018_round_number_cascades/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e018_round_numbers.py | tee backtests/validation_reports/E018_results.txt
