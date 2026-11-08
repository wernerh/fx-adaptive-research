"""E018: round-number crossing continuation ("price cascades"), DEV ONLY (val and OOS untouched).

Pre-registered in experiments/2026-11-08_E018_round_number_cascades/ (backlog B15).
Decision: fxresearch.fixes.decide(n_trials=1) on per-event signed 60-minute mid return (B1 rule, block-20 bootstrap).
Control levels (offset 23 pips), 15/120-minute horizons, by-year, costs and calendar shares are descriptive only.
Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e018_round_numbers.py [--synthetic]
"""
import argparse
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.fixes import decide
from fxresearch.predictive import evaluate_predictor
from fxresearch.round_numbers import (
    CONTROL_OFFSET, DESCRIPTIVE_HORIZONS, build_trades, calendar_shares, cost_summary, detect_crossings,
)
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


def run(offset: float):
    ev = detect_crossings(bars, offset=offset)
    tr, skips = build_trades(bars, ev)
    s = pd.Series(tr["direction"].astype(float).to_numpy(), index=tr["entry_ts"])
    y = pd.Series(tr["ret_pips"].to_numpy(), index=tr["entry_ts"])
    res = evaluate_predictor(s, y)
    return ev, tr, skips, res


def short(r: dict) -> dict:
    return {k: r.get(k) for k in ("n_active", "hit_rate", "binom_p", "mean_signed_pips", "mean_signed_ci95_block_boot")}


ev, tr, skips, res = run(0.0)
res["decision"] = decide(res, n_trials=1)
cev, ctr, cskips, cres = run(CONTROL_OFFSET)

horizons = {}
for h in DESCRIPTIVE_HORIZONS:
    x = tr[f"signed_{h}m_pips"].dropna()
    horizons[f"{h}m"] = {"n": int(len(x)), "mean_signed_pips": round(float(x.mean()), 3) if len(x) else None,
                         "hit_rate": round(float((x > 0).mean()), 4) if len(x) else None}
by_year = (tr.assign(year=pd.to_datetime(tr["trading_date"]).dt.year).groupby("year")["signed_pips"]
           .agg(n="size", mean="mean", hit=lambda v: (v > 0).mean()).round(3))
by_dir = tr.groupby("direction")["signed_pips"].agg(n="size", mean="mean", hit=lambda v: (v > 0).mean()).round(3)
c = cost_summary(tr) if len(tr) else {}
cal = calendar_shares(tr)
diff = (round(res["mean_signed_pips"] - cres["mean_signed_pips"], 3)
        if "mean_signed_pips" in res and "mean_signed_pips" in cres else None)
n_dates = int(pd.Index(trading_date(bars.index)).nunique())

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE018 DEV round-number (00/50) crossing continuation, 60 min (pre-registered rule, 1 trial):")
    print(pd.Series(res).to_string())
    print("events:", len(ev), "trades:", len(tr), "skipped:", skips)
    print("\nControl levels (23/73), descriptive:")
    print(pd.Series(short(cres)).to_string())
    print("control events:", len(cev), "trades:", len(ctr), "skipped:", cskips)
    print("round minus control mean signed (pips):", diff)
    print("\nOther horizons (descriptive):", horizons)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nBy crossing direction (descriptive):\n", by_dir.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
    print("\nCalendar shares (event bar within +-15 min):", cal)
print("dev trading dates with bars:", n_dates)
print("E018 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E018_synthetic_smoke" if args.synthetic else "E018_results"
dump({"result": res, "n_events": int(len(ev)), "n_trades": int(len(tr)), "skips": skips,
      "control": {"result": short(cres), "n_events": int(len(cev)), "n_trades": int(len(ctr)), "skips": cskips},
      "round_minus_control_mean_pips": diff, "horizons": horizons,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "by_direction": by_dir.reset_index().to_dict(orient="records"),
      "cost_check": c, "calendar_shares": cal, "n_trials": 1, "blocks": ["dev"],
      "n_dev_trading_dates": n_dates}, out_dir / f"{stem}.json")
if not args.synthetic:
    tr.to_csv(out_dir / "E018_trades.csv", index=False)
