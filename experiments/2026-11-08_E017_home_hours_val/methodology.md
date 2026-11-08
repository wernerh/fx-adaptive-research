# E017 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only** (2021-01-21..2023-06-30, `splits.DEFAULT_PLAN`).
  Dev and OOS are not evaluated.
- **Unit:** FX trading date (17:00 NY roll, `sessions.trading_date`). Both windows lie inside one trading date.
  - `eu` leg: NY clock hours 03:00-08:00 (bars with NY hour 3..7, DST-aware), direction short.
  - `us` leg: NY clock hours 12:00-17:00 (NY hour 12..16), direction long. Exit at 16:59 bar close, next to the 17:00 roll.
  - Leg mid return = mid close of last bar minus mid open of first bar, pips. A leg needs >= 275 of 300 bars (E009/E012 55-of-60 share);
    a date is used only if **both** legs pass. Dropped val dates are counted and reported.
- **Statistic (1 trial):** daily signed = -eu + us. `predictive.evaluate_predictor` with a constant +1 signal: hit rate (Wilson CI),
  binomial p vs 0.5, moving-block bootstrap 95% CI of the mean (block 20, 2000 draws, seed 0).
- **Decision rule (B1 rule, `fixes.decide(res, n_trials=1)`):**
  - **SIGNAL** if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** each leg's signed mean, hit rate, CI; median entry and exit spreads per leg
  (03:00, 07:59, 12:00, 16:59 NY); share of entries with spread > 2.0 pips (SPEC 4 max, not applied as a filter); net at bid/ask
  (short leg sells bid open / buys ask close; long leg buys ask open / sells bid close); SPEC 4 net = bid/ask net minus 2 x (0.1 slippage
  + 0.1 commission); costs x1.5 = gross - 1.5 x (gross - SPEC 4 net); SPEC 4 net hit rate.
- **What follows:**
  - SIGNAL with SPEC 4 net > 0 and costs x1.5 net > 0 -> candidate for a human OOS decision, logged in agent_decision_log.md; **not a
    LEAD**, no notification (dev unusable). Any further dev-free test would need fresh data.
  - SIGNAL failing the cost gate -> "mid drift, not tradable"; closed.
  - WEAK or NONE -> hypothesis rejected for these windows; no re-test with other hours on val.
- **Code:** `src/fxresearch/home_hours.py`, `scripts/run_e017_home_hours.py`; tests `tests/test_home_hours.py` (legs fixed, DST-aware
  NY windows, signed = -eu + us, manual mid match, net = mid - 2 spreads - SPEC 4, coverage drop, random-walk no-SIGNAL).
- **Command:** `python scripts/run_e017_home_hours.py | tee backtests/validation_reports/E017_results.txt`
- **Trial count:** dev unchanged at 227; val trials +1 when it runs (3 -> 4); total 230 -> 231.
