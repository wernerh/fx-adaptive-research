"""E043: post-jump reversal after 5-minute Lee-Mykland jumps (fade -sign(r) from t+10 to t+70 min), DEV ONLY.

Pre-registered in experiments/2026-11-11_E043_post_jump_reversal/ (backlog B48). Val and OOS untouched.
Decision: fxresearch.post_jump.decide_b48 on per-event signed mid returns. Everything else is descriptive.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e043_post_jump.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.post_jump import (K, MIN_ABS_MOVE, THRESHOLD, cost_summary, counts, decide_b48, evaluate,
                                  frame_from_bars)
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

g, allj = frame_from_bars(bars)
ev = allj[allj["tested"]] if len(allj) else allj
res = evaluate(ev) if len(ev) else {"n": 0, "note": "no events"}
res["decision"] = decide_b48(res)
cnt = counts(g, allj)


def _ev(frame, col="signed_pips"):
    return evaluate(frame, col) if len(frame) >= 3 else {"n": int(len(frame))}


desc = {}
if len(ev):
    m = ev["ny_minutes"]
    desc = {
        "continuation_mean_pips_reported_only": round(float(-ev["signed_pips"].mean()), 3),
        "positive_jumps_short_eurusd": _ev(ev[ev["r"] > 0]),
        "negative_jumps_long_eurusd": _ev(ev[ev["r"] < 0]),
        "release_proxy_0825_0850_ny": _ev(ev[(m >= 8 * 60 + 25) & (m <= 8 * 60 + 50)]),
        "not_release_proxy": _ev(ev[~((m >= 8 * 60 + 25) & (m <= 8 * 60 + 50))]),
        "release_proxy_share": round(float(((m >= 8 * 60 + 25) & (m <= 8 * 60 + 50)).mean()), 4),
        "london_open_0200_0400_ny": _ev(ev[(m >= 120) & (m < 240)]),
        "not_london_open": _ev(ev[~((m >= 120) & (m < 240))]),
        "skipped_bar_t5_t10_signed": _ev(ev, "skipped_bar_signed_pips"),
        "median_abs_jump_pips": round(float(ev["move_pips"].abs().median()), 3),
        "median_abs_L": round(float(ev["L"].abs().median()), 3),
        "share_events_positive_jump": round(float((ev["r"] > 0).mean()), 4),
        "events_by_ny_hour": ev.groupby(m // 60).size().to_dict(),
    }
    if len(ev) >= 3:
        q = pd.qcut(ev["L"].abs().rank(method="first"), 3, labels=["low", "mid", "high"])
        for lab in ("low", "mid", "high"):
            desc[f"abs_L_tercile_{lab}"] = _ev(ev[q == lab])
    by_year = (ev.assign(year=pd.to_datetime(ev["trading_date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                    hit=("signed_pips", lambda s: (s > 0).mean())).round(3))
else:
    by_year = pd.DataFrame()
c = cost_summary(ev)

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print(f"\nE043 DEV fade -sign(r) t+10 -> t+70 min after 5-min LM jumps (|L| > {THRESHOLD:.3f}, |move| >= "
          f"{MIN_ABS_MOVE / 0.0001:.0f} pips, K {K}) (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("Counts:", cnt)
    print("\nDescriptive:")
    for k, val in desc.items():
        print(" ", k, ":", val)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
print("E043 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E043_synthetic_smoke" if args.synthetic else "E043_results"
dump({"result": res, "counts": cnt, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"), "cost_check": c, "n_trials": 1, "blocks": ["dev"],
      "threshold": THRESHOLD, "K": K, "min_abs_move": MIN_ABS_MOVE,
      "first_slot": str(g.index[0]) if len(g) else None, "last_slot": str(g.index[-1]) if len(g) else None},
     out_dir / f"{stem}.json")
if not args.synthetic:
    allj.to_csv(out_dir / "E043_events.csv", index=False)
