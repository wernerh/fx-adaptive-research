"""Market data loading, normalisation and quality checks.

Canonical bar schema (see data/data_dictionary.md):

    index  : ts (tz-aware UTC, bar OPEN time, 1-minute frequency)
    columns: bid_open, bid_high, bid_low, bid_close,
             ask_open, ask_high, ask_low, ask_close, volume (optional)

Mid prices are always DERIVED, never stored, so costs cannot be silently dropped.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from .sessions import is_weekend_bar

PIP = 0.0001  # EUR/USD
OHLC = ("open", "high", "low", "close")
BAR_COLUMNS = [f"{side}_{f}" for side in ("bid", "ask") for f in OHLC]


def _read_side(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    ts_col = next(c for c in df.columns if c in ("timestamp", "time", "datetime", "date", "ts"))
    ts = df[ts_col]
    if np.issubdtype(ts.dtype, np.number):  # epoch milliseconds (dukascopy-node default)
        idx = pd.to_datetime(ts, unit="ms", utc=True)
    else:
        idx = pd.to_datetime(ts, utc=True)
    out = df[list(OHLC) + (["volume"] if "volume" in df.columns else [])].copy()
    out.index = pd.DatetimeIndex(idx, name="ts")
    return out.sort_index()


def _read_many(paths) -> pd.DataFrame:
    if isinstance(paths, (str, Path)):
        paths = [paths]
    df = pd.concat([_read_side(Path(p)) for p in paths]).sort_index()
    return df[~df.index.duplicated(keep="first")]


def load_bid_ask_csv(bid_path, ask_path) -> pd.DataFrame:
    """Load bid and ask 1-minute OHLC CSVs (e.g. exported with dukascopy-node).
    Each argument may be one path or a list of paths (e.g. one file per year)."""
    bid = _read_many(bid_path).add_prefix("bid_")
    ask = _read_many(ask_path).add_prefix("ask_")
    df = bid.join(ask, how="inner")
    if "bid_volume" in df.columns:
        df["volume"] = df.pop("bid_volume")
    df = df.drop(columns=[c for c in df.columns if c == "ask_volume"])
    return validate_bars(df)


def load_parquet(path: str | Path) -> pd.DataFrame:
    return validate_bars(pd.read_parquet(path))


def validate_bars(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in BAR_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"missing columns: {missing}")
    if not isinstance(df.index, pd.DatetimeIndex) or df.index.tz is None:
        raise ValueError("index must be a tz-aware DatetimeIndex")
    df = df.tz_convert("UTC") if str(df.index.tz) != "UTC" else df
    if df.index.has_duplicates:
        df = df[~df.index.duplicated(keep="first")]
    return df.sort_index()


def mid(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {f: (df[f"bid_{f}"] + df[f"ask_{f}"]) / 2 for f in OHLC}, index=df.index
    )


def spread_pips(df: pd.DataFrame) -> pd.Series:
    return (df["ask_close"] - df["bid_close"]) / PIP


def quality_report(df: pd.DataFrame) -> dict:
    """Summary of data problems. Write the output to data/data_quality_reports.md."""
    trading = df[~is_weekend_bar(df.index).to_numpy()]
    sp = spread_pips(trading)
    expected = pd.date_range(trading.index.min(), trading.index.max(), freq="1min", tz="UTC")
    expected = expected[~is_weekend_bar(expected).to_numpy()]
    gaps = expected.difference(trading.index)
    return {
        "first_bar": str(df.index.min()),
        "last_bar": str(df.index.max()),
        "bars": int(len(df)),
        "weekend_bars": int(len(df) - len(trading)),
        "missing_trading_minutes": int(len(gaps)),
        "missing_pct": round(100 * len(gaps) / max(len(expected), 1), 3),
        "crossed_quotes": int((sp < 0).sum()),
        "zero_spread_bars": int((sp == 0).sum()),
        "spread_pips_median": round(float(sp.median()), 3),
        "spread_pips_p95": round(float(sp.quantile(0.95)), 3),
        "spread_pips_p99": round(float(sp.quantile(0.99)), 3),
        "bad_ohlc": int(
            ((trading["bid_high"] < trading[["bid_open", "bid_close"]].max(axis=1))
             | (trading["bid_low"] > trading[["bid_open", "bid_close"]].min(axis=1))).sum()
        ),
    }


def synthetic_bars(
    start: str = "2024-01-01",
    end: str = "2024-03-31",
    spread_pips_: float = 0.3,
    vol_pips_per_min: float = 0.6,
    seed: int = 7,
) -> pd.DataFrame:
    """Random-walk bid/ask bars for tests and pipeline smoke runs.

    By construction there is NO edge in this data; any strategy that shows a
    meaningful positive expectancy after costs on it indicates a bug or leakage.
    """
    rng = np.random.default_rng(seed)
    idx = pd.date_range(start, end, freq="1min", tz="UTC", inclusive="left")
    idx = idx[~is_weekend_bar(idx).to_numpy()]
    n = len(idx)
    steps = rng.normal(0, vol_pips_per_min * PIP, size=(n, 4))
    close = 1.08 + np.cumsum(steps[:, 3])
    open_ = np.concatenate([[1.08], close[:-1]])
    hi = np.maximum(open_, close) + np.abs(steps[:, 1]) * 0.5
    lo = np.minimum(open_, close) - np.abs(steps[:, 2]) * 0.5
    half = spread_pips_ * PIP / 2
    df = pd.DataFrame(index=pd.DatetimeIndex(idx, name="ts"))
    for f, v in zip(OHLC, (open_, hi, lo, close)):
        df[f"bid_{f}"] = v - half
        df[f"ask_{f}"] = v + half
    df["volume"] = rng.integers(10, 200, n)
    return df
