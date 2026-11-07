"""Backtest one strategy on one split block and append a row to backtests/performance_summary.csv.

    python scripts/run_backtest.py asian_range_breakout --block dev --experiment E002
    python scripts/run_backtest.py london_us_continuation --synthetic
"""
import argparse
import csv
from datetime import datetime, timezone

import pandas as pd

from _common import ROOT, dump, load_bars
from fxresearch.backtest import CostModel, simulate
from fxresearch.features import daily_features
from fxresearch.metrics import trade_metrics
from fxresearch.splits import DEFAULT_PLAN
from fxresearch.strategies import REGISTRY

ap = argparse.ArgumentParser()
ap.add_argument("strategy", choices=sorted(REGISTRY))
ap.add_argument("--block", choices=["dev", "val", "oos", "all"], default="dev")
ap.add_argument("--experiment", default="SMOKE")
ap.add_argument("--synthetic", action="store_true")
ap.add_argument("--slippage", type=float, default=0.1)
ap.add_argument("--commission", type=float, default=0.1)
args = ap.parse_args()

if args.block == "oos":
    ok = input("OOS is evaluated ONCE per strategy version. Type the experiment id to confirm: ")
    if ok.strip() != args.experiment:
        raise SystemExit("aborted")

bars = load_bars(args.synthetic)
feats = daily_features(bars)
if not args.synthetic and args.block != "all":
    split = DEFAULT_PLAN.assign(feats.index)
    feats = feats[split == args.block]

mod = REGISTRY[args.strategy]
signals = mod.generate_signals(bars, feats, mod.Params())
trades = simulate(bars, signals, CostModel(slippage_pips=args.slippage, commission_pips=args.commission))
m = trade_metrics(trades, trading_days=len(feats))
print(pd.Series(m).to_string())

stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
tag = "synthetic" if args.synthetic else args.block
report_dir = ROOT / "backtests" / "validation_reports"
dump({"strategy": args.strategy, "experiment": args.experiment, "block": tag, "params": str(mod.Params()),
      "costs": {"slippage": args.slippage, "commission": args.commission}, "metrics": m, "run_at": stamp},
     report_dir / f"{args.experiment}_{args.strategy}_{tag}.json")
trades.to_csv(report_dir / f"{args.experiment}_{args.strategy}_{tag}_trades.csv", index=False)

if not args.synthetic:
    summary = ROOT / "backtests" / "performance_summary.csv"
    keys = ["run_at", "experiment", "strategy", "block", "trades", "win_rate", "expectancy_pips",
            "expectancy_r", "t_stat", "profit_factor", "max_drawdown_pips", "sharpe_daily_annualised",
            "median_hold_min", "pct_within_15m", "pips_per_exposure_hour"]
    row = {"run_at": stamp, "experiment": args.experiment, "strategy": args.strategy, "block": tag, **m}
    with summary.open("a", newline="") as fh:
        csv.DictWriter(fh, fieldnames=keys, extrasaction="ignore").writerow(row)
