# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-10 R069 E033 (B28 + B29) volume-conditioned next-day trades: low-UV reversal and high-UV continuation,
# 20:00 NY on D -> 16:55 NY on D+1, DEV block only, 2 trials.
# Pre-registered in experiments/2026-11-10_E033_volume_reversal/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e033_volume_reversal.py | tee backtests/validation_reports/E033_results.txt
