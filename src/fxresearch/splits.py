"""Chronological data splits. The out-of-sample block is LOCKED (docs/SPEC.md section 5).

Rules:
* Splits are by trading date, never shuffled.
* An embargo of `embargo_days` is left between blocks so rolling features
  (e.g. 14-day ATR) cannot straddle a boundary.
* The OOS block may be evaluated ONCE per strategy version. Each evaluation is
  logged in experiments/experiment_registry.csv (column oos_touched).
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import pandas as pd


@dataclass(frozen=True)
class SplitPlan:
    dev_end: date      # inclusive
    val_end: date      # inclusive
    embargo_days: int = 20

    def assign(self, dates: pd.Index) -> pd.Series:
        d = pd.to_datetime(pd.Index(dates))
        dev_end, val_end = pd.Timestamp(self.dev_end), pd.Timestamp(self.val_end)
        emb = pd.Timedelta(days=self.embargo_days)
        lab = pd.Series("embargo", index=dates)
        lab[d <= dev_end] = "dev"
        lab[(d > dev_end + emb) & (d <= val_end)] = "val"
        lab[d > val_end + emb] = "oos"
        return lab


# Default plan for EUR/USD 2015-01 .. latest. See SPEC 5.1.
DEFAULT_PLAN = SplitPlan(dev_end=date(2020, 12, 31), val_end=date(2023, 6, 30))


def walk_forward_folds(dates: pd.Index, train_years: int = 3, test_months: int = 6):
    """Yield (train_dates, test_dates) rolling folds inside the dev+val region."""
    d = pd.to_datetime(pd.Index(sorted(set(dates))))
    start = d.min()
    while True:
        train_end = start + pd.DateOffset(years=train_years)
        test_end = train_end + pd.DateOffset(months=test_months)
        if test_end > d.max():
            break
        yield d[(d >= start) & (d < train_end)], d[(d >= train_end) & (d < test_end)]
        start = start + pd.DateOffset(months=test_months)
