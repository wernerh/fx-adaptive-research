# E008 Results

**Run:** GitHub Actions run 42411061401, 2026-11-07 (outputs commit 0a4f98d). Block: **dev only**. val and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E008_results.json`, `backtests/validation_reports/E008_results.txt`.
Statistic: partial Spearman IC of predictor vs |outcome| given prior 14-day ATR. Magnitude test, no trades, no costs.

| Test | n | Partial IC | p | Block-boot 95% CI | Raw-pips IC (descriptive) | Decision |
|---|---|---|---|---|---|---|
| asia_range -> abs US 08-12 NY | 1538 | 0.0599 | 0.0188 | (0.0123, 0.1126) | 0.1895 | NOT_USEFUL |
| asia_range -> abs US 08-09 NY | 1537 | 0.0516 | 0.0434 | (0.0111, 0.1034) | 0.2146 | NOT_USEFUL |
| london_range -> abs US 08-12 NY | 1540 | 0.0099 | 0.6978 | (-0.0438, 0.0572) | 0.1435 | NOT_USEFUL |
| london_range -> abs US 08-09 NY | 1539 | -0.0014 | 0.9552 | (-0.0517, 0.0430) | 0.1649 | NOT_USEFUL |

Descriptive terciles (|US 08-12| in pips, by Asia range tercile): low 24.03, mid 25.85, high 26.95.
By London range tercile: low 26.40, mid 25.23, high 25.12.

**Overall (pre-registered rule): NOT_USEFUL.** Trials: 4 (dev total now 30).
