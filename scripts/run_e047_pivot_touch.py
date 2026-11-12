"""E047: pivot-point R1/S1 first touch, continuation (long after R1 touch, short after S1 touch, 120 min), DEV ONLY.

Pre-registered in experiments/2026-11-12_E047_pivot_touch/ (backlog B56). Val and OOS untouched.
Decision: fxresearch.pivot_touch.decide_b56 on per-event signed 120-minute mid returns (UTC-date cluster bootstrap, t-test).
Legs, 60/180-minute holds, thesis bracket, traditional-direction mean, excluding the thesis window, by year, calendar shares,
costs and the +-0.0023 control levels are descriptive only. Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e047_pivot_touch.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.pivot_touch import (CONTROL_SHIFT, DESCRIPTIVE_HORIZONS, HORIZON_MIN, bracket_outcomes, decide_b56,
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


def run(shift: float):
    ev, cnt = detect_events(bars, shift=shift)
    tr, skips = build_trades(bars, ev, horizon=HORIZON_MIN, descriptive_horizons=DESCRIPTIVE_HORIZONS)
    res = _ev(tr) if len(tr) else {"n": 0, "note": "no events"}
    return ev, cnt, tr, skips, res


ev, cnt, tr, skips, res = run(0.0)
res["decision"] = decide_b56(res)
controls = {}
for name, sh in (("plus_0023", CONTROL_SHIFT), ("minus_0023", -CONTROL_SHIFT)):
    cev, ccnt, ctr, cskips, cres = run(sh)
    controls[name] = {"result": cres, "n_events": int(len(cev)), "n_trades": int(len(ctr)), "skips": cskips,
                      "counts": ccnt}

desc, by_year, cal = {}, pd.DataFrame(), {}
if len(tr):
    leg = tr["direction"].map({1: "R1", -1: "S1"})
    desc["R1_long"] = _ev(tr[leg == "R1"])
    desc["S1_short"] = _ev(tr[leg == "S1"])
    desc["traditional_direction_mean_pips_reported_only"] = round(float(-tr["signed_pips"].mean()), 3)
    for h in DESCRIPTIVE_HORIZONS:
        desc[f"horizon_{h}m"] = _ev(tr, f"signed_{h}m_pips")
    br = bracket_outcomes(bars, tr, ev)
    vc = br.value_counts().to_dict()
    res_n = vc.get("win", 0) + vc.get("loss", 0)
    desc["thesis_bracket_0_15pct"] = {"counts": {k: int(v) for k, v in vc.items()},
                                      "win_rate_resolved": round(vc.get("win", 0) / res_n, 4) if res_n else None}
    tdd = pd.to_datetime(tr["trading_date"])
    thesis = (tdd >= "2017-06-01") & (tdd <= "2017-12-29")
    desc["excluding_2017_06_01_to_2017_12_29"] = _ev(tr[~thesis.to_numpy()])
    desc["thesis_window_only"] = _ev(tr[thesis.to_numpy()])
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
ev_per_year = (ev.assign(year=pd.to_datetime(ev["trading_date"]).dt.year).groupby("year").size().to_dict()
               if len(ev) else {})
c = cost_summary(tr) if len(tr) else {}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE047 DEV pivot R1/S1 first touch, continuation, 120 min (pre-registered rule, 1 trial):")
    print(pd.Series(res).to_string())
    print("events:", len(ev), "trades:", len(tr), "skipped:", skips, "counts:", cnt)
    for k, v in controls.items():
        print(f"\nControl levels {k} (descriptive):")
        print(pd.Series(v["result"]).to_string())
        print("events:", v["n_events"], "trades:", v["n_trades"], "skipped:", v["skips"])
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
    print("\nEvents per year:", ev_per_year)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
    print("\nCalendar shares (event bar within +-15 min):", cal)
print("E047 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E047_synthetic_smoke" if args.synthetic else "E047_results"
dump({"result": res, "n_events": int(len(ev)), "n_trades": int(len(tr)), "skips": skips, "counts": cnt,
      "controls": controls, "descriptive": desc, "events_per_year": ev_per_year,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "cost_check": c, "calendar_shares": cal, "n_trials": 1, "blocks": ["dev"]}, out_dir / f"{stem}.json")
if not args.synthetic:
    tr.to_csv(out_dir / "E047_trades.csv", index=False)
