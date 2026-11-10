"""E033 (B28 + B29): next-day reversal after a low-unexpected-volume day (B28) and next-day continuation after a
high-unexpected-volume day (B29), DEV ONLY, 2 trials.

Pre-registered in experiments/2026-11-10_E033_volume_reversal/ (backlog B28, B29). Val and OOS untouched.
Bars are restricted to dev trading dates BEFORE any computation. The volume gate runs first: if it fails, the run stops as
BLOCKED (0 trials used) and nothing else is computed.
Decision: fxresearch.volume_reversal.decide_b28 / decide_b29 on per-event signed mid returns. Everything else is descriptive.

    python scripts/run_e033_volume_reversal.py [--synthetic]
"""
import argparse
import sys
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch import daily_reversal
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.volume_reversal import (ENTRY_HM, EXIT_HM, cost_summary, counts, decide_b28, decide_b29, evaluate_b28,
                                        frame_from_bars, volume_gate)

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E033_synthetic_smoke" if args.synthetic else "E033_results"

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())
print("columns:", list(bars.columns))

gate = volume_gate(bars)
print("Volume gate:", gate)
if not gate["ok"]:
    print("E033 decision: BLOCKED (volume gate failed; 0 trials used)")
    dump({"status": "BLOCKED", "volume_gate": gate, "n_trials": 0, "blocks": ["dev"]}, out_dir / f"{stem}.json")
    sys.exit(0)

vol = pd.to_numeric(bars["volume"], errors="coerce")
vol_desc = {"bar_volume_min": float(vol.min()), "bar_volume_median": float(vol.median()), "bar_volume_max": float(vol.max())}

df = frame_from_bars(bars)
low = df[df["tested_low"]]
high = df[df["tested_high"]]
mid_t = df[df["tested_mid"]]

res28 = evaluate_b28(low["reversal_pips"]) if len(low) else {"n": 0, "note": "no events"}
res28["decision"] = decide_b28(res28)
res29 = evaluate_b28(high["continuation_pips"]) if len(high) else {"n": 0, "note": "no events"}
res29["decision"] = decide_b29(res29)
cnt = counts(df)


def _ev(frame, col):
    return evaluate_b28(frame[col]) if len(frame) else {}


# E021-type large-move days (|16:00 -> 16:00 NY move| > rolling p80 of 60 valid dates), same dev bars.
e21, _ = daily_reversal.daily_frame(bars)
e21 = daily_reversal.mark_events(e21)
large = set(e21.loc[e21["is_large"], "date"])
df["e21_large"] = df["date"].isin(large)
low, high, mid_t = df[df["tested_low"]], df[df["tested_high"]], df[df["tested_mid"]]

band = df[df["uv"].notna() & df["valid"]]
desc = {
    "volume_bar_stats": vol_desc,
    "low_reversal": res28, "high_continuation": res29,
    "mid_tercile_reversal": _ev(mid_t, "reversal_pips"),
    "high_tercile_reversal": _ev(high, "reversal_pips"),
    "low_tercile_continuation": _ev(low, "continuation_pips"),
    "low_share_e21_large": round(float(low["e21_large"].mean()), 3) if len(low) else None,
    "high_share_e21_large": round(float(high["e21_large"].mean()), 3) if len(high) else None,
    "low_reversal_excl_e21_large": _ev(low[~low["e21_large"]], "reversal_pips"),
    "high_continuation_excl_e21_large": _ev(high[~high["e21_large"]], "continuation_pips"),
    "corr_uv_range_pips": round(float(band["uv"].corr(band["range_pips"])), 3) if len(band) > 2 else None,
    "corr_uv_abs_r_pips": round(float(band["uv"].corr(band["r_pips"].abs())), 3) if len(band) > 2 else None,
    "mean_abs_r_low": round(float(low["r_pips"].abs().mean()), 3) if len(low) else None,
    "mean_abs_r_high": round(float(high["r_pips"].abs().mean()), 3) if len(high) else None,
    "control_all_tradable_banded_reversal": _ev(df[df["tradable"] & df["uv_p33"].notna()], "reversal_pips"),
}


def _by_year(frame, col):
    if not len(frame):
        return []
    g = frame.assign(year=pd.to_datetime(frame["date"]).dt.year).groupby("year")[col]
    return (pd.DataFrame({"n": g.size(), "mean": g.mean(), "hit": g.apply(lambda s: (s > 0).mean())}).round(3)
            .reset_index().to_dict(orient="records"))


by_year = {"low_reversal": _by_year(low, "reversal_pips"), "high_continuation": _by_year(high, "continuation_pips")}
costs = {"low_reversal": cost_summary(low, "rev", "reversal_pips"),
         "high_continuation": cost_summary(high, "cont", "continuation_pips")}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE033 DEV volume-conditioned next-day trades {ENTRY_HM} NY on D -> {EXIT_HM} NY on D+1 (pre-registered, 2 trials):")
    print("B28 low-UV reversal:\n", pd.Series(res28).to_string())
    print("B29 high-UV continuation:\n", pd.Series(res29).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):", by_year)
    print("\nDEV cost check (descriptive):", costs)
print("E033 decision B28:", res28["decision"])
print("E033 decision B29:", res29["decision"])

dump({"status": "complete", "volume_gate": gate, "result_b28": res28, "result_b29": res29, "counts": cnt,
      "descriptive": desc, "by_year": by_year, "cost_check": costs, "n_trials": 2, "blocks": ["dev"],
      "entry_hm_ny": list(ENTRY_HM), "exit_hm_ny": list(EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_date": str(df["date"].iloc[-1]) if len(df) else None}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E033_days.csv", index=False)
