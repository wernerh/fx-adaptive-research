# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R077 E036 (B34) val confirmation of E035/B33: position -sign(O20), O20 = sum of the 20 previous val
# overnight returns (17:05 -> 07:00 NY), hold 07:00 -> 16:55 NY, VAL block only, 1 trial, p < 0.05.
# Pre-registered in experiments/2026-11-10_E036_overnight_reversal_val/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e036_overnight_reversal_val.py | tee backtests/validation_reports/E036_results.txt
