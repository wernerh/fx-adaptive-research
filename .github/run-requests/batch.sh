# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-11 R089 E040 (B43) post-FOMC reversal of the pre-statement EUR/USD drift:
# -sign(mid 16:00 NY t-1 -> 13:55 NY t) x (mid 02:00 -> 14:00 NY t+1), scheduled FOMC statements, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-11_E040_post_fomc_reversal/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e040_post_fomc_reversal.py | tee backtests/validation_reports/E040_results.txt
