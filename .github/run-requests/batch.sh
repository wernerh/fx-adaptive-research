# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-08 E012 (NY 18:00 hour drift Wed/Thu, val only, 2 trials; B9/B10)
set -euo pipefail
python scripts/run_e012_ny18_drift.py | tee backtests/validation_reports/E012_results.txt
