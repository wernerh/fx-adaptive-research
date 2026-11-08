"""E016 (backlog B13): intraday momentum into the CME FX futures settlement, spot EUR/USD. DEV ONLY.

Pre-registered in experiments/2026-11-08_E016_cme_settle_momentum/. Val and OOS are never evaluated here: bars are
truncated before 2021-01-01 and only trading dates in the dev block are used.
Requires the reviewed settlement file data/calendars/cme_fx_settlement.json (phase 1 output, promoted after review).

    python scripts/run_e016_cme_settle_momentum.py [--synthetic]
"""
import argparse
from datetime import date, time

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.cme_settle import cost_summary, decide_b13, evaluate, load_settlement, momentum_frame, reversal_flag
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
if args.synthetic:
    plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0)  # whole synthetic range = "dev"
    settle = time(14, 0)  # placeholder for the smoke run only; NOT the verified settlement time
else:
    plan = DEFAULT_PLAN
    path = ROOT / "data" / "calendars" / "cme_fx_settlement.json"
    if not path.exists():
        raise SystemExit(f"{path} missing: promote the reviewed phase-1 settlement time first.")
    settle = load_settlement(path)
    bars = bars[bars.index < pd.Timestamp("2021-01-01", tz="UTC")]  # dev only; val/OOS never read

f = momentum_frame(bars, settle)
blk = plan.assign(pd.Index(f.index))
f = f[blk.to_numpy() == "dev"]
dropped = [str(d) for d in f.index[f["signed_pips"].isna()]]
res = evaluate(f)
res["decision"] = decide_b13(res)
res["reversal_exploratory"] = reversal_flag(res)
costs = cost_summary(f)
res["lead_cost_gate"] = bool(costs.get("n_traded", 0) > 0 and costs["mean_net_spec4_pips"] > 0
                             and costs["mean_net_costs_x1_5_pips"] > 0)
yearly = f["signed_pips"].groupby(pd.to_datetime(pd.Index(f.index)).year).agg(["count", "mean"]).round(3)
weekday = f["signed_pips"].groupby(pd.to_datetime(pd.Index(f.index)).dayofweek).agg(["count", "mean"]).round(3)

print(f"E016 DEV ONLY. settlement S = {settle.strftime('%H:%M')} CT; weekday trading dates: {len(f)}; "
      f"dropped for missing quotes: {len(dropped)}")
print("\nPre-registered test (1 trial): signed = sign(r1 roll -> S-30) x r2 (S-30 -> S), |r1| < 1 pip -> 0")
print(res)
print("\nCost check (descriptive; gates only the LEAD label):", costs)
print("\nPer-year (descriptive):\n", yearly.to_string())
print("\nPer-weekday (descriptive, 0=Mon):\n", weekday.to_string())
print("\nDropped dates:", dropped)
print("\nE016 decision:", res["decision"], "| reversal (exploratory):", res["reversal_exploratory"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E016_synthetic_smoke" if args.synthetic else "E016_results"
dump({"test": res, "cost_check": costs, "settle_time_ct": settle.strftime("%H:%M"),
      "per_year": yearly.reset_index().to_dict(orient="records"),
      "per_weekday": weekday.reset_index().to_dict(orient="records"),
      "dropped": dropped, "n_trials": 1, "blocks": ["dev"], "decision": res["decision"]}, out_dir / f"{stem}.json")
