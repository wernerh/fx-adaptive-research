# E048 Conclusion (2026-11-14, R155)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule: < 300 trades -> NONE; SIGNAL if mean signed > 1.0 pip AND FX-trading-date cluster bootstrap 95% CI lower > 0 AND one-sided
t p < 0.05 (1 trial); WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B58: n 372, mean -0.744 pips, CI (-2.614, 1.137), t p 0.7897 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- A 1h close beyond the previous-24-hour high/low, followed by a 5m break-and-retest, gives no EUR/USD continuation over 60 min on dev;
  the 30- and 120-min holds and both legs do not differ from zero either.
- Entering at the breakout close without waiting for the retest (+0.312, descriptive) is also indistinguishable from zero and
  negative after SPEC 4 costs. The retest filter does not add value.
- Net of SPEC 4 costs the tested mean is -1.201 pips per trade.

## Next
B58 closed NONE (rejected_hypotheses.md); B58v closed unearned (0 trials). No dev re-test with other look-backs, retest tolerances,
windows, holds, the no-retest variant or the long leg alone. Next `ready` item: B59 (multi-timeframe alignment, human-directed).
