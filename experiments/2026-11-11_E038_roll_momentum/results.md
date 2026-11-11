# E038 Results

**Run:** GitHub Actions run 42939744082, 2026-11-11 (outputs commit 64780e4). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E038_results.json`, `backtests/validation_reports/E038_results.txt`,
`backtests/validation_reports/E038_days.csv`. All figures below are copied from those files.

## Counts
Trading dates 1561; weekend trading dates dropped 1; missing start 9; missing entry 2; zero signal 0; missing exit 0; entry skipped
(16:25 NY spread > 2.0 pips) 8; **tested 1542**.

## B38 (1 dev trial): sign(r1) x r2, r1 = 17:00 NY start of D -> 16:25 NY, r2 = 16:25 -> 16:55 NY
| n | mean (pips) | median | SD | hits / nonzero | hit rate | binomial p (1-sided) | t | t p (1-sided) | block-20 95% CI |
|---|---|---|---|---|---|---|---|---|---|
| 1542 | 0.255 | 0.175 | 4.776 | 796 / 1533 | 0.5192 | 0.06924 | 2.099 | 0.018 | (0.023, 0.501) |

**Decision (`decide_b38`): WEAK** (mean > 0 and CI lower > 0; mean not > 1.0 pip and binomial p not < 0.05). Reversal flag: False.

## Descriptive (not trials; do not change the decision)
- OLS slope of r2 on r1: 0.00152, t 0.72, p 0.4718. SD r1 57.44 pips, SD r2 4.774 pips. Share long 0.498.
- Unconditional long r2: mean -0.282, hit 0.4553, CI (-0.552, -0.061) (EUR/USD drifts down into the roll on dev).
- |r1| terciles: low -0.028 (CI (-0.337, 0.267)); mid +0.542 (CI (0.249, 0.885)); high +0.253 (CI (-0.21, 0.804)).
- EDT n 1013 +0.426 (CI (0.202, 0.731)); EST n 529 -0.072 (CI (-0.475, 0.354)).
- Fridays n 306 +0.183; Mon-Thu n 1236 +0.273 (CI (-0.016, 0.553)).
- Excluding FOMC statement dates (47 in tested): n 1495, +0.25, CI (0.038, 0.489). Excluding month-ends: n 1470, +0.201,
  CI (-0.046, 0.453).
- Next-date reversal reading: n 1537, -0.072, CI (-3.117, 3.066) (no reversal detectable).
- By year: 2015 +0.409, 2016 +0.293, 2017 +0.496, 2018 +0.458, 2019 -0.353, 2020 +0.229.
- Spreads: 16:25 NY median / p90 0.3 / 0.5 pips; 16:55 NY 0.5 / 1.0 pips.
- Costs: mean signed mid +0.255; net at bid/ask -0.225; net SPEC 4 -0.425; net costs x1.5 -0.765.
