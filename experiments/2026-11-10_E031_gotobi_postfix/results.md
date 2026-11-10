# E031 Results

**Run:** GitHub Actions run 42762105863, 2026-11-10 (outputs commit 74fae18). Block: **dev only** (2015-01-01..2020-12-31,
2,240,215 bars, last bar 2020-12-31 21:59 UTC). Val not used, OOS untouched.
**Raw outputs:** `backtests/validation_reports/E031_results.json`, `backtests/validation_reports/E031_results.txt`,
`backtests/validation_reports/E031_days.csv`.
Weekday dates 1561, gotobi dates 462 (weekend-shifted 123, month-end 72). Exclusions: missing entry 0, missing exit 0, low coverage 0,
entry skipped for spread 2; events tested **460**.

## Pre-registered test (1 dev trial)
Signed = +(mid 10:55 - mid 09:55 Asia/Tokyo), pips, on gotobi Tokyo dates.

| n | mean | median | SD | hit | t p (1-sided) | block-20 CI 95% | Decision |
|---|---|---|---|---|---|---|---|
| 460 | +0.799 | 0.550 | 8.674 | 0.5348 | 0.0244 | (-0.154, 1.632) | **WEAK** |

## Descriptive (not trials; do not change the decision)
- Non-gotobi control (same trade): n 1096, mean +0.778, hit 0.542, t p 0.002, CI (0.234, 1.212). Gotobi minus control **+0.021**.
- Month-end gotobi: n 72, mean +1.200, CI (-0.225, 2.195). Gotobi not month-end: n 388, mean +0.725, CI (-0.279, 1.524).
- Weekend-shifted: n 123, mean -0.190; not shifted: n 337, mean +1.160, CI (0.159, 2.015).
- Last half hour 10:25 -> 10:55: gotobi n 460 +0.458, CI (-0.081, 0.899); control n 1096 +0.494, CI (0.166, 0.855).
- Exploratory, conditional on pre-fix move sign (mid 09:55 - 08:55): gotobi after down move n 238 +1.365, CI (0.091, 2.336); gotobi
  after up move n 221 +0.207; control after down move n 591 +1.323, CI (0.697, 1.797).
- By year (n / mean / hit): 2015 75 / -1.039 / 0.440; 2016 76 / -0.032 / 0.526; 2017 78 / +1.379 / 0.551; 2018 77 / -0.090 / 0.481;
  2019 77 / +0.744 / 0.571; 2020 77 / +3.768 / 0.636.
- By weekday (n / mean / hit): Fri 190 / +0.764 / 0.537; Mon 67 / +0.448 / 0.463; Thu 68 / -0.048 / 0.515; Tue 67 / +0.748 / 0.552;
  Wed 68 / +2.142 / 0.603.
- Costs (events, n 460): mid +0.799, net bid/ask +0.490, SPEC 4 net +0.290, costs x1.5 +0.036 pips; median spread entry 0.2, exit 0.3.
- Costs (control, n 1096): mid +0.778, net bid/ask +0.487, SPEC 4 net +0.287, x1.5 +0.042.
- Limitation: Japanese public holidays not in repo (not shifted, count not computed); gotobi rule UNVERIFIED as Ito & Yamada's;
  EUR/USD is only the USD leg of a USD/JPY effect.
