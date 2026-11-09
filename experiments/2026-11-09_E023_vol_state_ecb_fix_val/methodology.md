# E023 Methodology (pre-registered 2026-11-09 R044, before any run)

Identical to E022 (experiments/2026-11-09_E022_vol_state_ecb_fix/methodology.md) except the block. Only the differences and the
fixed rule are restated here.

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Val block only** (2021-01-21..2023-06-30,
  `splits.DEFAULT_PLAN`, 20-day embargo after dev). `vol_state_fix.restrict_to_block` first drops every bar at or after
  2023-07-01 00:00 UTC (OOS never read), then every bar whose trading date is not `val`, **before** any computation.
- **History:** the rolling 60-valid-date range history is built from val dates only; the first 60 valid val dates are burn-in (no dev
  history is used, so the val result is independent of dev data). Expected ~640 val trading dates, ~580 post burn-in, ~190 events.
- **Definitions, trade, exclusions, statistic:** unchanged from E022 (`vol_state_fix` constants: WINDOW 60, PCTL 67, coverage 90% of
  1,440 bars, strict `>` threshold, P = adjacent date in the val trading-date set, short 02:00 -> 08:15 NY, quote = open of first bar
  in [T, T+5 min), exclusions missing_entry / missing_exit / entry spread > 2.0 pips, block-10 bootstrap 2000 draws seed 0).
- **Decision rule (`vol_state_fix.decide_b19`, unchanged from E022):**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap 95% CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
  - "Val pass" = SIGNAL.
- **LEAD (docs/AUTONOMOUS_PROTOCOL.md), computed in the script:** `lead` = val SIGNAL AND val mean net > 0 at SPEC 4 AND at costs
  x1.5 (`lead_cost_gate`). Condition 4 (not a known calendar effect): the window ends at the ECB fix, which *is* the strategy.
- **Descriptive (not trials, do not change the decision):** as E022: control on normal val dates, all post-burn-in val dates, by year,
  by weekday, median range, mean prior range and median threshold of events, median spreads, net at bid/ask, SPEC 4 and x1.5.
- **What follows:**
  - SIGNAL and cost gate -> LEAD: write agent_logs/LEADS.md, propose the exact OOS command, notify the human, pause this line. No OOS
    run without explicit human approval.
  - SIGNAL without the cost gate, WEAK or NONE -> B19 line closed for this definition; no re-test with other percentiles, windows,
    vol measures or blocks. B20 proceeds independently.
- **Code:** `src/fxresearch/vol_state_fix.py` (`restrict_to_block` added; all other functions unchanged), `scripts/run_e023_vol_state_ecb_val.py`;
  test `tests/test_vol_state_fix.py::test_restrict_to_block_val_only_and_no_later_bars` (only val trading dates kept, nothing at or
  after the cut-off). Synthetic smoke run passed (1 event, NONE; the whole synthetic range is labelled val in the smoke plan).
- **Command:** `python scripts/run_e023_vol_state_ecb_val.py | tee backtests/validation_reports/E023_results.txt` (also writes
  `E023_results.json` and `E023_days.csv`).
- **Trial count:** val +1 when it runs (4 -> 5); dev unchanged at 232; total 236 -> 237.
