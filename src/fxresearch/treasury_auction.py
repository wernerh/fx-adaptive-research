"""E039 (backlog B40 + B41): US Treasury coupon-auction demand shock -> EUR/USD continuation, DEV ONLY, 2 trials.

Pre-registered 2026-11-11 R086 in experiments/2026-11-11_E039_treasury_auction/ (Krohn, Vala, Uthemann & Yang 2025, proxy variant).
* Auction calendar: Fiscal Data API `v1/accounting/od/auctions_query` (fetched on the runner by scripts/fetch_treasury_auctions.py).
  Qualifying = nominal Note or Bond auctions incl. reopenings; Bills, CMBs, TIPS and FRNs excluded (`qualify`).
* Event = (auction date D, competitive close time T, America/New_York). Same T on the same date -> one event.
* Quotes = bid/ask OPEN of the first 1-minute bar in [t, t+5 min) (E011 rule); missing -> NaN, never filled.
* s = sign(mid(T+10) - mid(T-10)); entry at the T+10 quote (spread > 2.0 pips -> skipped); position s.
* B40 exit: 16:00 NY quote on the 10th trading date after D; B41 exit: 16:00 NY quote on the 1st trading date after D.
* Decision (`decide`, per arm): < 150 tested events -> NONE; SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND
  one-sided t p < 0.025; WEAK if mean > 0 and (CI lower > 0 or t p < 0.025); else NONE.
The side uses only quotes at or before T+10 min on D; every exit is strictly later (tested).
"""
from __future__ import annotations

import re
from datetime import date, datetime, time, timedelta

import numpy as np
import pandas as pd

from .data import PIP
from .roll_momentum import evaluate  # block-20 moving-block bootstrap, 2000 draws, seed 0; one-sided t and binomial p
from .sessions import trading_date
from .vol_state_fix import COMMISSION_RT_PIPS, MAX_ENTRY_SPREAD_PIPS, SLIPPAGE_ENTRY_PIPS, _get, ny_quotes

NY = "America/New_York"
WINDOW_MIN = 10
EDGE_MINUTES = 5
EXIT_HM = (16, 0)
HOLDS = {"B40": 10, "B41": 1}
ALPHA_T = 0.025
MIN_MEAN_PIPS = 1.0
MIN_EVENTS = 150
BOOT_BLOCK = 20
GATE_MIN_PER_YEAR = 50
GATE_MAX_PER_YEAR = 110
GATE_MIN_PARSED = 0.95
DEV_FROM = date(2015, 1, 1)
DEV_TO = date(2020, 12, 31)
ARM_EXCLUSIONS = ("not_trading_date", "missing_window", "zero_signal", "entry_skipped_spread", "exit_outside_dev",
                  "missing_exit")

_TIME_RE = re.compile(r"^\s*(\d{1,2}):(\d{2})(?::\d{2})?\s*([AaPp]\.?\s*[Mm]\.?)?\s*$")


def parse_close_time(x) -> time | None:
    """'01:00 PM', '1:00 PM', '13:00', '11:30 AM', '01:00:00 PM' -> time; anything else (incl. 'null', NaN) -> None."""
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return None
    m = _TIME_RE.match(str(x))
    if not m:
        return None
    h, mi, ap = int(m.group(1)), int(m.group(2)), m.group(3)
    if ap:
        ap = ap.replace(".", "").replace(" ", "").upper()
        if not 1 <= h <= 12:
            return None
        h = h % 12 + (12 if ap == "PM" else 0)
    if not (0 <= h <= 23 and 0 <= mi <= 59):
        return None
    return time(h, mi)


def _yes(x) -> bool:
    return str(x).strip().lower() in ("yes", "y", "true", "1")


def qualify(rec: dict) -> tuple[bool, str]:
    """Nominal Note/Bond (incl. reopenings) -> (True, 'ok'); else (False, reason)."""
    st = str(rec.get("security_type", "")).strip().lower()
    term = str(rec.get("security_term", "")).lower()
    if st not in ("note", "bond"):
        return False, f"type_{st or 'missing'}"
    if _yes(rec.get("inflation_index_security")) or "tips" in st or "tips" in term:
        return False, "tips"
    if _yes(rec.get("floating_rate")) or "frn" in st or "frn" in term:
        return False, "frn"
    return True, "ok"


def tenor_bucket(rec: dict) -> str:
    """'short' for 2/3/5/7-year (original term), 'long' for 10/20/30-year; 'unknown' if unparsed (descriptive only)."""
    term = str(rec.get("original_security_term") or rec.get("security_term") or "")
    m = re.match(r"\s*(\d+)\s*-?\s*Year", term, re.I)
    if not m:
        return "unknown"
    y = int(m.group(1))
    return "short" if y <= 7 else "long"


