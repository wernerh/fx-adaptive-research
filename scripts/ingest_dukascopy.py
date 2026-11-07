"""Convert Dukascopy bid/ask 1-minute CSV exports into the canonical parquet file.

Download first (Node.js required), one file per side, e.g.:

    npx dukascopy-node -i eurusd -from 2015-01-01 -to 2026-11-01 -t m1 -p bid -f csv -dir data/raw
    npx dukascopy-node -i eurusd -from 2015-01-01 -to 2026-11-01 -t m1 -p ask -f csv -dir data/raw

Then:

    python scripts/ingest_dukascopy.py data/raw/<bid>.csv data/raw/<ask>.csv

Writes data/processed/eurusd_m1.parquet and prints a data quality report to paste into
data/data_quality_reports.md.
"""
import argparse
import json

from _common import PROCESSED
from fxresearch.data import load_bid_ask_csv, quality_report

ap = argparse.ArgumentParser()
ap.add_argument("bid_csv")
ap.add_argument("ask_csv")
args = ap.parse_args()

bars = load_bid_ask_csv(args.bid_csv, args.ask_csv)
PROCESSED.parent.mkdir(parents=True, exist_ok=True)
bars.to_parquet(PROCESSED)
print(json.dumps(quality_report(bars), indent=2))
