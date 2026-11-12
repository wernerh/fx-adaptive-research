# E046 Methodology (pre-registered 2026-11-12 R110, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner), mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any
  computation; val and OOS untouched. FOMC dates: `data/calendars/fomc_dates.csv` (validated in E013), scheduled and not cancelled
  only (2020-03-18 cancelled slot and unscheduled 2019-10-04, 2020-03-02, 2020-03-15 ignored). No external download.
- **Tested dates:** Mon-Fri trading dates (`sessions.trading_date`, 17:00 NY roll) present in the dev bars.
- **Cycle (B54, unchanged):** day 0 = statement date. Days counted in Mon-Fri dates (numpy business days; US holidays not skipped,
  limitation). k_next = -(Mon-Fri dates from D to the next statement date S >= D); if k_next >= -6 use it, else k = Mon-Fri dates
  since the previous statement date. No previous statement and k_next < -6 -> `pre_cycle`. Weeks: -1: k -6..-2; 0: -1..3;
  1: 4..8; 2: 9..13; 3: 14..18; 4: 19..23; 5: 24..28; 6: 29..33; k > 33 -> `unassigned`.
- **Position:** s = +1 in weeks 2, 4, 6; s = -1 in weeks -1, 1, 3, 5; week 0 -> `week0_excluded`.
- **Trade:** entry at the 20:00 NY quote on the NY calendar date before D (first 1-minute bar in [20:00, 20:05),
  `vol_state_fix.ny_quotes`; Sunday 20:00 for Monday dates), exit at the 16:55 NY quote on D. Signed = s x (mid exit - mid entry)/pip.
- **Exclusions (counted, first reason in this order):** `pre_cycle`, `unassigned`, `week0_excluded`, `missing_entry`,
  `missing_exit`, `entry_skipped_spread` (ask - bid at entry > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** `overnight_reversal.evaluate_b32`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block
  bootstrap 95% CI of the mean (blocks of 20 consecutive tested dates, 2000 draws, seed 0).
- **Decision rule (`fomc_cycle.decide_b54` = `overnight_reversal.decide_b34`, unchanged from the backlog draft = E041/E044 rule):**
  - < 500 tested dates -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** long mean by cycle week -1..6 incl. week 0; even-only long leg and
  odd-only short leg; share long; unconditional long over the same hold; same test with the cycle lagged one weekday (paper Panel B
  analogue); opposite-sign mean (reported only); by year (lesson R092); net at bid/ask, SPEC 4 and costs x1.5; exclusion counts.
- **What follows:** SIGNAL -> B55 val confirmation (own pre-registration, rule unchanged, 1 val trial, < 200 dates NONE). Not a LEAD
  until val passes and SPEC 4 and x1.5 net > 0. WEAK or NONE -> B54 closed, B55 closed unearned; no re-test with other week
  definitions, holds, lags or the opposite sign.
- **Power note (written before data):** ~48 dev meetings x ~25 assigned non-week-0 dates -> n ~1,200; SD ~40-60 pips -> SE ~1.3-1.7.
- **Code:** `src/fxresearch/fomc_cycle.py`; `scripts/run_e046_fomc_cycle.py`; tests `tests/test_fomc_cycle.py` (constants, calendar
  filter, k counting across weekends and both sides of a meeting, week mapping / positions, unassigned gap, entry 20:00 previous
  calendar date (Sunday for Monday) / exit 16:55 D and sign, week-0 and pre-cycle exclusions, positions independent of prices
  (no look-ahead), spread exclusion, decision rule, pooled random walk -> |mean| < 2 and no SIGNAL). 382 tests pass. Synthetic smoke run passed
  (NONE, 28 dates).
- **Command (batch.sh):** `python scripts/run_e046_fomc_cycle.py | tee backtests/validation_reports/E046_results.txt` (also writes
  `E046_results.json` and `E046_days.csv`).
- **Trial count:** dev +1 when it runs (255 -> 256); val unchanged at 9; total 264 -> 265.
