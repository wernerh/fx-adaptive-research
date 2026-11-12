# E047 Methodology (pre-registered 2026-11-12 R125, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner), mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every bar whose FX trading date is not `dev` **before** any
  computation; val and OOS untouched. No external download.
- **Day:** UTC calendar date; bars on a UTC Sunday belong to the following Monday's date; Saturday bars dropped (`pivot_touch.day_key`).
- **Levels (exact integers, 2 x mid in 1e-5 units as E018/E045):** from the previous date with bars d-1 (Monday -> Friday):
  H = max(bid_high + ask_high), L = min(bid_low + ask_low), C = bid_close + ask_close of the last bar; P = (H + L + C)/3,
  R1 = 2P - L, S1 = 2P - H, compared as 3 x level = 2H - L + 2C and 2L - H + 2C against 3 x price. d-1 needs >= 1,000 bars,
  else date d is excluded (counted `dates_excluded_prev_bars`).
- **Event (bars t-1 and t on the same date d):** R1 touch c(t-1) < R1 <= h(t) -> s = +1; S1 touch c(t-1) > S1 >= l(t) -> s = -1.
  Only the first touch of each level per date (<= 1 R1 and <= 1 S1 event per date). If the first-touch bar of one level also meets
  the other level's touch condition, that event is skipped (counted `both_touch`; fixed now, before data).
- **Trade (`round_numbers.build_trades`, unchanged E018/E045 code, horizon 120):** entry = open of the first bar at or after t + 1 min
  (<= t + 5 min); exit = open of the first bar at or after entry + 120 min (<= + 5 min); >= 110/120 bars in the window. Skips counted
  under the first failing check in E018 order: entry bar missing (`coverage`), entry NY time in [16:30, 18:30) (`roll`), exit missing /
  coverage (`coverage`), exit in roll (`roll`), entry spread > 2.0 pips (`spread`, SPEC 4), entry before the previous trade's exit
  (`overlap`). Signed = s x (mid open exit - mid open entry), pips.
- **Statistic (1 trial):** `post_jump.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), cluster bootstrap 95% CI
  of the mean resampling **UTC dates** with all their events (2000 draws, seed 0).
- **Decision rule (`pivot_touch.decide_b56` = E045/E043 thresholds, unchanged from the backlog draft):**
  - < 300 events (trades) -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** R1-only and S1-only legs; 60- and 180-minute holds; thesis-faithful bracket
  (target/stop = entry mid +- 0.15% x P in the trade direction, first hit by mid high/low from the entry bar within 24 h; win rate of
  resolved, same-bar double hits and unresolved counted); traditional-direction mean (= minus the rule mean); excluding and only
  2017-06-01 .. 2017-12-29 (thesis sample); by year and events per year (lesson R092); share and mean of events within +-15 min of
  08:30 NY, 10:00 NY and 16:00 London, and outside them; net at bid/ask, SPEC 4 and costs x1.5; control levels R1/S1 shifted by
  +0.0023 and by -0.0023 through the identical procedure (mechanism predicts pivot > control).
- **What follows:** SIGNAL -> B57 val confirmation (own pre-registration, rule unchanged, 1 val trial, < 120 events NONE). Not a LEAD
  until B57 passes and net > 0 at SPEC 4 and costs x1.5 (AUTONOMOUS_PROTOCOL). WEAK or NONE -> B56 closed, B57 closed unearned.
- **Command (research-batch):** `python scripts/run_e047_pivot_touch.py | tee backtests/validation_reports/E047_results.txt`
- **Outputs:** `backtests/validation_reports/E047_results.{json,txt}`, `E047_trades.csv`.
- **Tests:** `tests/test_pivot_touch.py` (day key, exact levels, touch definition, near miss, first touch only, both-touch skip,
  previous-date bar floor, no look-ahead, control shift, trade sign, decision rule, no SIGNAL on random walks).
