"""Convert Dukascopy bid/ask 1-minute CSV exports into the canonical parquet file.

Download first (Node.js required), e.g. one file per side:

    npx dukascopy-node -i eurusd -from 2015-01-01 -to 2026-11-01 -t m1 -p bid -v -f csv -dir data/raw
    npx dukascopy-node -i eurusd -from 2015-01-01 -to 2026-11-01 -t m1 -p ask -v -f csv -dir data/raw

Then either pass the two files:

    python scripts/ingest_dukascopy.py --bid data/raw/<bid>.csv --ask data/raw/<ask>.csv

or a directory of per-year files named eurusd-m1-bid-YYYY.csv / eurusd-m1-ask-YYYY.csv
(as produced by .github/workflows/e001-data-baseline.yml):

    python scripts/ingest_dukascopy.py --dir data/raw

Writes data/processed/eurusd_m1.parquet and a data quality JSON to
backtests/validation_reports/data_quality_<first>_<last>.json.
"""
import argparse
import json
from pathlib import Path

from _common import PROCESSED, ROOT
from fxresearch.data import load_bid_ask_csv, quality_report

ap = argparse.ArgumentParser()
ap.add_argument("--bid", nargs="*", default=[])
ap.add_argument("--ask", nargs="*", default=[])
ap.add_argument("--dir", default=None)
args = ap.parse_args()

bid, ask = list(args.bid), list(args.ask)
if args.dir:
    d = Path(args.dir)
    bid += sorted(str(p) for p in d.glob("*bid*.csv"))
    ask += sorted(str(p) for p in d.glob("*ask*.csv"))
if not bid or not ask:
    raise SystemExit("need bid and ask files")

bars = load_bid_ask_csv(bid, ask)
PROCESSED.parent.mkdir(parents=True, exist_ok=True)
bars.to_parquet(PROCESSED)
q = quality_report(bars)
q["source"] = "Dukascopy via dukascopy-node, 1-minute bid and ask"
q["files"] = {"bid": [Path(p).name for p in bid], "ask": [Path(p).name for p in ask]}
out = ROOT / "backtests" / "validation_reports" / f"data_quality_{q['first_bar'][:10]}_{q['last_bar'][:10]}.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(q, indent=2))
print(json.dumps(q, indent=2))
