# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-11 R097 E043 (B48) post-jump reversal: 5-min Lee-Mykland jumps (|L| > 5.395, K 270, |move| >= 5 pips),
# position -sign(r) from t+10 to t+70 min, DEV block only, 1 trial, date-cluster bootstrap, p < 0.05, < 300 events NONE.
# Pre-registered in experiments/2026-11-11_E043_post_jump_reversal/. No val, no OOS. No external download.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/run_e043_post_jump.py | tee backtests/validation_reports/E043_results.txt
