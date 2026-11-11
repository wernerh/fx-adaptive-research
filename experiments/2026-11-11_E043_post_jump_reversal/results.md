# E043 Results

**Run:** GitHub Actions run 43050165053, 2026-11-11 (outputs commit 6f57ad1). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E043_results.json`, `backtests/validation_reports/E043_results.txt`,
`backtests/validation_reports/E043_events.csv`. All figures below are copied from those files.

## Counts
grid slots 450720; slots with quote 448664; valid returns 448330; tested slots 445874; **jumps 2764**; excluded: roll hour 30,
week open 2, inside a previous hold 825, missing entry 2, missing exit 5, entry skipped (spread) 4; **events tested 1896**
(1160 trading dates). Threshold |L| > 5.395, K 270, |move| >= 5 pips.

## B48 (1 trial; date-cluster bootstrap, 2000 draws, seed 0)

| n | dates | mean (pips) | median | SD | hit rate | t | t p (1-sided) | date-cluster 95% CI |
|---|---|---|---|---|---|---|---|---|
| 1896 | 1160 | -0.693 | 0.325 | 21.066 | 0.5053 | -1.432 | 0.9238 | (-1.607, 0.251) |

**Decision (pre-registered rule): NONE** (mean < 0: neither SIGNAL nor WEAK).

## Costs (descriptive)
Mean signed mid -0.693; net bid/ask -0.978; net SPEC 4 -1.178; net costs x1.5 -1.420. Median spread entry / exit 0.3 / 0.3.

## Descriptive (not trials; do not change the decision)
- Continuation (opposite sign) mean +0.693 (reported only, not a trial).
- Positive jumps (short EUR/USD): n 973, -0.035, CI (-1.449, 1.38). Negative jumps (long): n 923, -1.386, CI (-2.701, -0.072).
- US-release proxy 08:25-08:50 NY: n 256, -2.123, CI (-5.324, 1.027); rest n 1640, -0.469, CI (-1.412, 0.467); release share 0.135.
- London open 02:00-04:00 NY: n 258, +0.253, CI (-1.842, 2.333); rest n 1638, -0.841.
- Skipped bar t+5 -> t+10, signed by the fade: n 1896, +0.491, CI (0.067, 0.946) (a small immediate reversal inside the skipped bar).
- |L| terciles: low +0.621 CI (-0.736, 1.978); mid -0.383; high -2.315 CI (-4.259, -0.426).
- Median |jump| 14.85 pips; median |L| 6.706; share positive jumps 0.5132. Busiest NY hours: 08 (339), 10 (329), 09 (192), 03 (176).
- By year: 2015 -4.33 (n 335), 2016 -0.778, 2017 +0.389, 2018 +0.35, 2019 +0.286, 2020 +0.143.
