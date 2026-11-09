# E028 Results

**Run:** GitHub Actions run 42712247364, 2026-11-09 (outputs commit 612642d). Block: **dev only** (2015-01-01..2020-12-31). Val not
used, OOS untouched (dev bars 2,240,215, last bar 2020-12-31 21:59 UTC).
**Raw outputs:** `backtests/validation_reports/E028_results.json`, `backtests/validation_reports/E028_results.txt`, `backtests/validation_reports/E028_days.csv`.
Trading dates 1562, valid 1550, invalid (missing signal quote) 12, burn-in 60, post burn-in valid 1490. Events 74 (36 positive r,
38 negative r); missing exit 0, entry skipped for spread 0; events tested 74. Share long 0.486; mean |r| of events 118.978 pips;
median band SD of events 42.306 pips.

## Pre-registered test (1 dev trial)
Signed = sign(r(D) - m(D)) x (mid 16:30 NY - mid 12:00 NY) on dev event date D, pips; event = r(D) (17:00 NY open -> 12:00 NY)
outside m +/- 2 s of the 60 prior valid dates.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 5 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 74 | 1.061 | 3.825 | 32.491 | 0.5946 | 0.281 | 0.3897 | (-5.625, 8.569) | **NONE** |

## Descriptive (not trials; do not change the decision)
- **Reversal reading:** mean positive; nothing to log as exploratory.
- **Positive-r events (up moves):** n 36, +9.457, CI (1.159, 20.025), t p 0.0179. **Negative-r events:** n 38, -6.892, CI
  (-16.431, 5.496). Post-hoc split, not evidence (see conclusion).
- **Other thresholds:** k 1.5 n 186, -0.042, CI (-3.043, 2.872); k 2.5 n 35, -4.003, CI (-16.621, 10.179).
- **Control (long 12:00 -> 16:30 NY on post-burn-in non-event dates):** +1.108.
- **FOMC:** 1 event on a statement date; excluding it n 73, +1.841, CI (-5.857, 8.52).
- **First Fridays:** 5 events; excluding them n 69, +1.444, CI (-5.102, 8.752).
- **By year (n / mean / hit):** 2015 10 / -0.14 / 0.70; 2016 11 / +7.364 / 0.727; 2017 11 / +7.336 / 0.727; 2018 7 / +18.979 / 0.857;
  2019 17 / +1.112 / 0.588; 2020 18 / -12.972 / 0.278.
- **By weekday (n / mean / hit):** Mon 11 / +5.709 / 0.636; Tue 12 / +0.625 / 0.667; Wed 10 / -3.51 / 0.70; Thu 22 / +2.241 / 0.682;
  Fri 19 / -0.313 / 0.368. (Post-hoc, not evidence.)
- **Costs:** mid +1.061, net bid/ask +0.707, SPEC 4 net +0.507, costs x1.5 +0.229 pips per event; median spread entry 0.25, exit 0.4 pips.
