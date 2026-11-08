"""E017: home-hours depreciation, short EUR/USD 03:00-08:00 NY + long 12:00-17:00 NY (VAL ONLY; OOS untouched).

Pre-registered in experiments/2026-11-08_E017_home_hours_val/ (backlog B14).
Decision: fxresearch.fixes.decide(n_trials=1) on the daily signed mid return (B1 rule).
Cost check (bid/ask, SPEC 4 slippage/commission per leg, costs x1.5) is descriptive; it gates only the candidate label.
Dev is NOT evaluated (scanned by E009).

    python scripts/run_e017_home_hours.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fixes import decide
from fxresearch.home_hours import E017_LEGS, cost_summary, daily_frame
from fxresearch.predictive import evaluate_predictor
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 1, 31), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN

d_all = daily_frame(bars)
blk = plan.assign(pd.Index(d_all.index)).to_numpy()
d = d_all[blk == "val"]
from fxresearch.sessions import trading_date  # noqa: E402
all_td = pd.Index(sorted(set(trading_date(bars.index))))
n_val_dates = int((plan.assign(all_td).to_numpy() == "val").sum())
n_dropped = n_val_dates - len(d)

res = evaluate_predictor(pd.Series(1.0, index=d.index), d["signed_pips"])
res["decision"] = decide(res, n_trials=1)
legs = {}
for leg in E017_LEGS:
    r = evaluate_predictor(pd.Series(1.0, index=d.index), d[f"{leg.name}_signed_pips"])
    legs[leg.name] = {k: r.get(k) for k in ("n_active", "hit_rate", "binom_p", "mean_signed_pips", "mean_signed_ci95_block_boot")}
c = cost_summary(d)
cost_gate = bool(c["mean_net_spec4_pips"] > 0 and c["mean_net_costs_x1_5_pips"] > 0)
candidate = res["decision"] == "SIGNAL" and cost_gate

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("E017 VAL daily signed return (pre-registered rule, 1 trial):")
    print(pd.Series(res).to_string())
    print("\nPer-leg signed mid (descriptive, not trials):")
    print(pd.DataFrame(legs).T.to_string())
    print("\nVAL cost check (descriptive; gates only the candidate label):")
    print(pd.Series(c).to_string())
print("val trading dates:", n_val_dates, "dropped for coverage (either leg < 275 bars):", n_dropped)
print("E017 decision:", res["decision"])
print("E017 val SIGNAL + cost gate (candidate for human OOS decision, not a LEAD):", candidate)

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E017_synthetic_smoke" if args.synthetic else "E017_results"
dump({"result": res, "legs": legs, "cost_check": c, "cost_gate": cost_gate, "candidate_for_human_oos": candidate,
      "n_trials": 1, "blocks": ["val"], "n_val_trading_dates": n_val_dates,
      "n_val_dates_dropped_coverage": n_dropped}, out_dir / f"{stem}.json")
