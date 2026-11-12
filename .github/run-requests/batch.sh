# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-12 R110 E046 (B54) even- vs odd-week FOMC cycle: long EUR/USD in cycle weeks 2/4/6, short in -1/1/3/5, week 0
# excluded, 20:00 NY (start of D) -> 16:55 NY D, DEV block only, 1 trial, block-20 bootstrap, p < 0.05, < 500 dates NONE.
# Pre-registered in experiments/2026-11-12_E046_fomc_cycle/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e046_fomc_cycle.py | tee backtests/validation_reports/E046_results.txt
