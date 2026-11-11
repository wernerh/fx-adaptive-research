# E039 Results

**Run:** GitHub Actions run 42960104359, 2026-11-11 (outputs commit a04cc2c). Block: **dev only** (2,240,215 EUR/USD bars,
2015-01-01 22:00 UTC -> 2020-12-31 21:59 UTC). Val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E039_results.json`, `backtests/validation_reports/E039_results.txt`,
`backtests/validation_reports/E039_events.csv`, `E039_calendar_parsed.csv`, `E039_auctions_raw.csv`, `E039_auctions_fetch.json`,
`E039_ustb_download.log`. All figures below are copied from those files.

## Calendar gate (phase 1, Fiscal Data API on the runner): **pass**
Qualifying nominal Note/Bond auctions per dev year: 2015 72, 2016 72, 2017 72, 2018 72, 2019 73, 2020 80 (gate 50-110). Parsed
close-time share 1.0 (gate >= 0.95). 441 qualifying auctions -> 440 events (1 multi-auction event). Excluded from the raw calendar:
bills 1340, TIPS 73, FRN 73. Close times: 13:00 NY 414 events, 11:30 NY 24, 11:00 NY 1, 10:00 NY 1. First event 2015-01-12, last
2020-12-29.

## B40 (hold to 16:00 NY on the 10th trading date after D; trial 1 of 2, t p < 0.025)
Counts: events 440; not_trading_date 0; missing_window 0; zero_signal 1; entry_skipped_spread 0; exit_outside_dev 4; missing_exit 4;
**tested 431**.

| n | mean (pips) | median | SD | hits / nonzero | hit rate | binomial p (1-sided) | t | t p (1-sided) | block-20 95% CI |
|---|---|---|---|---|---|---|---|---|---|
| 431 | 1.426 | 7.65 | 176.469 | 226 / 431 | 0.5244 | 0.16769 | 0.168 | 0.4334 | (-11.651, 11.979) |

**Decision (`treasury_auction.decide`): NONE** (mean > 1.0 pip, but CI lower < 0 and t p not < 0.025).

## B41 (hold to 16:00 NY on the 1st trading date after D; trial 2 of 2, t p < 0.025)
Counts: events 440; zero_signal 1; exit_outside_dev 0; missing_exit 2; other exclusions 0; **tested 437**.

| n | mean (pips) | median | SD | hits / nonzero | hit rate | binomial p (1-sided) | t | t p (1-sided) | block-20 95% CI |
|---|---|---|---|---|---|---|---|---|---|
| 437 | 1.655 | 2.95 | 57.337 | 227 / 437 | 0.5195 | 0.22204 | 0.603 | 0.2733 | (-3.106, 7.394) |

**Decision: NONE** (mean > 1.0 pip, but CI lower < 0 and t p not < 0.025).

## Costs (descriptive)
- B40: mean signed mid +1.426; net bid/ask +1.157; net SPEC 4 +0.957; net costs x1.5 +0.722. Median spread entry / exit 0.3 / 0.2.
- B41: mean signed mid +1.655; net bid/ask +1.386; net SPEC 4 +1.186; net costs x1.5 +0.952. Median spread entry / exit 0.3 / 0.2.
- Costs are small relative to the target SD (176 / 57 pips); the binding constraint is noise, not cost.

## Descriptive (not trials; do not change the decision)
- Auction window (T-10 -> T+10 min) SD 7.943 pips; share long 0.514.
- OLS slope of arm return on window move: B40 1.0284 (t 0.968, p 0.3337); B41 0.0516 (t 0.15, p 0.8811).
- By tenor: B40 short (2/3/5/7-y) n 280 +9.484, CI (-6.377, 25.755); long (10/20/30-y) n 150 -13.461, CI (-33.844, -0.239).
  B41 short n 284 +2.521, CI (-2.327, 10.571); long n 152 -0.073, CI (-8.614, 9.445).
- Unconditional long: B40 +1.071 (CI (-20.567, 26.861)); B41 +0.742 (CI (-4.423, 7.05)).
- Non-auction control (same weekday and time one week earlier): B40 n 422 -1.249 (CI (-19.633, 15.616)); B41 n 423 -3.494
  (CI (-9.72, 2.151)).
- ustbondtrusd (2019-2020): status ok, 144 events with data, sign agreement with the EUR/USD window 0.59. Same events, EUR/USD sign:
  B40 n 139 +1.024, B41 n 143 +1.677. Treasury-CFD sign: B40 n 139 -3.927 (CI (-12.127, 15.582)); B41 n 143 -0.668
  (CI (-7.51, 6.001)).
- By year, B40: 2015 +16.497, 2016 +5.561, 2017 +12.186, 2018 -24.525, 2019 +3.643, 2020 -4.672.
  B41: 2015 -0.976, 2016 +6.26, 2017 +8.087, 2018 -2.854, 2019 -7.467, 2020 +6.418.
