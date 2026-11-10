# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R063 E031 (B26) USD depreciation after the Tokyo fix on gotobi dates: long EUR/USD 09:55 -> 10:55
# Asia/Tokyo on gotobi Tokyo dates, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-10_E031_gotobi_postfix/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e031_gotobi_postfix.py | tee backtests/validation_reports/E031_results.txt
