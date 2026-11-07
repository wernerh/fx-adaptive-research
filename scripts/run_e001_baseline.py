"""E001: predictive power of Asian/London structure for US-session direction (no costs).

    python scripts/run_e001_baseline.py               # dev + val blocks only
    python scripts/run_e001_baseline.py --include-oos # ONLY after dev/val conclusions are written
    python scripts/run_e001_baseline.py --synthetic   # smoke test on random-walk data
"""
import argparse

from _common import ROOT, dump, load_bars
from fxresearch.features import daily_features
from fxresearch.predictive import run_baseline
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from datetime import date

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
ap.add_argument("--include-oos", action="store_true")
ap.add_argument("--out", default=None)
args = ap.parse_args()

bars = load_bars(args.synthetic)
feats = daily_features(bars)
plan = SplitPlan(date(2024, 1, 31), date(2024, 2, 29), embargo_days=0) if args.synthetic else DEFAULT_PLAN
split = plan.assign(feats.index)
res = run_baseline(feats, split)
if not args.include_oos:
    res = res[res["block"] != "oos"]

print(res.to_string(index=False))

if args.synthetic:
    out = ROOT / "backtests" / "validation_reports" / "E001_synthetic_smoke.json"
else:
    out = args.out or ROOT / "backtests" / "validation_reports" / "E001_results.json"
dump(res.to_dict(orient="records"), out)
