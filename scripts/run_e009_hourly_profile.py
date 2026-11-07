"""E009: exploratory hourly return profile scan (DEV ONLY; val and OOS untouched).

Pre-registered in experiments/2026-11-07_E009_hourly_profile/.

    python scripts/run_e009_hourly_profile.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.hourly_profile import N_CELLS, hourly_returns, scan
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
hr = hourly_returns(bars)
plan = SplitPlan(date(2024, 12, 31), date(2025, 1, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
res = scan(hr, plan.assign)  # dev only by pre-registration

with pd.option_context("display.width", 250, "display.max_columns", 40, "display.max_rows", 400):
    print(res.to_string(index=False))

cands = res[res["decision"] == "CANDIDATE"].sort_values("t_p")
notes = res[res["decision"] == "NOTE"].sort_values("t_p")
overall = "CANDIDATES" if len(cands) else "NONE"
print(f"\nCANDIDATE cells: {len(cands)}; NOTE cells: {len(notes)}")
print(cands[["family", "cell", "n", "mean_pips", "ci_lo", "ci_hi", "t_p", "sign_p"]].to_string(index=False))
print("E009 overall decision:", overall)

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E009_synthetic_smoke" if args.synthetic else "E009_results"
dump({"results": res.to_dict(orient="records"), "overall_decision": overall, "n_trials": N_CELLS,
      "candidates": cands["cell"].tolist(), "notes": notes["cell"].tolist(), "blocks": ["dev"]},
     out_dir / f"{stem}.json")
