# E022 Methodology (pre-registered 2026-11-09 R042, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Trading dates:** the sorted set of `sessions.trading_date` values present in the dev bars (17:00 NY roll).
- **Prior-day range:** RNG(P) = (max mid high - min mid low) / pip over all 1-minute bars of trading date P (17:00 -> 17:00 NY);
  mid high = (bid_high + ask_high) / 2, mid low = (bid_low + ask_low) / 2. P is **valid** if it has >= 90% of 1,440 expected bars
  (>= 1,296); otherwise `low_coverage`, counted, and left out of the rolling history.
- **Threshold:** for valid P, thr(P) = `np.percentile(RNG of the 60 valid dates before P, 67)` (numpy default linear interpolation,
  past only). The first 60 valid dates are burn-in.
- **Event:** D (each trading date after the first) is **high-vol** if P = the trading date immediately before D in the set is valid,
  past burn-in, and RNG(P) > thr(P) (strictly greater). Otherwise its state is `prev_invalid`, `burn_in` or `normal` (counted).
- **Quote at hh:mm NY on NY date d:** bid/ask **open** of the first bar in [hh:mm, hh:mm+5) America/New_York
  (`vol_state_fix.ny_quotes`). Missing -> excluded, never filled. No timestamp between 16:30 and 18:30 NY is used (R030 lesson).
- **Trade per high-vol D:** short EUR/USD from 02:00 NY to 08:15 NY on calendar date D. Exclusions, counted, first reason in this
  order: `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at 02:00 > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return per tested event = -(mid 08:15 - mid 02:00) / pip. `vol_state_fix.evaluate`: mean, median,
  SD, hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (block 10 events, 2000 draws, seed 0).
- **Decision rule (`vol_state_fix.decide_b19`), unchanged from the backlog draft:**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** the same short on `normal` dates after burn-in (control) and on all
  post-burn-in dates; by year; by weekday; median daily range; mean prior range and median threshold of events; median spreads at
  entry and exit; net per event at bid/ask (half spread at entry and at exit), SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission)
  and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)). Limitation stated: ECB monetary-policy days are not identifiable (no ECB
  calendar in repo). A significant negative mean (EUR up before the fix) is logged as exploratory only.
- **What follows:**
  - SIGNAL -> queue val confirmation B19v as its own experiment with this rule unchanged (LEAD needs dev SIGNAL + val pass + SPEC 4
    and x1.5 net > 0).
  - WEAK or NONE -> B19 closed for this definition; no re-test with other percentiles, windows or vol measures on dev. B20 proceeds
    independently (fixed in R041).
- **Power note (written before data):** ~1,560 dev trading dates, ~1,500 post burn-in, ~490 events; SE ~1.2-1.4 pips.
- **Calendar label:** pre-ECB-fix window (ECB reference rate 14:15 CET ~ 08:15 NY, ~ 09:15 NY in the 2-3 weeks a year when US/EU DST
  differ; the exit is fixed at 08:15 NY and not shifted). Exit precedes US 08:30 releases. Contains the Frankfurt/London opens.
- **Implementation choices fixed now:** vol measure is the full trading-date mid range from 1-minute high/low (not ATR, not close-to-
  close); coverage 90% of 1,440 bars; P = adjacent date in the dev trading-date set (a holiday gap is not excluded).
- **Code:** `src/fxresearch/vol_state_fix.py`, `scripts/run_e022_vol_state_ecb.py`; tests `tests/test_vol_state_fix.py` (constants
  fixed, past-only strict threshold and event on the next date, invalid prior date excluded from history, no look-ahead, spread skip,
  missing quote counted, cost ordering, ranges/quotes from bars, low-coverage day invalid, random-walk SIGNAL rate <= 0.10 over 40
  seeds, strong effect gives SIGNAL, rule edges). Synthetic smoke run passed (no events: 43 burn-in dates < 60, as expected).
- **Command:** `python scripts/run_e022_vol_state_ecb.py | tee backtests/validation_reports/E022_results.txt` (also writes
  `E022_results.json` and `E022_days.csv`).
- **Trial count:** dev +1 when it runs (231 -> 232); val unchanged at 4; total 235 -> 236.
