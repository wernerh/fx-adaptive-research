"""E010: ECB 14:15 CET reference-rate reversal signal test (DEV ONLY; val and OOS untouched).

Pre-registered in experiments/2026-11-08_E010_ecb_fix_reversal/.

    python scripts/run_e010_ecb_fix.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fixes import E010_TESTS, ECB_FIX_WINDOWS, run_fix_tests
from fxresearch.outcomes import window_outcome
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
feats = pd.concat([window_outcome(bars, tz, s, e, name) for name, (tz, s, e) in ECB_FIX_WINDOWS.items()],
                  axis=1, join="outer")
# Drop partial windows (holidays / early closes): require >= 55 of 60 minute bars.
for name in ECB_FIX_WINDOWS:
    feats.loc[feats[f"y_{name}_bars"] < 55, f"y_{name}_ret_pips"] = float("nan")

plan = SplitPlan(date(2024, 1, 31), date(2024, 2, 29), embargo_days=0) if args.synthetic else DEFAULT_PLAN
split = plan.assign(feats.index)
res = run_fix_tests(feats, split, E010_TESTS, blocks=("dev",))  # dev only by pre-registration

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(res.to_string(index=False))

overall = "SIGNAL" if (res["decision"] == "SIGNAL").any() else ("WEAK" if (res["decision"] == "WEAK").any() else "NONE")
print("E010 overall decision:", overall)

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E010_synthetic_smoke" if args.synthetic else "E010_results"
dump({"results": res.to_dict(orient="records"), "overall_decision": overall, "n_trials": len(E010_TESTS),
      "blocks": ["dev"]}, out_dir / f"{stem}.json")
