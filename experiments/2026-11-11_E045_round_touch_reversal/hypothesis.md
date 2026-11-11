# E045 Hypothesis: take-profit reversal at round numbers, rejected touches (B52), dev only (pre-registered 2026-11-11 R103, before any run)

- **H1 (B52):** on the dev block, after the first 1-minute EUR/USD bar of a trading date that touches a round level (multiple of
  0.0050, "00/50") and closes back on the side it came from (rejected touch), a position fading the level (short after an up-touch,
  long after a down-touch) entered at t + 1 min and held 60 minutes earns a mean signed mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** Osler (2003, JF 58(5), 1791-1819, DOI 10.1111/1540-6261.00588, abstract VERIFIED 2026-11-07): take-profit
  orders cluster at round numbers, "which helps explain reversals at support and resistance". 00/50 level definition from Osler (2002,
  VERIFIED abstract); Osler 2003's own digit definition, hour-scale persistence and exact touch definition UNVERIFIED.
- **Parent experiment / variable changed (one):** E018 (B15, stop-loss arm: continuation after a close crosses a level, NONE on dev).
  Changed: the event (rejected touch instead of close crossing) with the sign the take-profit arm implies (fade). Levels, fills,
  exclusions, horizon and control levels as E018.
- **Contamination note:** E018 dev results are known for close-crossing events (mean -0.128, controls -0.803, 15/120 min
  -0.405/-0.777). Rejected-touch events are disjoint from E018 events at bar t, but later crossings on the same date overlap in time.
  The sign is fixed from Osler (2003), not from E018. No touch-based statistic has been computed on dev. Dev usable.
- **Prior expectation:** weak (E018 round crossings reversed less than control crossings; 1990s order data may not describe modern
  e-trading, lesson R033; E043 found no hour-scale post-move drift). ~263 registered trials: a single p just under 0.05 is expected
  noise (lesson R092), hence the separate val confirmation (B53) before anything counts.
- **Why now:** top (only) `ready` backlog item after the R102 refill; no research-batch run queued or in progress.