def calendar_from_records(records: list[dict]) -> pd.DataFrame:
    rows = []
    for r in records:
        ok, why = qualify(r)
        try:
            d = datetime.strptime(str(r.get("auction_date"))[:10], "%Y-%m-%d").date()
        except ValueError:
            d, ok, why = None, False, "bad_date"
        rows.append({"auction_date": d, "security_type": r.get("security_type"), "security_term": r.get("security_term"),
                     "original_security_term": r.get("original_security_term"), "cusip": r.get("cusip"),
                     "reopening": r.get("reopening"), "closing_time_comp_raw": r.get("closing_time_comp"),
                     "close_time": parse_close_time(r.get("closing_time_comp")), "qualifying": ok, "reason": why,
                     "tenor": tenor_bucket(r)})
    return pd.DataFrame(rows)


def calendar_gate(cal: pd.DataFrame, years=range(2015, 2021)) -> dict:
    """Pre-registered gate: every full dev year has 50-110 qualifying auctions and >= 95% of them have a parsed close time."""
    q = cal[cal["qualifying"]] if len(cal) else cal
    per_year = {int(y): int((pd.to_datetime(q["auction_date"]).dt.year == y).sum()) if len(q) else 0 for y in years}
    parsed = float(q["close_time"].notna().mean()) if len(q) else 0.0
    ok = all(GATE_MIN_PER_YEAR <= n <= GATE_MAX_PER_YEAR for n in per_year.values()) and parsed >= GATE_MIN_PARSED
    return {"qualifying_per_year": per_year, "parsed_close_share": round(parsed, 4), "n_qualifying": int(len(q)),
            "pass": bool(ok)}


def auction_events(cal: pd.DataFrame) -> pd.DataFrame:
    """One row per distinct (date, close time) among qualifying auctions with a parsed close time."""
    q = cal[cal["qualifying"] & cal["close_time"].notna()].copy()
    if q.empty:
        return pd.DataFrame(columns=["date", "close_time", "n_auctions", "tenor"])
    g = q.groupby(["auction_date", "close_time"])
    ev = g.agg(n_auctions=("cusip", "size"),
               tenor=("tenor", lambda s: s.iloc[0] if s.nunique() == 1 else "mixed")).reset_index()
    return ev.rename(columns={"auction_date": "date"}).sort_values(["date", "close_time"]).reset_index(drop=True)


def quotes_at(bars: pd.DataFrame, ts_utc) -> pd.DataFrame:
    """bid/ask open of the first bar in [t, t+5 min) for each UTC timestamp t; NaN if none."""
    idx = bars.index
    t = pd.DatetimeIndex(ts_utc)
    pos = idx.searchsorted(t, side="left")
    b = np.full(len(t), np.nan)
    a = np.full(len(t), np.nan)
    for i, (p, ti) in enumerate(zip(pos, t)):
        if p < len(idx) and idx[p] < ti + pd.Timedelta(minutes=EDGE_MINUTES):
            b[i] = bars["bid_open"].iloc[p]
            a[i] = bars["ask_open"].iloc[p]
    return pd.DataFrame({"bid": b, "ask": a})


def weekday_trading_dates(bars: pd.DataFrame) -> list:
    all_d = sorted({pd.Timestamp(x).date() for x in pd.Index(trading_date(bars.index)).unique()})
    return [d for d in all_d if d.weekday() < 5]


def _ny_utc(d: date, t: time, shift_min: int = 0) -> pd.Timestamp:
    return (pd.Timestamp(datetime.combine(d, t)).tz_localize(NY) + pd.Timedelta(minutes=shift_min)).tz_convert("UTC")


