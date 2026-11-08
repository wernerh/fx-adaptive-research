"""E015 (backlog B12): NFP release reaction continuation, plus the BLS release-date parser.

Two parts:

1. Calendar parsing (`parse_archive_index`, `validate_year`) for the official BLS Employment Situation archive index
   (https://www.bls.gov/bls/news-release/empsit.htm). Archived releases are linked as
   `/news.release/archives/empsit_MMDDYYYY.htm`, where MMDDYYYY is the release date. The page is downloaded on the GitHub
   runner by scripts/fetch_nfp_dates.py because this workspace cannot reach bls.gov. No date is typed by hand: every row
   carries the source URL of the index page and the archive link it was parsed from. A year is valid only with exactly
   12 releases, one in each calendar month, all on weekdays.

2. The pre-registered test (methodology in experiments/2026-11-08_E015_nfp_continuation/):
   on each release day (08:30 America/New_York),
     P0 = mid open of the first bar in [08:30, 08:35) NY
     P1 = mid close of the last bar in [08:40, 08:45) NY      -> r1 = P1 - P0 (first-15-minute reaction)
     E  = mid open of the first bar in [08:45, 08:50) NY      (entry, after r1 is fully known)
     X  = mid close of the last bar in [09:40, 09:45) NY      -> r2 = X - E (next hour)
   signed = sign(r1) * r2 if |r1| >= 1.0 pip, else 0 (no trade; the day stays in n).
   r2 uses only bars at or after 08:45, r1 only bars before 08:45, so the signal cannot look ahead.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass
from datetime import date

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import NY

INDEX_URL = "https://www.bls.gov/bls/news-release/empsit.htm"
RELEASES_PER_YEAR = 12

# Pre-registered constants (E015 methodology; fixed before any price data).
T_RELEASE = 8 * 60 + 30     # 08:30 NY
T_ENTRY = 8 * 60 + 45       # 08:45 NY
T_EXIT = 9 * 60 + 45        # 09:45 NY
EDGE_MINUTES = 5            # open quote from the first bar in [t, t+5); close quote from the last bar in [t-5, t)
MIN_REACTION_PIPS = 1.0     # |r1| below this -> no trade (signed 0, kept in n)
MIN_MEAN_PIPS = 1.0
ALPHA = 0.05
BOOT_BLOCK = 4              # monthly events; block 4 ~ one quarter-plus, as in E013
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1   # SPEC 4
COMMISSION_RT_PIPS = 0.1    # SPEC 4

_LINK_RE = re.compile(r"empsit_(\d{2})(\d{2})(\d{4})\.htm", re.I)


@dataclass(frozen=True)
class Release:
    release_date: date
    link: str


def parse_archive_index(page: str) -> list[Release]:
    """All archived Employment Situation releases linked from the BLS archive index, de-duplicated, sorted."""
    out: dict[date, Release] = {}
    for m in _LINK_RE.finditer(page):
        mm, dd, yyyy = (int(x) for x in m.groups())
        try:
            d = date(yyyy, mm, dd)
        except ValueError:
            continue
        out.setdefault(d, Release(d, m.group(0)))
    return sorted(out.values(), key=lambda r: r.release_date)


def validate_year(releases: list[Release], year: int) -> tuple[bool, str]:
    rs = [r for r in releases if r.release_date.year == year]
    if len(rs) != RELEASES_PER_YEAR:
        return False, f"{len(rs)} releases (need {RELEASES_PER_YEAR})"
    months = sorted(r.release_date.month for r in rs)
    if months != list(range(1, 13)):
        return False, f"not one release per calendar month: months {months}"
    wk = [str(r.release_date) for r in rs if r.release_date.weekday() >= 5]
    if wk:
        return False, f"weekend release dates: {wk}"
    return True, "ok"


def non_friday(releases: list[Release]) -> list[str]:
    return [str(r.release_date) for r in releases if r.release_date.weekday() != 4]


# ---------------------------------------------------------------- E015 test -------------------------------------------

def _edge(bars: pd.DataFrame, minutes: np.ndarray, nyd: pd.Index, t: int, kind: str) -> pd.DataFrame:
    if kind == "open":
        sel = (minutes >= t) & (minutes < t + EDGE_MINUTES)
        g = bars.loc[sel, ["bid_open", "ask_open"]].groupby(nyd[sel]).first()
        g.columns = ["bid", "ask"]
    else:
        sel = (minutes >= t - EDGE_MINUTES) & (minutes < t)
        g = bars.loc[sel, ["bid_close", "ask_close"]].groupby(nyd[sel]).last()
        g.columns = ["bid", "ask"]
    g.index = pd.Index([pd.Timestamp(x).date() for x in g.index])
    return g


def reaction_frame(bars: pd.DataFrame, release_dates) -> pd.DataFrame:
    """Per release date: r1, r2, signed continuation return (mid) and bid/ask net of the continuation trade.

    Rows with any missing edge quote keep NaN in r1/r2/signed (dropped and listed by the caller, never filled).
    """
    ny = bars.index.tz_convert(NY)
    minutes = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    nyd = pd.Index(ny.date)
    p0 = _edge(bars, minutes, nyd, T_RELEASE, "open")
    p1 = _edge(bars, minutes, nyd, T_ENTRY, "close")
    e = _edge(bars, minutes, nyd, T_ENTRY, "open")
    x = _edge(bars, minutes, nyd, T_EXIT, "close")
    rows = []
    for d in release_dates:
        r = {"date": d, "r1_pips": np.nan, "r2_pips": np.nan, "direction": 0, "signed_pips": np.nan,
             "net_bidask_pips": np.nan, "entry_spread_pips": np.nan}
        if all(d in q.index for q in (p0, p1, e, x)):
            mid = {k: (q.loc[d, "bid"] + q.loc[d, "ask"]) / 2 for k, q in (("p0", p0), ("p1", p1), ("e", e), ("x", x))}
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
    """Pre-registered statistics. Mean / CI over all valid release days (no-trade days count as 0);
    binomial hit rate over traded days with r2 != 0 (one-sided, H1: continuation share > 0.5)."""
    v = f["signed_pips"].dropna().to_numpy(dtype=float)
    n = len(v)
    traded = f.loc[f["signed_pips"].notna() & (f["direction"] != 0), "signed_pips"].to_numpy(dtype=float)
    nz = traded[traded != 0]
    hits = int((nz > 0).sum())
    out = {"n": n, "n_traded": int(len(traded)), "n_no_trade": int(n - len(traded))}
    if n < 3:
        return out
    lo, hi = block_bootstrap_mean_ci(v, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    binom_p = float(stats.binomtest(hits, len(nz), 0.5, alternative="greater").pvalue) if len(nz) else 1.0
    out.update({
        "mean_signed_pips": round(float(v.mean()), 3),
        "median_signed_pips": round(float(np.median(v)), 3),
        "sd_signed_pips": round(float(v.std(ddof=1)), 3),
        "mean_signed_ci95_block_boot": (round(lo, 3), round(hi, 3)) if not math.isnan(lo) else (None, None),
        "hits": hits,
        "hit_rate_traded": round(hits / len(nz), 4) if len(nz) else None,
        "binom_p": round(binom_p, 5),
        "mean_abs_r1_pips": round(float(f["r1_pips"].abs().mean()), 3),
        "mean_abs_r2_pips": round(float(f["r2_pips"].abs().mean()), 3),
    })
    return out


def decide_b12(res: dict) -> str:
    """Pre-registered E015 rule (B1 rule, 1 trial).
    SIGNAL: mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05.
    WEAK:   mean signed > 0 and (CI lower > 0 or binomial p < 0.05), not SIGNAL.
    NONE:   otherwise (a significant negative mean is reported as exploratory 'reversal' only)."""
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
    """Exploratory only (not a trial): mean signed < 0 with block-bootstrap CI upper < 0."""
    if "mean_signed_pips" not in res:
        return False
    hi = res["mean_signed_ci95_block_boot"][1]
    return res["mean_signed_pips"] < 0 and hi is not None and hi < 0


def cost_summary(f: pd.DataFrame) -> dict:
    """Descriptive cost check on traded days: bid/ask net, SPEC 4 net and costs x1.5 net (no-trade days excluded)."""
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
