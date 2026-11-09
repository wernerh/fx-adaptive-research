# E023 Conclusion (2026-11-09, R045)

## Decision: **NONE on val** (pre-registered rule `vol_state_fix.decide_b19`, applied exactly). **No LEAD.** E022 not confirmed.
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean +1.197 pips (> 1.0) but CI (-3.144, 5.919) includes 0 and one-sided t p 0.304 (>= 0.05) -> neither WEAK condition holds -> **NONE**.
- LEAD gate: condition 2 (val pass) fails, so no lead regardless of the positive net cost check (SPEC 4 +0.622, x1.5 +0.335).

## Reading the result (no new numbers)
- The val mean on high-vol dates (+1.197) is about the same as on normal val dates (+1.15) and all val dates (+1.167): no sign that
  the prior-day range conditioning adds anything, as already suspected from the dev control. The dev result (+3.646, CI lower 0.011)
  is best read as a marginal chance/regime outcome among ~237 trials.
- A small unconditional European-morning USD-up drift (~+1 pip, n.s. on val) remains consistent with E010/E017/E022 but is below a
  tradable size and has been seen on both dev and val; it cannot be cleanly re-tested without fresh data.
- The prior expectation written before data (val most likely WEAK or NONE) held.

## Next
Per methodology: B19 line closed for this definition; no re-test with other percentiles, windows, vol measures or blocks. Added to
knowledge/rejected_hypotheses.md. B20 (post-London-fix, dev) is the next `ready` item and proceeds independently.
