# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R056 E028 (B23) intraday continuation on overreaction days: 17:00 -> 12:00 NY move beyond rolling
# mean +/- 2 SD of 60 valid dates, followed 12:00 -> 16:30 NY, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-09_E028_overreaction_day/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e028_overreaction_day.py | tee backtests/validation_reports/E028_results.txt