def build_events(ev: pd.DataFrame, bars: pd.DataFrame, dates: list | None = None, exit_q: pd.DataFrame | None = None
                 ) -> pd.DataFrame:
    """Per event: window move, side, entry, exits for each arm and the first exclusion reason per arm."""
    if dates is None:
        dates = weekday_trading_dates(bars)
    if exit_q is None:
        exit_q = ny_quotes(bars, *EXIT_HM)
    pos = {d: i for i, d in enumerate(dates)}
    df = ev.copy().reset_index(drop=True)
    if df.empty:
        return df
    pre = quotes_at(bars, [_ny_utc(d, t, -WINDOW_MIN) for d, t in zip(df["date"], df["close_time"])])
    post = quotes_at(bars, [_ny_utc(d, t, WINDOW_MIN) for d, t in zip(df["date"], df["close_time"])])
    df["pre_mid"] = ((pre["bid"] + pre["ask"]) / 2).to_numpy()
    df["entry_mid"] = ((post["bid"] + post["ask"]) / 2).to_numpy()
    df["entry_spread_pips"] = ((post["ask"] - post["bid"]) / PIP).to_numpy()
    df["window_pips"] = (df["entry_mid"] - df["pre_mid"]) / PIP
    df["side"] = np.sign(df["window_pips"])
    for arm, h in HOLDS.items():
        exit_dates, mids, sprs, excl = [], [], [], []
        for r in df.itertuples(index=False):
            k = pos.get(r.date)
            xd = dates[k + h] if (k is not None and k + h < len(dates)) else None
            q = _get(exit_q, xd) if xd is not None else None
            exit_dates.append(xd)
            mids.append(sum(q) / 2 if q else np.nan)
            sprs.append((q[1] - q[0]) / PIP if q else np.nan)
            if k is None:
                excl.append("not_trading_date")
            elif np.isnan(r.window_pips):
                excl.append("missing_window")
            elif r.window_pips == 0:
                excl.append("zero_signal")
            elif r.entry_spread_pips > MAX_ENTRY_SPREAD_PIPS:
                excl.append("entry_skipped_spread")
            elif xd is None:
                excl.append("exit_outside_dev")
            elif q is None:
                excl.append("missing_exit")
            else:
                excl.append(None)
        df[f"{arm}_exit_date"] = exit_dates
        df[f"{arm}_exit_mid"] = mids
        df[f"{arm}_exit_spread_pips"] = sprs
        df[f"{arm}_ret_pips"] = (df[f"{arm}_exit_mid"] - df["entry_mid"]) / PIP
        df[f"{arm}_signed_pips"] = df["side"] * df[f"{arm}_ret_pips"]
        df[f"{arm}_excluded"] = excl
        df[f"{arm}_tested"] = df[f"{arm}_excluded"].isna()
    return df


def arm_events(df: pd.DataFrame, arm: str) -> pd.DataFrame:
    """Tested events of one arm with the columns vol_state_fix.cost_summary expects."""
    e = df[df[f"{arm}_tested"]].copy()
    e["signed_pips"] = e[f"{arm}_signed_pips"]
    e["exit_spread_pips"] = e[f"{arm}_exit_spread_pips"]
    e["net_bidask_pips"] = e["signed_pips"] - (e["entry_spread_pips"] + e["exit_spread_pips"]) / 2
    e["net_spec4_pips"] = e["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    e["net_x1_5_pips"] = e["signed_pips"] - 1.5 * (e["signed_pips"] - e["net_spec4_pips"])
    return e


def decide(res: dict) -> str:
    """Pre-registered B40/B41 rule (per arm): < 150 tested events -> NONE. SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI
    lower > 0 AND one-sided t p < 0.025; WEAK if mean > 0 and (CI lower > 0 or t p < 0.025); else NONE."""
    if "mean_pips" not in res or res.get("n", 0) < MIN_EVENTS:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_block_boot"][0]
    lo_pos = lo is not None and not np.isnan(lo) and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA_T:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA_T):
        return "WEAK"
    return "NONE"


def counts(df: pd.DataFrame, arm: str) -> dict:
    vc = df[f"{arm}_excluded"].value_counts() if len(df) else pd.Series(dtype=int)
    out = {"events": int(len(df))}
    out.update({k: int(vc.get(k, 0)) for k in ARM_EXCLUSIONS})
    out["tested"] = int(df[f"{arm}_tested"].sum()) if len(df) else 0
    return out


def control_events(ev: pd.DataFrame, cal: pd.DataFrame) -> pd.DataFrame:
    """Descriptive non-auction control: same close time on the same weekday one week earlier, if that date had no qualifying
    auction."""
    auction_dates = set(cal.loc[cal["qualifying"], "auction_date"])
    c = ev.copy()
    c["date"] = [d - timedelta(days=7) for d in c["date"]]
    c = c[~c["date"].isin(auction_dates)]
    return c.drop_duplicates(["date", "close_time"]).reset_index(drop=True)


def evaluate_arm(df: pd.DataFrame, arm: str) -> dict:
    e = arm_events(df, arm)
    res = evaluate(e["signed_pips"]) if len(e) else {"n": 0, "note": "no events"}
    res["decision"] = decide(res)
    return res
