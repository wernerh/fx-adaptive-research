# E033 Methodology (pre-registered 2026-11-10 R069, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask with the `volume` field, mid derived. **Dev block only**
  (2015-01-01..2020-12-31, `splits.DEFAULT_PLAN`): bars whose trading date is not `dev` are dropped **before** any computation.
  Val and OOS untouched.
- **Volume gate (first, fixed now):** if `volume` is missing, or zero/NaN on > 1% of dev bars (`volume_reversal.volume_gate`), the
  experiment stops as **BLOCKED** with 0 trials used; nothing else is computed and B28/B29 become `blocked`.
- **Dates:** trading date D (17:00 NY roll, SPEC 2). D is **valid** if >= 1,300 of its 1,440 one-minute bars exist.
- **Volume signal:** V(D) = sum of `volume` over D's bars. UV(D) = V(D) / mean(V over the previous 21 valid dates) - 1 (past only).
  Bands: p33 and p67 = `np.percentile` (linear) of UV over the previous 60 valid dates that have a UV (past only).
  **Low** (B28): UV(D) < p33 (strict). **High** (B29): UV(D) > p67 (strict). Mid tercile = the rest (descriptive only).
  Burn-in: 21 valid dates, then 60 UV values. Low-coverage dates never enter any history.
- **Move:** R(D) = (mid 16:55 NY on D - mid at the open of D) / pip. Open = bid/ask OPEN of the first bar in [17:00, 17:05) NY of
  trading date D; 16:55 = first bar in [16:55, 17:00) NY on calendar date D. Missing -> `missing_signal_quote` (not an event).
- **Trade:** B28 position -sign(R(D)); B29 position +sign(R(D)). Entry 20:00 NY on calendar date D (first bar in [20:00, 20:05),
  start of trading date D+1, after the roll spread normalises, lesson R059); exit 16:55 NY on calendar date D+1.
  Signed return = position x (mid exit - mid entry) / pip.
- **Exclusions, counted per arm, first reason in this order:** `missing_signal_quote`, `friday_excluded` (D is a Friday; weekend gap
  belongs to B17), `zero_move` (R = 0), `missing_entry`, `missing_exit`, `entry_skipped_spread` (ask-bid at 20:00 NY > 2.0 pips).
- **Statistic (2 trials):** `vol_state_fix.evaluate`: mean, median, SD, hit rate, one-sided t-test (H1 mean > 0), moving-block
  bootstrap 95% CI of the mean (block 10 events, 2000 draws, seed 0).
- **Decision rule (`volume_reversal.decide_b28` = `decide_b29`, unchanged from the backlog draft):** applied to each arm separately.
  - < 150 tested events -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.025 (Bonferroni for 2 trials).
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.025), but not SIGNAL.
  - **NONE** otherwise.
- **Null calibration (code tests, written before data):** i.i.d. t(4) samples of 380: SIGNAL rate <= 5% over 200 draws; random daily
  volumes with random-walk prices (1,500 dates, 3 seeds): neither arm ever SIGNAL; past-only UV/bands (a future volume change
  leaves earlier flags unchanged); bars after 16:59 NY on D do not change D's volume, UV or R.
- **Descriptive (not trials, do not change any decision):** mid-tercile and high-tercile reversal means, low-tercile continuation;
  share of events that are E021-type large-move days (`daily_reversal.mark_events` on the same dev bars) and each arm excluding
  them; correlation of UV with the daily range and with |R|; mean |R| per arm; all-banded-date reversal control; by year;
  entry/exit spreads; net per event at bid/ask, SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5.
- **What follows:**
  - SIGNAL in an arm -> that arm earns its val confirmation (B28v / B29v) as its own pre-registered experiment. Not a LEAD yet.
  - WEAK or NONE -> that arm is closed; no re-test with other percentiles, windows, holds or volume definitions.
  - BLOCKED -> 0 trials; B28/B29 `blocked` (volume field unusable).
- **Calendar label:** daily-frequency volume-conditioned reversal/continuation; the hold contains Tokyo/ECB/London fixes and US releases.
- **Code:** `src/fxresearch/volume_reversal.py`; `scripts/run_e033_volume_reversal.py`; tests `tests/test_volume_reversal.py`.
  Synthetic smoke run passed (65 synthetic dates < 81-date burn-in -> no events -> NONE/NONE; gate ok).
- **Command:** `python scripts/run_e033_volume_reversal.py | tee backtests/validation_reports/E033_results.txt` (also writes
  `E033_results.json` and `E033_days.csv`).
