# E012 Conclusion (2026-11-08)

## Decision: **WEAK** (pre-registered rule, applied exactly). No lead.
Rule per test: SIGNAL if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05;
WEAK if mean signed > 0 and (CI lower > 0 or p < 0.05); else NONE.
- `wed_ny18_long` (B9): mean +0.65 pips (< 1.0), CI (-0.08, 2.02) includes 0, binom p 0.049 < 0.05 -> **WEAK**.
- `thu_ny18_long` (B10): mean +0.94 pips (< 1.0), CI (-0.36, 2.47) includes 0, binom p 0.139 -> **NONE**.

Per the pre-registration, WEAK or NONE -> hypothesis rejected for these cells; not re-tested with other hours or weekdays on val.
The cost gate also fails for both tests (net negative at bid/ask, SPEC 4 and costs x1.5), so even a SIGNAL would not have been a lead.

## What we learned
- The E009 dev candidates roughly halved on val (Wed +1.33 -> +0.65, Thu +1.24 -> +0.94 pips mid) and lost significance: the
  usual shrinkage expected from picking 2 of 192 cells.
- The 18:00 NY hour sits right after the 17:00 roll; median entry spread 1.5-1.7 pips on val, much wider than the 0.2-0.4 pips seen at
  the Tokyo fix. Mid-quote drift here is smaller than the cost of trading it. Net SPEC 4 hit rate ~0.44.
- Confirms the risk noted in B9: rollover-hour mid moves are not tradable at retail spreads.

## Next
B9 and B10 done. No `ready` items remain (B6 blocked, B7/B8 parked). Next run: refill pass per docs/AUTONOMOUS_PROTOCOL.md step 4.
