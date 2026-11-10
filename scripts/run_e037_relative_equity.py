"""E037 (B35 + B36): relative equity performance -> next-day EUR/USD (Hau & Rey 2006, lagged extension), DEV ONLY, 2 trials.

Pre-registered in experiments/2026-11-10_E037_relative_equity/ (backlog B35, B36). Val and OOS untouched.
EUR/USD bars are restricted to dev trading dates BEFORE any computation; index bars are cut at 2021-01-01 UTC.
The data gate runs first: if it fails, the run stops as BLOCKED (0 trials used) and no trade result is computed.
Decision: fxresearch.relative_equity.decide_b35 per arm on per-date signed mid returns. Everything else is descriptive.

    python scripts/run_e037_relative_equity.py [--synthetic] [--index-dir data/raw_index]
"""
import argparse
import sys
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch import month_end_hedging as mh
from fxresearch import relative_equity as re_
from fxresearch.data import synthetic_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
ap.add_argument("--index-dir", default=str(ROOT / "data" / "raw_index"))
args = ap.parse_args()

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E037_synthetic_smoke" if args.synthetic else "E037_results"

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

if args.synthetic:
    eu = synthetic_bars("2024-01-01", "2024-03-31", seed=11)
    us = synthetic_bars("2024-01-01", "2024-03-31", seed=12)
else:
    eu = mh.load_index(args.index_dir, re_.EU_INDEX)
    us = mh.load_index(args.index_dir, re_.US_INDEX)
    cut = pd.Timestamp("2021-01-01", tz="UTC")  # dev only: never read index bars from val/OOS dates
    eu, us = eu[eu.index < cut], us[us.index < cut]
idx_desc = {lab: {"bars": int(len(f)), "first": str(f.index.min()) if len(f) else None,
                  "last": str(f.index.max()) if len(f) else None}
            for lab, f in (("eu", eu), ("us", us))}
print("index data:", idx_desc)

if len(eu) and len(us):
    df, dropped = re_.frame_from_bars(bars, eu, us)
else:
    df, dropped = pd.DataFrame(), 0
gate = re_.data_gate(df, eu, us)
print("Data gate:", gate)
if not gate["ok"]:
    print("E037 decision: BLOCKED (data gate failed; 0 trials used)")
    dump({"status": "BLOCKED", "data_gate": gate, "index_data": idx_desc, "n_trials": 0, "blocks": ["dev"]},
         out_dir / f"{stem}.json")
    sys.exit(0)

res, costs = {}, {}
for arm in re_.ARMS:
    ev = re_.arm_events(df, arm)
    r = re_.evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
    r["decision"] = re_.decide_b35(r)
    res[arm] = r
    c = ev
    costs[arm] = {"n": int(len(c)),
                  "mean_signed_mid_pips": round(float(c["signed_pips"].mean()), 3) if len(c) else None,
                  "mean_net_bidask_pips": round(float(c["net_bidask_pips"].mean()), 3) if len(c) else None,
                  "mean_net_spec4_pips": round(float(c["net_spec4_pips"].mean()), 3) if len(c) else None,
                  "mean_net_costs_x1_5_pips": round(float(c["net_x1_5_pips"].mean()), 3) if len(c) else None,
                  "median_spread_entry_pips": round(float(c["entry_spread_pips"].median()), 3) if len(c) else None,
                  "median_spread_exit_pips": round(float(c["exit_spread_pips"].median()), 3) if len(c) else None}
cnt = {**re_.counts(df), "weekend_trading_dates_dropped": int(dropped)}


def _ev(x):
    x = pd.Series(x).dropna()
    return re_.evaluate(x) if len(x) >= 2 * re_.BOOT_BLOCK else {"n": int(len(x))}


stmt = set()
cal_path = ROOT / "data" / "calendars" / "fomc_dates.csv"
if cal_path.exists() and not args.synthetic:
    cal = pd.read_csv(cal_path)
    cal = cal[cal["scheduled"].astype(str).str.lower().eq("true") & ~cal["cancelled"].astype(str).str.lower().eq("true")]
    stmt = {pd.Timestamp(x).date() for x in cal["statement_date"]}

