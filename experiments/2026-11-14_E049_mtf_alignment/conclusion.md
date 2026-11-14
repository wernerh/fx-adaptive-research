# E049 Conclusion (2026-11-14, R157)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule: < 300 trades -> NONE; SIGNAL if mean signed > 1.0 pip AND FX-trading-date cluster bootstrap 95% CI lower > 0 AND one-sided
t p < 0.05 (1 trial); WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B59: n 5317, mean +0.216 pips, CI (-0.156, 0.599), t p 0.1469 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- Requiring the 1h, 30m and 15m closes to sit on the same side of their EMA20 and entering on a 5m EMA20 cross in that direction
  gives no EUR/USD edge over 60 min on dev; the estimate is precise (n 5317) and well under the 1-pip bar.
- The unfiltered 5m cross is slightly negative (-0.286, descriptive); alignment lifts it by about half a pip, which still leaves the
  rule negative after any realistic cost (SPEC 4 net -0.256, bid/ask net -0.056).
- The 10m trigger, both legs and the 30/120-min holds all sit within a fraction of a pip of zero; 2015 is the only year above 1 pip.

## Next
B59 closed NONE (rejected_hypotheses.md); B59v closed unearned (0 trials). No dev re-test with other EMA lengths, timeframes,
triggers, windows, holds, the short leg alone, or as a filter on B58. No `ready` item remains: next run is a backlog refill.
