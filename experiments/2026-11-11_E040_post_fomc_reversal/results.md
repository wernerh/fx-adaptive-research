# E040 Results

**Run:** GitHub Actions run 42980196892, 2026-11-11 (outputs commit e5d07ab). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E040_results.json`, `backtests/validation_reports/E040_results.txt`,
`backtests/validation_reports/E040_events.csv`. All figures below are copied from those files.

## Events
Scheduled dev statements: 47. Unscheduled excluded: 2019-10-04, 2020-03-02, 2020-03-15. Cancelled excluded: 2020-03-18.
Counts: events 47; not_trading_day 0; missing_pre 0; zero_signal 0; missing_entry 0; missing_exit 0; entry_skipped_spread 0;
**tested 47**.

## B43 (1 trial; i.i.d. bootstrap, t p < 0.05, >= 40 events)

| n | mean (pips) | median | SD | hits / nonzero | hit rate | binomial p (1-sided) | t | t p (1-sided) | bootstrap 95% CI |
|---|---|---|---|---|---|---|---|---|---|
| 47 | 2.623 | 0.1 | 61.879 | 24 / 47 | 0.5106 | 0.5 | 0.291 | 0.3863 | (-14.684, 21.44) |

**Decision (`post_fomc_reversal.decide_b43`): NONE** (mean > 1.0 pip, but CI lower < 0 and t p not < 0.05).

## Costs (descriptive)
Mean signed mid +2.623; net bid/ask +2.336; net SPEC 4 +2.136; net costs x1.5 +1.893. Median spread entry / exit 0.3 / 0.3.

## Descriptive (not trials; do not change the decision)
- Pre-statement drift P: mean 16.905 pips, mean |P| 31.746; share short (P > 0) 0.66.
- Unconditional short 02:00 -> 14:00 NY t+1: n 47, +1.657, CI (-14.532, 19.472).
- P > 0 subset: n 31, +3.245, CI (-18.914, 26.297). P < 0 subset: n 16, +1.419, CI (-21.632, 25.274).
- 0-12 h window (14:00 NY t -> 02:00 NY t+1), same sign: n 47, +2.01, median -6.25, CI (-15.172, 20.396).
- OLS slope of r on P: 0.15114 (t 0.689, p 0.4942) - positive, i.e. not a reversal.
- Non-FOMC Wednesday control (same rule): n 263, +5.093, t p 0.087, CI (-1.595, 12.679); 5 missing_pre.
- By year: 2015 +8.519, 2016 +12.244, 2017 +8.0, 2018 +7.031, 2019 -4.431, 2020 -18.229.
