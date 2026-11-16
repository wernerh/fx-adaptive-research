# E051 Conclusion (2026-11-16, R213)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule (E019): SIGNAL if mean daily signed > 1.0 pip AND moving-block bootstrap (block 20, 2000 draws, seed 0) 95% CI lower > 0 AND
one-sided t p < 0.05 (1 trial); WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- B62: n 1241, mean +1.953 pips, CI (-1.244, 4.581), t p 0.0852 -> mean > 1 pip but CI lower < 0 and p > 0.05, so not SIGNAL;
  mean > 0 but neither CI lower > 0 nor p < 0.05, so not WEAK -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- The point estimate is positive and above 1 pip, but with daily SD ~50 pips the test cannot separate it from zero; the power note
  in B62 said a NONE does not rule out a smaller effect. This is not evidence for an edge and must not be read as "nearly significant".
- The by-year pattern is uneven (one negative year, 2019 carries much of the mean), and feature importances are flat across lags,
  which is what a forest fitted mostly to noise looks like.
- Turnover is high (a flip roughly every 2 days), but costs are small relative to the gross mean at the 0.2-pip median spread; the
  failure is statistical, not costs.

## Next
B62 closed NONE (rejected_hypotheses.md); B63 closed unearned (0 trials). No dev re-test with other tree counts, lag counts, refit
intervals, probability thresholds, other classifiers or one leg (rule 7: no loosening). Next run: backlog refill unless an item is ready.
