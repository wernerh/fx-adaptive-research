# E032 Results

**Run:** GitHub Actions run 42783232861, 2026-11-10 (outputs commit a21f2cd). Block: **val only** (2021-01-21..2023-06-30,
910,768 bars, 2021-01-20 22:00 UTC -> 2023-06-30 20:59 UTC). Dev not used, OOS untouched.
**Raw outputs:** `backtests/validation_reports/E032_results.json`, `backtests/validation_reports/E032_results.txt`,
`backtests/validation_reports/E032_days.csv`.
Weekday trading dates 637. Exclusions: missing entry 0, missing exit 0, low coverage 0, entry skipped for spread 1; dates tested **636**.

## Pre-registered test (1 val trial)
Signed = +(mid 02:00 NY - mid 20:55 NY previous evening), pips, every valid val trading date.

| n | mean | median | SD | hit | t | t p (1-sided) | block-20 CI 95% | Decision |
|---|---|---|---|---|---|---|---|---|
| 636 | -0.534 | -0.300 | 14.119 | 0.4921 | -0.955 | 0.8299 | (-1.606, 0.669) | **NONE** |

## Descriptive (not trials; do not change the decision)
- EDT dates n 420 mean -0.388, CI (-1.395, 0.961); EST dates n 216 mean -0.820, CI (-2.687, 1.253).
- First hour 20:55 -> 21:55: n 636 mean +0.033, CI (-0.683, 0.687). Rest 21:55 -> 02:00: mean -0.568, CI (-1.259, 0.238).
- Monday (Sunday-evening entries) n 126 mean -0.944; Tue-Fri n 510 mean -0.433.
- By year (n / mean / hit): 2021 247 / -0.532 / 0.470; 2022 260 / -0.292 / 0.515; 2023 129 / -1.029 / 0.488.
- By weekday (n / mean / hit): Mon 126 / -0.944 / 0.476; Tue 127 / +0.179 / 0.465; Wed 127 / -0.419 / 0.504; Thu 128 / -1.783 / 0.484;
  Fri 128 / +0.295 / 0.531.
- Costs (n 636): mid -0.534, net bid/ask -0.906, SPEC 4 net -1.106, costs x1.5 -1.392 pips; median spread entry 0.3, exit 0.4.
