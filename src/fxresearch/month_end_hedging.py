"""E034 (backlog B30): month-end pre-fix equity-hedging flow (Melvin & Prins 2015), DEV ONLY, 2 trials in one experiment.

Definitions (fixed in the backlog, R071, and pre-registered 2026-11-10 R072, before any run):
* Month-end D = last trading date of each calendar month among the EUR/USD dev trading dates (`fixes.month_end_flag`, E007
  definition; 17:00 NY roll). D-1 = the trading date immediately before D in the same set. Anchor A(D) = the month-end of the
  previous calendar month in the same set (the first month-end in the data has none -> `no_prev_month_end`, counted).
* Index quotes (EUS.IDX/EUR = EU Stocks 50 CFD, USA500.IDX/USD = US 500 CFD, Dukascopy m1 bid/ask): quote on London calendar date d
  = mid of the bid/ask OPEN of the first bar in [16:00, 16:05) Europe/London (E011 quote rule). Holiday fallback (fixed before
  data, R072): if the index has no such quote on the target date, use the latest London calendar date in [target - 5 days, target]
  that has one (past only); the end quote must fall on a date strictly after the start-quote date. None -> `missing_index_quote`.
* S(D) = [ln EU(D-1) - ln EU(A)] - [ln US(D-1) - ln US(A)] (EU minus US equity log return, month-end fix to D-1 fix; past only).
  Position = -sign(S): EU equities outperformed -> short EUR/USD; US outperformed -> long EUR/USD. S = 0 -> `zero_signal`.
* Trades on EUR/USD (quote = bid/ask OPEN of the first bar in [T, T+5 min) Europe/London on London calendar date):
  (a) HOUR: 15:00 -> 16:00 London on D (pre-fix hour, same window as E007 `pre_month_end`).
  (b) DAY:  16:00 London on D-1 -> 16:00 London on D.
  Exclusions per window, counted, first reason in this order: `no_prev_month_end`, `missing_index_quote`, `zero_signal`,
  `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at entry > 2.0 pips, SPEC 4).
* Signed return = position x (mid exit - mid entry) / PIP.
* Statistic per window: mean, one-sided t-test, i.i.d. bootstrap CI (block 1, 2000 draws, seed 0).
* Decision (`decide_b30`): < 50 tested events -> NONE. SIGNAL if mean > 1.0 pip AND CI lower > 0 AND one-sided t p < 0.025
  (Bonferroni for 2 trials). WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE.
* Data gate (checked first): index data missing, or `missing_index_quote` on > 5% of month-ends that have an anchor -> BLOCKED,
  0 trials used.
S uses index quotes at or before 16:00 London on D-1; both trades enter at or after that instant, so nothing looks ahead.
"""
from __future__ import annotations

from datetime import timedelta
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP, _read_many
from .fixes import month_end_flag
from .metrics import block_bootstrap_mean_ci
from .sessions import trading_date

LONDON_TZ = "Europe/London"
FIX_HM = (16, 0)
PRE_HM = (15, 0)
POST_HM = (17, 0)                # descriptive post-fix hour exit
EDGE_MINUTES = 5
FALLBACK_DAYS = 5
MAX_ENTRY_SPREAD_PIPS = 2.0
MIN_MEAN_PIPS = 1.0
ALPHA = 0.025                    # Bonferroni for 2 trials
MIN_EVENTS = 50
BOOT_BLOCK = 1
BOOT_N = 2000
MAX_MISSING_INDEX_SHARE = 0.05
SLIPPAGE_ENTRY_PIPS = 0.1        # SPEC 4
COMMISSION_RT_PIPS = 0.1         # SPEC 4
EU_INDEX = "eusidxeur"
US_INDEX = "usa500idxusd"
EXCL_ORDER = ("no_prev_month_end", "missing_index_quote", "zero_signal", "missing_entry", "missing_exit",
              "entry_skipped_spread")


