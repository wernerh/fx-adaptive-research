# E035 Methodology (pre-registered 2026-11-10 R075, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Clock:** America/New_York local time for every quote. Trading date D = 17:00 NY roll (SPEC 2, `sessions.trading_date`).
- **Quotes:** bid/ask **open** of the first 1-minute bar in [T, T+5 min) (E011 rule); missing -> excluded, never filled.
  - Open of D: first bar in [17:05, 17:10) NY whose trading date is D, i.e. the evening that opens D (Sunday evening for Mondays)
    (`overnight_reversal.evening_quotes`).
  - 07:00 and 16:55: first bar in [07:00, 07:05) / [16:55, 17:00) NY on NY calendar date D (`vol_state_fix.ny_quotes`). 16:55 avoids
    the 17:00 roll (lesson R059).
- **Returns:** r_on(D) = (mid 07:00 - mid 17:05 open) / pip; r_id(D) = (mid 16:55 - mid 07:00) / pip.
- **Signals (fixed in backlog R074):**
  - B32: position -sign(r_on(D)).
  - B33: position -sign(O20(D)), O20(D) = sum of r_on over the 20 previous dates with a valid r_on (strictly before D; missing r_on
    dates are skipped and the window reaches further back). The first 20 dev dates with a valid r_on are burn-in (counted, no B33 trade).
- **Trade per date (both arms):** enter at the 07:00 NY quote, exit at 16:55 NY on D. Signed return = position x r_id(D).
  Exclusions per arm, counted, first reason in this order: `missing_signal` (B32: 17:05 or 07:00 quote missing; B33: burn-in),
  `zero_signal`, `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at 07:00 > 2.0 pips, SPEC 4). Because the 07:00
  quote is both the end of r_on and the B32 entry, a missing 07:00 is counted as `missing_signal` for B32.
- **Statistic (2 trials):** `overnight_reversal.evaluate_b32`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block
  bootstrap 95% CI of the mean (**block 20 dates**, 2000 draws, seed 0).
- **Decision rule (`decide_b32`, same for B33, unchanged from the backlog draft):**
  - < 500 tested dates -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.025 (Bonferroni for 2 trials).
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.025), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** continuation reading (negative mean) logged as exploratory only; OLS
  slope of r_id on r_on; |r_on| terciles (B32) and |O20| terciles (B33); Mondays vs Tue-Fri; share long; SD of r_on and r_id;
  unconditional long r_id (KMW intraday direction, descriptive only); share of dates where B32 and B33 take the same side; by year;
  median spreads; net per date at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5
  (gross - 1.5 x (gross - SPEC 4 net)).
- **What follows:**
  - SIGNAL in either arm -> B34 (val confirmation of that arm, own experiment and pre-registration, rule unchanged). Not a LEAD until
    val passes and SPEC 4 and x1.5 net > 0.
  - WEAK or NONE in both -> B32 and B33 closed; B34 closed unearned; no re-test on dev with other windows or smoothing lengths.
    Next: backlog refill (no other `ready` item).
- **Power note (written before data):** ~1,550 dev dates; 07:00 -> 16:55 NY SD likely ~45 pips -> SE ~1.2 pips (block bootstrap may
  widen it); the p < 0.025 bar binds near +2.4 pips.
- **Calendar label:** the hold contains the 08:30 NY releases, the 10:00 NY option cut and the 16:00 London fix (11:00 NY, 10:00 NY in
  DST-mismatch weeks); not a fix strategy.
- **Code:** `src/fxresearch/overnight_reversal.py`; `scripts/run_e035_overnight_reversal.py`; tests `tests/test_overnight_reversal.py`
  (constants fixed, B32 fade sign/return, O20 past-only with missing values skipped, B33 burn-in and side, exclusion order, side
  independent of later prices, quotes from bars at NY 17:05 (previous evening) / 07:00 / 16:55, random-walk SIGNAL rate <= 0.05 over
  80 arm-seeds, strong reversal -> SIGNAL and < 500 dates -> NONE, cost columns). Synthetic smoke run passed.
- **Command:** `python scripts/run_e035_overnight_reversal.py | tee backtests/validation_reports/E035_results.txt` (also writes
  `E035_results.json` and `E035_days.csv`).
- **Trial count:** dev +2 when it runs (242 -> 244); val unchanged at 8; total 250 -> 252.
