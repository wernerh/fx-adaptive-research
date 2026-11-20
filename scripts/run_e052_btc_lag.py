"""E052 (B64): lagged daily Bitcoin return -> next-day EUR/USD, 16:00 NY daily hold, DEV ONLY, 1 trial.

Pre-registered in experiments/2026-11-20_E052_btc_lag/ (backlog B64, R308). Val and OOS untouched.
EUR/USD bars are restricted to dev trading dates BEFORE any computation; BTC bars are cut at 2021-01-01 UTC.
The data gate runs first: if it fails, the run stops as BLOCKED (0 trials used) and no trade result is computed.
Decision: fxresearch.btc_lag.decide_b64 on daily signed mid returns. Everything else is descriptive.

    python scripts/run_e052_btc_lag.py [--synthetic] [--btc-dir data/raw_btc]
"""
import argparse
import sys
from datetime import date

import numpy as np
import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch import btc_lag as bl
from fxresearch import month_end_hedging as mh
from fxresearch.data import PIP, synthetic_bars
from fxresearch.sessions import trading_date
from fxresearch.splits import DEFAULT_PLAN, SplitPlan
from fxresearch.tsmom import cost_summary, daily_quotes, evaluate

ap = argparse.ArgumentParser()
ap.add_argument("--synthetic", action="store_true")
ap.add_argument("--btc-dir", default=str(ROOT / "data" / "raw_btc"))
args = ap.parse_args()

out_dir = ROOT / "backtests" / "validation_reports"
stem = "E052_synthetic_smoke" if args.synthetic else "E052_results"

if args.synthetic:
    bars = synthetic_bars("2024-01-01", "2024-03-31")
    plan = SplitPlan(date(2024, 3, 31), date(2024, 6, 30), embargo_days=0)
    btc = synthetic_bars("2024-01-01", "2024-03-31", seed=21)
    for c in btc.columns:
        btc[c] = btc[c] * 40000.0
    start, end = date(2024, 1, 3), date(2024, 3, 29)
else:
    bars = load_bars(False)
    plan = DEFAULT_PLAN
    btc = mh.load_index(args.btc_dir, bl.BTC)
    btc = btc[btc.index < pd.Timestamp("2021-01-01", tz="UTC")]  # dev only: never read BTC bars from val/OOS dates
    start, end = bl.START, bl.END
td = pd.Index(trading_date(bars.index))
bars = bars[(plan.assign(td).to_numpy() == "dev")]
print("dev bars:", len(bars), bars.index.min(), "->", bars.index.max())
btc_desc = {"bars": int(len(btc)), "first": str(btc.index.min()) if len(btc) else None,
            "last": str(btc.index.max()) if len(btc) else None}
print("btc data:", btc_desc)

q = daily_quotes(bars)
bm = bl.btc_mids(btc, q.index)
gate = bl.data_gate(q, bm, len(btc), start, end)
print("Data gate:", gate)
if not gate["ok"]:
    print("E052 decision: BLOCKED (data gate failed; 0 trials used)")
    dump({"status": "BLOCKED", "data_gate": gate, "btc_data": btc_desc, "n_trials": 0, "blocks": ["dev"]},
         out_dir / f"{stem}.json")
    sys.exit(0)

df, skips = bl.build_daily(q, bm, start, end)
res = evaluate(df["signed_pips"]) if len(df) else {"n": 0, "note": "no events"}
res["decision"] = bl.decide_b64(res)


def _ev(x):
    x = pd.Series(x, dtype=float).dropna()
    return evaluate(x) if len(x) >= 40 else {"n": int(len(x))}


desc = {}
if len(df):
    mid = ((q["bid"] + q["ask"]) / 2).to_numpy(dtype=float)
    contemp = np.array([(mid[p] - mid[p - 1]) / PIP for p in df["pos"]])
    ok = np.isfinite(contemp)
    desc["same_day_corr_b_vs_eurusd_prev1600_to_D1600"] = {
        "n": int(ok.sum()), "corr": round(float(np.corrcoef(df["b"].to_numpy()[ok], contemp[ok])[0, 1]), 4) if ok.sum() > 2 else None}
    desc["lag_corr_b_vs_next_move"] = round(float(df["b"].corr(df["ret_pips"])), 4)
    desc["share_long_eurusd"] = round(float((df["signal"] > 0).mean()), 4)
    desc["b_stats"] = {"mean": round(float(df["b"].mean()), 5), "sd": round(float(df["b"].std()), 5),
                       "abs_median": round(float(df["b"].abs().median()), 5)}
    desc["mondays_weekend_b"] = _ev(df.loc[df["weekday"] == 0, "signed_pips"])
    desc["tue_to_fri"] = _ev(df.loc[df["weekday"] != 0, "signed_pips"])
    terc = pd.qcut(df["b"].abs(), 3, labels=["low", "mid", "high"])
    for lab in ("low", "mid", "high"):
        desc[f"abs_b_tercile_{lab}"] = _ev(df.loc[terc == lab, "signed_pips"])
    desc["buy_and_hold_same_dates"] = _ev(df["ret_pips"])
    by_year = (df.assign(year=pd.to_datetime(df["date"]).dt.year).groupby("year")
               .agg(n=("signed_pips", "size"), mean=("signed_pips", "mean"), hit=("signed_pips", lambda v: (v > 0).mean()),
                    long_share=("signal", lambda s: (s > 0).mean())).round(3))
else:
    by_year = pd.DataFrame()
c = cost_summary(df) if len(df) else {"n_days": 0}

with pd.option_context("display.width", 250, "display.max_columns", 40):
    print("\nE052 DEV lagged Bitcoin -> next-day EUR/USD, s = sign(ln BTC 16:00 NY D / prev date), 16:00 NY D -> 16:00 NY next"
          " (pre-registered, 1 trial):")
    print(pd.Series(res).to_string())
    print("grid dates:", len(q), "test days:", len(df), "excluded:", skips)
    print("\nDescriptive:")
    for k, v in desc.items():
        print(" ", k, ":", v)
    print("\nBy year (descriptive):\n", by_year.to_string())
    print("\nDEV cost check (descriptive; swap/carry NOT included):")
    print(pd.Series(c).to_string())
print("E052 decision B64:", res["decision"])

dump({"status": "complete", "data_gate": gate, "btc_data": btc_desc, "result_b64": res, "n_grid_dates": int(len(q)),
      "n_test_days": int(len(df)), "skips": skips, "descriptive": desc,
      "by_year": by_year.reset_index().to_dict(orient="records"), "cost_check": c,
      "first_test_date": str(df["date"].iloc[0]) if len(df) else None,
      "last_test_date": str(df["date"].iloc[-1]) if len(df) else None,
      "window": [str(start), str(end)], "n_trials": 1, "blocks": ["dev"]}, out_dir / f"{stem}.json")
if not args.synthetic:
    df.to_csv(out_dir / "E052_daily.csv", index=False)
