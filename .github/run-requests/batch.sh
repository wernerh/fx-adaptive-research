# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-09 R051 E026 (B21) calendar-free post-08:30 NY release-window continuation: sign(08:30 -> 08:45 NY move)
# held 08:45 -> 10:45 NY when |move| > rolling p90 of 60 valid dates, DEV block only, 1 trial.
# Pre-registered in experiments/2026-11-09_E026_release_continuation/. No OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e026_release_continuation.py | tee backtests/validation_reports/E026_results.txt
