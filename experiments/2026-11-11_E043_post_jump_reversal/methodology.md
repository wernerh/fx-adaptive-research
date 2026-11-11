# E043 Methodology (pre-registered 2026-11-11 R097, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask (repo pipeline, cached on the runner), mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any
  computation; val and OOS untouched. No external download.
- **Grid:** 5-minute slots on the NY clock (UTC floor to 5 min; NY offsets are whole hours) over trading time: every slot not in the
  weekend closure (`sessions.is_weekend_bar`, Fri 17:00 -> Sun 17:00 NY). Holidays stay on the grid with missing quotes.
  Quote at slot T = bid/ask open of the first 1-minute bar in [T, T+5 min); missing -> NaN, never filled.
- **Returns:** r_t = ln mid(t+5) - ln mid(t), t+5 in clock time; weekend slot or missing quote -> missing.
- **Jump test (Lee-Mykland 2008, no periodicity filter):** sigma_t^2 = mean of |r_j||r_{j-1}| over j = t-268 .. t-1 with both
  returns valid (= (1/(K-2)) x sum when all valid; K = 270; r_t excluded, past only). Test only if >= 90% of the previous 269 grid
  returns are valid and sigma > 0. Jump if |r_t / sigma_t| > 5.395 (n 288, alpha 0.01; `post_jump.lm_threshold`) AND
  |mid(t+5) - mid(t)| >= 0.0005.
- **Trade:** s = -sign(r_t). Entry at the slot quote of t+10 min, exit at t+70 min (60-minute hold). Signed = s x (mid exit - mid
  entry) / pip.
- **Exclusions (counted, first reason in this order):** `roll_hour` (jump slot NY time in [16:55, 17:55)); `week_open` (slot before
  first valid quote after the weekend gap + 60 min); `inside_hold` (slot before the exit time of the previous **tested** event; only
  tested events block, excluded jumps do not); `missing_entry`; `missing_exit`; `entry_skipped_spread` (ask - bid at entry > 2.0
  pips, SPEC 4).
- **Statistic (1 trial):** `post_jump.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), **date-cluster
  bootstrap** 95% percentile CI of the mean (resample trading dates of the jump slot with all their events, 2000 draws, seed 0).
- **Decision rule (`decide_b48`, unchanged from the backlog draft):**
  - < 300 tested events -> **NONE**.
  - **SIGNAL** if mean > 1.0 pip AND bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** continuation mean (opposite sign, reported only); positive vs negative
  jumps; jumps starting 08:25-08:50 NY (US-release proxy) vs rest and its share; 02:00-04:00 NY vs rest; by year (lesson R092); |L|
  terciles; skipped bar t+5 -> t+10 signed mean; events by NY hour; net at bid/ask, SPEC 4 and costs x1.5; exclusion counts.
- **Implementation choices fixed now, before data:** half-open roll window [16:55, 17:55); week open = first valid quote after a
  weekend gap in the grid; sigma uses the mean of valid adjacent products (handles missing returns); only tested events block later
  jumps.
- **What follows:** SIGNAL -> B49 val confirmation (own pre-registration, rule unchanged, 1 val trial, < 120 events NONE). Not a
  LEAD until val passes and SPEC 4 and x1.5 net > 0, and not explained by the 08:30 release window alone. WEAK or NONE -> B48
  closed, B49 closed unearned; no re-test with other thresholds, holds, K or the opposite sign.
- **Power note (written before data):** expected ~500-1500 events; 60-min SD after a jump perhaps 10-15 pips -> SE ~0.4-0.7 pip.
- **Code:** `src/fxresearch/post_jump.py`; `scripts/run_e043_post_jump.py`; tests `tests/test_post_jump.py` (constants and
  threshold 5.395, weekend-free grid and first-bar quote, sigma past only, 5-pip floor and burn-in, entry t+10 / exit t+70 / fade
  sign / skipped bar, exclusions roll/hold/spread/missing exit, week-open exclusion, date-cluster bootstrap, decision rule,
  injected reversal -> SIGNAL and injected continuation -> NONE, pure jumps on random walk -> no SIGNAL). Synthetic smoke run
  passed (NONE, 1 event).
- **Command (batch.sh):** `python scripts/run_e043_post_jump.py | tee backtests/validation_reports/E043_results.txt` (also
  writes `E043_results.json` and `E043_events.csv`).
- **Trial count:** dev +1 when it runs (252 -> 253); val unchanged at 9; total 261 -> 262.
