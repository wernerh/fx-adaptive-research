# E029 Methodology (pre-registered 2026-11-10 R058, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only** (2021-01-21..2023-06-30,
  `splits.DEFAULT_PLAN`). The script first drops every bar at or after 2023-07-01 UTC, then every bar whose trading date is not `val`
  (`vol_state_fix.restrict_to_block`), **before** any computation (val-only burn-in, no dev history, as E023/E025). Dev and OOS untouched.
- **Dates:** the sorted trading-date set of the val bars (17:00 NY roll, SPEC 2).
- **Quotes:** open of D = bid/ask **open** of the first bar in [17:00, 17:05) NY whose trading date is D (`overreaction_day.open_quotes`).
  Close of D = first bar in [16:55, 17:00) NY on NY calendar date D (`vol_state_fix.ny_quotes`). Entry = first bar in [17:05, 17:10) NY
  whose trading date is N = D + 1 calendar day (`open_quotes(bars, 17, 5)`). Exit = first bar in [02:00, 02:05) NY on NY calendar date N
  (`ny_quotes`). Missing -> excluded, never filled.
- **Signal:** R(D) = (mid close of D - mid open of D) / pip. D is valid if both quotes exist; otherwise `invalid_missing_signal_quote`
  (counted, not in the rolling history, never an event).
- **Bands:** m(D), s(D) = mean and sample SD (ddof=1) of R over the 60 valid dates before D (past only; valid Fridays stay in the
  history); first 60 valid val dates burn-in. **Event:** valid D past burn-in with R(D) > m + 2s or R(D) < m - 2s (strict).
- **Trade per event:** position -sign(R(D) - m(D)) entered at the 17:05 NY entry quote and exited at the 02:00 NY exit quote.
  Exclusions, counted, first reason in this order: `friday_excluded` (D is a Friday; the weekend gap belongs to B17), `missing_entry`,
  `missing_exit`, `entry_skipped_spread` (ask-bid at 17:05 > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return = -sign x (mid 02:00 - mid 17:05) / pip. `overreaction_fade.evaluate_b24` (=
  `overreaction_day.evaluate_b23`): mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the
  mean (**block 5 events**, 2000 draws, seed 0). Fewer than 10 events -> "insufficient sample" -> NONE.
- **Decision rule (`overreaction_fade.decide_b24`, thresholds identical to E022/E024/E028, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Null calibration (code test, written before data):** on fat-tailed random walks sized like val (~600 dates, ~25 events), the
  rule returned SIGNAL in 4.3% of 300 seeds (small-n block bootstrap; R058 scratch check), <= 8% over the 100 seeds in the test.
- **Descriptive (not trials, do not change the decision):** a negative mean (continuation reading) is logged as exploratory only;
  positive vs negative days separately; exit 03:00 NY; k = 1.5 and k = 2.5; control = long 17:05 -> 02:00 NY on post-burn-in
  tradable non-event dates; events on FOMC statement dates and result excluding them; first-Friday count; share short; mean |R| and
  median band SD of events; by year; by weekday of D; median entry spread of all events (roll-hour spreads are wide) and of tested
  events; net per event at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5
  (gross - 1.5 x (gross - SPEC 4 net)).
- **What follows:**
  - SIGNAL -> logged as a val-only SIGNAL (not a LEAD: no clean dev pass). Recorded in agent_decision_log.md as needing a human
    decision before any OOS use; no automatic follow-up.
  - WEAK or NONE -> B24 closed for this definition; no re-test with other k, windows, hours or exits. Next: backlog refill.
- **Power note (written before data):** n ~ 15-35 events; SE ~3-5 pips. Low power, stated up front.
- **Calendar label:** Asian session after a large NY day; contains the Tokyo fix (19:55 / 20:55 NY by DST).
- **Code:** `src/fxresearch/overreaction_fade.py` (reuses `overreaction_day.open_quotes/add_bands/_event/evaluate_b23/decide_b23`,
  `vol_state_fix.ny_quotes`, cost constants); `scripts/run_e029_overreaction_fade.py`; tests `tests/test_overreaction_fade.py`
  (constants fixed, bands/event/fade sign, Friday excluded but kept in history, strict threshold, invalid dates excluded from history,
  missing-entry / missing-exit / spread exclusions, no look-ahead, quotes from bars incl. the 17:05 entry on calendar D and 02:00 exit
  on D + 1, random-walk SIGNAL rate <= 0.08, strong fade gives SIGNAL, insufficient sample -> NONE). Synthetic smoke run passed (no
  events in the short synthetic val block: burn-in, as expected).
- **Command:** `python scripts/run_e029_overreaction_fade.py | tee backtests/validation_reports/E029_results.txt` (also writes
  `E029_results.json` and `E029_days.csv`).
