# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-07 E004 + E006
set -euo pipefail
python scripts/run_backtest.py asian_range_breakout --block dev --experiment E004
python scripts/run_backtest.py asian_range_breakout --block dev --experiment E004diag --slippage 0 --commission 0
python scripts/run_e006_short_window.py | tee backtests/validation_reports/E006_results.txt
