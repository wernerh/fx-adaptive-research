# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-16 R209 E050 (B60) 2-state Markov switching (switching mean + variance) sign of 8-day expected return,
# walk-forward (first fit to 2015-12-31, refit every 21 trading dates), 16:00 NY daily hold, DEV block only, 1 trial,
# block-20 bootstrap, p < 0.05, mean > 1 pip. Pre-registered in experiments/2026-11-16_E050_markov_switch/. No val, no OOS.
# No external download (statsmodels via pyproject).
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e050_markov_switch.py | tee backtests/validation_reports/E050_results.txt
