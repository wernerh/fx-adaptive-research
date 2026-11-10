"""E035: overnight -> intraday reversal in EUR/USD (B32: -sign(r_on) x r_id; B33: -sign(O20) x r_id), DEV ONLY, 2 trials.

Pre-registered in experiments/2026-11-10_E035_overnight_reversal/ (backlog B32 + B33). Val and OOS untouched.
Decision: fxresearch.overnight_reversal.decide_b32 / decide_b33 on per-date signed mid returns (block-20 bootstrap, p < 0.025).
Everything else is descriptive. Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e035_overnight_reversal.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.overnight_reversal import (BOOT_BLOCK, ENTRY_HM, EXIT_HM, OPEN_HM, SMOOTH_N, arm_events, counts, decide_b32,
                                           decide_b33, evaluate_b32, frame_from_bars, slope)
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.vol_state_fix import cost_summary

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

df = frame_from_bars(bars)
ev32 = arm_events(df, "b32") if len(df) else df
ev33 = arm_events(df, "b33") if len(df) else df
res32 = evaluate_b32(ev32["signed_pips"]) if len(ev32) else {"n": 0, "note": "no events"}
res32["decision"] = decide_b32(res32)
res33 = evaluate_b32(ev33["signed_pips"]) if len(ev33) else {"n": 0, "note": "no events"}
res33["decision"] = decide_b33(res33)
cnt = counts(df)


def _ev(frame, col="signed_pips"):
    return evaluate_b32(frame[col]) if len(frame) else {}


desc = {"continuation_reading_note": "a negative mean (continuation) is logged as exploratory only (not a trial)"}
if len(ev32):
    desc["slope_r_id_on_r_on"] = slope(df)
    terc = pd.qcut(ev32["r_on_pips"].abs(), 3, labels=["low", "mid", "high"])
    for k in ["low", "mid", "high"]:
        desc[f"b32_abs_r_on_tercile_{k}"] = _ev(ev32[terc == k])
    desc["b32_mondays"] = _ev(ev32[ev32["weekday"] == 0])
    desc["b32_tue_fri"] = _ev(ev32[ev32["weekday"] != 0])
    desc["b32_share_long"] = round(float((ev32["side"] > 0).mean()), 3)
    desc["sd_r_on_pips"] = round(float(ev32["r_on_pips"].std()), 3)
    desc["sd_r_id_pips"] = round(float(ev32["r_id_pips"].std()), 3)
    desc["unconditional_long_r_id"] = _ev(ev32, "r_id_pips")
if len(ev33):
    terc33 = pd.qcut(ev33["o20_pips"].abs(), 3, labels=["low", "mid", "high"])
    for k in ["low", "mid", "high"]:
        desc[f"b33_abs_o20_tercile_{k}"] = _ev(ev33[terc33 == k])
    desc["b33_share_long"] = round(float((ev33["side"] > 0).mean()), 3)
    both = df[df["b32_tested"] & df["b33_tested"]]
    desc["b32_b33_same_side_share"] = round(float((both["b32_side"] == both["b33_side"]).mean()), 3) if len(both) else None


def _by_year(frame):
    if not len(frame):
        return []
    g = frame.assign(year=pd.to_datetime(frame["date"]).dt.year).groupby("year")["signed_pips"]
    return (pd.DataFrame({"n": g.size(), "mean": g.mean(), "hit": g.apply(lambda s: (s > 0).mean())}).round(3)
            .reset_index().to_dict(orient="records"))


by_year = {"b32": _by_year(ev32), "b33": _by_year(ev33)}
cost = {"b32": cost_summary(ev32), "b33": cost_summary(ev33)}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE035 DEV overnight {OPEN_HM}->{ENTRY_HM} NY, hold {ENTRY_HM} -> {EXIT_HM} NY (pre-registered, 2 trials, "
          f"block {BOOT_BLOCK}, p < 0.025)")
    print("\nB32 -sign(r_on) x r_id:")
    print(pd.Series(res32).to_string())
    print(f"\nB33 -sign(O{SMOOTH_N}) x r_id:")
    print(pd.Series(res33).to_string())
    print("\nCounts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):", by_year)
    print("\nDEV cost check (descriptive):", cost)
print("E035 decision: B32", res32["decision"], "| B33", res33["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E035_synthetic_smoke" if args.synthetic else "E035_results"
dump({"result_b32": res32, "result_b33": res33, "counts": cnt, "descriptive": desc, "by_year": by_year,
      "cost_check": cost, "n_trials": 2, "blocks": ["dev"], "boot_block": BOOT_BLOCK, "smooth_n": SMOOTH_N,
      "open_hm_ny": list(OPEN_HM), "entry_hm_ny": list(ENTRY_HM), "exit_hm_ny": list(EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E035_days.csv", index=False)
