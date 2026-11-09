# E024 Hypothesis: post-London-fix EUR appreciation on high-volatility dates (dev only; pre-registered 2026-11-09 R046, before any run)

- **H1 (B20):** on trading dates D whose previous trading date had a large EUR/USD mid range (RNG(D-1), 17:00 -> 17:00 NY, strictly
  above the 67th percentile of the 60 valid trading dates before D-1), a long EUR/USD position from 11:05 NY to 16:00 NY on D
  (starting after the 5-minute WM/R London 4pm fix window) earns a mean signed mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** the USD depreciates after the fixes; EUR "strongly increase[s] in value against the U.S. dollar between
  8:00 a.m. and 5:00 p.m." (Krohn, Mueller & Whelan AEA 2019 draft, opened 2026-11-09 R041; JF 2024 version VERIFIED (abstract) in
  research/academic_studies.md). Vol-state amplification and the 11:00 a.m.-5:00 p.m. ET window: **UNVERIFIED** (model summary
  only). Every parameter here was fixed in the backlog (R041) before any data.
- **Parent experiment / variable changed:** none formally; one new variable (prior-day range vol-state conditioning, identical
  definition to E022) relative to the unconditional relatives E007 (London fix 1 h windows, dev NONE) and E017 (long 12:00-17:00 NY
  leg of home-hours, val WEAK).
- **Prior expectation:** low. E022 (same condition, pre-ECB-fix short) was a marginal dev SIGNAL that did not confirm on val (E023
  NONE). The fix line has given sub-pip, WEAK or unconfirmed results (E007, E010, E011, E017, E022/E023). ~480 events, ~5 h SD
  ~22-28 pips -> SE ~1.1-1.3 pips.
- **Why dev is clean:** E009 scanned unconditional weekday x hour means on dev; E007 computed unconditional 1 h post-fix windows on
  dev. No vol-conditional signed return of 11:05-16:00 NY has been computed on dev.
- **Independence from E022/E023:** fixed in R041 that B20 does not depend on B19's result; it is a separate trial. The E023 val
  failure is recorded here as context only and changes no parameter.
- **Why now:** top (only) `ready` backlog item.
