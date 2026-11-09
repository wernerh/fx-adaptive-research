# E020 Hypothesis: weekend-gap reversal (dev only; pre-registered 2026-11-09 R037, before any run)

- **H1 (B17):** after a large weekend gap (|mid 20:00 NY Sunday - mid 16:00 NY Friday| strictly above the 67th percentile of the
  previous 26 valid weekends), a position against the gap from 20:00 NY Sunday to 16:00 NY Monday earns a mean signed mid return
  > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** in spot FX, "after a large price difference between Friday close and subsequent Monday open, most markets are
  likely to reverse", read as weekend overreaction (Dao, McGroarty & Urquhart 2016, JMFM 37-38, 158-167,
  DOI 10.1016/j.mulfin.2016.11.001; abstract VERIFIED 2026-11-09 R036, research/academic_studies.md). The paper's data period, currency
  list, gap threshold and horizons are UNVERIFIED; every parameter here was fixed in the backlog (R036) before any data.
- **Parent experiment / variable changed:** none (new mechanism: weekend-gap conditioning).
- **Prior expectation:** low. ~95 events, SE ~4-5 pips; only a mean of ~8-10 pips clears the CI bar.
- **Why dev is clean:** E009 scanned unconditional weekday x hour means; E019 used 16:00 NY quotes but only a 252-day sign. No
  gap-conditional statistic has been computed on dev.
- **Why now:** top `ready` backlog item (B17, added R036); B16 closed in R035.
