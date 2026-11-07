"""E008: do pre-US session ranges predict the SIZE of the US move? (DEV ONLY; val and OOS untouched).

Pre-registered in experiments/2026-11-07_E008_vol_timing/.

    python scripts/run_e008_vol_timing.py [--synthetic]
"""
import argparse
from datetime import date, time

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.features import daily_features
from fxresearch.outcomes import window_outcome
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_timing import ALPHA, E008_TESTS, MIN_IC, run_vol_tests

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
feats = daily_features(bars).join(
    window_outcome(bars, "America/New_York", time(8, 0), time(9, 0), "us_0800_0900"), how="left")
# Drop partial sessions/windows (holidays, early closes): require >= 95% of expected minute bars.
for col, full in (("asia_bars", 360), ("london_bars", 240)):
    pred = col.replace("_bars", "_range_pips")
    feats.loc[feats[col] < 0.95 * full, pred] = float("nan")
feats.loc[feats["y_us_bars"] < 228, "y_us_ret_pips"] = float("nan")
feats.loc[feats["y_us_0800_0900_bars"] < 57, "y_us_0800_0900_ret_pips"] = float("nan")

plan = SplitPlan(date(2024, 1, 31), date(2024, 2, 29), embargo_days=0) if args.synthetic else DEFAULT_PLAN
split = plan.assign(feats.index)
res = run_vol_tests(feats, split, E008_TESTS, blocks=("dev",))  # dev only by pre-registration

with pd.option_context("display.width", 250, "display.max_columns", 40, "display.max_colwidth", 80):
    print(res.to_string(index=False))

overall = "USEFUL" if (res["decision"] == "USEFUL").any() else "NOT_USEFUL"
print("E008 overall decision:", overall)

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E008_synthetic_smoke" if args.synthetic else "E008_results"
dump({"results": res.to_dict(orient="records"), "overall_decision": overall, "n_trials": len(E008_TESTS),
      "rule": {"min_partial_ic": MIN_IC, "alpha": ALPHA, "ci_lower_gt_0": True}, "blocks": ["dev"]},
     out_dir / f"{stem}.json")
