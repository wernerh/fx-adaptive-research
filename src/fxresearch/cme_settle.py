"""E016 (backlog B13): intraday momentum into the CME FX futures daily settlement, in spot EUR/USD. DEV ONLY.

Two parts:

1. Settlement-time parsing (`find_fx_windows`, `validate_settlement`). The settlement time is read from official CME Group
   pages fetched on the GitHub runner by scripts/fetch_cme_settlement.py (raw files saved under backtests/calendars/).
   No time is typed by hand: the reviewed value is promoted to data/calendars/cme_fx_settlement.json with its source URL,
   and phase 2 refuses to run without that file.

2. The pre-registered test (methodology in experiments/2026-11-08_E016_cme_settle_momentum/). With S = settlement time in
   America/Chicago on the calendar date of trading date D (Mon-Fri):
     P0 = mid open of the first bar of trading date D (at/after the 17:00 NY roll), within 60 minutes of the roll
     P1 = mid close of the last bar in [S-35, S-30) CT           -> r1 = P1 - P0  (rest of the day so far)
     E  = mid open of the first bar in [S-30, S-25) CT           (entry; r1 fully known)
     X  = mid close of the last bar in [S-5, S) CT               -> r2 = X - E    (last 30 minutes into settlement)
   signed = sign(r1) * r2 if |r1| >= 1.0 pip, else 0 (no trade; the day stays in n).
   r1 uses only bars before S-30, r2 only bars from S-30, so the signal cannot look ahead (tested).
"""
from __future__ import annotations

import json
import math
import re
from datetime import time
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import NY, trading_date

CT = ZoneInfo("America/Chicago")

SOURCE_URLS = (
    "https://www.cmegroup.com/market-data/files/Daily-Settlement-Time-Ranges.pdf",
    "https://www.cmegroup.com/confluence/display/EPICSANDBOX/Daily+Settlement+Time+Details",
    "https://www.cmegroup.com/confluence/display/EPICSANDBOX/Euro",
)

# Pre-registered constants (E016 methodology; fixed before any price data).
WINDOW_MIN = 30            # target window: last 30 minutes before S
EDGE_MINUTES = 5           # open quote: first bar in [t, t+5); close quote: last bar in [t-5, t)
START_MAX_DELAY_MIN = 60   # P0 must come from a bar within 60 min after the 17:00 NY roll (Sunday opens can be late)
MIN_REACTION_PIPS = 1.0    # |r1| below this -> no trade (signed 0, kept in n)
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 20            # daily observations (SPEC default block for daily series)
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1  # SPEC 4
COMMISSION_RT_PIPS = 0.1   # SPEC 4

_T = r"(\d{1,2}:\d{2}(?::\d{2})?)"
_FX_RE = re.compile(r"\b(FX|Euro\s*FX|Foreign\s+Exchange)\b[^\n]{0,80}?" + _T + r"\s*(?:-|–|to)\s*" + _T + r"\s*(CT|CST|CDT|Central)",
                    re.I)


def find_fx_windows(text: str) -> list[dict]:
    """All 'FX ... HH:MM[:SS] - HH:MM[:SS] CT' settlement windows found in a page's text (one line at a time)."""
    out = []
    for line in text.splitlines():
        for m in _FX_RE.finditer(line):
            out.append({"label": m.group(1), "start": m.group(2), "end": m.group(3), "tz": m.group(4).upper(),
                        "line": line.strip()[:300]})
    return out


def _hhmm(s: str) -> time:
    parts = [int(x) for x in s.split(":")]
    return time(parts[0], parts[1], parts[2] if len(parts) > 2 else 0)


def validate_settlement(windows: list[dict]) -> tuple[bool, str, str | None]:
    """Valid if at least one window was found and all found windows agree on the end time (= S, CT).
    Returns (ok, note, settle_time 'HH:MM')."""
    if not windows:
        return False, "no FX settlement window found", None
    ends = sorted({_hhmm(w["end"]).strftime("%H:%M") for w in windows})
    if len(ends) != 1:
        return False, f"conflicting FX window end times: {ends}", None
    s = ends[0]
    if not (time(7, 0) <= _hhmm(s) <= time(16, 0)):
        return False, f"implausible settlement time {s} CT", None
    return True, "ok", s


