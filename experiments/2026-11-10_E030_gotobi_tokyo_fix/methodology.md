# E030 Methodology (pre-registered 2026-11-10 R061, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Universe:** Mon-Fri trading dates (17:00 NY roll, SPEC 2) present in the dev bars. 08:55-09:55 Tokyo = 23:55-00:55 UTC, after the
  17:00 NY roll, so the trading date equals the Tokyo calendar date (tested).
- **Gotobi date (`gotobi_fix.gotobi_info`, rule fixed in backlog R060):** Tokyo date with day of month 5, 10, 15, 20, 25 or 30, or the
  last calendar day of the month; a nominal day on Saturday/Sunday moves to the preceding Friday (flag `weekend_shifted` only if
  that Friday is not itself nominal). `month_end` flag = a source day is the month's last day. Japanese public holidays are not in
  the repo: not shifted, count not computed (limitation). ~30% of weekdays (tested: 27-33% over 2015-2020).
- **Quotes:** quote at hh:mm = bid/ask **open** of the first bar in [hh:mm, hh:mm+5) Asia/Tokyo on the Tokyo date
  (`gotobi_fix.local_quotes`). Entry 08:55, exit 09:55. (E011 used open of the first bar to close of the last bar inside the window;
  the exit here is the 09:55 bar open, i.e. one tick later. Fixed now, as written in the backlog.)
- **Exclusions, counted, first reason in this order:** `missing_entry`, `missing_exit`, `low_coverage` (< 55 of the 60 one-minute
  bars in [08:55, 09:55) Tokyo, E011's coverage rule), `entry_skipped_spread` (ask-bid at 08:55 > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return = -(mid exit - mid entry) / pip per tested gotobi date. `gotobi_fix.evaluate`: mean, median,
  SD, hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (**block 20 events**, 2000 draws, seed 0).
  Fewer than 40 tested events -> "insufficient sample" -> NONE.
- **Decision rule (`gotobi_fix.decide_b25`, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** non-gotobi control (same trade on tradable non-gotobi dates) and the
  difference gotobi minus control; month-end vs other gotobi; weekend-shifted vs not; 09:25 -> 09:55 Tokyo last half hour (gotobi
  and control); by year; by weekday; median spreads at entry/exit; net per event at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage -
  0.1 commission) and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)), for events and control.
- **What follows:**
  - SIGNAL -> queue val confirmation B25v as its own experiment with this rule unchanged. LEAD needs dev SIGNAL + val pass + SPEC 4
    and x1.5 net > 0 (AUTONOMOUS_PROTOCOL). Calendar label: the Tokyo fix *is* the strategy.
  - WEAK or NONE -> B25 closed for this definition; no re-test on dev with other windows or day rules. Next: B26 (post-fix, dev).
- **Calendar label:** Tokyo 09:55 JST fix (= 19:55 NY in EST, 20:55 NY in EDT on the previous NY calendar date; same trading date).
- **Code:** `src/fxresearch/gotobi_fix.py`; `scripts/run_e030_gotobi_fix.py`; tests `tests/test_gotobi_fix.py` (constants fixed,
  12 calendar cases incl. leap year and weekend shifts, gotobi share, Tokyo-date keying and short sign, cost arithmetic, exclusion
  order, calendar-only flag / no look-ahead, random-walk pipeline gives no SIGNAL (3 seeds), fat-tailed null SIGNAL rate <= 5% over
  200 draws, strong effect -> SIGNAL, small effect -> WEAK, insufficient sample -> NONE). Synthetic smoke run passed (NONE, 13 events).
- **Command:** `python scripts/run_e030_gotobi_fix.py | tee backtests/validation_reports/E030_results.txt` (also writes
  `E030_results.json` and `E030_days.csv`).
- **Trial count:** dev +1 when it runs (236 -> 237); val unchanged at 7; total 243 -> 244.
