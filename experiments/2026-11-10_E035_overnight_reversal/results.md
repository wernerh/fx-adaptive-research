# E035 Results

**Run:** GitHub Actions run 42865880407, 2026-11-10 (outputs commit cfd1951). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val not used, OOS untouched.
**Raw outputs:** `backtests/validation_reports/E035_results.json`, `backtests/validation_reports/E035_results.txt`,
`backtests/validation_reports/E035_days.csv`.

Trading dates 1,562; valid r_on dates 1,554. B32: missing signal 8, zero/entry/exit/spread exclusions 0, **tested 1,554**.
B33: burn-in 20, missing entry 6, other exclusions 0, **tested 1,536**.

## Pre-registered tests (2 dev trials, hold 07:00 -> 16:55 NY, signed mid pips, block-20 bootstrap)

| Arm | Position | n | mean | median | SD | hit | t | t p (1-sided) | block boot CI 95% | Decision |
|---|---|---|---|---|---|---|---|---|---|---|
| B32 | -sign(r_on) | 1554 | -0.285 | -1.4 | 45.419 | 0.4813 | -0.247 | 0.5976 | (-2.421, 1.843) | **NONE** |
| B33 | -sign(O20) | 1536 | +2.695 | 2.15 | 44.862 | 0.5267 | 2.354 | 0.0093 | (0.47, 5.027) | **SIGNAL** |

## Costs (descriptive)
- B32: mid -0.285, net bid/ask -0.733, SPEC 4 -0.933, x1.5 -1.258; median spread entry 0.3, exit 0.5.
- B33: mid +2.695, net bid/ask +2.247, SPEC 4 **+2.047**, x1.5 **+1.723**; median spread entry 0.3, exit 0.5.

## Descriptive (not trials; do not change any decision)
- OLS slope of r_id on r_on: -0.0049 (t -0.151, p 0.88). SD r_on 35.512, SD r_id 45.416 pips.
- Unconditional long r_id (07:00 -> 16:55 NY): +0.56 (CI (-1.652, 2.952), t p 0.314).
- B32 |r_on| terciles low/mid/high: -0.372 / -1.383 / +0.901. Mondays +0.861 (n 311), Tue-Fri -0.571. Share long 0.506.
- B33 |O20| terciles low/mid/high: +2.602 / +1.18 / +4.304 (high CI (0.256, 9.656)). Share long 0.482.
- Share of dates where B32 and B33 take the same side: 0.498.
- By year B32: 2015 -6.931, 2016 +3.376, 2017 -1.347, 2018 +0.352, 2019 +1.575, 2020 +1.248.
- By year B33: 2015 +8.867 (n 239), 2016 +2.48, 2017 +2.651, 2018 +1.365, 2019 +0.736, 2020 +0.557.
