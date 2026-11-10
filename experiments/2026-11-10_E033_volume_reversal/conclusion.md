# E033 Conclusion (2026-11-10, R070)

## Decision: **B28 NONE, B29 NONE on dev** (pre-registered rules `volume_reversal.decide_b28` / `decide_b29`, applied exactly). **No LEAD.**
Rule per arm: < 150 tested events -> NONE; SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.025;
WEAK if mean > 0 and (CI lower > 0 or p < 0.025); else NONE. Volume gate passed (0 zero/NaN bars), so both trials are used.
- B28: n 426 (>= 150), mean -2.034 (not > 0) -> **NONE**. t p 0.789, CI (-6.772, 3.013).
- B29: n 391 (>= 150), mean -0.213 (not > 0) -> **NONE**. t p 0.528, CI (-6.616, 4.78).
- LEAD gate fails at condition 1 for both arms. Net SPEC 4 negative in both (-2.73 / -0.894).

## Reading the result (no new numbers)
- With the Dukascopy volume proxy, neither the published low-volume next-day reversal nor the high-volume continuation appears in
  dev EUR/USD 2015-2020 over a 20:00 NY -> 16:55 NY hold. Both signs are opposite to the hypotheses (point estimates near zero, CIs
  wide: SD 52-61 pips per event as expected in the prior).
- Excluding E021-type large-move days leaves both arms at about zero, so the E021 contamination does not hide an effect.
- This does not refute the CLS-volume result (different volume measure, different sample, different hold), as stated before the run.

## Next
Per methodology: NONE -> both arms closed; no re-test with other percentiles, windows, holds or volume definitions. Added to
knowledge/rejected_hypotheses.md. No `ready` item remains: next run is a backlog refill.
