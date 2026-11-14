"""E049: multi-timeframe trend alignment (1h + 30m + 15m close vs EMA20 agree), 5-minute EMA20-cross trigger, 60-minute
hold, DEV ONLY.

Pre-registered in experiments/2026-11-14_E049_mtf_alignment/ (backlog B59). Val and OOS untouched.
Decision: fxresearch.mtf_alignment.decide_b59 on per-trade signed 60-minute mid returns (FX-trading-date cluster bootstrap,
one-sided t-test). Control (no alignment), 10-minute trigger, legs, 30/120-minute holds, by year, calendar shares and costs are
descriptive only. Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e049_mtf_alignment.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.mtf_alignment import (ALT_TRIGGER_TF, DESCRIPTIVE_HORIZONS, HORIZON_MIN, decide_b59, detect_events,
                                      evaluate)
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


def _run(ev):
    return build_trades(bars, ev, horizon=HORIZON_MIN, descriptive_horizons=DESCRIPTIVE_HORIZONS)


ev, cnt = detect_events(bars)
tr, skips = _run(ev)
res = _ev(tr) if len(tr) else {"n": 0, "note": "no events"}
res["decision"] = decide_b59(res)

desc, by_year, cal = {}, pd.DataFrame(), {}
for name, kw in (("control_no_alignment_5m", {"aligned": False}),
                 ("trigger_10m_aligned", {"trigger_minutes": ALT_TRIGGER_TF})):
    v_ev, v_cnt = detect_events(bars, **kw)
    v_tr, v_sk = _run(v_ev)
    desc[name] = {"result": _ev(v_tr) if len(v_tr) else {"n": 0}, "counts": v_cnt, "skips": v_sk,
                  "cost_check": cost_summary(v_tr) if len(v_tr) else {}}
if len(tr):
    desc["long_leg"] = _ev(tr[tr["direction"] > 0])
    desc["short_leg"] = _ev(tr[tr["direction"] < 0])
    for h in DESCRIPTIVE_HORIZONS:
        desc[f"horizon_{h}m"] = _ev(tr, f"signed_{h}m_pips")
    tdd = pd.to_datetime(tr["trading_date"])
    sig_t = pd.DatetimeIndex(tr["event_ts"]) + pd.Timedelta(minutes=1)
    ny, ld = sig_t.tz_convert("America/New_York"), sig_t.tz_convert("Europe/London")
    nym = np.asarray(ny.hour * 60 + ny.minute)
    ldm = np.asarray(ld.hour * 60 + ld.minute)
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
c = cost_summary(tr) if len(tr) else {}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE049 DEV 1h+30m+15m EMA20 alignment + 5m EMA20 cross, 60 min (pre-registered rule, 1 trial):")
    print(pd.Series(res).to_string())
    print("events:", len(ev), "trades:", len(tr), "skipped:", skips)
    print("counts:", cnt)
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
    print("\nCalendar shares (signal close within +-15 min):", cal)
print("E049 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E049_synthetic_smoke" if args.synthetic else "E049_results"
dump({"result": res, "n_events": int(len(ev)), "n_trades": int(len(tr)), "skips": skips, "counts": cnt,
      "descriptive": desc, "by_year": by_year.reset_index().to_dict(orient="records"),
      "cost_check": c, "calendar_shares": cal, "n_trials": 1, "blocks": ["dev"]}, out_dir / f"{stem}.json")
if not args.synthetic:
    tr.to_csv(out_dir / "E049_trades.csv", index=False)
