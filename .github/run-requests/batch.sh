# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-11 R083 E038 (B38) intraday momentum into the 17:00 NY spot roll: sign(mid 17:00 NY start of D -> 16:25 NY)
# x (16:25 -> 16:55 NY), DEV block only, 1 trial. Pre-registered in experiments/2026-11-11_E038_roll_momentum/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e038_roll_momentum.py | tee backtests/validation_reports/E038_results.txt
