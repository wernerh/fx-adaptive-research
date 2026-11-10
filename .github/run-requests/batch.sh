# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R075 E035 (B32 + B33) overnight -> intraday reversal: position -sign(r_on) (B32) or -sign(O20) (B33),
# r_on = 17:05 NY (evening opening D) -> 07:00 NY, hold 07:00 -> 16:55 NY on D, DEV block only, 2 trials.
# Pre-registered in experiments/2026-11-10_E035_overnight_reversal/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e035_overnight_reversal.py | tee backtests/validation_reports/E035_results.txt
