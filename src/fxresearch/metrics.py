"""Performance and exposure metrics. All P&L figures are NET of modelled costs."""
from __future__ import annotations

import math

import numpy as np
import pandas as pd


def max_drawdown(cum: pd.Series) -> float:
    if cum.empty:
        return 0.0
    peak = cum.cummax().clip(lower=0)
    return float((cum - peak).min())


def max_consecutive_losses(net: pd.Series) -> int:
    best = run = 0
    for x in net:
        run = run + 1 if x <= 0 else 0
        best = max(best, run)
    return best


def trade_metrics(trades: pd.DataFrame, trading_days: int | None = None) -> dict:
    """Standard metric block written to backtests/performance_summary.csv."""
    if trades.empty:
        return {"trades": 0}
    net = trades["net_pips"]
    wins, losses = net[net > 0], net[net <= 0]
    hold = trades["hold_minutes"]
    daily = net.groupby(pd.to_datetime(trades["entry_time"]).dt.date).sum()
    if trading_days:  # include zero-P&L days so Sharpe is not inflated by selectivity
        n_zero = max(trading_days - len(daily), 0)
        daily_vals = np.concatenate([daily.to_numpy(), np.zeros(n_zero)])
    else:
        daily_vals = daily.to_numpy()
    sd = daily_vals.std(ddof=1) if len(daily_vals) > 1 else np.nan
    sharpe = float(daily_vals.mean() / sd * math.sqrt(252)) if sd and sd > 0 else np.nan
    t_stat = float(net.mean() / (net.std(ddof=1) / math.sqrt(len(net)))) if len(net) > 1 and net.std() > 0 else np.nan
    return {
        "trades": int(len(trades)),
        "win_rate": round(float((net > 0).mean()), 4),
        "avg_win_pips": round(float(wins.mean()), 3) if len(wins) else 0.0,
        "avg_loss_pips": round(float(losses.mean()), 3) if len(losses) else 0.0,
        "expectancy_pips": round(float(net.mean()), 3),
        "expectancy_r": round(float(trades["r_multiple"].mean()), 4),
        "t_stat": round(t_stat, 2) if not np.isnan(t_stat) else None,
        "profit_factor": round(float(wins.sum() / -losses.sum()), 3) if losses.sum() < 0 else None,
        "total_net_pips": round(float(net.sum()), 2),
        "max_drawdown_pips": round(max_drawdown(net.cumsum()), 2),
        "max_consecutive_losses": max_consecutive_losses(net),
        "sharpe_daily_annualised": round(sharpe, 2) if not np.isnan(sharpe) else None,
        "avg_hold_min": round(float(hold.mean()), 1),
        "median_hold_min": round(float(hold.median()), 1),
        "pct_within_5m": round(float((hold <= 5).mean()), 4),
        "pct_within_15m": round(float((hold <= 15).mean()), 4),
        "pct_within_30m": round(float((hold <= 30).mean()), 4),
        "pips_per_exposure_hour": round(float(net.sum() / (hold.sum() / 60)), 3),
        "avg_mae_pips": round(float(trades["mae_pips"].mean()), 2),
        "avg_mfe_pips": round(float(trades["mfe_pips"].mean()), 2),
        "avg_spread_at_entry_pips": round(float(trades["spread_at_entry_pips"].mean()), 3),
        "costs_share_of_gross": round(
            float((trades["gross_pips"] - net).sum() / max(trades["gross_pips"].abs().sum(), 1e-9)), 4
        ),
    }


def wilson_interval(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (float("nan"), float("nan"))
    p = successes / n
    denom = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (centre - half, centre + half)


def block_bootstrap_mean_ci(x: np.ndarray, block: int = 20, n_boot: int = 2000, seed: int = 0,
                            alpha: float = 0.05) -> tuple[float, float]:
    """Moving-block bootstrap CI for the mean; respects autocorrelation and volatility clustering."""
    x = np.asarray(x, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < block * 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    k = int(math.ceil(n / block))
    starts = rng.integers(0, n - block + 1, size=(n_boot, k))
    means = np.array([np.concatenate([x[s:s + block] for s in row])[:n].mean() for row in starts])
    return (float(np.quantile(means, alpha / 2)), float(np.quantile(means, 1 - alpha / 2)))
