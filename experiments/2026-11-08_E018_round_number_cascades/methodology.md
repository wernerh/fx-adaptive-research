# E018 Methodology (pre-registered before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS are not
  touched.
- **Price for level crossings:** mid close of bar t, held as the integer bid_close + ask_close in 1e-5 units (exact level arithmetic).
- **Levels:** L = k x 0.0050 (00 and 50). **Up-crossing** at bar t: mid(t-1) < L <= mid(t). **Down-crossing:** mid(t-1) > L >= mid(t).
  Bars t-1 and t must share a trading date (17:00 NY roll, `sessions.trading_date`), so weekend gaps never create events. If one bar
  crosses several levels, the level nearest mid(t) is the event level.
- **Events:** only the **first** crossing (either direction) of each level per trading date.
- **Trade per event:** entry at the open of the first bar at or after t + 1 min (SPEC 4 fill rule), at most 5 minutes later; exit at
  the open of the first bar at or after entry + 60 min, at most 5 minutes later; the window [entry, entry + 60 min) needs >= 55 bars.
- **Exclusions (counted and reported), first failing check in this order:** entry bar missing (coverage); entry NY time in
  [16:30, 18:30) (roll); exit bar missing or < 55 bars (coverage); exit NY time in [16:30, 18:30) (roll); entry spread
  (ask_open - bid_open) > 2.0 pips (SPEC 4, spread); entry before the previous trade's exit (overlap, SPEC 4 no overlapping trades).
  Skipped events open no trade.
- **Statistic (1 trial):** signed = direction x (mid open at exit - mid open at entry), pips, one value per trade.
  `predictive.evaluate_predictor(direction, return)`: hit rate (Wilson CI), binomial p vs 0.5, moving-block bootstrap 95% CI of the mean
  (block 20 events, 2000 draws, seed 0).
- **Decision rule (B1 rule, `fixes.decide(res, n_trials=1)`), unchanged from the backlog draft:**
  - **SIGNAL** if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or binomial p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** control levels offset by 23 pips (ending 23/73) through the identical
  procedure, and round minus control mean; 15- and 120-minute horizons on the same trades (NaN if that exit fails coverage; no roll rule
  applied); by year; by crossing direction; median entry/exit spread; net at bid/ask (long buys ask open, sells bid open; short the
  reverse); SPEC 4 net = bid/ask net - 0.1 slippage - 0.1 commission; costs x1.5 = gross - 1.5 x (gross - SPEC 4 net); share of events
  within +-15 min of 08:30, 10:00 and 11:00 NY. A significant **negative** mean (reversal, the take-profit reading) is logged as
  exploratory only and needs its own pre-registration.
- **What follows:**
  - SIGNAL -> queue val confirmation B15v as its own experiment with this rule unchanged (LEAD needs dev SIGNAL + val pass + SPEC 4 and
    x1.5 net > 0). Report the dev cost check now; a SIGNAL that fails the cost gate on dev is still confirmed on val only if SPEC 4 net > 0.
  - WEAK or NONE -> B15 closed for this definition; no re-test with other horizons, offsets or level steps on dev.
- **Code:** `src/fxresearch/round_numbers.py`, `scripts/run_e018_round_numbers.py`; tests `tests/test_round_numbers.py` (constants
  fixed, up/down crossing definitions, touch from above, first crossing per level per trading date incl. roll reset, multi-level jump,
  control levels, entry/exit timing and signed return, roll/spread/overlap/coverage exclusions, no look-ahead, random walk no SIGNAL).
- **Command:** `python scripts/run_e018_round_numbers.py | tee backtests/validation_reports/E018_results.txt` (also writes
  `E018_results.json` and `E018_trades.csv`).
- **Trial count:** dev +1 when it runs (227 -> 228); val unchanged at 4; total 231 -> 232.