def london_quotes(bars: pd.DataFrame, hour: int, minute: int = 0) -> pd.DataFrame:
    """Per London calendar date: bid/ask open of the first bar in [hh:mm, hh:mm+5) Europe/London."""
    if len(bars) == 0:
        return pd.DataFrame(columns=["bid_open", "ask_open"])
    ldn = bars.index.tz_convert(LONDON_TZ)
    mins = np.asarray(ldn.hour) * 60 + np.asarray(ldn.minute)
    t0 = hour * 60 + minute
    sel = (mins >= t0) & (mins < t0 + EDGE_MINUTES)
    d = pd.Index(ldn.date)[sel]
    out = bars.loc[sel, ["bid_open", "ask_open"]].groupby(d).first()
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="ldn_date")
    return out


def load_index(raw_dir: str | Path, name: str) -> pd.DataFrame:
    """Load <name>-m1-bid-*.csv and <name>-m1-ask-*.csv from raw_dir into bid_/ask_ OHLC columns (empty frame if absent)."""
    d = Path(raw_dir)
    bid = sorted(d.glob(f"{name}-m1-bid-*.csv"))
    ask = sorted(d.glob(f"{name}-m1-ask-*.csv"))
    if not bid or not ask:
        return pd.DataFrame(columns=["bid_open", "ask_open"], index=pd.DatetimeIndex([], tz="UTC", name="ts"))
    b = _read_many(bid).add_prefix("bid_")
    a = _read_many(ask).add_prefix("ask_")
    df = b.join(a, how="inner")
    return df.drop(columns=[c for c in df.columns if c.endswith("_volume")])


def index_mid_on_or_before(q: pd.DataFrame, target, after=None, lookback_days: int = FALLBACK_DAYS):
    """Latest London date in [target - lookback, target] (and > after, if given) with a quote -> (date, mid); else None."""
    for k in range(lookback_days + 1):
        d = target - timedelta(days=k)
        if after is not None and d <= after:
            return None
        if d in q.index:
            b, a = q.loc[d, "bid_open"], q.loc[d, "ask_open"]
            if not (pd.isna(b) or pd.isna(a)) and b > 0 and a > 0:
                return d, (float(b) + float(a)) / 2
    return None


def _fx(q: pd.DataFrame, d):
    if d in q.index:
        b, a = q.loc[d, "bid_open"], q.loc[d, "ask_open"]
        if not (pd.isna(b) or pd.isna(a)):
            return float(b), float(a)
    return None


def month_end_table(fx_dates) -> pd.DataFrame:
    """Rows: date (month-end D), prev_date (D-1), anchor (previous month's D or None)."""
    dates = sorted(set(fx_dates))
    if not dates:
        return pd.DataFrame(columns=["date", "prev_date", "anchor"])
    flag = month_end_flag(pd.Index(dates))
    pos = {d: i for i, d in enumerate(dates)}
    me = [d for d, f in zip(dates, flag.to_numpy()) if f]
    rows = []
    for i, d in enumerate(me):
        j = pos[d]
        prev = dates[j - 1] if j > 0 else None
        anchor = None
        if i > 0:
            a = me[i - 1]
            # anchor must be the previous calendar month's month-end
            if (a.year * 12 + a.month) == (d.year * 12 + d.month) - 1:
                anchor = a
        rows.append({"date": d, "prev_date": prev, "anchor": anchor})
    return pd.DataFrame(rows)


