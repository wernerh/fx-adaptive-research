# E021 Hypothesis: next-session reversal after a large daily move (dev only; pre-registered 2026-11-09 R039, before any run)

- **H1 (B18):** after a large daily EUR/USD move on trading date D (|mid 16:00 NY on D - mid 16:00 NY on the previous trading
  date| strictly above the 80th percentile of the previous 60 valid trading dates), a position against that move from 20:00 NY on D
  to 10:45 NY on the next trading date earns a mean signed mid return > 1 pip per event. Fridays excluded (weekend belongs to B17).
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** "Significant intraday price-reversal patterns are observed in five of the seven currency futures contracts"
  after large 1-day returns and opening gaps, CME 1988-2003, mostly reversals after the euro's introduction (Rentzler, Tandon & Yu
  2006, JFM 26(11), 1089-1130, DOI 10.1002/fut.20226; abstract VERIFIED 2026-11-09 R036, research/academic_studies.md). The paper's
  threshold and horizon are UNVERIFIED; every parameter here was fixed in the backlog (R036) before any data.
- **Parent experiment / variable changed:** none (new mechanism: conditioning on a large prior-day move).
- **Prior expectation:** low. Futures data 1988-2003, possibly arbitraged away (Neely, Weller & Ulrich 2009); E020 found large
  weekend gaps extended rather than reversed. ~240 events, SE ~2.5 pips; only a mean of ~5 pips clears the CI bar.
- **Why dev is clean:** E009 scanned unconditional hour-of-day means; E019 computed 16:00-16:00 daily returns conditional only on the
  252-day sign; E020 conditioned on weekend gaps only. No return conditional on a large prior-day move has been computed on dev.
- **Why now:** top (only) `ready` backlog item (B18, added R036); B17 closed in R038.
