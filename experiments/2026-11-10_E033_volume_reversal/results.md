# E033 Results

**Run:** GitHub Actions run 42808245508, 2026-11-10 (outputs commit b7585fc). Block: **dev only** (2,240,215 bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val not used, OOS untouched.
**Raw outputs:** `backtests/validation_reports/E033_results.json`, `backtests/validation_reports/E033_results.txt`,
`backtests/validation_reports/E033_days.csv`.

**Volume gate:** ok (2,240,215 dev bars, 0 zero/NaN volume bars, share 0.0). Bar volume min 0.000137, median 143.34, max 138027.44.
Trading dates 1562, valid 1556 (6 low coverage), dates with a UV band 1475.

| Arm | events | missing signal quote | Friday excluded | zero move | missing entry | missing exit | spread skip | tested |
|---|---|---|---|---|---|---|---|---|
| Low UV (B28) | 533 | 4 | 97 | 1 | 2 | 3 | 0 | **426** |
| High UV (B29) | 494 | 2 | 99 | 1 | 0 | 1 | 0 | **391** |
| Mid (descriptive) | 448 | 0 | 97 | 0 | 2 | 0 | 0 | 349 |

## Pre-registered tests (2 dev trials)
Hold 20:00 NY on D -> 16:55 NY on D+1, signed mid pips.

| Arm | n | mean | median | SD | hit | t | t p (1-sided) | block-10 CI 95% | Decision |
|---|---|---|---|---|---|---|---|---|---|
| B28 low-UV reversal, -sign(R) | 426 | -2.034 | -0.2 | 52.158 | 0.4977 | -0.805 | 0.7893 | (-6.772, 3.013) | **NONE** |
| B29 high-UV continuation, +sign(R) | 391 | -0.213 | 1.4 | 60.8 | 0.5064 | -0.069 | 0.5276 | (-6.616, 4.78) | **NONE** |

## Descriptive (not trials; do not change any decision)
- Mid-tercile reversal n 349 mean +0.852, CI (-4.181, 6.788). High-tercile reversal +0.213. Low-tercile continuation +2.034.
- All banded tradable dates, reversal control: n 1166 mean -0.417, CI (-3.672, 2.92).
- E021 large-move overlap: low arm 0.117, high arm 0.292. Excluding them: low reversal n 376 +0.08, CI (-4.909, 5.346);
  high continuation n 277 +0.03, CI (-6.751, 5.215).
- corr(UV, daily range) 0.275; corr(UV, |R|) 0.185; mean |R| low 31.961, high 51.835 pips.
- By year, low reversal (n / mean / hit): 2015 47 / -16.777 / 0.447; 2016 86 / +1.428 / 0.453; 2017 68 / -9.687 / 0.426;
  2018 70 / +2.609 / 0.486; 2019 74 / -3.123 / 0.486; 2020 81 / +6.253 / 0.654.
- By year, high continuation: 2015 49 / +0.149 / 0.449; 2016 67 / -3.618 / 0.463; 2017 73 / -9.56 / 0.466; 2018 79 / +8.052 / 0.544;
  2019 65 / -5.033 / 0.477; 2020 58 / +9.323 / 0.638.
- Costs: low reversal mid -2.034, net bid/ask -2.53, SPEC 4 -2.73, x1.5 -3.078; high continuation mid -0.213, bid/ask -0.694,
  SPEC 4 -0.894, x1.5 -1.234. Median spread entry 0.3, exit 0.5 (both arms).