desc = {}
for arm in re_.ARMS:
    ev = df[df[f"{arm}_tested"]].copy()
    if not len(ev):
        continue
    s = ev[f"{arm}_s"]
    terc = pd.qcut(s.abs(), 3, labels=["low", "mid", "high"]) if len(ev) >= 30 else None
    d = {
        "share_long_eurusd": round(float((ev[f"{arm}_side"] > 0).mean()), 3),
        "s_stats": {"mean": round(float(s.mean()), 5), "sd": round(float(s.std()), 5),
                    "abs_median": round(float(s.abs().median()), 5)},
        "eu_leg_only_position_minus_sign_s_eu": _ev(-np.sign(ev[f"{arm}_s_eu"]) * ev["move_pips"]),
        "us_leg_only_position_plus_sign_s_us": _ev(np.sign(ev[f"{arm}_s_us"]) * ev["move_pips"]),
        "mondays": _ev(ev.loc[ev["weekday"] == 0, f"{arm}_signed_pips"]),
        "fridays_weekend_hold": _ev(ev.loc[ev["weekday"] == 4, f"{arm}_signed_pips"]),
        "excl_fomc_statement_dates": _ev(ev.loc[~ev["date"].isin(stmt), f"{arm}_signed_pips"]),
        "fomc_statement_dates_in_tested": int(ev["date"].isin(stmt).sum()),
        "excl_month_end_D_or_next": _ev(ev.loc[~(ev["month_end"] | ev["next_is_month_end"]), f"{arm}_signed_pips"]),
        "by_year": (ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")[f"{arm}_signed_pips"]
                    .agg(n="size", mean="mean", hit=lambda x: (x > 0).mean()).round(3).reset_index()
                    .to_dict(orient="records")),
    }
    if terc is not None:
        for lab in ("low", "mid", "high"):
            d[f"abs_s_tercile_{lab}"] = _ev(ev.loc[terc == lab, f"{arm}_signed_pips"])
    desc[arm] = d
both = df[df["b35_tested"] & df["b36_tested"]]
desc["b35_b36_same_side_share"] = round(float((both["b35_side"] == both["b36_side"]).mean()), 3) if len(both) else None
desc["unconditional_long_eurusd_b35_dates"] = _ev(df.loc[df["b35_tested"], "move_pips"])
desc["sd_move_pips"] = round(float(df.loc[df["b35_tested"], "move_pips"].std()), 3)
cont = df[df["b35_tested"] & df["contemp_move_pips"].notna()]
desc["contemporaneous_corr_s1_vs_eurusd_1600_prev_to_1600_D"] = {
    "n": int(len(cont)),
    "corr": round(float(cont["b35_s"].corr(cont["contemp_move_pips"])), 4) if len(cont) > 2 else None,
    "note": "Hau-Rey predicts NEGATIVE in this sign convention (EU outperformance with EUR depreciation)",
}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE037 DEV relative equity -> next-day EUR/USD, position = -sign(EU50 minus US500 log return), 16:05 D -> 16:00 next")
    for arm in re_.ARMS:
        print(f"\n{arm.upper()}:\n", pd.Series(res[arm]).to_string())
        print("Costs (descriptive):", costs[arm])
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
print("E037 decision B35:", res["b35"]["decision"])
print("E037 decision B36:", res["b36"]["decision"])

dump({"status": "complete", "data_gate": gate, "index_data": idx_desc, "result_b35": res["b35"], "result_b36": res["b36"],
      "counts": cnt, "cost_check": costs, "descriptive": desc, "n_trials": 2, "blocks": ["dev"],
      "boot_block": re_.BOOT_BLOCK, "smooth_n": re_.SMOOTH_N,
      "first_date": str(df["date"].iloc[0]), "last_date": str(df["date"].iloc[-1])}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E037_days.csv", index=False)
