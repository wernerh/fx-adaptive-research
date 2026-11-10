"""E034 (B30): month-end pre-fix equity-hedging flow (Melvin & Prins 2015), DEV ONLY, 2 trials (HOUR and DAY windows).

Pre-registered in experiments/2026-11-10_E034_month_end_hedging/ (backlog B30). Val and OOS untouched.
EUR/USD bars are restricted to dev trading dates BEFORE any computation; index bars are cut at 2021-01-01 UTC.
The data gate runs first: if it fails, the run stops as BLOCKED (0 trials used) and no trade result is computed.
Decision: fxresearch.month_end_hedging.decide_b30 per window on per-event signed mid returns. Everything else is descriptive.

    python scripts/run_e034_month_end_hedging.py [--synthetic] [--index-dir data/raw_index]
"""
import argparse
import sys
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch import month_end_hedging as mh
from fxresearch.data import synthetic_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
ap.add_argument("--index-dir", default=str(ROOT / "data" / "raw_index"))
args = ap.parse_args()

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E034_synthetic_smoke" if args.synthetic else "E034_results"

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

if args.synthetic:
    eu = synthetic_bars("2024-01-01", "2024-03-31", seed=11)
    us = synthetic_bars("2024-01-01", "2024-03-31", seed=12)
else:
    eu = mh.load_index(args.index_dir, mh.EU_INDEX)
    us = mh.load_index(args.index_dir, mh.US_INDEX)
if not args.synthetic:  # dev only: never read index bars from val/OOS dates
    cut = pd.Timestamp("2021-01-01", tz="UTC")
    eu, us = eu[eu.index < cut], us[us.index < cut]
idx_desc = {lab: {"bars": int(len(f)), "first": str(f.index.min()) if len(f) else None,
                  "last": str(f.index.max()) if len(f) else None,
                  "median_mid": float(((f["bid_open"] + f["ask_open"]) / 2).median()) if len(f) else None}
            for lab, f in (("eu", eu), ("us", us))}
print("index data:", idx_desc)

df = mh.build_events(bars, eu, us) if len(eu) and len(us) else pd.DataFrame()
gate = mh.data_gate(df, eu, us)
print("Data gate:", gate)
if not gate["ok"]:
    print("E034 decision: BLOCKED (data gate failed; 0 trials used)")
    dump({"status": "BLOCKED", "data_gate": gate, "index_data": idx_desc, "n_trials": 0, "blocks": ["dev"]},
         out_dir / f"{stem}.json")
    if len(df) and not args.synthetic:
        df.to_csv(out_dir / "E034_month_ends.csv", index=False)
    sys.exit(0)

res, cnt, costs = {}, {}, {}
for win in ("hour", "day"):
    ev = df[df[f"{win}_tested"]]
    r = mh.evaluate_b30(ev[f"{win}_signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
    r["decision"] = mh.decide_b30(r)
    res[win], cnt[win], costs[win] = r, mh.counts(df, win), mh.cost_summary(ev, win)


def _ev(x):
    x = pd.Series(x).dropna()
    return mh.evaluate_b30(x) if len(x) >= 3 else {"n": int(len(x))}


desc = {}
for win in ("hour", "day"):
    ev = df[df[f"{win}_tested"]].copy()
    if not len(ev):
        continue
    med = ev["s"].abs().median()
    qe = pd.to_datetime(ev["date"]).dt.month.isin([3, 6, 9, 12])
    eu_pos = -np.sign(ev["s_eu"])
    us_pos = np.sign(ev["s_us"])
    desc[win] = {
        "unconditional_long_eurusd": _ev(ev[f"{win}_move_pips"]),
        "abs_s_above_median": _ev(ev.loc[ev["s"].abs() > med, f"{win}_signed_pips"]),
        "abs_s_at_or_below_median": _ev(ev.loc[ev["s"].abs() <= med, f"{win}_signed_pips"]),
        "eu_leg_only_position_minus_sign_s_eu": _ev(eu_pos * ev[f"{win}_move_pips"]),
        "us_leg_only_position_plus_sign_s_us": _ev(us_pos * ev[f"{win}_move_pips"]),
        "quarter_ends": _ev(ev.loc[qe, f"{win}_signed_pips"]),
        "other_month_ends": _ev(ev.loc[~qe, f"{win}_signed_pips"]),
        "fallback_quote_months_excluded": _ev(ev.loc[~ev["fallback_quote"], f"{win}_signed_pips"]),
        "share_short_eurusd": round(float((ev["position"] < 0).mean()), 3),
        "corr_s_move": round(float(ev["s"].corr(ev[f"{win}_move_pips"])), 3) if len(ev) > 2 else None,
        "by_year": (ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")[f"{win}_signed_pips"]
                    .agg(["size", "mean"]).round(3).reset_index().to_dict(orient="records")),
    }
post = df[df["post_tested"]]
desc["post_fix_hour_same_position_16_17_london"] = _ev(post["post_signed_pips"]) if len(post) else {"n": 0}
desc["s_stats"] = {"mean": round(float(df["s"].mean()), 5), "sd": round(float(df["s"].std()), 5),
                   "abs_median": round(float(df["s"].abs().median()), 5)}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE034 DEV month-end equity-hedging flow, position = -sign(EU50 minus US500 log return since last month-end fix)")
    for win in ("hour", "day"):
        print(f"\n{win.upper()} window:\n", pd.Series(res[win]).to_string())
        print("Counts:", cnt[win])
        print("Costs (descriptive):", costs[win])
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
print("E034 decision B30-hour:", res["hour"]["decision"])
print("E034 decision B30-day:", res["day"]["decision"])

dump({"status": "complete", "data_gate": gate, "index_data": idx_desc, "result_hour": res["hour"], "result_day": res["day"],
      "counts": cnt, "cost_check": costs, "descriptive": desc, "n_trials": 2, "blocks": ["dev"],
      "first_month_end": str(df["date"].iloc[0]), "last_month_end": str(df["date"].iloc[-1])}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E034_month_ends.csv", index=False)
