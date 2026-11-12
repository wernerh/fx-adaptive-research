# E046 Results

**Run:** GitHub Actions run 43155068137, 2026-11-12 (outputs commit 2d401c7). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E046_results.json`, `backtests/validation_reports/E046_results.txt`,
`backtests/validation_reports/E046_days.csv`. All figures below are copied from those files.

## Counts
dev trading dates 1561; pre-cycle 12; unassigned (k > 33) 25; week 0 excluded 235; missing entry 0; missing exit 5; entry spread
skip 3; tested **1281**. FOMC statement dates used 47.

## B54 (1 trial; moving-block bootstrap, block 20 dates, 2000 draws, seed 0)

| n | mean (pips) | median | SD | hit rate | t | t p (1-sided) | block-20 95% CI |
|---|---|---|---|---|---|---|---|
| 1281 | 1.152 | 1.75 | 54.926 | 0.5129 | 0.75 | 0.2265 | (-2.517, 4.226) |

**Decision (pre-registered rule): NONE** (mean > 1 pip but CI lower < 0 and t p > 0.05: neither SIGNAL nor WEAK).

## Costs (descriptive)
Mean signed mid 1.152; net bid/ask 0.681; net SPEC 4 0.481; net costs x1.5 0.146. Median spread entry/exit 0.3/0.5.

## Descriptive (not trials; do not change the decision)
- Long mean by cycle week (incl. week 0): -1: n 235, -0.717; 0: n 235, +4.218; 1: n 230, -7.167; 2: n 228, +3.272; 3: n 229, -0.831;
  4: n 227, -1.328; 5: n 111, +8.182; 6: n 21, -3.257.
- Even long leg n 476, +0.79, CI (-3.786, 5.823), t p 0.3674; odd short leg n 805, +1.365, CI (-3.167, 5.234), t p 0.2493. Share long 0.3716.
- Unconditional long, same hold: n 1281, -0.564, CI (-3.314, 2.482).
- Cycle lagged one date (reported only): +0.414, CI (-2.79, 3.301). Opposite sign -1.152 (reported only).
- By year: 2015 -3.92, 2016 +1.186, 2017 +2.228, 2018 +3.037, 2019 +2.641, 2020 +1.498.
