# E028 Methodology (pre-registered 2026-11-09 R056, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Dates:** the sorted trading-date set of the dev bars (17:00 NY roll, SPEC 2).
- **Quotes:** open of D = bid/ask **open** of the first bar in [17:00, 17:05) NY whose trading date is D
  (`overreaction_day.open_quotes`; for a Monday this is Sunday 17:00 NY). 12:00 and 16:30 NY quotes = first bar in [hh:mm, hh:mm+5)
  NY on NY calendar date D (`vol_state_fix.ny_quotes`). Missing -> excluded, never filled.
- **Signal:** r(D) = (mid 12:00 NY - mid open of D) / pip. D is valid if both quotes exist; otherwise `invalid_missing_signal_quote`
  (counted, not in the rolling history, never an event).
- **Bands:** m(D), s(D) = mean and sample SD (ddof=1) of r over the 60 valid dates before D (past only); first 60 valid dates burn-in.
  **Event:** valid D past burn-in with r(D) > m + 2s or r(D) < m - 2s (strict).
- **Trade per event:** position sign(r(D) - m(D)) entered at the 12:00 NY quote (the same quote that ends the signal) and exited at the
  16:30 NY quote on D (before the 17:00 roll). Exclusions, counted, first reason in this order: `missing_exit`,
  `entry_skipped_spread` (ask-bid at 12:00 > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return = sign x (mid 16:30 - mid 12:00) / pip. `overreaction_day.evaluate_b23`: mean, median, SD,
  hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (**block 5 events**, 2000 draws, seed 0).
  Fewer than 10 events -> "insufficient sample" -> NONE.
- **Decision rule (`overreaction_day.decide_b23`, thresholds identical to E022/E024, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** a negative mean (reversal reading) is logged as exploratory only;
  positive vs negative events separately; k = 1.5 and k = 2.5; control = long 12:00 -> 16:30 NY on post-burn-in non-event dates;
  events on FOMC statement dates (data/calendars/fomc_dates.csv) and result excluding them; events on first-Friday-of-month dates and
  result excluding them; share long; mean |r| and median band SD of events; by year; by weekday; median spreads at entry/exit; net
  per event at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)).
- **What follows:**
  - SIGNAL -> queue val confirmation B23v as its own experiment with this rule unchanged and a val-only burn-in (as E023/E025). LEAD
    needs dev SIGNAL + val pass + SPEC 4 and x1.5 net > 0.
  - WEAK or NONE -> B23 closed for this definition; no re-test on dev with other k, windows or hours. Next: B24 (val only).
- **Power note (written before data):** ~1,560 dev dates, ~1,500 post burn-in, ~45-75 events (fat tails may give more); SE ~3 pips.
- **Calendar label:** post-London-fix afternoon (hold starts after the 11:00 NY fix; contains 14:00 NY FOMC statements on those dates).
- **Code:** `src/fxresearch/overreaction_day.py` (reuses `vol_state_fix.ny_quotes`, `decide_b19`, cost constants);
  `scripts/run_e028_overreaction_day.py`; tests `tests/test_overreaction_day.py` (constants fixed, bands/event/sign, strict threshold,
  invalid dates excluded from the history, spread / missing-exit exclusions, no look-ahead, quotes from bars incl. the previous-day
  17:00 open, fat-tailed random-walk SIGNAL rate <= 0.10 over 40 seeds, strong continuation gives SIGNAL, insufficient sample -> NONE).
  Synthetic smoke run passed (no events in the short synthetic dev block: burn-in, as expected).
- **Command:** `python scripts/run_e028_overreaction_day.py | tee backtests/validation_reports/E028_results.txt` (also writes
  `E028_results.json` and `E028_days.csv`).
- **Trial count:** dev +1 when it runs (235 -> 236); val unchanged at 6; total 241 -> 242.
