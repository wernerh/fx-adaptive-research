# E045 Methodology (pre-registered 2026-11-11 R103, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner), mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any
  computation; val and OOS untouched. No external download.
- **Prices:** exact integer units of 2 x mid in 1e-5 (E018 `_to_units`): close c(t) = bid_close + ask_close, high
  h(t) = bid_high + ask_high, low l(t) = bid_low + ask_low. Levels L = k x 0.0050 (00 and 50); control levels L + 0.0023 (23/73).
- **Event (bar t, bars t-1 and t in the same trading date, `sessions.trading_date`):** up-touch c(t-1) < L, h(t) >= L, c(t) < L;
  down-touch c(t-1) > L, l(t) <= L, c(t) > L. If one bar touches several levels (either side), the level nearest c(t) counts (exact
  tie -> the up-touch level; fixed now, before data). Only the first touch event of each level per trading date counts; a level
  already crossed by close (E018 crossing, c(t'-1) < L <= c(t') or c(t'-1) > L >= c(t'), every level a bar crosses) at an earlier
  bar of the same trading date is not eligible. Position s = -1 after an up-touch, +1 after a down-touch.
- **Trade (`round_numbers.build_trades`, unchanged E018 code):** entry = open of the first bar at or after t + 1 min (<= t + 5 min);
  exit = open of the first bar at or after entry + 60 min (<= + 5 min); >= 55/60 bars in the window. Skips counted under the first
  failing check in E018 order: entry bar missing (`coverage`), entry NY time in [16:30, 18:30) (`roll`), exit missing / window
  coverage (`coverage`), exit in roll (`roll`), entry spread > 2.0 pips (`spread`, SPEC 4), entry before the previous trade's exit
  (`overlap`). Signed = s x (mid open exit - mid open entry), pips.
- **Statistic (1 trial):** `post_jump.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), date-cluster bootstrap
  95% CI of the mean (resample trading dates with all their events, 2000 draws, seed 0).
- **Decision rule (`round_touch.decide_b52` = E043 thresholds, unchanged from the backlog draft):**
  - < 300 events -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** control levels (23/73) through the identical procedure and the
  round-minus-control difference (mechanism predicts round > control); 15- and 120-minute horizons; up- vs down-touches; share of
  events whose level is crossed by mid close on a bar in [entry, exit) and results within crossed / not crossed (post-hoc split,
  reported only); opposite-sign (continuation) mean, reported only; by year (lesson R092); events per year; median entry spread;
  net at bid/ask, SPEC 4 and costs x1.5; events within +-15 min of 08:30, 10:00 and 11:00 NY (share and mean) and outside them.
- **What follows:** SIGNAL -> B53 val confirmation (own pre-registration, rule unchanged, 1 val trial, < 120 events NONE). Not a LEAD
  until val passes and SPEC 4 and x1.5 net > 0. WEAK or NONE -> B52 closed, B53 closed unearned; no re-test with other level grids,
  touch definitions, horizons or the opposite sign.
- **Power note (written before data):** ~1-2 events per trading date (~1,500-3,000 on dev); 60-min SD ~10-12 pips -> SE ~0.3 pips;
  the 1-pip bar binds, not the CI.
- **Code:** `src/fxresearch/round_touch.py`; `scripts/run_e045_round_touch.py`; tests `tests/test_round_touch.py` (constants;
  up/down touch; near miss and close-on-level are not touches; first touch only; earlier crossing makes the level ineligible but an
  earlier touch counts; nearest level on a two-sided bar; no event across the 17:00 NY roll; control levels; fade sign and no
  look-ahead (truncating or changing bars after t leaves the event unchanged); crossed-within-hold; decision rule; pooled random walk
  -> |mean| < 1.5 and no SIGNAL). Synthetic smoke run passed (NONE, 14 trades).
- **Command (batch.sh):** `python scripts/run_e045_round_touch.py | tee backtests/validation_reports/E045_results.txt` (also writes
  `E045_results.json` and `E045_trades.csv`).
- **Trial count:** dev +1 when it runs (254 -> 255); val unchanged at 9; total 263 -> 264.
