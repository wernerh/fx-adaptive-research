"""E012: NY 18:00-19:00 hour long drift on trading-date Wednesday / Thursday (VAL ONLY; OOS untouched).

Pre-registered in experiments/2026-11-08_E012_ny18_drift_val/ (backlog B9, B10; dev-derived from E009).
Decision: fxresearch.fixes.decide(n_trials=1) per test on mid returns (B1 rule, E009 follow-up rule).
Cost check (bid/ask, SPEC 4 slippage/commission, costs x1.5) is reported separately; it gates only the LEAD label.
A dev reproduction of the E009 cells is printed as a consistency check (no new trial).

    python scripts/run_e012_ny18_drift.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fixes import decide
from fxresearch.ny_hour_drift import E012_TESTS, cost_summary, ny_hour_frame
from fxresearch.predictive import evaluate_predictor
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 1, 31), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN

frames = {h: ny_hour_frame(bars, h) for h in sorted({t.ny_hour for t in E012_TESTS})}
rows, cost_rows, dev_check = [], [], []
for t in E012_TESTS:
    f = frames[t.ny_hour]
    blk = plan.assign(pd.Index(f.index)).to_numpy()
    for block in ("dev", "val"):  # dev = reproduction check only; val = the pre-registered test
        d = f[(blk == block) & (f["weekday"] == t.weekday).to_numpy()]
        res = evaluate_predictor(pd.Series(float(t.direction), index=d.index), d["ret_pips"])
        if block == "dev":
            dev_check.append({"test": t.name, "n": res.get("n_active"), "mean_signed_pips": res.get("mean_signed_pips")})
            continue
        res["decision"] = decide(res, n_trials=1)
        res["binom_p_bonferroni_2"] = min(1.0, 2 * res["binom_p"]) if "binom_p" in res else None
        c = cost_summary(d, t.direction)
        res["lead_cost_gate"] = bool(c["mean_net_spec4_pips"] > 0 and c["mean_net_costs_x1_5_pips"] > 0)
        rows.append({"block": block, "test": t.name, "weekday": t.weekday, "ny_hour": t.ny_hour,
                     "direction": t.direction, **res})
        cost_rows.append({"test": t.name, **c})

res = pd.DataFrame(rows)
costs = pd.DataFrame(cost_rows)
with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("Dev reproduction of E009 cells (consistency check, not a trial):")
    print(pd.DataFrame(dev_check).to_string(index=False))
    print("\nVAL results (pre-registered rule, 1 trial per test):")
    print(res.to_string(index=False))
    print("\nVAL cost check (descriptive; gates only the LEAD label):")
    print(costs.to_string(index=False))

overall = "SIGNAL" if (res["decision"] == "SIGNAL").any() else ("WEAK" if (res["decision"] == "WEAK").any() else "NONE")
lead_tests = res.loc[(res["decision"] == "SIGNAL") & res["lead_cost_gate"], "test"].tolist()
print("E012 overall decision:", overall)
print("E012 tests meeting SIGNAL + cost gate (lead candidates):", lead_tests or "none")

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E012_synthetic_smoke" if args.synthetic else "E012_results"
dump({"results": res.to_dict(orient="records"), "cost_check": costs.to_dict(orient="records"),
      "dev_reproduction": dev_check, "overall_decision": overall, "lead_candidates": lead_tests,
      "n_trials": len(E012_TESTS), "blocks": ["val"]}, out_dir / f"{stem}.json")
