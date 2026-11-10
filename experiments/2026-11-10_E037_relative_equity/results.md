# E037 Results

**Run:** GitHub Actions run 42915756793, 2026-11-10 (outputs commit b92e783). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E037_results.json`, `backtests/validation_reports/E037_results.txt`,
`backtests/validation_reports/E037_days.csv`, `backtests/validation_reports/E037_index_download.log`.

## Data gate
EU Stocks 50 CFD 1,876,816 bars, US 500 CFD 2,247,871 bars (2015-01-02 -> 2020-12-31). Dates 1561, dates missing a 16:00 London index
quote 28 (share 0.0179 <= 0.10) -> gate **ok**.

Counts: B35 burn-in 1, missing index quote 47, zero signal 0, missing entry 0, missing exit 4, entry spread skip 0, **tested 1509**.
B36 burn-in 20, missing index quote 55, zero signal 0, missing entry 0, missing exit 4, entry spread skip 0, **tested 1482**.
Weekend trading dates dropped 1.

## Pre-registered tests (2 dev trials, 16:05 London D -> 16:00 London next date, signed mid pips, block-20 bootstrap)

| Arm | n | mean | median | SD | hit | t | t p (1-sided) | block boot CI 95% | Decision |
|---|---|---|---|---|---|---|---|---|---|
| B35 -sign(S1) | 1509 | +1.268 | -0.5 | 56.401 | 0.4964 | 0.874 | 0.1912 | (-1.411, 3.942) | **NONE** |
| B36 -sign(S20) | 1482 | -0.88 | -2.5 | 55.818 | 0.4757 | -0.607 | 0.7281 | (-3.418, 1.868) | **NONE** |

## Costs (descriptive)
- B35: mid +1.268, net bid/ask +1.032, SPEC 4 +0.832, x1.5 +0.613; median spread entry 0.2, exit 0.2.
- B36: mid -0.88, net bid/ask -1.117, SPEC 4 -1.317, x1.5 -1.535; median spread entry 0.2, exit 0.2.

## Descriptive (not trials; do not change the decision)
- Contemporaneous corr(S1(D), EUR/USD 16:00 prev -> 16:00 D) **-0.2279** (n 1509): negative, the sign Hau-Rey predict in this
  convention. The contemporaneous relation is present; the lagged next-day extension is not.
- B35 legs: EU-only -0.395 (CI (-3.014, 2.762)); US-only +1.2 (CI (-1.764, 3.602)). B36 legs: EU-only +0.528, US-only -1.528.
- B35 |S1| terciles low/mid/high: -0.688 / +3.169 / +1.324 (all CIs span 0). B36 terciles: +0.985 / -0.778 / -2.848.
- B35 by year: 2015 +3.501, 2016 +1.734, 2017 +3.677, 2018 +2.215, 2019 +2.286, 2020 -5.802.
- B36 by year: 2015 +4.814, 2016 -5.773, 2017 -1.334, 2018 +0.21, 2019 +0.482, 2020 -3.269.
- B35 Mondays -0.796 (n 296), Fridays (weekend hold) -1.439 (n 301). B36 Mondays -4.456, Fridays +1.944.
- Excluding FOMC statement dates: B35 +1.607 (n 1463, t p 0.133), B36 -0.755. Excluding month-end D or next date: B35 +0.494,
  B36 -0.404.
- Share long EUR/USD: B35 0.534, B36 0.599. B35/B36 same side on 0.593 of dates. Unconditional long on B35 dates +0.139.
  SD of the hold move 56.415 pips.
