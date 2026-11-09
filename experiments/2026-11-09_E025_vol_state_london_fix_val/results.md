# E025 Results

**Run:** GitHub Actions run 42634668404, 2026-11-09 (outputs commit 3b9cb59). Block: **val only** (2021-01-21..2023-06-30). Dev not
re-used, OOS untouched (val bars 910,768, last bar 2023-06-30 20:59 UTC).
**Raw outputs:** `backtests/validation_reports/E025_results.json`, `backtests/validation_reports/E025_results.txt`, `backtests/validation_reports/E025_days.csv`.
Trading dates 637, valid 637, low coverage 0; states: prev_invalid 0, burn-in 60, normal 372, high 204.
Excluded: missing entry 0, missing exit 0, entry skipped for spread 0. Events tested 204.
Mean prior-date range of events 118.539 pips; median threshold 88.424 pips; median daily range 74.4 pips.

## Pre-registered test (1 val trial)
Signed = +(mid 16:00 NY - mid 11:05 NY) on val trading date D, pips, on dates whose previous trading date's mid range > p67 of the 60 valid val dates before it.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 10 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 204 | 0.582 | 0.575 | 24.746 | 0.5098 | 0.336 | 0.3687 | (-1.992, 3.14) | **NONE** |

`lead_cost_gate` False (x1.5 net -0.197) and `lead` False (no SIGNAL).

## Descriptive (not trials; do not change the decision)
- **Control, normal val dates, same long:** n 371, mean -0.053, median -0.15, hit 0.4879, t p 0.5171, CI (-2.46, 1.925).
- **All post-burn-in val dates, same long:** n 575, mean +0.172, median -0.1, hit 0.4957, t p 0.4326, CI (-1.768, 1.895).
- **FOMC statement days:** 4 events; excluding them n 200, mean -0.298, t p 0.5699, CI (-2.869, 2.099).
- **By year (n / mean / hit):** 2021 63 / +0.694 / 0.556; 2022 103 / +0.32 / 0.466; 2023 38 / +1.103 / 0.553.
- **By weekday (n / mean / hit):** Mon 42 / -3.404 / 0.452; Tue 30 / -8.763 / 0.333; Wed 31 / +10.09 / 0.581; Thu 50 / +4.42 / 0.52;
  Fri 51 / -0.182 / 0.608. (Post-hoc, not evidence.)
- **Costs:** mid +0.582, net bid/ask +0.262, SPEC 4 net +0.062, costs x1.5 -0.197 pips per event; median spread entry 0.3, exit 0.3 pips.
