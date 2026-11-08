"""E015 (backlog B12): NFP first-15-minute reaction continuation over 08:45-09:45 NY. DEV ONLY.

Pre-registered in experiments/2026-11-08_E015_nfp_continuation/. Val and OOS are never evaluated here: bars and
release dates are restricted to the dev block before any computation.
Requires the reviewed date file data/calendars/nfp_dates.csv (phase 1 output, promoted after review).

    python scripts/run_e015_nfp_continuation.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.nfp import cost_summary, decide_b12, evaluate, reaction_frame, reversal_flag
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
if args.synthetic:
    plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0)  # whole synthetic range = "dev"
    # Placeholder Fridays for the smoke run only; not NFP dates.
    cal = pd.DataFrame({"release_date": ["2024-01-05", "2024-02-02", "2024-03-08"]})
else:
    plan = DEFAULT_PLAN
    path = ROOT / "data" / "calendars" / "nfp_dates.csv"
    if not path.exists():
        raise SystemExit(f"{path} missing: promote the reviewed backtests/calendars/nfp_dates.csv first.")
    cal = pd.read_csv(path)
    bars = bars[bars.index < pd.Timestamp("2021-01-01", tz="UTC")]  # dev only; val/OOS never read

cal["release_date"] = pd.to_datetime(cal["release_date"]).dt.date
cal["block"] = plan.assign(pd.Index(cal["release_date"])).to_numpy()
rel = sorted(cal.loc[cal["block"] == "dev", "release_date"])

# Benchmark (descriptive): same windows on every other dev Friday.
idx_dates = pd.Index(sorted(set(bars.index.tz_convert("America/New_York").date)))
bench_days = [d for d, b in zip(idx_dates, plan.assign(idx_dates)) if b == "dev" and d.weekday() == 4 and d not in set(rel)]

f = reaction_frame(bars, rel)
dropped = [str(d) for d in f.index[f["signed_pips"].isna()]]
res = evaluate(f)
res["decision"] = decide_b12(res)
res["reversal_exploratory"] = reversal_flag(res)
costs = cost_summary(f)
res["lead_cost_gate"] = bool(costs.get("n_traded", 0) > 0 and costs["mean_net_spec4_pips"] > 0
                             and costs["mean_net_costs_x1_5_pips"] > 0)
b = reaction_frame(bars, bench_days)
bench = evaluate(b)
yearly = f["signed_pips"].groupby(pd.to_datetime(pd.Index(f.index)).year).agg(["count", "mean"]).round(3)

print(f"E015 DEV ONLY. NFP release days in dev: {len(rel)}; dropped for missing quotes: {dropped or 'none'}")
print("\nPre-registered test (1 trial): signed = sign(r1 08:30-08:45) x r2 08:45-09:45 NY, |r1| < 1 pip -> 0")
print(res)
print("\nCost check (descriptive; gates only the LEAD label):", costs)
print("\nDescriptive (not a trial): non-NFP dev Fridays, same windows:", bench)
print("\nPer-year (descriptive):\n", yearly.to_string())
print("\nPer-release:\n", f.round(2).to_string())
print("\nE015 decision:", res["decision"], "| reversal (exploratory):", res["reversal_exploratory"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E015_synthetic_smoke" if args.synthetic else "E015_results"
dump({"test": res, "cost_check": costs, "benchmark_non_nfp_fridays": bench,
      "per_year": yearly.reset_index().to_dict(orient="records"),
      "per_release": f.reset_index().astype({"date": str}).to_dict(orient="records"),
      "dropped": dropped, "n_trials": 1, "blocks": ["dev"], "decision": res["decision"]}, out_dir / f"{stem}.json")
