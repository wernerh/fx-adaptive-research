# E052 Hypothesis: lagged daily Bitcoin return -> next-day EUR/USD (B64), dev only (pre-registered 2026-11-20 R308, before any run)

- **H1 (B64):** on dev test dates 2017-05-09..2020-12-31, going long (short) EUR/USD from 16:00 NY on D to 16:00 NY on the next
  trading date when BTC/USD rose (fell) from 16:00 NY on the previous trading date to 16:00 NY on D earns a mean signed mid return
  > 1 pip per day.
- **H0:** the mean daily signed return is zero.
- **Origin [PUB, EUR-specific OOS, gross only]:** Feng & Zhang, "Currency exchange rate predictability: The new power of Bitcoin
  prices", JIMF 132 (2023) 102811, doi:10.1016/j.jimonfin.2023.102811 (opened R307; entry in research/academic_studies.md). EUR row,
  daily OOS direction-of-change 51.79%, Clark-West 2.0081; in-sample b1 for EUR positive. Paper's FX closing time UNVERIFIED; the
  16:00 NY convention here is our adaptation.
- **Mechanism (story):** Bitcoin as a 24/7 risk-appetite / dollar-sentiment gauge: BTC up -> USD weaker -> EUR/USD up next day.
- **Parent experiment / variable changed:** none (new family: lagged crypto cross-market signal). Hold, return definition and
  decision rule follow E050/E051 (B16 rule, 16:00 NY daily hold); source market is new.
- **Contamination note:** daily 16:00 NY EUR/USD returns on dev were used by E019, E041, E042, E050, E051; no Bitcoin series has been
  used in this repo. Dev usable.
- **Prior expectation:** weak. Published 51.79% DoC implies ~1-1.5 pips/day gross, below our detection limit (SE ~1.5 pips at
  n ~900, CI half-width ~3 pips): a NONE does not rule out the published effect; a SIGNAL would mean a larger effect than published
  (treat with suspicion). 271 registered trials after this one (lesson R092).
- **Why now:** top `ready` backlog item (B64, added R307); last research-batch run 43840273851 (E051) recorded R213; nothing queued
  or in progress.
