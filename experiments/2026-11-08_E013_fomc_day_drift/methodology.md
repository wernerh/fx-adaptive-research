# E013 Methodology (pre-registered 2026-11-08, before any run)

## Two phases (backlog B11 data rule)
1. **Phase 1, date file (this run, R017):** `scripts/fetch_fomc_dates.py` runs on the research-batch runner (this workspace
   cannot reach federalreserve.gov), downloads the official Federal Reserve pages
   (`monetarypolicy/fomchistoricalYYYY.htm` per year, fallback `monetarypolicy/fomccalendars.htm`), parses them with
   `fxresearch.fomc`, and commits `backtests/calendars/fomc_dates.csv` + `fomc_fetch_report.json` (raw HTML for any year that
   fails validation). **No experiment runs in phase 1 and no price data are touched.**
2. **Review (next run):** a later run checks the report: every year 2015-2023 valid (exactly 8 scheduled meetings, statement
   dates on weekdays, meetings <= 3 days), every row carries its source URL and heading text, unscheduled actions listed.
   Only then is the file copied to `data/calendars/fomc_dates.csv` and phase 2 queued. If the parse fails, fix the parser
   from the committed raw HTML and re-fetch; the decision rule below does not change. No date may be typed by hand.
3. **Phase 2, test:** `python scripts/run_e013_fomc_day.py | tee backtests/validation_reports/E013_results.txt`.

## Test definition (fixed now)
- **Data:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (statement dates 2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). Val and OOS dates are filtered out before any computation. Val confirmation (B11v) only if SIGNAL.
- **Events:** scheduled FOMC meetings; statement date = last day of the meeting. Unscheduled actions and conference calls are
  excluded from the test and listed in the output.
- **Window:** entry = mid open of the first bar in [16:00, 16:05) America/New_York on the previous business day (Mon -> Fri);
  exit = mid close of the last bar in [15:55, 16:00) NY on the statement day (covers 14:00 statement and 14:30 press conference).
  DST handled by the IANA tz database. A meeting with a missing entry or exit quote is dropped and listed (never filled).
- **Trials:** 1 (dev). Benchmark and sub-window below are descriptive, not trials.
- **Statistics (`fomc.evaluate_long`):** n, mean, median, sd, hit rate, one-sided one-sample t-test (H1: mean > 0),
  moving-block bootstrap 95% CI of the mean (block 4 meetings, 2000 draws, seed 0; block 4 chosen now because meetings are
  ~6 weeks apart, so the project default block of 20 days would span ~2.5 years).
- **Decision rule (`fomc.decide_b11`):**
  - **SIGNAL** if mean > 10.0 pips AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Cost check (descriptive; gates only the LEAD label):** long at the ask open, exit at the bid close; SPEC 4 net = bid/ask net
  - 0.1 pip entry slippage - 0.1 pip commission; costs x1.5 net = gross - 1.5 x (gross - SPEC 4 net). Median entry spread reported.
- **Descriptive (not trials):** same window on every other dev weekday (non-FOMC benchmark); 13:00-16:00 NY sub-window on statement
  days; per-year counts and means; per-meeting table.
- **What follows:**
  - SIGNAL -> pre-register B11v (val only, same window and rule, 1 trial). Not a LEAD until val confirms and the cost gate passes.
  - WEAK / NONE -> B11 closed; no re-test with other windows on dev (a different window would be a new trial and needs a reason).
- **Code:** `src/fxresearch/fomc.py`, `scripts/fetch_fomc_dates.py`, `scripts/run_e013_fomc_day.py`; tests `tests/test_fomc.py`
  (parser on synthetic HTML incl. cross-month, unscheduled, conference call and en-dash cases; 8-per-year validation;
  DST-aware 16:00 NY edges; missing quotes -> NaN; decision rule; random-walk no-SIGNAL).
- **Trial count:** dev +1 when phase 2 runs (226 -> 227).

## Addendum 2026-11-08 R018 (before phase 2; no price data touched)
- Phase 1 fetch (run 42458841737) failed validation for 2017-2019: the parser missed `Jan/Feb 31-1`-style cross-month headings.
  Parser fixed; phase 1 re-queued.
- `March 17-18 (cancelled) Meeting` (2020) had no statement. New `cancelled` column in the date file: cancelled scheduled slots
  count toward the 8-per-year validation but are **excluded from the test and listed** (like unscheduled actions) and also
  excluded from the non-FOMC benchmark. Window, decision rule, thresholds and bootstrap block are unchanged.

## Addendum 2026-11-08 R019 (phase-1 review; before phase 2; no price data touched)
- Re-fetch (run 42462817989, outputs 952a8a1): `all_years_valid: true`, 72 scheduled meetings 2015-2023, 8 per year; all scheduled
  statement dates are weekdays; meetings span <= 2 days; every row carries a federalreserve.gov source URL and heading text.
  Cross-month headings now parse (e.g. `Jan/Feb 31-1 Meeting` 2017 -> statement 2017-02-01; `Jul/Aug 31-1` 2018 -> 2018-08-01).
- Excluded and listed: unscheduled 2019-10-04, 2020-03-02, 2020-03-15; cancelled scheduled slot 2020-03-18.
- Dev test set: **47** scheduled statement days (48 minus the cancelled slot).
- Promoted unchanged to `data/calendars/fomc_dates.csv` (test asserts it equals the runner output). Phase 2 queued.
  Window, rule, thresholds, block unchanged.
