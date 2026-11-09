# E025 Methodology (pre-registered 2026-11-09 R048, before any run)

Identical to E024 (experiments/2026-11-09_E024_vol_state_london_fix/methodology.md) except the block, and the block handling is
identical to E023. Only the differences and the fixed rule are restated here.

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only** (2021-01-21..2023-06-30,
  `splits.DEFAULT_PLAN`, 20-day embargo after dev). `vol_state_fix.restrict_to_block` first drops every bar at or after
  2023-07-01 00:00 UTC (OOS never read), then every bar whose trading date is not `val`, **before** any computation.
- **History:** the rolling 60-valid-date range history is built from val dates only; the first 60 valid val dates are burn-in (no dev
  history used). Expected ~637 val trading dates, ~577 post burn-in, ~200 events.
- **Definitions, trade, exclusions, statistic:** unchanged from E024 (`vol_state_fix` constants WINDOW 60, PCTL 67, coverage 90% of
  1,440 bars, strict `>` threshold, P = adjacent date in the val trading-date set; `vol_state_london` ENTRY 11:05 NY, EXIT 16:00 NY,
  SIDE long; quote = open of first bar in [T, T+5 min); exclusions missing_entry / missing_exit / entry spread > 2.0 pips; block-10
  bootstrap 2000 draws seed 0).
- **Decision rule (`vol_state_london.decide_b20`, unchanged from E024):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap 95% CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
  - "Val pass" = SIGNAL.
- **LEAD (docs/AUTONOMOUS_PROTOCOL.md), computed in the script:** `lead` = val SIGNAL AND val mean net > 0 at SPEC 4 AND at costs
  x1.5 (`lead_cost_gate`, as E023). The result excluding FOMC statement days (data/calendars/fomc_dates.csv) is reported and must be
  stated in any LEAD write-up (known-calendar-effect check).
- **Descriptive (not trials, do not change the decision):** as E024: control on normal val dates, all post-burn-in val dates, FOMC-day
  events and excl FOMC, by year, by weekday, median range, mean prior range and median threshold of events, median spreads, net at
  bid/ask, SPEC 4 and x1.5.
- **What follows:**
  - SIGNAL and cost gate -> LEAD: write agent_logs/LEADS.md, propose the exact OOS command, notify the human, pause this line. No OOS
    run without explicit human approval.
  - SIGNAL without the cost gate, WEAK or NONE -> B20 line closed for this definition; no re-test with other percentiles, windows,
    vol measures or blocks.
- **Code:** `scripts/run_e025_vol_state_london_val.py` (E024 script with E023's val restriction and lead gate; no library change);
  test `tests/test_vol_state_london.py::test_e025_val_restriction_feeds_b20_frame_with_val_dates_only`. Synthetic smoke run passed
  (1 event, NONE; whole synthetic range labelled val in the smoke plan).
- **Command:** `python scripts/run_e025_vol_state_london_val.py | tee backtests/validation_reports/E025_results.txt` (also writes
  `E025_results.json` and `E025_days.csv`).
- **Trial count:** val +1 when it runs (5 -> 6); dev unchanged at 233; total 238 -> 239.
