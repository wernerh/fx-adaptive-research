# E021 Conclusion (2026-11-09, R040)

## Decision: **NONE on dev** (pre-registered rule `daily_reversal.decide_b18`, applied exactly). **No lead.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean -2.55 pips (not > 0), CI (-7.097, 4.167) includes 0, one-sided t p 0.7756 -> **NONE**.
- Per the methodology, B18 is closed for this definition; no re-test with other thresholds, windows or horizons on dev.
- Cost check also negative: SPEC 4 net -3.041, costs x1.5 -3.287 pips per event.

## Reading the result (cautions, no new numbers)
- The intraday reversal after large 1-day moves reported for CME currency futures 1988-2003 (Rentzler, Tandon & Yu 2006) did not
  appear in 2015-2020 EUR/USD spot over the next Asian/London session at the 1-pip bar; the hit rate was 0.493.
- The up/down asymmetry (+6.6 after up moves, -12.1 after down moves) mostly mirrors the dev-period EUR/USD downtrend; it is post-hoc
  and not evidence. Any direction-split test needs its own pre-registration on fresh data and counts as a new trial.
- The small 16:00-20:00 NY reversal before entry is descriptive only (CI includes 0) and is not tradable under SPEC session rules.
- Power note held: SE ~3.4 pips; NONE does not rule out a reversal of a few pips.

## Next
B18 closed (recorded in knowledge/rejected_hypotheses.md). Backlog has no `ready` items -> next run refills.
