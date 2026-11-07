"""Timezone-aware FX session definitions.

Every session is anchored to the local clock of its financial centre, so daylight
saving is handled by the IANA tz database rather than by hard-coded UTC offsets.

Key conventions (see docs/SPEC.md section 2):

* Timestamps in all data are tz-aware UTC and mark the bar OPEN.
* The FX trading day rolls at 17:00 America/New_York. A bar belongs to trading
  day D if (bar time in New York + 7 hours) falls on calendar date D.
* Sessions are half-open intervals [start, end).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from zoneinfo import ZoneInfo

import pandas as pd

NY = ZoneInfo("America/New_York")
UTC = ZoneInfo("UTC")
ROLL_OFFSET = timedelta(hours=7)  # 17:00 NY + 7h = 00:00 of the next trading date


@dataclass(frozen=True)
class Session:
    name: str
    tz: str
    start: time
    end: time

    def window_utc(self, trading_date: date) -> tuple[pd.Timestamp, pd.Timestamp]:
        """UTC [start, end) of this session on the given trading date."""
        zone = ZoneInfo(self.tz)
        start = datetime.combine(trading_date, self.start, tzinfo=zone)
        end = datetime.combine(trading_date, self.end, tzinfo=zone)
        if end <= start:  # session crosses local midnight
            end += timedelta(days=1)
        return (pd.Timestamp(start).tz_convert("UTC"), pd.Timestamp(end).tz_convert("UTC"))


# Default research sessions. Change ONLY via a recorded experiment (one variable at a time).
ASIA = Session("asia", "Asia/Tokyo", time(9, 0), time(15, 0))
LONDON = Session("london", "Europe/London", time(8, 0), time(12, 0))
US = Session("us", "America/New_York", time(8, 0), time(12, 0))
DEFAULT_SESSIONS: tuple[Session, ...] = (ASIA, LONDON, US)


def trading_date(ts: pd.Timestamp | pd.DatetimeIndex):
    """Map UTC timestamp(s) to FX trading date (17:00 New York roll)."""
    if isinstance(ts, pd.DatetimeIndex):
        if ts.tz is None:
            raise ValueError("timestamps must be tz-aware")
        return (ts.tz_convert(NY) + ROLL_OFFSET).date
    if ts.tzinfo is None:
        raise ValueError("timestamp must be tz-aware")
    return (ts.tz_convert(NY) + ROLL_OFFSET).date()


def label_sessions(index: pd.DatetimeIndex, sessions=DEFAULT_SESSIONS) -> pd.DataFrame:
    """Return a frame with `trading_date` and one boolean column per session.

    Sessions may overlap in principle, so each gets its own column rather than a
    single categorical label.
    """
    if index.tz is None:
        raise ValueError("index must be tz-aware UTC")
    out = pd.DataFrame(index=index)
    out["trading_date"] = trading_date(index)
    for s in sessions:
        local = index.tz_convert(s.tz)
        t = local.time
        if s.start < s.end:
            mask = (t >= s.start) & (t < s.end)
        else:
            mask = (t >= s.start) | (t < s.end)
        # A local clock window must also belong to the trading date it is anchored to.
        anchor_dates = pd.Index(local.date)
        if s.end <= s.start:
            # bars after local midnight belong to the previous local date's session
            anchor_dates = pd.Index(
                [d - timedelta(days=1) if tt < s.end else d for d, tt in zip(local.date, t)]
            )
        out[s.name] = mask & (anchor_dates == pd.Index(out["trading_date"]))
    return out


def is_weekend_bar(index: pd.DatetimeIndex) -> pd.Series:
    """True for bars between Friday 17:00 NY and Sunday 17:00 NY (market closed)."""
    ny = index.tz_convert(NY)
    dow = ny.dayofweek
    hour = ny.hour
    closed = (dow == 5) | ((dow == 4) & (hour >= 17)) | ((dow == 6) & (hour < 17))
    return pd.Series(closed, index=index)
