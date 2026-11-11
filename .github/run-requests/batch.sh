# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-11 R100 E044 (B50) daily realized skewness: s = sign(RS of 5-min mid returns 18:00 -> 16:55 NY of D),
# EUR/USD 20:00 NY D -> 16:55 NY D+1, DEV block only, 1 trial, block-20 bootstrap, p < 0.05, < 500 dates NONE.
# Pre-registered in experiments/2026-11-11_E044_realized_skew/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e044_realized_skew.py | tee backtests/validation_reports/E044_results.txt
