"""E013 (backlog B11): FOMC statement-day EUR/USD drift, plus the FOMC date-file parser.

Two parts:

1. Calendar parsing (`parse_historical_page`, `parse_calendars_page`) for official Federal Reserve pages
   (fomchistoricalYYYY.htm and fomccalendars.htm). Pages are downloaded on the GitHub runner by
   scripts/fetch_fomc_dates.py, because this workspace cannot reach federalreserve.gov. No date is typed by hand:
   every row carries its source URL and the raw heading text it was parsed from. A year is valid only with
   exactly 8 scheduled meetings.

2. The pre-registered window (methodology in experiments/2026-11-08_E013_fomc_day_drift/):
   long EUR/USD mid from 16:00 America/New_York on the previous business day to 16:00 NY on the statement day.
   Entry = mid open of the first bar in [16:00, 16:05) NY; exit = mid close of the last bar in [15:55, 16:00) NY.
   Calendar-only, so nothing can look ahead.
"""
from __future__ import annotations

import html as _html
import math
import re
from dataclasses import dataclass
from datetime import date, timedelta

import numpy as np
import pandas as pd
from scipy import stats

from .data import PIP
from .metrics import block_bootstrap_mean_ci
from .sessions import NY

MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
          "november", "december"]
_MON3 = {m[:3]: i + 1 for i, m in enumerate(MONTHS)}
_MONTH_RE = r"(Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|June?|July?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"

SCHEDULED_PER_YEAR = 8

# Pre-registered constants (E013 methodology; fixed before any data).
WINDOW_HOUR = 16            # 16:00 NY entry (previous business day) and exit (statement day)
SUB_WINDOW_START_HOUR = 13  # descriptive 13:00-16:00 NY sub-window on statement day
EDGE_MINUTES = 5            # entry bar must be in [16:00, 16:05), exit bar in [15:55, 16:00)
MIN_MEAN_PIPS = 10.0
ALPHA = 0.05
BOOT_BLOCK = 4              # meetings are ~6 weeks apart; block 4 ~ half a year
BOOT_N = 2000
SLIPPAGE_ENTRY_PIPS = 0.1   # SPEC 4
COMMISSION_RT_PIPS = 0.1    # SPEC 4


def _month_num(tok: str) -> int:
    return _MON3[tok.strip().lower()[:3]]


