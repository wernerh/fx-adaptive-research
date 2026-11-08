# E017 Results

**Run:** GitHub Actions run 42515271388, 2026-11-08 (outputs commit 86f67f5). Block: **val only** (2021-01-21..2023-06-30). Dev and OOS untouched.
**Raw outputs:** `backtests/validation_reports/E017_results.json`, `backtests/validation_reports/E017_results.txt`.
Val trading dates 637; dropped for coverage (either leg < 275 bars): 1; used 636.

## Pre-registered test (1 trial)
Daily signed = -(mid 03:00-08:00 NY) + (mid 12:00-17:00 NY).

| n | Mean signed pips | Block-boot 95% CI (block 20) | Hit rate (Wilson CI) | Binomial p | Decision |
|---|---|---|---|---|---|
| 636 | 2.179 | (0.001, 4.265) | 0.5157 (0.4769, 0.5544) | 0.4512 | **WEAK** |

## Per leg (descriptive, not trials)
| Leg | Direction | Mean signed pips | CI | Hit | p |
|---|---|---|---|---|---|
| eu 03:00-08:00 NY | short | 1.776 | (-0.211, 3.83) | 0.511 | 0.6062 |
| us 12:00-17:00 NY | long | 0.403 | (-1.028, 1.578) | 0.522 | 0.2843 |

## Cost check (descriptive; gates only the candidate label)
Mean mid 2.179; net at bid/ask 0.018; SPEC 4 net -0.382; costs x1.5 -1.663; SPEC 4 net hit rate 0.4858.
Median spreads (pips): eu entry 0.3, exit 0.3; us entry 0.3, **exit (16:59 NY) 3.0**. Share of entries with spread > 2.0: 0.0016 per leg.
Cost gate: False. Candidate for human OOS decision: False.