def load_settlement(path: Path) -> time:
    """Reviewed, promoted settlement time (phase-1 output). Raises if missing or not reviewed."""
    d = json.loads(Path(path).read_text())
    if not d.get("reviewed") or "settle_time_ct" not in d or not d.get("source_url"):
        raise ValueError(f"{path}: needs settle_time_ct, source_url and reviewed=true")
    return _hhmm(d["settle_time_ct"])


# ---------------------------------------------------------------- E016 test -------------------------------------------

def _minus(t: time, minutes: int) -> int:
    return t.hour * 60 + t.minute - minutes


def momentum_frame(bars: pd.DataFrame, settle: time) -> pd.DataFrame:
    """Per weekday trading date: r1, r2, signed return (mid), entry spread and bid/ask net of the signed trade.
    Days with any missing edge quote keep NaN (dropped and listed by the caller, never filled)."""
    idx = bars.index
    td = pd.Index(trading_date(idx))
    ct = idx.tz_convert(CT)
    ny = idx.tz_convert(NY)
    cmin = np.asarray(ct.hour) * 60 + np.asarray(ct.minute)
    cdate = pd.Index(ct.date)

    # P0: first bar of each trading date, only if within START_MAX_DELAY_MIN of the 17:00 NY roll.
    nymin = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    since_roll = (nymin - 17 * 60) % (24 * 60)
    first = bars[["bid_open", "ask_open"]].groupby(td).first()
    first_delay = pd.Series(since_roll, index=idx).groupby(td).first()
    first = first[first_delay <= START_MAX_DELAY_MIN]
    first.columns = ["bid", "ask"]

    s_min = settle.hour * 60 + settle.minute
    t_entry = s_min - WINDOW_MIN

    def edge(t: int, kind: str) -> pd.DataFrame:
        if kind == "open":
            sel = (cmin >= t) & (cmin < t + EDGE_MINUTES)
            g = bars.loc[sel, ["bid_open", "ask_open"]].groupby(cdate[sel]).first()
        else:
            sel = (cmin >= t - EDGE_MINUTES) & (cmin < t)
            g = bars.loc[sel, ["bid_close", "ask_close"]].groupby(cdate[sel]).last()
        g.columns = ["bid", "ask"]
        return g

    p1, e, x = edge(t_entry, "close"), edge(t_entry, "open"), edge(s_min, "close")
    days = sorted(d for d in set(td) if d.weekday() < 5)
    rows = []
    for d in days:
        r = {"date": d, "r1_pips": np.nan, "r2_pips": np.nan, "direction": 0, "signed_pips": np.nan,
             "net_bidask_pips": np.nan, "entry_spread_pips": np.nan}
        if all(d in q.index for q in (first, p1, e, x)):
            mid = {k: (q.loc[d, "bid"] + q.loc[d, "ask"]) / 2 for k, q in (("p0", first), ("p1", p1), ("e", e), ("x", x))}
            if not any(np.isnan(v) for v in mid.values()):
                r1 = (mid["p1"] - mid["p0"]) / PIP
                r2 = (mid["x"] - mid["e"]) / PIP
                direction = int(np.sign(r1)) if abs(r1) >= MIN_REACTION_PIPS else 0
                r.update(r1_pips=r1, r2_pips=r2, direction=direction, signed_pips=direction * r2,
                         entry_spread_pips=(e.loc[d, "ask"] - e.loc[d, "bid"]) / PIP)
                if direction > 0:
                    r["net_bidask_pips"] = (x.loc[d, "bid"] - e.loc[d, "ask"]) / PIP
                elif direction < 0:
                    r["net_bidask_pips"] = (e.loc[d, "bid"] - x.loc[d, "ask"]) / PIP
                else:
                    r["net_bidask_pips"] = 0.0
        rows.append(r)
    return pd.DataFrame(rows).set_index("date")


