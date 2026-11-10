# E036 Methodology (pre-registered 2026-11-10 R077, before any run)

Identical to E035 arm B33 (experiments/2026-11-10_E035_overnight_reversal/methodology.md) except the block and the alpha for one
trial; block handling identical to E023/E025. Only the differences and the fixed rule are restated here.

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only** (2021-01-21..2023-06-30,
  `splits.DEFAULT_PLAN`, 20-day embargo after dev). `vol_state_fix.restrict_to_block` first drops every bar at or after
  2023-07-01 00:00 UTC (OOS never read), then every bar whose trading date is not `val`, **before** any computation.
- **History:** O20 is built from val dates only; the first 20 val dates with a valid r_on are burn-in (no dev history used).
  Expected ~637 val trading dates, ~610 tested.
- **Definitions, trade, exclusions, statistic:** unchanged from E035 B33 (`overnight_reversal` OPEN 17:05, ENTRY 07:00, EXIT 16:55 NY;
  quote = open of first bar in [T, T+5 min); exclusions missing_signal / zero_signal / missing_entry / missing_exit / entry spread
  > 2.0 pips; `evaluate_b32`: one-sided t, moving-block bootstrap block 20 dates, 2000 draws, seed 0).
- **Decision rule (`overnight_reversal.decide_b34`, E035 rule with alpha 0.05 for 1 trial, as fixed in backlog B34 R074/R076):**
  - < 500 tested dates -> **NONE** (insufficient sample).
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap 95% CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise. "Val pass" = SIGNAL.
- **LEAD (docs/AUTONOMOUS_PROTOCOL.md), computed in the script:** `lead` = val SIGNAL AND val mean net > 0 at SPEC 4 AND at costs x1.5
  (`lead_cost_gate`, as E023/E025). Known-calendar check (must be stated in any LEAD write-up): results excluding FOMC statement days
  (data/calendars/fomc_dates.csv) and excluding the last trading date of each month are reported; the hold contains the 08:30 NY
  releases, 10:00 NY option cut and the London 4pm fix every day, so those are not separable by date exclusion and are listed as a risk.
- **Descriptive (not trials, do not change the decision):** |O20| terciles; long vs short days; share long; unconditional long r_id;
  Mondays vs Tue-Fri; SD of r_on and r_id; by year; the B32 daily arm on val (NOT a trial, B32 closed on dev); median spreads; net at
  bid/ask, SPEC 4 and x1.5.
- **What follows:**
  - SIGNAL and cost gate -> LEAD: write agent_logs/LEADS.md, propose the exact OOS command, notify the human, pause this line. No OOS
    run without explicit human approval.
  - SIGNAL without the cost gate, WEAK or NONE -> B33/B34 line closed; no re-test with other smoothing lengths, windows or blocks.
    Next: backlog refill (no other `ready` item).
- **Code:** `src/fxresearch/overnight_reversal.py` (`ALPHA_VAL`, `decide_b34` added; E035 functions unchanged);
  `scripts/run_e036_overnight_reversal_val.py`; tests in `tests/test_overnight_reversal.py` (B34 thresholds and that the E035 rule
  is untouched, random-walk SIGNAL rate <= 0.10 over 60 seeds at n 620, val restriction with burn-in inside val). Synthetic smoke run
  passed (44 dates, NONE; whole synthetic range labelled val in the smoke plan).
- **Command:** `python scripts/run_e036_overnight_reversal_val.py | tee backtests/validation_reports/E036_results.txt` (also writes
  `E036_results.json` and `E036_days.csv`).
- **Trial count:** val +1 when it runs (8 -> 9); dev unchanged at 244; total 252 -> 253.