def build_events(fx_bars: pd.DataFrame, eu_bars: pd.DataFrame, us_bars: pd.DataFrame) -> pd.DataFrame:
    """One row per month-end D with the signal, both trades, exclusions and cost columns."""
    td = sorted({pd.Timestamp(x).date() for x in trading_date(fx_bars.index)})
    tab = month_end_table(td)
    q_fix, q_pre, q_post = (london_quotes(fx_bars, *FIX_HM), london_quotes(fx_bars, *PRE_HM),
                            london_quotes(fx_bars, *POST_HM))
    eu_q, us_q = london_quotes(eu_bars, *FIX_HM), london_quotes(us_bars, *FIX_HM)
    rows = []
    for r in tab.itertuples(index=False):
        row = {"date": r.date, "prev_date": r.prev_date, "anchor": r.anchor}
        legs = {}
        if r.anchor is not None and r.prev_date is not None:
            for lab, q in (("eu", eu_q), ("us", us_q)):
                s = index_mid_on_or_before(q, r.anchor)
                e = index_mid_on_or_before(q, r.prev_date, after=s[0]) if s else None
                legs[lab] = (s, e)
                row[f"{lab}_start_date"], row[f"{lab}_start"] = s if s else (None, np.nan)
                row[f"{lab}_end_date"], row[f"{lab}_end"] = e if e else (None, np.nan)
        for lab in ("eu", "us"):
            row.setdefault(f"{lab}_start_date", None)
            row.setdefault(f"{lab}_start", np.nan)
            row.setdefault(f"{lab}_end_date", None)
            row.setdefault(f"{lab}_end", np.nan)
        row["s_eu"] = np.log(row["eu_end"] / row["eu_start"]) if row["eu_start"] > 0 and row["eu_end"] > 0 else np.nan
        row["s_us"] = np.log(row["us_end"] / row["us_start"]) if row["us_start"] > 0 and row["us_end"] > 0 else np.nan
        row["s"] = row["s_eu"] - row["s_us"]
        row["position"] = -np.sign(row["s"]) if not np.isnan(row["s"]) else np.nan
        row["fallback_quote"] = bool(any(row[f"{lab}_{k}_date"] is not None and row[f"{lab}_{k}_date"] != tgt
                                         for lab in ("eu", "us")
                                         for k, tgt in (("start", r.anchor), ("end", r.prev_date))))
        for win, (qe, de), (qx, dx) in (("hour", (q_pre, r.date), (q_fix, r.date)),
                                        ("day", (q_fix, r.prev_date), (q_fix, r.date)),
                                        ("post", (q_fix, r.date), (q_post, r.date))):
            e = _fx(qe, de) if de is not None else None
            x = _fx(qx, dx) if dx is not None else None
            row[f"{win}_entry_mid"] = sum(e) / 2 if e else np.nan
            row[f"{win}_entry_spread_pips"] = (e[1] - e[0]) / PIP if e else np.nan
            row[f"{win}_exit_mid"] = sum(x) / 2 if x else np.nan
            row[f"{win}_exit_spread_pips"] = (x[1] - x[0]) / PIP if x else np.nan
        rows.append(row)
    df = pd.DataFrame(rows)
    if df.empty:
        return df
    for win in ("hour", "day", "post"):
        excl = []
        for r in df.itertuples(index=False):
            if r.anchor is None or r.prev_date is None:
                excl.append("no_prev_month_end")
            elif np.isnan(r.s):
                excl.append("missing_index_quote")
            elif r.s == 0:
                excl.append("zero_signal")
            elif np.isnan(getattr(r, f"{win}_entry_mid")):
                excl.append("missing_entry")
            elif np.isnan(getattr(r, f"{win}_exit_mid")):
                excl.append("missing_exit")
            elif getattr(r, f"{win}_entry_spread_pips") > MAX_ENTRY_SPREAD_PIPS:
                excl.append("entry_skipped_spread")
            else:
                excl.append(None)
        df[f"{win}_excluded"] = excl
        df[f"{win}_tested"] = df[f"{win}_excluded"].isna()
        move = (df[f"{win}_exit_mid"] - df[f"{win}_entry_mid"]) / PIP
        df[f"{win}_move_pips"] = move
        df[f"{win}_signed_pips"] = df["position"] * move
        nb = df[f"{win}_signed_pips"] - (df[f"{win}_entry_spread_pips"] + df[f"{win}_exit_spread_pips"]) / 2
        n4 = nb - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
        df[f"{win}_net_bidask_pips"] = nb
        df[f"{win}_net_spec4_pips"] = n4
        df[f"{win}_net_x1_5_pips"] = df[f"{win}_signed_pips"] - 1.5 * (df[f"{win}_signed_pips"] - n4)
    return df


