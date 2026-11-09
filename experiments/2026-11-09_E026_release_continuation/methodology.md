# E026 Methodology (pre-registered 2026-11-09 R051, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Dates:** the sorted trading-date set of the dev bars (17:00 NY roll; for 08:30-12:00 NY the NY calendar date equals the trading
  date).
- **Quote at hh:mm NY on date d:** bid/ask **open** of the first bar in [hh:mm, hh:mm+5) America/New_York
  (`vol_state_fix.ny_quotes`). Missing -> excluded, never filled.
- **Jump:** J(D) = (mid 08:45 - mid 08:30) / pip. D is valid if both quotes exist; otherwise `invalid_missing_jump_quote` (counted, not
  in the rolling history, never an event).
- **Threshold:** thr(D) = `np.percentile` (linear) of |J| over the 60 valid dates before D (past only); first 60 valid dates burn-in.
  **Event:** valid D past burn-in with |J(D)| > thr(D) strictly.
- **Trade per event:** position sign(J(D)) entered at the 08:45 quote (the same quote that closes the jump; known at that bar's open)
  and exited at the 10:45 NY quote on D (before the London 4pm fix at 11:00 NY). Exclusions, counted, first reason in this order:
  `missing_exit`, `entry_skipped_spread` (ask-bid at 08:45 > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return = sign(J) x (mid 10:45 - mid 08:45) / pip. `vol_state_fix.evaluate`: mean, median, SD, hit
  rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (block 10 events, 2000 draws, seed 0).
- **Decision rule (`release_continuation.decide_b21`, thresholds identical to E022/E024, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** a negative mean (reversal reading) is logged as exploratory only;
  horizons 08:45 -> 09:30 and 08:45 -> 12:00 NY; p80 and p95 thresholds; control = same trade on post-burn-in non-event dates;
  events on first-Friday-of-month dates (NFP proxy from dates alone) and the result on / off them; events on FOMC statement dates
  (data/calendars/fomc_dates.csv; none expected); mean |J| and median threshold of events; share long; by year; by weekday; median
  spreads at entry/exit; net per event at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5
  (gross - 1.5 x (gross - SPEC 4 net)).
- **What follows:**
  - SIGNAL -> queue val confirmation B21v as its own experiment with this rule unchanged and a val-only burn-in (as E023/E025). LEAD
    needs dev SIGNAL + val pass + SPEC 4 and x1.5 net > 0.
  - WEAK or NONE -> B21 closed for this definition; no re-test on dev with other percentiles, windows or horizons. Next: B22.
- **Power note (written before data):** ~1,560 dev dates, ~1,500 post burn-in, ~145-150 events; SE ~1.8-2.1 pips.
- **Calendar label:** US 08:30 NY release window; the hold contains the 10:00 NY releases; exit before the London fix. Events are
  selected by the jump, not by a calendar; no release-date file is used.
- **Code:** `src/fxresearch/release_continuation.py` (reuses `vol_state_fix.ny_quotes`, `evaluate`, `decide_b19`, cost constants);
  `scripts/run_e026_release_continuation.py`; tests `tests/test_release_continuation.py` (constants fixed, threshold and sign,
  invalid dates excluded from the history, spread / missing-exit exclusions, no look-ahead, quotes from bars at 08:30/08:45/10:45,
  random-walk SIGNAL rate <= 0.10 over 40 seeds, strong continuation gives SIGNAL, first-Friday flag). Synthetic smoke run passed (no
  events: burn-in, as expected).
- **Command:** `python scripts/run_e026_release_continuation.py | tee backtests/validation_reports/E026_results.txt` (also writes
  `E026_results.json` and `E026_days.csv`).
- **Trial count:** dev +1 when it runs (233 -> 234); val unchanged at 6; total 239 -> 240.
