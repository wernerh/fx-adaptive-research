# E014 Results

**Run:** GitHub Actions run 42475560383, 2026-11-08 (outputs commit 671906f). Block: **val only** (2021-01-21..2023-06-30). OOS untouched.
**Raw outputs:** `backtests/validation_reports/E014_results.json`, `backtests/validation_reports/E014_results.txt`.
Scheduled statement days in val: 20 (none dropped for missing quotes). Unscheduled excluded: none. Cancelled excluded: none.

## Pre-registered test (1 trial)
Long EUR/USD mid, 16:00 NY previous business day -> 16:00 NY scheduled FOMC statement day.

| n | Mean pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 4) | Decision |
|---|---|---|---|---|---|---|---|---|
| 20 | 19.99 | 38.125 | 72.128 | 0.70 | 1.239 | 0.11514 | (-9.53, 51.018) | **NONE** |

## Cost check (gates only the LEAD label)
Median entry spread 0.25 pips; mean net at bid/ask 19.66, SPEC 4 19.46, costs x1.5 19.195.

## Descriptive (not trials)
- Non-FOMC val weekdays, same window: n 617, mean -2.563 pips, CI (-6.692, 1.152).
- 13:00-16:00 NY sub-window on statement day: n 20, mean 17.47, CI (-2.116, 39.659), p 0.082.
- Pooled dev+val (information only, no rule): n 67, mean 20.898.
- Per year: 2021 -2.888 (8), 2022 15.906 (8), 2023 73.913 (4).
- Per-meeting table: see `E014_results.txt`.
