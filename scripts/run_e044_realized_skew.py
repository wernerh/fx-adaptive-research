"""E044: daily realized skewness -> next-day EUR/USD (s = sign(RS(D)), 20:00 NY D -> 16:55 NY D+1), DEV ONLY.

Pre-registered in experiments/2026-11-11_E044_realized_skew/ (backlog B50). Val and OOS untouched.
Decision: fxresearch.realized_skew.decide_b50 on per-date signed mid returns. Everything else is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e044_realized_skew.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.realized_skew import (ENTRY_HM, EXIT_HM, cost_summary, counts, decide_b50, evaluate, frame_from_bars,
                                      minute_skew)
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
args = ap.parse_args()

bars = load_bars(args.synthetic)
plan = SplitPlan(date(2024, 2, 29), date(2024, 3, 31), embargo_days=0) if args.synthetic else DEFAULT_PLAN
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())

g, df = frame_from_bars(bars)
ev = df[df["tested"]]
res = evaluate(ev["signed_pips"]) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b50(res)
cnt = counts(df)


def _ev(frame, col="signed_pips"):
    return evaluate(frame[col]) if len(frame) >= 40 else {"n": int(len(frame))}


desc = {}
if len(ev):
    ms = minute_skew(bars)
    ev = ev.assign(rs_1min=[ms.get(d, np.nan) for d in ev["date"]])
    side1 = np.sign(ev["rs_1min"])
    both = ev["r_day_pips"].notna()
    desc = {
        "share_long": round(float((ev["side"] > 0).mean()), 4),
        "opposite_sign_mean_pips_reported_only": round(float(-ev["signed_pips"].mean()), 3),
        "unconditional_long_same_hold": _ev(ev, "long_pips"),
        "corr_rs_r_day": round(float(ev.loc[both, "rs"].corr(ev.loc[both, "r_day_pips"])), 4) if both.sum() > 2 else None,
        "share_sign_rs_eq_sign_r_day": round(float((np.sign(ev.loc[both, "rs"]) == np.sign(ev.loc[both, "r_day_pips"])).mean()), 4)
        if both.sum() else None,
        "within_r_day_pos": _ev(ev[ev["r_day_pips"] > 0]),
        "within_r_day_neg": _ev(ev[ev["r_day_pips"] < 0]),
        "rs_mean": round(float(ev["rs"].mean()), 4), "rs_median": round(float(ev["rs"].median()), 4),
        "rs_sd": round(float(ev["rs"].std()), 4),
        "robust_1min_rs_sign_agreement": round(float((side1 == ev["side"]).mean()), 4),
        "robust_1min_rs_signed": _ev(ev.assign(s1=side1 * ev["long_pips"]), "s1"),
        "median_n_returns": float(ev["n_returns"].median()),
    }
    if len(ev) >= 3:
        q = pd.qcut(ev["rs"].abs().rank(method="first"), 3, labels=["low", "mid", "high"])
        for lab in ("low", "mid", "high"):
            desc[f"abs_rs_tercile_{lab}"] = _ev(ev[q == lab])
    by_year = (ev.assign(year=pd.to_datetime(ev["date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                    hit=("signed_pips", lambda s: (s > 0).mean())).round(3))
else:
    by_year = pd.DataFrame()
c = cost_summary(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE044 DEV sign(RS(D)) x EUR/USD {ENTRY_HM} NY D -> {EXIT_HM} NY D+1 (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E044 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E044_synthetic_smoke" if args.synthetic else "E044_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"), "cost_check": c, "n_trials": 1, "blocks": ["dev"],
      "entry_hm_ny": list(ENTRY_HM), "exit_hm_ny": list(EXIT_HM),
      "first_date": str(df["date"].iloc[0]) if len(df) else None, "last_date": str(df["date"].iloc[-1]) if len(df) else None},
     out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E044_days.csv", index=False)
