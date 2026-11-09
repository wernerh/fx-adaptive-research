# E027 Methodology (pre-registered 2026-11-09 R053, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Clock:** Europe/London local time for every quote, so US/UK DST mismatch weeks do not shift the windows.
- **Dates:** sorted trading-date set of the dev bars (17:00 NY roll); 08:00-16:00 London lies inside one trading date, so the London
  calendar date equals the trading date.
- **Quote at hh:mm London on date d:** bid/ask **open** of the first bar in [hh:mm, hh:mm+5) Europe/London
  (`london_momentum.london_quotes`). Missing -> excluded, never filled.
- **Signal:** r1(D) = (mid 08:30 - mid 08:00 London) / pip. No threshold: every valid date is an event.
- **Trade per date:** position sign(r1(D)) entered at the 15:25 London quote, exited at the 15:55 London quote (before the 16:00 fix
  window). Exclusions, counted, first reason in this order: `invalid_missing_signal_quote` (08:00 or 08:30 missing), `zero_signal`
  (r1 = 0, no trade), `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at 15:25 > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return = sign(r1) x (mid 15:55 - mid 15:25) / pip. `london_momentum.evaluate_b22`: mean, median,
  SD, hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (**block 20 events**, 2000 draws, seed 0).
- **Decision rule (`london_momentum.decide_b22`, thresholds identical to E022/E024/E026, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** negative mean (reversal reading) logged as exploratory only; first-hour
  signal variant (sign of 08:00 -> 09:00 London, same hold); OLS slope of the unsigned 15:25-15:55 return on r1; |r1| terciles;
  month-end dates (last trading date of the month, `fixes.month_end_flag`, cf. E007/B8) vs others; DST-mismatch dates (London-NY
  offset 4 h at 15:25 London, i.e. hold 11:25-11:55 NY instead of 10:25-10:55 NY; count and result); share long; unconditional
  last-half-hour mean; by year; by weekday; median spreads; net per date at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1
  commission) and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)).
- **What follows:**
  - SIGNAL -> queue val confirmation B22v as its own experiment with this rule unchanged. LEAD needs dev SIGNAL + val pass + SPEC 4
    and x1.5 net > 0.
  - WEAK or NONE -> B22 closed for this definition; no re-test on dev with other windows, horizons or the first-hour variant.
    Next: backlog refill (no other `ready` item).
- **Power note (written before data):** ~1,560 dev dates, ~1,500 tested; 30-min SD ~6-8 pips -> SE ~0.2 pips; the 1.0-pip mean is
  the binding condition.
- **Calendar label:** London open -> pre-London-fix half hour; the hold is 10:25-10:55 NY normally (after the 10:00 NY releases),
  11:25-11:55 NY in DST-mismatch weeks.
- **Code:** `src/fxresearch/london_momentum.py`; `scripts/run_e027_london_momentum.py`; tests `tests/test_london_momentum.py`
  (constants fixed, sign/return, exclusion order, side independent of later prices, quotes from bars at London 08:00/08:30/15:25/15:55,
  DST-mismatch flag, random-walk SIGNAL rate <= 0.10 over 40 seeds, strong momentum -> SIGNAL and significant sub-pip -> WEAK,
  month-end flag and slope). Synthetic smoke run passed.
- **Command:** `python scripts/run_e027_london_momentum.py | tee backtests/validation_reports/E027_results.txt` (also writes
  `E027_results.json` and `E027_days.csv`).
- **Trial count:** dev +1 when it runs (234 -> 235); val unchanged at 6; total 240 -> 241.
