# E019 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS are not
  touched. Lookback and hold therefore never reach outside dev (the last dev date has no next date and is dropped as `no_next`).
- **Trading dates:** sorted unique `sessions.trading_date` (17:00 NY roll) of the dev bars. Lookback and hold are counted in this list.
- **Quote:** at 16:00 NY on trading date D = bid/ask **open** of the first bar in [16:00, 16:05) America/New_York on NY date D
  (`fomc.ny_edge_quotes`; 16:00 is before the roll, so NY date = trading date). Missing -> NaN.
- **Signal:** s(D) = sign(mid16(D) - mid16(D-252)), D-252 = 252 positions earlier in the list (fixed; the upper end of the paper's
  1-12 month range; other lookbacks are new trials). s = 0 is a flat day, kept in n with signed return 0.
- **Return:** r(D) = mid16(D+1) - mid16(D), pips, D+1 = next trading date in the list. Signed = s(D) x r(D), one value per test date.
  Weekend holds (Friday -> Monday) are part of the hold.
- **Test dates:** list positions >= 252 (first test date ~early 2016). Excluded and counted, first failing check in this order:
  no 16:00 quote on D (`missing_now`), on D-252 (`missing_past`), on D+1 (`missing_next`); last date `no_next`.
- **Statistic (1 trial):** `tsmom.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI
  of the mean (block 20 days, 2000 draws, seed 0).
- **Decision rule (`tsmom.decide_b16`), unchanged from the backlog draft:**
  - **SIGNAL** if mean daily signed > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** long days and short days separately; flat days; buy-and-hold mean over
  the same days; by year (n, mean, hit, long share); sign flips; round trips = maximal runs of the same non-zero signal on consecutive
  list positions (an exclusion, flat day or flip ends a run), each charged half the 16:00 spread at entry and at exit (bid/ask net),
  SPEC 4 net = bid/ask net - 0.1 slippage - 0.1 commission per round trip, costs x1.5 = gross - 1.5 x (gross - SPEC 4 net); all
  reported per day and per round trip; median 16:00 spread. **Limitation:** overnight swap/carry is not in the data (EUR paid
  negative carry vs USD for most of 2015-2020: hurts long days, helps short days); stated in results, not modelled.
- **What follows:**
  - SIGNAL -> queue val confirmation B16v as its own experiment with this rule unchanged (LEAD needs dev SIGNAL + val pass + SPEC 4 and
    x1.5 net > 0, and a statement on carry).
  - WEAK or NONE -> B16 closed for this definition; no re-test with other lookbacks or hold times on dev.
- **Power note (written before data):** daily SD ~45 pips, n ~1,250 overlapping signals -> bootstrap SE ~1.5-2 pips; only a mean of
  roughly 3-4 pips/day clears the CI bar. A NONE does not rule out a small effect.
- **Code:** `src/fxresearch/tsmom.py`, `scripts/run_e019_tsmom.py`; tests `tests/test_tsmom.py` (constants fixed, signal/return
  definition, exclusion order, no look-ahead, 16:00 NY open quote from bars, runs and costs, random walk no SIGNAL (5 seeds),
  strong trend gives SIGNAL, rule edges).
- **Command:** `python scripts/run_e019_tsmom.py | tee backtests/validation_reports/E019_results.txt` (also writes `E019_results.json`
  and `E019_daily.csv`).
- **Trial count:** dev +1 when it runs (228 -> 229); val unchanged at 4; total 232 -> 233.