def evaluate(f: pd.DataFrame) -> dict:
    """Pre-registered statistics. Mean / CI over all valid days (no-trade days count as 0); binomial test of the
    continuation share over traded days with r2 != 0 (one-sided, H1 > 0.5). OLS slope of r2 on r1 is descriptive."""
    ok = f["signed_pips"].notna()
    v = f.loc[ok, "signed_pips"].to_numpy(dtype=float)
    n = len(v)
    traded = f.loc[ok & (f["direction"] != 0), "signed_pips"].to_numpy(dtype=float)
    nz = traded[traded != 0]
    hits = int((nz > 0).sum())
    out = {"n": n, "n_traded": int(len(traded)), "n_no_trade": int(n - len(traded))}
    if n < 3:
        return out
    lo, hi = block_bootstrap_mean_ci(v, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    binom_p = float(stats.binomtest(hits, len(nz), 0.5, alternative="greater").pvalue) if len(nz) else 1.0
    r1 = f.loc[ok, "r1_pips"].to_numpy(dtype=float)
    r2 = f.loc[ok, "r2_pips"].to_numpy(dtype=float)
    slope = stats.linregress(r1, r2) if np.std(r1) > 0 else None
    out.update({
        "mean_signed_pips": round(float(v.mean()), 3),
        "median_signed_pips": round(float(np.median(v)), 3),
        "sd_signed_pips": round(float(v.std(ddof=1)), 3),
        "mean_signed_ci95_block_boot": (round(lo, 3), round(hi, 3)) if not math.isnan(lo) else (None, None),
        "hits": hits,
        "hit_rate_traded": round(hits / len(nz), 4) if len(nz) else None,
        "binom_p": round(binom_p, 5),
        "ols_slope_r2_on_r1": round(float(slope.slope), 5) if slope else None,
        "ols_slope_p": round(float(slope.pvalue), 5) if slope else None,
        "mean_abs_r1_pips": round(float(np.abs(r1).mean()), 3),
        "mean_abs_r2_pips": round(float(np.abs(r2).mean()), 3),
    })
    return out


def decide_b13(res: dict) -> str:
    """Pre-registered E016 rule (B1 rule, 1 trial).
    SIGNAL: mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05.
    WEAK:   mean signed > 0 and (CI lower > 0 or binomial p < 0.05), not SIGNAL.
    NONE:   otherwise (a significant negative mean is exploratory 'reversal' only)."""
    if "mean_signed_pips" not in res:
        return "NONE"
    m, p = res["mean_signed_pips"], res["binom_p"]
    lo = res["mean_signed_ci95_block_boot"][0]
    lo_pos = lo is not None and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


def reversal_flag(res: dict) -> bool:
    if "mean_signed_pips" not in res:
        return False
    hi = res["mean_signed_ci95_block_boot"][1]
    return res["mean_signed_pips"] < 0 and hi is not None and hi < 0


def cost_summary(f: pd.DataFrame) -> dict:
    """Descriptive cost check on traded days: bid/ask net, SPEC 4 net and costs x1.5 net."""
    t = f[f["signed_pips"].notna() & (f["direction"] != 0)]
    if t.empty:
        return {"n_traded": 0}
    gross = t["signed_pips"]
    net_spec = t["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS
    cost = gross - net_spec
    return {
        "n_traded": int(len(t)),
        "median_entry_spread_pips": round(float(t["entry_spread_pips"].median()), 3),
        "mean_gross_traded_pips": round(float(gross.mean()), 3),
        "mean_net_bidask_pips": round(float(t["net_bidask_pips"].mean()), 3),
        "mean_net_spec4_pips": round(float(net_spec.mean()), 3),
        "mean_net_costs_x1_5_pips": round(float((gross - 1.5 * cost).mean()), 3),
    }


def fetch_with_retries(get, url: str, attempts: int = 3, sleep=None, wait_s: float = 30.0):
    """E016 phase-1 re-fetch (R027): call get(url) -> (status, final_url, ctype, body) up to `attempts` times.

    Retries ONLY on transport failures (status -1: timeout / connection error). An HTTP answer of any code, including a
    refusal (401/403/429), is returned at once and never retried or worked around (R024 lesson). Returns the last result
    plus the list of per-attempt statuses for the fetch report.
    """
    import time as _time

    sleep = sleep or _time.sleep
    tries = []
    res = None
    for k in range(attempts):
        res = get(url)
        tries.append(res[0])
        if res[0] != -1:
            break
        if k < attempts - 1:
            sleep(wait_s * (k + 1))
    return res, tries
