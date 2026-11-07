# E007 Conclusion (2026-11-07)

## Decision: **NONE** (pre-registered rule, applied exactly)
Rule per test: SIGNAL if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.0125;
WEAK if mean signed > 0 and (CI lower > 0 or p < 0.05). No test met either condition. **B1v (val) is not queued.**

## What we learned
- Both full-sample effects point in the predicted direction (pre +0.64, post +0.48 pips signed) but are small, below the 1.0-pip
  bar, and both bootstrap CIs include 0. Even if real, they are a fraction of a round-trip cost.
- Month-end subsets (n = 72) go the **opposite** way to the hypothesis. `post_month_end` signed mean is -4.51 pips with a
  bootstrap CI of (-7.19, -1.88), i.e. EUR/USD tended to **fall** (USD continued up) in the hour after the month-end fix.
  The binomial test is not significant (hit rate 0.417, p = 0.19), so the mean is driven by a few large moves.
  This is **exploratory and post hoc** (wrong sign vs pre-registration, 1 of 4 trials, n = 72). It is not a signal and must not be
  traded or tuned on dev. It may only become a hypothesis via a new pre-registered test on val (see backlog B8).
- The 15:00-16:00 London window is volatile (mean |return| 13.3 pips; 19.7 pips at month end), consistent with Evans (2018).

## Next
B1 done. Next ready backlog item: B2 (volatility timing).
