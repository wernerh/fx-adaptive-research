# E026 Results

**Run:** GitHub Actions run 42664624217, 2026-11-09 (outputs commit 067d5aa). Block: **dev only** (2015-01-01..2020-12-31). Val not
used, OOS untouched (dev bars 2,240,215, last bar 2020-12-31 21:59 UTC).
**Raw outputs:** `backtests/validation_reports/E026_results.json`, `backtests/validation_reports/E026_results.txt`, `backtests/validation_reports/E026_days.csv`.
Trading dates 1562, valid 1555, invalid (missing jump quote) 7, burn-in 60, post-burn-in valid 1495, events 169.
Excluded: missing exit 0, entry skipped for spread 0. Events tested 169.
Mean |J| of events 32.909 pips; median threshold 15.255 pips; share long 0.533.

## Pre-registered test (1 dev trial)
Signed = sign(J) x (mid 10:45 NY - mid 08:45 NY) on dev trading date D, pips, on dates where |J| = |mid 08:45 - mid 08:30 NY| > p90 of |J| over the 60 valid dates before D.

| n | Mean signed pips | Median | SD | Hit rate | t | One-sided t p | Block-boot 95% CI (block 10 events) | Decision |
|---|---|---|---|---|---|---|---|---|
| 169 | -0.42 | 1.1 | 33.825 | 0.5325 | -0.161 | 0.5639 | (-5.278, 2.488) | **NONE** |

## Descriptive (not trials; do not change the decision)
- **Reversal reading:** the mean is negative (-0.42) but its CI includes 0 by a wide margin; exploratory only, not a trial.
- **Horizons:** 08:45 -> 09:30 NY mean -0.453 (CI -3.88, 2.552); 08:45 -> 12:00 NY mean -2.608 (CI -7.563, 0.669).
- **Control, non-event post-burn-in dates, same trade:** n 1325, mean -0.465, CI (-1.673, 0.782).
- **Thresholds:** p80 n 302, mean -0.144, CI (-3.98, 2.873); p95 n 97, mean -4.232, CI (-10.567, 0.165).
- **First-Friday (NFP proxy):** 32 events, mean -0.797, CI (-5.077, 9.144); other events n 137, mean -0.331, CI (-6.152, 2.775).
- **FOMC statement days:** 3 events.
- **By year (n / mean / hit):** 2015 22 / +9.514 / 0.545; 2016 31 / -4.421 / 0.516; 2017 30 / -0.873 / 0.467; 2018 29 / -0.666 / 0.552;
  2019 25 / -1.728 / 0.600; 2020 32 / -1.702 / 0.531.
- **By weekday (n / mean / hit):** Mon 11 / +9.018 / 0.636; Tue 21 / +11.643 / 0.667; Wed 19 / -3.489 / 0.526; Thu 47 / -8.623 / 0.468;
  Fri 71 / +0.803 / 0.521. (Post-hoc, small cells, not evidence.)
- **Costs:** mid -0.42, net bid/ask -0.696, SPEC 4 net -0.896, costs x1.5 -1.135 pips per event; median spread entry 0.3, exit 0.3 pips.
