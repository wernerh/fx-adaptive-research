# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 E010 (ECB 14:15 CET fix reversal, dev only, 2 trials)
set -euo pipefail
python scripts/run_e010_ecb_fix.py | tee backtests/validation_reports/E010_results.txt
