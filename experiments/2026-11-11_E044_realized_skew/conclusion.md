# E044 Conclusion (2026-11-11, R101)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule: < 500 tested dates -> NONE; SIGNAL if mean signed > 1.0 pip AND block-20 bootstrap 95% CI lower > 0 AND one-sided t p < 0.05
(1 trial); WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B50: n 1238 dates, mean -0.183 pips, CI (-3.845, 4.329), t p 0.5436 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- The sign of daily realized skewness carries no information about the next ~21 hours of EUR/USD on dev; the mean is essentially zero
  and the 1-minute RS version is also flat (+0.181). Net of SPEC 4 costs it is -0.865 pips.
- RS is strongly tied to the plain daily return (corr 0.564), so this largely restates the E033 window's known null for daily-return
  conditioning (B28/B29 NONE). The within-R(D) halves move in opposite directions but both CIs span zero.
- The high-|RS| tercile (+3.279) is post-hoc and its CI spans zero; it is not queued (lesson R076).
- Jiang, Han & Yin (2019) is a cross-sectional currency result; this time-series EUR/USD test does not refute it.

## Next
B50 closed NONE (rejected_hypotheses.md); B51 closed unearned (0 trials). No dev re-test with |RS| subsets, other return
frequencies, windows or the opposite sign. No `ready` item remains: next run is a backlog refill.
