# E030 Results

**Run:** GitHub Actions run 42749648254, 2026-11-10 (outputs commit 9e2c50a). Block: **dev only** (2015-01-01..2020-12-31,
2,240,215 bars, last bar 2020-12-31 21:59 UTC). Val not used, OOS untouched.
**Raw outputs:** `backtests/validation_reports/E030_results.json`, `backtests/validation_reports/E030_results.txt`,
`backtests/validation_reports/E030_days.csv`.
Weekday dates 1561, gotobi dates 462 (weekend-shifted 123, month-end 72). Exclusions: missing entry 0, missing exit 0, low coverage 0,
entry skipped for spread 4; events tested **458**.

## Pre-registered test (1 dev trial)
Signed = -(mid 09:55 - mid 08:55 Asia/Tokyo), pips, on gotobi Tokyo dates.

| n | mean | median | SD | hit | t p (1-sided) | block-20 CI 95% | Decision |
|---|---|---|---|---|---|---|---|
| 458 | +0.180 | 0.200 | 8.356 | 0.5153 | 0.3224 | (-0.552, 1.245) | **NONE** |

## Descriptive (not trials; do not change the decision)
- Non-gotobi control (same trade): n 1097, mean +0.411, hit 0.5387, t p 0.0779, CI (-0.133, 0.839). Gotobi minus control -0.231.
- Month-end gotobi: n 72, mean +2.639, hit 0.5833, t p 0.0075, CI (-0.264, 4.943). Gotobi not month-end: n 386, mean -0.278.
- Weekend-shifted: n 122, mean -0.449; not shifted: n 336, mean +0.408.
- Last half hour 09:25 -> 09:55: gotobi n 458 +0.088, CI (-0.387, 0.713); control n 1097 +0.502, CI (0.132, 0.852).
- By year (n / mean / hit): 2015 76 / +0.441 / 0.526; 2016 75 / +0.698 / 0.547; 2017 77 / -0.451 / 0.506; 2018 77 / -1.251 / 0.442;
  2019 77 / -0.284 / 0.532; 2020 76 / +1.968 / 0.539.
- By weekday (n / mean / hit): Fri 189 / +0.438 / 0.571; Mon 66 / +0.539 / 0.515; Thu 68 / -0.520 / 0.456; Tue 67 / -0.019 / 0.433;
  Wed 68 / +0.011 / 0.500.
- Costs (events, n 458): mid +0.180, net bid/ask -0.153, SPEC 4 net -0.353, costs x1.5 -0.619 pips; median spread entry 0.4, exit 0.2.
- Costs (control, n 1097): mid +0.411, net bid/ask +0.086, SPEC 4 net -0.114, x1.5 -0.376.
- Limitation: Japanese public holidays not in repo (not shifted, count not computed); gotobi rule UNVERIFIED as Ito & Yamada's;
  EUR/USD is only the USD leg of a USD/JPY effect.
