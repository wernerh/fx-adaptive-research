# E052 Conclusion (2026-11-20, R309)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule (`btc_lag.decide_b64`, B16): data gate >= 90% (passed, 0.9705); >= 500 tested dates (911); SIGNAL if mean daily signed > 1.0 pip
AND moving-block bootstrap (block 20, 2000 draws, seed 0) 95% CI lower > 0 AND one-sided t p < 0.05 (1 trial); WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- B64: n 911, mean +2.278 pips, CI (-0.674, 5.176), t p 0.0779 -> mean > 1 pip but CI lower < 0 and p > 0.05, so not SIGNAL;
  mean > 0 but neither CI lower > 0 nor p < 0.05, so not WEAK -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- As pre-registered, the published effect (~1-1.5 pips/day gross) is below our dev detection limit; a NONE does not refute
  Feng & Zhang, and the positive point estimate is not evidence for an edge.
- The Tue-Fri subset has t p < 0.05 and the high-|B| tercile has the largest mean, but these are descriptive splits, not
  pre-registered tests; both bootstrap CIs include zero. Testing either now would be a post-hoc subset (rule 7, lesson R076).
- One negative year (2017), and the signal mean is only ~1.2 pips above buy-and-hold on the same dates (long share 0.53 in a
  sample where EUR/USD drifted up), so part of the point estimate is drift exposure.
- Costs are not the binding constraint (SPEC 4 net +2.035, x1.5 +1.913); the failure is statistical.

## Next
B64 closed NONE (rejected_hypotheses.md); B65 closed unearned (0 trials). No dev re-test with Tue-Fri only, |B| thresholds, other
lags, other crypto, other hold times or closing times. Trials dev 262, val 9, total 271. Next run: backlog refill unless an item is ready.
