# E034 Results

**Run:** GitHub Actions run 42834778439, 2026-11-10 (outputs commit 2adc3fe). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val not used, OOS untouched.
**Raw outputs:** `backtests/validation_reports/E034_results.json`, `backtests/validation_reports/E034_results.txt`,
`backtests/validation_reports/E034_month_ends.csv`, `backtests/validation_reports/E034_index_download.log`.

**Index data:** EU Stocks 50 CFD 1,876,816 bars (2015-01-02 -> 2020-12-31 20:59 UTC), US 500 CFD 2,247,871 bars
(2015-01-02 -> 2020-12-31 21:14 UTC). **Data gate: ok** (71 anchored month-ends, 0 missing index quotes, share 0.0).
Month-ends 72 (2015-01-30 -> 2020-12-31); `no_prev_month_end` 1; zero signal 0; missing entry/exit 0; spread skips 0;
**tested 71 per window**; fallback-quote month-ends 4.

## Pre-registered tests (2 dev trials)
Position -sign(S), S = EU50 minus US500 log return from the previous month-end 16:00 London fix to 16:00 London on D-1. Signed mid pips.

| Window | n | mean | median | SD | hit | t | t p (1-sided) | i.i.d. boot CI 95% | Decision |
|---|---|---|---|---|---|---|---|---|---|
| HOUR 15:00 -> 16:00 London on D | 71 | +1.731 | 0.55 | 25.586 | 0.507 | 0.57 | 0.2852 | (-4.152, 7.559) | **NONE** |
| DAY 16:00 London D-1 -> 16:00 London D | 71 | +3.354 | 9.55 | 53.554 | 0.5493 | 0.528 | 0.2997 | (-9.322, 15.498) | **NONE** |

## Costs (descriptive)
- HOUR: mid +1.731, net bid/ask +1.437, SPEC 4 +1.237, x1.5 +0.989; median spread entry 0.3, exit 0.2.
- DAY: mid +3.354, net bid/ask +3.134, SPEC 4 +2.934, x1.5 +2.724; median spread entry 0.2, exit 0.2.

## Descriptive (not trials; do not change any decision)
- Unconditional long EUR/USD: HOUR +3.076 (CI (-2.795, 8.811), t p 0.156); DAY +12.501 (CI (1.329, 24.105), t p 0.0236).
  The conditional signal is below the unconditional long in both windows.
- Share of short EUR/USD positions 0.408; corr(S, move) HOUR -0.041, DAY +0.014. S mean -0.00664, SD 0.03056, |S| median 0.02062.
- |S| above / at-or-below median: HOUR +1.647 (n 35) / +1.813 (n 36); DAY +3.14 / +3.563.
- EU-only leg (-sign(EU MTD return)): HOUR -1.61, DAY -11.482 (CI (-23.458, 0.526)).
- US-only leg (+sign(US MTD return)): HOUR +4.962 (CI (-0.664, 10.801), t p 0.0505); DAY **+23.082** (n 71, hit 0.676,
  CI (12.099, 34.425), t p 0.0001). Post-hoc descriptive cell, not a trial; overlaps the unconditional long drift (+12.501).
- Quarter-ends / other month-ends: HOUR -6.427 (n 24) / +5.897 (n 47); DAY +7.335 / +1.321.
- Excluding fallback-quote months (n 67): HOUR +2.063, DAY +3.654.
- Post-fix hour 16:00 -> 17:00 London on D, same position: -1.355 (CI (-5.543, 2.662)).
- By year, HOUR: 2015 -4.486, 2016 -7.512, 2017 +12.408, 2018 -1.654, 2019 +6.063, 2020 +5.05.
- By year, DAY: 2015 -9.732, 2016 -36.754, 2017 +28.808, 2018 +14.663, 2019 +18.604, 2020 +3.446.
