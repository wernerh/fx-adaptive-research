# E031 Conclusion (2026-11-10, R064)

## Decision: **WEAK on dev** (pre-registered rule `gotobi_postfix.decide_b26`, applied exactly). **No LEAD.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and (CI lower > 0 or
p < 0.05); else NONE.
- mean +0.799 pips (< 1.0) and CI (-0.154, 1.632) includes 0 -> not SIGNAL. mean > 0 and t p 0.0244 < 0.05 -> **WEAK**.
- LEAD gate: condition 1 fails (WEAK, not SIGNAL). Costs: SPEC 4 net +0.290, x1.5 +0.036 pips per event (thin).

## Reading the result (no new numbers)
- The post-fix hour is positive on gotobi dates, but by the same amount as on non-gotobi dates (control +0.778, difference +0.021).
  The gotobi restriction adds nothing: this is the E011 all-date post-fix effect (WEAK, +0.785) seen on a subset, not a gotobi effect.
- The all-date post-fix hour remains a small, consistent dev pattern that does not reach the 1-pip bar and barely survives costs x1.5.
- Exploratory splits (after a pre-fix down move, not weekend-shifted, Wednesday, 2020) were read after the result and are not findings.
  Several mirror the control (control after down move +1.323), so they are not gotobi-specific either.

## Next
Per methodology: WEAK -> B26 closed; the gotobi Tokyo-fix line is closed on dev (no further windows or day rules). Added to
knowledge/rejected_hypotheses.md. No `ready` item remains: next run is a backlog refill.
