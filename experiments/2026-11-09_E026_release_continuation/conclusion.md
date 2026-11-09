# E026 Conclusion (2026-11-09, R052)

## Decision: **NONE on dev** (pre-registered rule `release_continuation.decide_b21`, applied exactly). **No LEAD.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean -0.42 pips (not > 0), CI (-5.278, 2.488) includes 0, one-sided t p 0.5639 -> **NONE**.
- LEAD gate: condition 1 fails; costs also negative (SPEC 4 net -0.896, x1.5 -1.135).

## Reading the result (no new numbers)
- After a large 08:30 -> 08:45 NY move, the next two hours show no continuation on dev: the event mean (-0.42) is indistinguishable
  from the non-event control (-0.465). The p80/p95 and alternative-horizon readings (descriptive) also show no positive continuation.
- The order-flow papers (Evans & Lyons 2008; Love & Payne 2008) describe how news is incorporated, not a tradable 2-hour drift
  after 08:45; on 1-minute EUR/USD data 2015-2020 the move after the first 15 minutes looks fully incorporated at this horizon.
- Prior written before data (low to moderate; NONE likely) held. A small effect (< ~4 pips) is not ruled out by this power.

## Next
Per methodology: B21 closed for this definition; no re-test on dev with other percentiles, windows or horizons. Added to
knowledge/rejected_hypotheses.md. Next `ready` item: B22 (London-open intraday momentum).
