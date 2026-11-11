# Research batch queue. Edit and push this file to run the commands below on GitHub Actions
# (workflow: .github/workflows/research-batch.yml). Run from repo root, data already ingested.
# Only pre-registered experiments may be queued here. Never queue --block oos without a written dev/val conclusion.
# Request: 2026-11-11 R086 E039 (B40 + B41) Treasury coupon-auction demand shock -> EUR/USD continuation: sign(EUR/USD T-10 -> T+10 min
# around the competitive close) x (T+10 -> 16:00 NY on the 10th / 1st trading date after D), DEV block only, 2 trials.
# Phase 1: auction calendar (dev dates only) from the Fiscal Data API; ustbondtrusd download is descriptive (failure tolerated).
# Pre-registered in experiments/2026-11-11_E039_treasury_auction/. No val, no OOS.
set -euo pipefail
mkdir -p backtests/validation_reports
python scripts/fetch_treasury_auctions.py | tee backtests/validation_reports/E039_auctions_fetch.log
bash scripts/download_dukascopy_ustb.sh 2>&1 | tee backtests/validation_reports/E039_ustb_download.log \
  || echo "USTB DOWNLOAD FAILED (descriptive only, E039 decision unaffected)" | tee -a backtests/validation_reports/E039_ustb_download.log
python scripts/run_e039_treasury_auction.py | tee backtests/validation_reports/E039_results.txt
