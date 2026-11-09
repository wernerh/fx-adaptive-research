# E022 Hypothesis: pre-ECB-fix USD appreciation on high-volatility dates (dev only; pre-registered 2026-11-09 R042, before any run)

- **H1 (B19):** on trading dates D whose previous trading date had a large EUR/USD mid range (RNG(D-1), 17:00 -> 17:00 NY, strictly
  above the 67th percentile of the 60 valid trading dates before D-1), a short EUR/USD position from 02:00 NY to 08:15 NY on D
  (ending at the ECB reference-rate fix, 14:15 CET) earns a mean signed mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** the USD "systematically appreciates against all currencies ahead of the three major currency fixes" (Krohn,
  Mueller & Whelan; JF 2024 version VERIFIED (abstract) in research/academic_studies.md; AEA 2020 draft opened 2026-11-09 R041).
  The draft's report that fix effects are larger in high-volatility / high-spread states and its EUR window 2:00-8:15 a.m. ET were
  read only via a model summary: **UNVERIFIED**. Every parameter here was fixed in the backlog (R041) before any data.
- **Parent experiment / variable changed:** none formally; one new variable (prior-day range vol-state conditioning) relative to the
  tested unconditional relatives E010 (ECB fix 1 h windows, dev WEAK) and E017 (short 03:00-08:00 NY leg of home-hours, val WEAK).
- **Prior expectation:** low. The fix line has given sub-pip or WEAK results (E007, E010, E011, E017). ~480 events, ~6 h SD
  ~25-30 pips -> SE ~1.2-1.4 pips; only a mean of ~2.5-3 pips clears the CI bar.
- **Why dev is clean:** E009 scanned unconditional weekday x hour means on dev (02:00-08:00 NY hours included); E008 used ATR as a
  control for US-window absolute moves, not for this window's signed return. No vol-conditional signed return of this window has
  been computed on dev.
- **Why now:** top `ready` backlog item (B19, added R041); ranked above B20 in R041 (window avoids 08:30 US releases and the FOMC
  14:00 statement).