def data_gate(df: pd.DataFrame, eu_bars: pd.DataFrame, us_bars: pd.DataFrame) -> dict:
    """Pre-registered gate: BLOCKED if an index series is empty or `missing_index_quote` on > 5% of anchored month-ends."""
    out = {"eu_bars": int(len(eu_bars)), "us_bars": int(len(us_bars))}
    if len(eu_bars) == 0 or len(us_bars) == 0:
        return {**out, "ok": False, "reason": "index data missing"}
    anchored = df[df["anchor"].notna() & df["prev_date"].notna()] if len(df) else df
    n = int(len(anchored))
    miss = int(anchored["s"].isna().sum()) if n else 0
    share = miss / n if n else 1.0
    ok = n > 0 and share <= MAX_MISSING_INDEX_SHARE
    return {**out, "ok": bool(ok), "anchored_month_ends": n, "missing_index_quote": miss,
            "missing_share": round(float(share), 4),
            "reason": None if ok else "missing index quotes on > 5% of month-ends"}


def evaluate_b30(signed) -> dict:
    """Mean test: mean, median, sd, hit, one-sided t p (H1 mean > 0), i.i.d. bootstrap CI (block 1, 2000 draws, seed 0)."""
    x = np.asarray(signed, dtype=float)
    x = x[~np.isnan(x)]
    n = len(x)
    if n < 3:
        return {"n": n, "note": "insufficient sample"}
    t = stats.ttest_1samp(x, 0.0, alternative="greater")
    lo, hi = block_bootstrap_mean_ci(x, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    res = {"n": n, "mean_pips": round(float(x.mean()), 3), "median_pips": round(float(np.median(x)), 3),
           "sd_pips": round(float(x.std(ddof=1)), 3), "hit_rate": round(float((x > 0).mean()), 4),
           "t_stat": round(float(t.statistic), 3), "t_p_one_sided": round(float(t.pvalue), 4),
           "mean_ci95_boot": (round(lo, 3), round(hi, 3))}
    if n < MIN_EVENTS:
        res["note"] = f"insufficient sample (< {MIN_EVENTS} events)"
    return res


def decide_b30(res: dict) -> str:
    """Pre-registered E034 rule per window: < 50 events -> NONE. SIGNAL if mean > 1.0 pip AND i.i.d. bootstrap CI lower > 0
    AND one-sided t p < 0.025; WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE."""
    if "mean_pips" not in res or res.get("n", 0) < MIN_EVENTS:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


def counts(df: pd.DataFrame, win: str) -> dict:
    if df.empty:
        return {"month_ends": 0}
    vc = df[f"{win}_excluded"].value_counts()
    out = {"month_ends": int(len(df))}
    for k in EXCL_ORDER:
        out[k] = int(vc.get(k, 0))
    out["tested"] = int(df[f"{win}_tested"].sum())
    out["fallback_quote_month_ends"] = int(df["fallback_quote"].sum())
    return out


def cost_summary(ev: pd.DataFrame, win: str) -> dict:
    if len(ev) == 0:
        return {"n": 0}
    return {"n": int(len(ev)), "mean_signed_mid_pips": round(float(ev[f"{win}_signed_pips"].mean()), 3),
            "mean_net_bidask_pips": round(float(ev[f"{win}_net_bidask_pips"].mean()), 3),
            "mean_net_spec4_pips": round(float(ev[f"{win}_net_spec4_pips"].mean()), 3),
            "mean_net_costs_x1_5_pips": round(float(ev[f"{win}_net_x1_5_pips"].mean()), 3),
            "median_spread_entry_pips": round(float(ev[f"{win}_entry_spread_pips"].median()), 3),
            "median_spread_exit_pips": round(float(ev[f"{win}_exit_spread_pips"].median()), 3)}
