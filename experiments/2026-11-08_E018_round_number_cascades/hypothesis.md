# E018 Hypothesis: round-number crossing continuation, "price cascades" (dev only; pre-registered 2026-11-08 R032, before any run)

- **H1 (B15):** after EUR/USD mid first crosses a round level (multiple of 0.0050, rates ending 00 or 50) on a trading date, the mid
  return over the next 60 minutes, signed by the crossing direction, is positive and > 1 pip on average (continuation).
- **H0:** the mean signed 60-minute return after a first crossing is zero.
- **Mechanism [PUB]:** stop-loss orders cluster just beyond round numbers, so crossing one triggers stops and a rapid self-reinforcing
  move; "Most results are statistically significant for hours, although not for days" (Osler 2002, FRBNY Staff Report 150, opened
  2026-11-08 R031; journal version 2005, venue UNVERIFIED). Consistent with Osler (2003, JF, VERIFIED (abstract)): stops cluster beyond
  round numbers, take-profits at them. Data are 1990s/2000 dealer orders; e-trading may have arbitraged the effect away
  (Neely, Weller & Ulrich 2009).
- **Parent experiment / variable changed:** none (new mechanism: price-level conditioning). Nearest prior: E006 (Asian-range false
  breaks, NONE).
- **Prior expectation:** low-to-moderate. A published microstructure mechanism, but on 20-year-old data, and EUR/USD is now one of the
  most liquid and algorithmically traded markets.
- **Why dev is clean:** E009 scanned unconditional hour-of-day means; E006 tested Asian-range breaks. No price-level-conditional statistic
  has been computed on dev.
- **Why now:** top `ready` backlog item (B15, added R031).
