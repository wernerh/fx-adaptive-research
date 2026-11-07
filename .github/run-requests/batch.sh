# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-07 E007 (London fix reversal, dev only)
set -euo pipefail
python scripts/run_e007_london_fix.py | tee backtests/validation_reports/E007_results.txt
