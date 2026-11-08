# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 E011 (Tokyo 09:55 JST fix reversal, dev only, 2 trials)
set -euo pipefail
python scripts/run_e011_tokyo_fix.py | tee backtests/validation_reports/E011_results.txt
