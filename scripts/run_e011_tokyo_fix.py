"""E011: Tokyo 09:55 JST fix reversal signal test (DEV ONLY; val and OOS untouched).

Pre-registered in experiments/2026-11-08_E011_tokyo_fix_reversal/.
Decision uses mid returns (E007/E010 rule). Bid/ask net and costs x1.5 are reported descriptively only.

    python scripts/run_e011_tokyo_fix.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fixes import E011_TESTS, TOKYO_FIX_WINDOWS, run_fix_tests, window_bidask_net
from fxresearch.outcomes import window_outcome
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
feats = pd.concat([window_outcome(bars, tz, s, e, name) for name, (tz, s, e) in TOKYO_FIX_WINDOWS.items()],
                  axis=1, join="outer")
# Drop partial windows (holidays / early closes): require >= 55 of 60 minute bars.
for name in TOKYO_FIX_WINDOWS:
    feats.loc[feats[f"y_{name}_bars"] < 55, f"y_{name}_ret_pips"] = float("nan")

plan = SplitPlan(date(2024, 1, 31), date(2024, 2, 29), embargo_days=0) if args.synthetic else DEFAULT_PLAN
split = plan.assign(feats.index)
res = run_fix_tests(feats, split, E011_TESTS, blocks=("dev",))  # dev only by pre-registration

# Descriptive cost check (not part of the decision rule), dev days with a full window only.
dev_days = split.index[(split == "dev").to_numpy()]
cost_rows = []
for t in E011_TESTS:
    tz, s, e = TOKYO_FIX_WINDOWS[t.window]
    nb = window_bidask_net(bars, tz, s, e, t.direction, t.window)
    ok = feats[f"y_{t.window}_ret_pips"].dropna().index.intersection(dev_days)
    nb = nb.reindex(ok)
    gross = t.direction * feats.loc[ok, f"y_{t.window}_ret_pips"]
    cost = gross - nb[f"{t.window}_net_pips"]
    cost_rows.append({
        "test": t.name, "n": int(len(ok)),
        "mean_signed_mid_pips": round(float(gross.mean()), 3),
        "median_entry_spread_pips": round(float(nb[f"{t.window}_entry_spread_pips"].median()), 3),
        "mean_roundtrip_cost_pips": round(float(cost.mean()), 3),
        "mean_net_bidask_pips": round(float(nb[f"{t.window}_net_pips"].mean()), 3),
        "mean_net_costs_x1_5_pips": round(float((gross - 1.5 * cost).mean()), 3),
    })
costs = pd.DataFrame(cost_rows)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(res.to_string(index=False))
    print("\nDescriptive cost check (not in decision rule):")
    print(costs.to_string(index=False))

overall = "SIGNAL" if (res["decision"] == "SIGNAL").any() else ("WEAK" if (res["decision"] == "WEAK").any() else "NONE")
print("E011 overall decision:", overall)

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E011_synthetic_smoke" if args.synthetic else "E011_results"
dump({"results": res.to_dict(orient="records"), "cost_check": costs.to_dict(orient="records"),
      "overall_decision": overall, "n_trials": len(E011_TESTS), "blocks": ["dev"]}, out_dir / f"{stem}.json")
