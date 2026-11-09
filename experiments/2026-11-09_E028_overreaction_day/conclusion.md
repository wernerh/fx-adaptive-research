# E028 Conclusion (2026-11-09, R057)

## Decision: **NONE on dev** (pre-registered rule `overreaction_day.decide_b23`, applied exactly). **No LEAD.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean +1.061 (> 1.0) but CI (-5.625, 8.569) includes 0 and one-sided t p 0.3897 -> neither WEAK condition holds -> **NONE**.
- LEAD gate: condition 1 fails. Net after costs is barely positive (SPEC 4 +0.507, x1.5 +0.229) but not significant.

## Reading the result (no new numbers)
- With 74 events and SD ~32 pips the test has SE ~3.8 pips, as the power note expected; a +1 pip mean is indistinguishable from zero
  and from the non-event control (+1.108). The overreaction trigger adds nothing over an unconditional afternoon hold.
- The up-move subset looks positive and the down-move subset negative. That pattern is what a general EUR appreciation drift on the
  afternoon would produce (both subsets share the long-afternoon component), it was not pre-registered, and 2020 alone (-12.97 on 18
  events) swings the total. It is not a basis for a new test on dev.
- The Caporale-Plastun intraday continuation finding (full-day trigger, no costs) does not transfer to a real-time 12:00 NY trigger on
  2015-2020 EUR/USD. Prior written before data (low) held.

## Next
Per methodology: B23 closed for this definition; no re-test on dev with other k, windows or hours. Added to
knowledge/rejected_hypotheses.md. Next `ready` item: B24 (val only).
