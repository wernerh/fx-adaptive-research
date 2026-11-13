"""E048: 1-hour swing-level breakout, 5-minute break-and-retest entry, 60-minute hold, DEV ONLY.

Pre-registered in experiments/2026-11-13_E048_breakout_retest/ (backlog B58). Val and OOS untouched.
Decision: fxresearch.breakout_retest.decide_b58 on per-trade signed 60-minute mid returns (FX-trading-date cluster bootstrap,
one-sided t-test). Legs, 30/120-minute holds, the enter-at-breakout-close variant, failed-break / no-retest counts, by year,
calendar shares and costs are descriptive only. Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e048_breakout_retest.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.breakout_retest import (DESCRIPTIVE_HORIZONS, HORIZON_MIN, breakout_close_events, decide_b58,
                                        detect_events, evaluate)
from fxresearch.round_numbers import build_trades, cost_summary
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


def _ev(frame, col="signed_pips"):
    return evaluate(frame, col) if len(frame.dropna(subset=[col])) >= 3 else {"n": int(len(frame))}


ev, setups, cnt = detect_events(bars)
tr, skips = build_trades(bars, ev, horizon=HORIZON_MIN, descriptive_horizons=DESCRIPTIVE_HORIZONS)
res = _ev(tr) if len(tr) else {"n": 0, "note": "no events"}
res["decision"] = decide_b58(res)

desc, by_year, cal = {}, pd.DataFrame(), {}
# descriptive variant: enter at the breakout 1h close, no retest, same hold and exclusions
bev = breakout_close_events(setups)
btr, bskips = build_trades(bars, bev, horizon=HORIZON_MIN, descriptive_horizons=DESCRIPTIVE_HORIZONS)
desc["variant_enter_at_breakout_close"] = {"result": _ev(btr) if len(btr) else {"n": 0}, "n_events": int(len(bev)),
                                           "skips": bskips,
                                           "cost_check": cost_summary(btr) if len(btr) else {}}
if len(tr):
    desc["long_leg"] = _ev(tr[tr["direction"] > 0])
    desc["short_leg"] = _ev(tr[tr["direction"] < 0])
    for h in DESCRIPTIVE_HORIZONS:
        desc[f"horizon_{h}m"] = _ev(tr, f"signed_{h}m_pips")
    tdd = pd.to_datetime(tr["trading_date"])
    ny = pd.Series([t.tz_convert("America/New_York") for t in tr["event_ts"]])
    ld = pd.Series([t.tz_convert("Europe/London") for t in tr["event_ts"]])
    nym = (ny.dt.hour * 60 + ny.dt.minute).to_numpy()
    ldm = (ld.dt.hour * 60 + ld.dt.minute).to_numpy()
    wins = {"ny_0830": np.abs(nym - 510) <= 15, "ny_1000": np.abs(nym - 600) <= 15, "london_1600": np.abs(ldm - 960) <= 15}
    near = np.zeros(len(tr), bool)
    for k, sel in wins.items():
        cal[f"share_within_15m_{k}"] = round(float(sel.mean()), 4)
        desc[f"within_15m_{k}"] = _ev(tr[sel])
        near |= sel
    desc["outside_release_fix_windows"] = _ev(tr[~near])
    by_year = (tr.assign(year=tdd.dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                    hit=("signed_pips", lambda s: (s > 0).mean())).round(3))
setups_per_year = (setups.assign(year=pd.to_datetime(setups["trading_date"]).dt.year)
                   .groupby(["year", "outcome"]).size().unstack(fill_value=0) if len(setups) else pd.DataFrame())
c = cost_summary(tr) if len(tr) else {}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE048 DEV 1h swing breakout + 5m break-and-retest, 60 min (pre-registered rule, 1 trial):")
    print(pd.Series(res).to_string())
    print("retest events:", len(ev), "trades:", len(tr), "skipped:", skips)
    print("counts:", cnt)
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
    print("\nSetups per year by outcome:\n", setups_per_year.to_string())
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
    print("\nCalendar shares (retest signal within +-15 min):", cal)
print("E048 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E048_synthetic_smoke" if args.synthetic else "E048_results"
dump({"result": res, "n_events": int(len(ev)), "n_trades": int(len(tr)), "skips": skips, "counts": cnt,
      "descriptive": desc,
      "setups_per_year": {str(k): {kk: int(vv) for kk, vv in v.items()}
                          for k, v in setups_per_year.to_dict(orient="index").items()},
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "cost_check": c, "calendar_shares": cal, "n_trials": 1, "blocks": ["dev"]}, out_dir / f"{stem}.json")
if not args.synthetic:
    tr.to_csv(out_dir / "E048_trades.csv", index=False)
