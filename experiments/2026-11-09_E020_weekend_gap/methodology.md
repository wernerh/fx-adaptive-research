# E020 Methodology (pre-registered 2026-11-09 R037, before any run)

- **Data and range:** Dukascopy EUR/USD 1-minute bid/ask, mid derived. **Dev block only** (2015-01-01..2020-12-31,
  `splits.DEFAULT_PLAN`). The script drops every bar whose trading date is not `dev` **before** any computation; val and OOS untouched.
- **Quote at hh:00 NY on NY date d:** bid/ask **open** of the first bar in [hh:00, hh:05) America/New_York (`fomc.ny_edge_quotes`).
  Missing -> excluded, never filled. No timestamp between 16:30 and 18:30 NY is used (R030 lesson).
- **Weekends:** indexed by calendar Monday W, for every Monday with W-3 >= first dev trading date and W <= last dev trading date.
  F = mid 16:00 NY Friday W-3; M = mid 20:00 NY Sunday W-1 (first bar of trading-date Monday at/after the Tokyo open in either DST
  state, 3 h after the roll); X = mid 16:00 NY Monday W. Gap G = (M - F) / pip. Weekends missing F, M or X (holiday weekends included)
  are excluded and counted (`missing_F`, `missing_M`, `missing_X`, first missing in that order). The rest are "valid".
- **Event:** a valid weekend is an event if |G| > `np.percentile(|G| of the previous 26 valid weekends, 67)` (numpy default linear
  interpolation, strictly greater, past only). The first 26 valid weekends are burn-in (no events).
- **Entry skip:** an event with ask-bid spread at M > 2.0 pips is skipped and counted (SPEC 4); it stays in the |G| history.
- **Statistic (1 trial):** signed return per tested event = -sign(G) x (X - M) / pip (mid). `weekend_gap.evaluate`: mean, median, SD,
  hit rate, one-sided t-test (H1 mean > 0), moving-block bootstrap 95% CI of the mean (block 4 events, 2000 draws, seed 0).
- **Decision rule (`weekend_gap.decide_b17`), unchanged from the backlog draft:**
  - **SIGNAL** if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05.
  - **WEAK** if mean > 0 and (CI lower > 0 or t p < 0.05), but not SIGNAL.
  - **NONE** otherwise.
- **Descriptive (not trials, do not change the decision):** all valid weekends after burn-in (no threshold); events with exit at
  16:00 NY Tuesday and Friday of the same week; the 17:00-20:00 NY Sunday move signed against the gap (reversal already before entry;
  17:00 quote = first bar in [17:00, 17:05) Sunday); up-gap and down-gap events separately; by year; median spreads at F, M, X; net
  per event at bid/ask (half spread at M and at X), SPEC 4 (bid/ask net - 0.1 slippage - 0.1 commission) and costs x1.5
  (gross - 1.5 x (gross - SPEC 4 net)); median threshold.
- **What follows:**
  - SIGNAL -> queue val confirmation B17v as its own experiment with this rule unchanged (LEAD needs dev SIGNAL + val pass + SPEC 4
    and x1.5 net > 0).
  - WEAK or NONE -> B17 closed for this definition; no re-test with other thresholds, windows or horizons on dev.
- **Power note (written before data):** ~310 dev weekends, ~95 events after burn-in; ~20 h SD ~40-50 pips -> SE ~4-5 pips; only a
  mean of ~8-10 pips clears the CI bar. A NONE does not rule out a small effect.
- **Calendar label:** weekend calendar effect; the London 4pm fix (11:00 NY Monday) and ECB fix (08:15 NY) are inside the hold.
- **Code:** `src/fxresearch/weekend_gap.py`, `scripts/run_e020_weekend_gap.py`; tests `tests/test_weekend_gap.py` (constants fixed,
  past-only strict threshold, no look-ahead, spread skip, cost ordering, F/M/X quotes from bars, missing bar counted, random walk no
  SIGNAL (5 seeds), strong reversal gives SIGNAL, rule edges). Synthetic smoke run passed (no events in 8 weekends, as expected).
- **Command:** `python scripts/run_e020_weekend_gap.py | tee backtests/validation_reports/E020_results.txt` (also writes
  `E020_results.json` and `E020_weekends.csv`).
- **Trial count:** dev +1 when it runs (229 -> 230); val unchanged at 4; total 233 -> 234.