def _clean(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = _html.unescape(s).replace("–", "-").replace("—", "-").replace("\xa0", " ")
    return re.sub(r"\s+", " ", s).strip()


@dataclass(frozen=True)
class Meeting:
    year: int
    start: date
    statement_date: date  # last day of the meeting
    scheduled: bool
    label: str            # raw heading / cell text the row was parsed from
    cancelled: bool = False  # scheduled slot that was cancelled (no statement that day); counts toward 8, excluded from tests


_HEAD_RE = re.compile(
    rf"^{_MONTH_RE}\.?\s+(\d{{1,2}})(?:\s*-\s*(?:{_MONTH_RE}\.?\s+)?(\d{{1,2}}))?\b(.*)$", re.I)


_SLASH_HEAD_RE = re.compile(
    rf"^{_MONTH_RE}\.?\s*/\s*{_MONTH_RE}\.?\s+(\d{{1,2}})\s*-\s*(\d{{1,2}})\b(.*)$", re.I)


def parse_heading(text: str, year: int) -> Meeting | None:
    """Parse one historical-page heading such as 'January 27-28 Meeting - 2015' or 'April 30-May 1 Meeting - 2019'.

    Scheduled = the heading says 'Meeting' and neither 'unscheduled' nor 'conference call'.
    """
    t = _clean(text)
    m = _HEAD_RE.match(t)
    ms = _SLASH_HEAD_RE.match(t)
    if ms:  # 'Jan/Feb 31-1 Meeting' style (historical pages 2017-2019)
        m1, m2, d1, d2, rest = ms.groups()
    elif m:
        m1, d1, m2, d2, rest = m.groups()
    else:
        return None
    rest_l = rest.lower()
    mo1 = _month_num(m1)
    mo2 = _month_num(m2) if m2 else mo1
    start = date(year, mo1, int(d1))
    end = date(year, mo2, int(d2)) if d2 else start
    if end < start:  # e.g. 'Dec 31-Jan 1' never happens for FOMC, but keep it explicit
        return None
    scheduled = ("meeting" in rest_l) and ("unscheduled" not in rest_l) and ("conference call" not in rest_l)
    if "meeting" not in rest_l and "conference call" not in rest_l and "unscheduled" not in rest_l:
        return None  # not a meeting heading (e.g. a minutes-release line)
    return Meeting(year, start, end, scheduled, t, cancelled=scheduled and "cancel" in rest_l)


def parse_historical_page(page: str, year: int) -> list[Meeting]:
    """Meetings from fomchistoricalYYYY.htm: headings in <h4>/<h5>/panel-heading elements."""
    heads = re.findall(r"<h[1-6][^>]*>(.*?)</h[1-6]>", page, flags=re.S | re.I)
    heads += re.findall(r'<div[^>]*class="[^"]*panel-heading[^"]*"[^>]*>(.*?)</div>', page, flags=re.S | re.I)
    out, seen = [], set()
    for h in heads:
        t = _clean(h)
        # headings normally end with ' - YYYY'; keep only this year's
        ym = re.search(r"(\d{4})\s*$", t)
        if ym and int(ym.group(1)) != year:
            continue
        mt = parse_heading(re.sub(r"\s*-\s*\d{4}\s*$", "", t), year)
        if mt and (mt.start, mt.statement_date, mt.scheduled) not in seen:
            seen.add((mt.start, mt.statement_date, mt.scheduled))
            out.append(mt)
    return sorted(out, key=lambda x: x.start)


def parse_calendar_cell(month_txt: str, date_txt: str, year: int) -> Meeting | None:
    """One fomccalendars.htm row: month cell ('January', 'Apr/May') and date cell ('25-26*', '15 (unscheduled)')."""
    mt, dt = _clean(month_txt), _clean(date_txt)
    months = re.findall(_MONTH_RE, mt, flags=re.I)
    days = re.findall(r"\d{1,2}", dt.split("(")[0])
    if not months or not days:
        return None
    mo1 = _month_num(months[0])
    mo2 = _month_num(months[-1])
    start = date(year, mo1, int(days[0]))
    end_mo = mo2 if len(days) > 1 else mo1
    end = date(year, end_mo, int(days[-1]))
    low = dt.lower()
    scheduled = not any(w in low for w in ("unscheduled", "notation", "conference call"))
    return Meeting(year, start, end, scheduled, f"{mt} {dt}", cancelled=scheduled and "cancel" in low)


def parse_calendars_page(page: str) -> dict[int, list[Meeting]]:
    """Meetings by year from fomccalendars.htm (sections headed 'YYYY FOMC Meetings')."""
    parts = re.split(r"(\d{4})\s+FOMC\s+Meetings", page)
    out: dict[int, list[Meeting]] = {}
    for i in range(1, len(parts) - 1, 2):
        year, body = int(parts[i]), parts[i + 1]
        months = re.findall(r'class="[^"]*fomc-meeting__month[^"]*"[^>]*>(.*?)</div>', body, flags=re.S | re.I)
        dates = re.findall(r'class="[^"]*fomc-meeting__date[^"]*"[^>]*>(.*?)</div>', body, flags=re.S | re.I)
        ms = []
        for mo, dt in zip(months, dates):
            mt = parse_calendar_cell(mo, dt, year)
            if mt:
                ms.append(mt)
        if ms and year not in out:
            out[year] = sorted(ms, key=lambda x: x.start)
    return out


def validate_year(meetings: list[Meeting]) -> tuple[bool, str]:
    sched = [m for m in meetings if m.scheduled]
    if len(sched) != SCHEDULED_PER_YEAR:
        return False, f"{len(sched)} scheduled meetings (need {SCHEDULED_PER_YEAR})"
    for m in sched:
        if m.statement_date.weekday() >= 5:
            return False, f"statement on a weekend: {m.statement_date}"
        if (m.statement_date - m.start).days > 2:
            return False, f"meeting longer than 3 days: {m.label}"
    return True, "ok"


# ---------------------------------------------------------------- E013 window ----------------------------------------

def prev_business_day(d: date) -> date:
    d = d - timedelta(days=1)
    while d.weekday() >= 5:
        d -= timedelta(days=1)
    return d


def ny_edge_quotes(bars: pd.DataFrame, hour: int) -> pd.DataFrame:
    """Per New York calendar date: quotes at `hour`:00 NY.

    open_*  : bid/ask open of the first bar in [hour:00, hour:05)
    close_* : bid/ask close of the last bar in [hour-1:55, hour:00)
    """
    ny = bars.index.tz_convert(NY)
    minutes = np.asarray(ny.hour) * 60 + np.asarray(ny.minute)
    t0 = hour * 60
    nyd = pd.Index(ny.date)
    o_sel = (minutes >= t0) & (minutes < t0 + EDGE_MINUTES)
    c_sel = (minutes >= t0 - EDGE_MINUTES) & (minutes < t0)
    o = bars.loc[o_sel, ["bid_open", "ask_open"]].groupby(nyd[o_sel]).first()
    c = bars.loc[c_sel, ["bid_close", "ask_close"]].groupby(nyd[c_sel]).last()
    out = o.join(c, how="outer")
    out.index = pd.Index([pd.Timestamp(x).date() for x in out.index], name="ny_date")
    return out


def window_frame(bars: pd.DataFrame, end_dates) -> pd.DataFrame:
    """Long-EUR/USD returns, 16:00 NY previous business day -> 16:00 NY on each date in `end_dates`.

    Rows missing an entry or exit quote are kept with NaN returns (counted as dropped, never filled).
    Columns: start_date, ret_pips (mid), net_bidask_pips, entry_spread_pips, sub_ret_pips (13:00-16:00 NY on D, mid).
    """
    q16 = ny_edge_quotes(bars, WINDOW_HOUR)
    q13 = ny_edge_quotes(bars, SUB_WINDOW_START_HOUR)
    rows = []
    for d in end_dates:
        s = prev_business_day(d)
        r = {"date": d, "start_date": s, "ret_pips": np.nan, "net_bidask_pips": np.nan,
             "entry_spread_pips": np.nan, "sub_ret_pips": np.nan}
        if s in q16.index and d in q16.index:
            e, x = q16.loc[s], q16.loc[d]
            if not (np.isnan(e["bid_open"]) or np.isnan(x["bid_close"])):
                r["ret_pips"] = ((x["bid_close"] + x["ask_close"]) / 2 - (e["bid_open"] + e["ask_open"]) / 2) / PIP
                r["net_bidask_pips"] = (x["bid_close"] - e["ask_open"]) / PIP
                r["entry_spread_pips"] = (e["ask_open"] - e["bid_open"]) / PIP
            if d in q13.index and not (np.isnan(q13.loc[d, "bid_open"]) or np.isnan(x["bid_close"])):
                e13 = q13.loc[d]
                r["sub_ret_pips"] = ((x["bid_close"] + x["ask_close"]) / 2
                                     - (e13["bid_open"] + e13["ask_open"]) / 2) / PIP
        rows.append(r)
    return pd.DataFrame(rows).set_index("date")


def evaluate_long(x: pd.Series) -> dict:
    """Stats for a long-only mean test: mean, sd, hit rate, one-sided t p (H1 mean > 0), block-bootstrap CI."""
    v = pd.Series(x).dropna().to_numpy(dtype=float)
    n = len(v)
    if n < 3:
        return {"n": n}
    t = stats.ttest_1samp(v, 0.0, alternative="greater")
    lo, hi = block_bootstrap_mean_ci(v, block=BOOT_BLOCK, n_boot=BOOT_N, seed=0)
    return {
        "n": n,
        "mean_pips": round(float(v.mean()), 3),
        "median_pips": round(float(np.median(v)), 3),
        "sd_pips": round(float(v.std(ddof=1)), 3),
        "hit_rate": round(float((v > 0).mean()), 4),
        "t_stat": round(float(t.statistic), 3),
        "t_p_one_sided": round(float(t.pvalue), 5),
        "mean_ci95_block_boot": (round(lo, 3), round(hi, 3)) if not math.isnan(lo) else (None, None),
    }


def decide_b11(res: dict) -> str:
    """Pre-registered E013 rule. SIGNAL: mean > 10 pips AND CI lower > 0 AND one-sided t p < 0.05.
    WEAK: mean > 0 and (CI lower > 0 or p < 0.05), not SIGNAL. NONE otherwise."""
    if "mean_pips" not in res:
        return "NONE"
    m, p = res["mean_pips"], res["t_p_one_sided"]
    lo = res["mean_ci95_block_boot"][0]
    lo_pos = lo is not None and lo > 0
    if m > MIN_MEAN_PIPS and lo_pos and p < ALPHA:
        return "SIGNAL"
    if m > 0 and (lo_pos or p < ALPHA):
        return "WEAK"
    return "NONE"


def cost_summary(df: pd.DataFrame) -> dict:
    gross = df["ret_pips"].dropna()
    net_spec = (df["net_bidask_pips"] - SLIPPAGE_ENTRY_PIPS - COMMISSION_RT_PIPS).loc[gross.index]
    cost = gross - net_spec
    return {
        "n": int(len(gross)),
        "median_entry_spread_pips": round(float(df.loc[gross.index, "entry_spread_pips"].median()), 3),
        "mean_net_bidask_pips": round(float(df.loc[gross.index, "net_bidask_pips"].mean()), 3),
        "mean_net_spec4_pips": round(float(net_spec.mean()), 3),
        "mean_net_costs_x1_5_pips": round(float((gross - 1.5 * cost).mean()), 3),
    }
