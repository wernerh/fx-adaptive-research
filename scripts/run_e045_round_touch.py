"""E045: take-profit reversal at round numbers, rejected touches (fade the first touch of a 00/50 level, 60 min), DEV ONLY.

Pre-registered in experiments/2026-11-11_E045_round_touch_reversal/ (backlog B52). Val and OOS untouched.
Decision: fxresearch.round_touch.decide_b52 on per-event signed 60-minute mid returns (date-cluster bootstrap, t-test).
Control levels (23/73), 15/120-minute horizons, up/down, crossed-within-hold share, by-year, costs and calendar shares are
descriptive only. Bars are restricted to dev trading dates BEFORE any computation.

    python scripts/run_e045_round_touch.py [--synthetic]
"""
import argparse
from datetime import date

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.round_numbers import DESCRIPTIVE_HORIZONS, build_trades, calendar_shares, cost_summary
from fxresearch.round_touch import CONTROL_OFFSET, crossed_within_hold, decide_b52, detect_touches, evaluate
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


def run(offset: float):
    ev = detect_touches(bars, offset=offset)
    tr, skips = build_trades(bars, ev)
    res = _ev(tr) if len(tr) else {"n": 0, "note": "no events"}
    return ev, tr, skips, res


ev, tr, skips, res = run(0.0)
res["decision"] = decide_b52(res)
cev, ctr, cskips, cres = run(CONTROL_OFFSET)
diff = (round(res["mean_pips"] - cres["mean_pips"], 3) if "mean_pips" in res and "mean_pips" in cres else None)

desc = {}
by_year = pd.DataFrame()
if len(tr):
    crossed = crossed_within_hold(bars, tr)
    desc = {
        "up_touches_short": _ev(tr[tr["direction"] < 0]),
        "down_touches_long": _ev(tr[tr["direction"] > 0]),
        "share_short": round(float((tr["direction"] < 0).mean()), 4),
        "share_level_crossed_by_close_within_hold": round(float(crossed.mean()), 4),
        "crossed_within_hold": _ev(tr[crossed]),
        "not_crossed_within_hold": _ev(tr[~crossed]),
        "continuation_mean_pips_reported_only": round(float(-tr["signed_pips"].mean()), 3),
    }
    for h in DESCRIPTIVE_HORIZONS:
        desc[f"horizon_{h}m"] = _ev(tr, f"signed_{h}m_pips")
    m = pd.Series([t.tz_convert("America/New_York") for t in tr["event_ts"]])
    mins = m.dt.hour * 60 + m.dt.minute
    for name, c in (("ny_0830", 8 * 60 + 30), ("ny_1000", 10 * 60), ("ny_1100", 11 * 60)):
        sel = ((mins - c).abs() <= 15).to_numpy()
        desc[f"within_15m_{name}"] = _ev(tr[sel])
    near = ((mins - 510).abs() <= 15) | ((mins - 600).abs() <= 15) | ((mins - 660).abs() <= 15)
    desc["outside_release_fix_windows"] = _ev(tr[~near.to_numpy()])
    by_year = (tr.assign(year=pd.to_datetime(tr["trading_date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"),
                    hit=("signed_pips", lambda s: (s > 0).mean())).round(3))
ev_per_year = (ev.assign(year=pd.to_datetime(ev["trading_date"]).dt.year).groupby("year").size().to_dict()
               if len(ev) else {})
c = cost_summary(tr) if len(tr) else {}
cal = calendar_shares(tr) if len(tr) else {}
n_dates = int(pd.Index(trading_date(bars.index)).nunique())

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE045 DEV fade first rejected touch of a 00/50 level, 60 min (pre-registered rule, 1 trial):")
    print(pd.Series(res).to_string())
    print("touch events:", len(ev), "trades:", len(tr), "skipped:", skips)
    print("\nControl levels (23/73), descriptive:")
    print(pd.Series(cres).to_string())
    print("control events:", len(cev), "trades:", len(ctr), "skipped:", cskips)
    print("round minus control mean signed (pips):", diff)
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
    print("\nEvents per year:", ev_per_year)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive):")
    print(pd.Series(c).to_string())
    print("\nCalendar shares (event bar within +-15 min):", cal)
print("dev trading dates with bars:", n_dates)
print("E045 decision:", res["decision"])

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E045_synthetic_smoke" if args.synthetic else "E045_results"
dump({"result": res, "n_events": int(len(ev)), "n_trades": int(len(tr)), "skips": skips,
      "control": {"result": cres, "n_events": int(len(cev)), "n_trades": int(len(ctr)), "skips": cskips},
      "round_minus_control_mean_pips": diff, "descriptive": desc, "events_per_year": ev_per_year,
      "by_year": by_year.reset_index().to_dict(orient="records"),
      "cost_check": c, "calendar_shares": cal, "n_trials": 1, "blocks": ["dev"],
      "n_dev_trading_dates": n_dates}, out_dir / f"{stem}.json")
if not args.synthetic:
    tr.to_csv(out_dir / "E045_trades.csv", index=False)
