"""E006: E001 predictors against SHORT US-session outcome windows (dev + val only).

Windows (pre-registered): 08:00-09:00 and 08:35-09:30 America/New_York.
Bonferroni multiplier = predictors x windows.

    python scripts/run_e006_short_window.py [--synthetic]
"""
import argparse
from datetime import date, time

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.features import daily_features
from fxresearch.outcomes import window_outcome
from fxresearch.predictive import PREDICTORS, run_baseline
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

WINDOWS = {
    "us_0800_0900": (time(8, 0), time(9, 0)),
    "us_0835_0930": (time(8, 35), time(9, 30)),
}

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
feats = daily_features(bars)
for name, (s, e) in WINDOWS.items():
    feats = feats.join(window_outcome(bars, "America/New_York", s, e, name), how="left")

plan = SplitPlan(date(2024, 1, 31), date(2024, 2, 29), embargo_days=0) if args.synthetic else DEFAULT_PLAN
split = plan.assign(feats.index)
n_trials = len(PREDICTORS) * len(WINDOWS)
res = pd.concat([run_baseline(feats, split, outcome=f"y_{n}_ret_pips", n_trials=n_trials) for n in WINDOWS])
res = res[res["block"] != "oos"]  # OOS locked

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(res.to_string(index=False))

# Context for the cost threshold: typical absolute move in each window.
ctx = {n: {b: round(float(feats.loc[split == b, f"y_{n}_ret_pips"].abs().mean()), 3) for b in ("dev", "val")}
       for n in WINDOWS}
print("mean |window return| pips:", ctx)

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E006_synthetic_smoke" if args.synthetic else "E006_results"
dump({"results": res.to_dict(orient="records"), "mean_abs_window_return_pips": ctx, "n_trials": n_trials},
     out_dir / f"{stem}.json")
