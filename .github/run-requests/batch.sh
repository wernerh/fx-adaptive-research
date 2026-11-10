# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R061 E030 (B25) USD appreciation into the Tokyo fix on gotobi dates: short EUR/USD 08:55 -> 09:55
# Asia/Tokyo on gotobi Tokyo dates, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-10_E030_gotobi_tokyo_fix/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e030_gotobi_fix.py | tee backtests/validation_reports/E030_results.txt
