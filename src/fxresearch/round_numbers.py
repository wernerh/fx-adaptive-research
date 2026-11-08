"""E018 (backlog B15): round-number crossing continuation ("price cascades", Osler 2002/2005), dev only.

Event definition (fixed in pre-registration, R032):
* Price p(t) = mid close of 1-minute bar t, held as the integer 2*mid in 1e-5 units (bid_close + ask_close, x 1e5),
  so level arithmetic is exact. Round levels L = k * 0.0050 (+ `offset` for the control levels).
* Up-crossing at bar t: p(t-1) < L <= p(t). Down-crossing: p(t-1) > L >= p(t). Bars t-1 and t must belong to the same
  FX trading date (17:00 NY roll), so weekend/holiday gaps never create events.
  If one bar crosses several levels, the level nearest p(t) is the event level.
* Only the FIRST crossing (either direction) of each level per trading date is an event.
* Entry: open of the first bar at or after t + 1 min (SPEC 4), must be <= t + 5 min. Exit: open of the first bar at or
  after entry + horizon, must be <= entry + horizon + 5 min. The window [entry, entry + horizon) needs >= 55/60 of its bars.
* Exclusions, each skipped event counted under the first failing check in this order: entry bar missing (`coverage`);
  entry NY clock time in [16:30, 18:30) (`roll`); exit bar missing or window coverage < 55/60 (`coverage`); exit NY time in
  [16:30, 18:30) (`roll`); entry spread (ask_open - bid_open) > 2.0 pips (`spread`); entry before the previous trade's
  exit (`overlap`). Skipped events do not open trades.
* Signed return = crossing direction x (mid open at exit - mid open at entry), pips.

Everything uses bar t's close or later prices for the trade, so nothing looks ahead.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from .data import PIP
from .sessions import NY, trading_date

LEVEL_STEP = 0.0050
CONTROL_OFFSET = 0.0023          # control levels end in 23 / 73
HORIZON_MIN = 60
DESCRIPTIVE_HORIZONS = (15, 120)
MAX_ENTRY_SPREAD_PIPS = 2.0      # SPEC 4
SLIPPAGE_ENTRY_PIPS = 0.1        # SPEC 4, timed exit
COMMISSION_RT_PIPS = 0.1         # SPEC 4
ROLL_START_MIN = 16 * 60 + 30    # 16:30 NY
ROLL_END_MIN = 18 * 60 + 30      # 18:30 NY
MAX_FILL_DELAY = pd.Timedelta(minutes=5)
COVERAGE_SHARE = 55 / 60

_SCALE = 100_000  # price units of 1e-5; p = bid + ask in these units = 2 * mid


def _to_units(x: float) -> int:
    return int(round(2 * x * _SCALE))


def detect_crossings(bars: pd.DataFrame, offset: float = 0.0, step: float = LEVEL_STEP) -> pd.DataFrame:
    """First crossing of each level per trading date. Columns: ts (bar t), direction (+1 up / -1 down), level, trading_date."""
    p = np.rint((bars["bid_close"].to_numpy() + bars["ask_close"].to_numpy()) * _SCALE).astype(np.int64)
    s, o = _to_units(step), _to_units(offset)
    q = p - o
    td = np.asarray(trading_date(bars.index))
    prev, cur = q[:-1], q[1:]
    same_td = td[:-1] == td[1:]
    up_k = np.floor_divide(cur, s)                 # highest level <= p(t)
    up = same_td & (up_k * s > prev)               # p(t-1) < L <= p(t)
    dn_k = -np.floor_divide(-cur, s)               # lowest level >= p(t)
    dn = same_td & (dn_k * s < prev)               # p(t-1) > L >= p(t)
    idx = np.nonzero(up | dn)[0] + 1
    if len(idx) == 0:
        return pd.DataFrame(columns=["ts", "direction", "level", "trading_date"])
    direction = np.where(up[idx - 1], 1, -1)
    k = np.where(direction > 0, up_k[idx - 1], dn_k[idx - 1])
    ev = pd.DataFrame({
        "ts": bars.index[idx],
        "direction": direction,
        "level_k": k,
        "trading_date": td[idx],
    })
    ev = ev.drop_duplicates(subset=["trading_date", "level_k"], keep="first").reset_index(drop=True)
    ev["level"] = np.round(ev["level_k"] * step + offset, 5)
    return ev.drop(columns="level_k")[["ts", "direction", "level", "trading_date"]]


def _ny_minutes(ts: pd.Timestamp) -> int:
    t = ts.tz_convert(NY)
    return t.hour * 60 + t.minute


def _in_roll(ts: pd.Timestamp) -> bool:
    m = _ny_minutes(ts)
    return ROLL_START_MIN <= m < ROLL_END_MIN


def _fill(index: pd.DatetimeIndex, at: pd.Timestamp) -> int | None:
    i = int(index.searchsorted(at, side="left"))
    if i >= len(index) or index[i] - at > MAX_FILL_DELAY:
        return None
    return i


def _covered(index: pd.DatetimeIndex, i_entry: int, horizon: int) -> bool:
    start = index[i_entry]
    j = int(index.searchsorted(start + pd.Timedelta(minutes=horizon), side="left"))
    return (j - i_entry) >= int(np.ceil(horizon * COVERAGE_SHARE))


def _horizon_return(idx: pd.DatetimeIndex, mid_open: np.ndarray, i_entry: int, horizon: int) -> float:
    """Mid open-to-open return over `horizon` minutes from entry (pips); NaN if fill/coverage fails."""
    i_exit = _fill(idx, idx[i_entry] + pd.Timedelta(minutes=horizon))
    if i_exit is None or not _covered(idx, i_entry, horizon):
        return float("nan")
    return float((mid_open[i_exit] - mid_open[i_entry]) / PIP)


def build_trades(bars: pd.DataFrame, events: pd.DataFrame, horizon: int = HORIZON_MIN,
                 descriptive_horizons=DESCRIPTIVE_HORIZONS) -> tuple[pd.DataFrame, dict]:
    """Apply fill, exclusion and non-overlap rules. Returns (trades, skip counts)."""
    idx = bars.index
    bo, ao = bars["bid_open"].to_numpy(), bars["ask_open"].to_numpy()
    mo = (bo + ao) / 2
    skips = {"roll": 0, "spread": 0, "coverage": 0, "overlap": 0}
    rows = []
    last_exit = None
    for ev in events.itertuples(index=False):
        i_en = _fill(idx, ev.ts + pd.Timedelta(minutes=1))
        if i_en is None:
            skips["coverage"] += 1
            continue
        t_en = idx[i_en]
        if _in_roll(t_en):
            skips["roll"] += 1
            continue
        i_ex = _fill(idx, t_en + pd.Timedelta(minutes=horizon))
        if i_ex is None or not _covered(idx, i_en, horizon):
            skips["coverage"] += 1
            continue
        t_ex = idx[i_ex]
        if _in_roll(t_ex):
            skips["roll"] += 1
            continue
        spread = (ao[i_en] - bo[i_en]) / PIP
        if spread > MAX_ENTRY_SPREAD_PIPS + 1e-9:
            skips["spread"] += 1
            continue
        if last_exit is not None and t_en < last_exit:
            skips["overlap"] += 1
            continue
        d = int(ev.direction)
        mid_en, mid_ex = (bo[i_en] + ao[i_en]) / 2, (bo[i_ex] + ao[i_ex]) / 2
        ret = (mid_ex - mid_en) / PIP
        net_ba = ((bo[i_ex] - ao[i_en]) if d > 0 else (bo[i_en] - ao[i_ex])) / PIP
        row = {
            "event_ts": ev.ts, "entry_ts": t_en, "exit_ts": t_ex, "trading_date": ev.trading_date,
            "direction": d, "level": ev.level, "ret_pips": ret, "signed_pips": d * ret,
            "net_bidask_pips": net_ba, "entry_spread_pips": spread,
            "exit_spread_pips": (ao[i_ex] - bo[i_ex]) / PIP,
        }
        for h in descriptive_horizons:
            row[f"signed_{h}m_pips"] = d * _horizon_return(idx, mo, i_en, h)
        rows.append(row)
        last_exit = t_ex
    cols = ["event_ts", "entry_ts", "exit_ts", "trading_date", "direction", "level", "ret_pips", "signed_pips",
            "net_bidask_pips", "entry_spread_pips", "exit_spread_pips"] + [f"signed_{h}m_pips" for h in descriptive_horizons]
    return pd.DataFrame(rows, columns=cols), skips


def cost_summary(trades: pd.DataFrame) -> dict:
    gross = trades["signed_pips"]
    net_spec = trades["net_bidask_pips"] - (SLIPPAGE_ENTRY_PIPS + COMMISSION_RT_PIPS)
    cost = gross - net_spec
    return {
        "n": int(len(trades)),
        "mean_signed_mid_pips": round(float(gross.mean()), 3),
        "mean_net_bidask_pips": round(float(trades["net_bidask_pips"].mean()), 3),
        "mean_net_spec4_pips": round(float(net_spec.mean()), 3),
        "mean_net_costs_x1_5_pips": round(float((gross - 1.5 * cost).mean()), 3),
        "net_spec4_hit_rate": round(float((net_spec > 0).mean()), 4) if len(trades) else None,
        "median_entry_spread_pips": round(float(trades["entry_spread_pips"].median()), 3),
        "median_exit_spread_pips": round(float(trades["exit_spread_pips"].median()), 3),
    }


def calendar_shares(trades: pd.DataFrame, window_min: int = 15) -> dict:
    """Share of events within +-window of 08:30, 10:00 and 11:00 NY (event bar time)."""
    m = np.array([_ny_minutes(t) for t in trades["event_ts"]]) if len(trades) else np.array([])
    out = {}
    for name, c in (("ny_0830", 8 * 60 + 30), ("ny_1000", 10 * 60), ("ny_1100", 11 * 60)):
        out[f"share_within_{window_min}m_{name}"] = round(float((np.abs(m - c) <= window_min).mean()), 4) if len(m) else None
    return out
