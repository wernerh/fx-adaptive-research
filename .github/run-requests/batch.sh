# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R058 E029 (B24) next-morning fade after an overreaction day: 17:00 -> 16:55 NY move beyond rolling
# mean +/- 2 SD of 60 valid val dates, faded 17:05 -> 02:00 NY next trading date, VAL block only (val-only burn-in), 1 trial.
# Pre-registered in experiments/2026-11-10_E029_overreaction_fade_val/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e029_overreaction_fade.py | tee backtests/validation_reports/E029_results.txt
