# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R066 E032 (B27) post-Tokyo-fix EUR appreciation, KMW window: long EUR/USD 20:55 -> 02:00
# America/New_York on every val trading date, VAL block only, 1 trial.
# Pre-registered in experiments/2026-11-10_E032_post_tokyo_kmw_val/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e032_post_tokyo_kmw.py | tee backtests/validation_reports/E032_results.txt
