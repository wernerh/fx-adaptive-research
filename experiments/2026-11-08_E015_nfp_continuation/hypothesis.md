# E015 Hypothesis: NFP first-15-minute reaction continues over the next hour (pre-registered 2026-11-08 R023, before any run and before the date file exists)

- **H1 (B12):** on US Employment Situation release days (08:30 America/New_York), the EUR/USD mid move over 08:45-09:45 NY has
  the same sign as the first 15-minute reaction (08:30-08:45 NY): mean of sign(r1) x r2 > 1.0 pip.
- **H0:** mean continuation return is zero (efficient-market prior: the news is priced within ~15 minutes).
- **Mechanism [PUB]:** scheduled US releases move FX within minutes (Andersen, Bollerslev, Diebold & Vega 2003, AER); for DEM/USD
  the news effect is significant over the first ~15 minutes and fades at longer horizons (Almeida, Goodhart & Payne 1998, JFQA,
  DOI 10.2307/2331101; research/academic_studies.md). A continuation would point to slow liquidity rebuilding after the release
  (microstructure), not new information.
- **Parent experiment / variable changed:** none (new information source: scheduled US data releases; first piece of B6's calendar).
- **Prior expectation:** low. The literature points to fast absorption; the efficient-market prior is no continuation.
- **Why monthly events:** E014 lesson: 8-per-year events cannot be confirmed on val. NFP gives ~72 dev and ~29 val releases.
- **Calendar label:** release-time effect. 08:45-09:45 NY is a liquid hour (London/NY overlap).
- **Why now:** top `ready` backlog item (B12) after B11 closed in R022.
