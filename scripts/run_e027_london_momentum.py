"""E027: London-open intraday momentum into the pre-London-fix half hour (sign(08:00 -> 08:30 London) held 15:25 -> 15:55 London),
DEV ONLY.

Pre-registered in experiments/2026-11-09_E027_london_momentum/ (backlog B22). Val and OOS untouched.
Decision: fxresearch.london_momentum.decide_b22 on per-date signed mid returns (block-20 bootstrap). Everything else is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e027_london_momentum.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.london_momentum import (ALT_SIGNAL_END_HM, BOOT_BLOCK, ENTRY_HM, EXIT_HM, SIGNAL_END_HM, SIGNAL_START_HM,
                                        counts, decide_b22, evaluate_b22, frame_from_bars, slope)
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
ev = df[df["tested"]] if len(df) else df
res = evaluate_b22(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b22(res)
cnt = counts(df)


def _ev(frame, col="signed_pips"):
    return evaluate_b22(frame[col]) if len(frame) else {}


desc = {"reversal_reading_note": "a negative mean is logged as exploratory only (not a trial)"}
if len(ev):
    hour = ev[ev["r1_hour_pips"].notna() & (ev["r1_hour_pips"] != 0)]
    desc["first_hour_signal_0800_0900"] = _ev(hour, "signed_hour_signal_pips")
    desc["slope_last_half_on_r1"] = slope(df)
    terc = pd.qcut(ev["r1_pips"].abs(), 3, labels=["low", "mid", "high"])
    for k in ["low", "mid", "high"]:
        desc[f"abs_r1_tercile_{k}"] = _ev(ev[terc == k])
    desc["month_end"] = _ev(ev[ev["month_end"]])
    desc["non_month_end"] = _ev(ev[~ev["month_end"]])
    desc["dst_mismatch"] = _ev(ev[ev["dst_mismatch"]])
    desc["share_long"] = round(float((ev["side"] > 0).mean()), 3)
    desc["mean_abs_r1_pips"] = round(float(ev["r1_pips"].abs().mean()), 3)
    desc["unconditional_last_half_mean_pips"] = round(float(ev["last_half_pips"].mean()), 3)


def _group(frame, key):
    if not len(frame):
        return pd.DataFrame()
    return (frame.assign(**{key: key_fn[key](frame)}).groupby(key)
            .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                 hit=("signed_pips", lambda s: (s > 0).mean())).round(3))


key_fn = {"year": lambda f: pd.to_datetime(f["date"]).dt.year,
          "weekday": lambda f: pd.to_datetime(f["date"]).dt.day_name()}
by_year = _group(ev, "year")
by_weekday = _group(ev, "weekday")
c = cost_summary(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE027 DEV sign(r1 {SIGNAL_START_HM}->{SIGNAL_END_HM} London) held {ENTRY_HM} -> {EXIT_HM} London "
          f"(pre-registered, 1 trial, block {BOOT_BLOCK}):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy weekday (descriptive):\n", by_weekday.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E027 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E027_synthetic_smoke" if args.synthetic else "E027_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_weekday": by_weekday.reset_index().to_dict(orient="records"),
      "cost_check": c, "n_trials": 1, "blocks": ["dev"], "boot_block": BOOT_BLOCK,
      "signal_hm_london": [list(SIGNAL_START_HM), list(SIGNAL_END_HM)], "alt_signal_end_hm": list(ALT_SIGNAL_END_HM),
      "entry_hm_london": list(ENTRY_HM), "exit_hm_london": list(EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E027_days.csv", index=False)
