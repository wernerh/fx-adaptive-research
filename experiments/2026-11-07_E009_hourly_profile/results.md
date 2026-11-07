# E009 Results

**Run:** GitHub Actions run 42420473476, 2026-11-07 (outputs commit 89082ec). Block: **dev only**. val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E009_results.json`, `backtests/validation_reports/E009_results.txt` (all 192 cells).
Exploratory scan of mean EUR/USD mid return per (date, clock hour), pips. No trades, no costs.

## CANDIDATE cells (pre-registered rule: |mean| >= 1.0, CI excludes 0, t p < 0.05/192 = 2.6e-4, sign p < 0.05)

| Cell | n | Mean (pips) | Block-boot 95% CI | Up-share | t p | Sign p | Bonferroni t p |
|---|---|---|---|---|---|---|---|
| Wed_ny_18 | 312 | +1.333 | (0.703, 2.055) | 0.590 | 1.98e-5 | 0.0017 | 0.0038 |
| Thu_ny_18 | 313 | +1.240 | (0.749, 2.024) | 0.654 | 9.47e-5 | <1e-6 | 0.0182 |

## NOTE cells (|mean| >= 1.0 and t p < 0.01, not CANDIDATE; spawn nothing)

| Cell | n | Mean | CI | t p | Sign p |
|---|---|---|---|---|---|
| utc_11 | 1556 | -1.016 | (-1.636, -0.362) | 8.1e-4 | 0.020 |
| ny_07 | 1556 | -1.118 | (-1.929, -0.478) | 4.9e-4 | 0.0008 |
| Mon_ny_08 | 311 | +2.312 | (0.445, 3.695) | 0.0041 | 0.089 |
| Mon_ny_09 | 311 | +2.482 | (0.586, 3.857) | 0.0057 | 0.0026 |
| Wed_ny_04 | 311 | -2.493 | (-3.484, -1.241) | 4.9e-4 | 0.0064 |
| Fri_ny_07 | 310 | -1.841 | (-3.052, -0.868) | 0.0022 | 0.0044 |

## Context for the NY 18:00 hour (all from E009_results.txt)
- Unconditional ny_18: n 1558, mean +0.866, CI (0.547, 1.199), up-share 0.595, t p 3.0e-7 -> NONE (mean < 1.0 pip).
- By weekday: Mon +0.433, Tue +0.634, Wed +1.333, Thu +1.240, Fri +0.685; month-end +1.856 (n 72, CI includes 0).
- NY 18:00-19:00 is the first full hour after the 17:00 NY roll. With `sessions.trading_date`, trading date Wed's 18:00 NY hour
  falls on **Tuesday evening** New York clock time (Thu -> Wednesday evening).
- Also: utc_22 (+0.550, sign p < 1e-6) and utc_02 (+0.691) show positive drift in thin hours; all below 1 pip.

**Overall (pre-registered rule): CANDIDATES (2 cells).** Trials: 192 (dev total now 222).
