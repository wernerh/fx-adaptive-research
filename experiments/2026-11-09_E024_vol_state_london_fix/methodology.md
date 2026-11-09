# E024 Methodology (pre-registered 2026-11-09 R046, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Vol state (identical to E022, `vol_state_fix`):** RNG(P) = full trading-date mid range (17:00 -> 17:00 NY) from 1-minute
  high/low; P valid if >= 90% of 1,440 bars; thr(P) = `np.percentile` (linear) of RNG over the 60 valid dates before P, past only;
  first 60 valid dates burn-in. D is **high-vol** if P (adjacent date in the dev trading-date set) is valid, past burn-in and
  RNG(P) > thr(P) strictly. Other states `prev_invalid`, `burn_in`, `normal`, counted.
- **Quote at hh:mm NY on NY date d:** bid/ask **open** of the first bar in [hh:mm, hh:mm+5) America/New_York
  (`vol_state_fix.ny_quotes`). Missing -> excluded, never filled. No timestamp between 16:30 and 18:30 NY is used (R030 lesson).
- **Trade per high-vol D:** **long** EUR/USD from 11:05 NY to 16:00 NY on calendar date D. Exclusions, counted, first reason in this
  order: `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at 11:05 > 2.0 pips, SPEC 4).
- **Statistic (1 trial):** signed return per tested event = +(mid 16:00 - mid 11:05) / pip. `vol_state_fix.evaluate`: mean, median,
  SD, hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (block 10 events, 2000 draws, seed 0).
- **Decision rule (`vol_state_london.decide_b20`, identical to E022's `decide_b19`, unchanged from the backlog draft):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** the same long on `normal` dates after burn-in (control) and on all
  post-burn-in dates; number of events on scheduled, non-cancelled FOMC statement dates (data/calendars/fomc_dates.csv; the 14:00 NY
  statement is inside the hold) and the result excluding them; by year; by weekday; median daily range; mean prior range and median
  threshold of events; median spreads at entry and exit; net per event at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1
  commission) and costs x1.5 (gross - 1.5 x (gross - SPEC 4 net)). A significant negative mean is logged as exploratory only.
- **What follows:**
  - SIGNAL -> queue val confirmation B20v as its own experiment with this rule unchanged (LEAD needs dev SIGNAL + val pass + SPEC 4
    and x1.5 net > 0, and not explained by FOMC days alone: if the result excluding FOMC days is not positive, this is stated).
  - WEAK or NONE -> B20 closed for this definition; no re-test with other percentiles, windows or vol measures on dev. The
    vol-state-at-fixes line (B19/B20) is then closed; backlog refill next.
- **Power note (written before data):** ~1,560 dev trading dates, ~1,500 post burn-in, ~490 events; SE ~1.1-1.3 pips.
- **Calendar label:** post-London-fix window (WM/R 4pm London = 11:00 NY except in the 2-3 weeks a year when US/UK DST differ, when
  it is 10:00 or 12:00 NY; the window is fixed in NY time and not shifted). Contains the 14:00 NY FOMC statement on statement days and
  the 15:00-16:00 NY CME-related hour; excludes US 08:30 and 10:00 releases.
- **Code:** `src/fxresearch/vol_state_london.py` (window, side, rule, FOMC flag), reusing `vol_state_fix` (E022) with new optional
  `side` / window arguments whose defaults keep E022/E023 behaviour unchanged (test added). `scripts/run_e024_vol_state_london.py`;
  tests `tests/test_vol_state_london.py` (constants fixed, long sign and E022 default unchanged, quotes from bars at 11:05/16:00, no
  look-ahead, random-walk SIGNAL rate <= 0.10 over 40 seeds, strong long effect gives SIGNAL, FOMC flag excludes cancelled
  meetings). Full suite 173 passed. Synthetic smoke run passed (no events: burn-in, as expected).
- **Command:** `python scripts/run_e024_vol_state_london.py | tee backtests/validation_reports/E024_results.txt` (also writes
  `E024_results.json` and `E024_days.csv`).
- **Trial count:** dev +1 when it runs (232 -> 233); val unchanged at 5; total 237 -> 238.
