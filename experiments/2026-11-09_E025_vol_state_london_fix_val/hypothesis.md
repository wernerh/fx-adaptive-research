# E025 Hypothesis: post-London-fix EUR appreciation on high-volatility dates, VAL confirmation of E024 (pre-registered 2026-11-09 R048, before any run)

- **H1 (B20v):** on val trading dates D whose previous trading date had a large EUR/USD mid range (RNG(D-1), 17:00 -> 17:00 NY,
  strictly above the 67th percentile of the 60 valid trading dates before D-1), a long EUR/USD position from 11:05 NY to 16:00 NY
  on D earns a mean signed mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Parent experiment:** E024 (B20), dev SIGNAL: n 472, mean +2.983 pips, block-boot CI (0.566, 4.847), one-sided t p 0.0053
  (backtests/validation_reports/E024_results.json, run 42617055931). **Variable changed (one):** block (dev -> val).
- **Mechanism [PUB]:** as E024 (Krohn, Mueller & Whelan, USD depreciates after the London fix; vol-state amplification and the
  11:00 a.m.-5:00 p.m. ET window UNVERIFIED, model summary only).
- **Prior expectation (written before data):** low-to-moderate. The sibling E022 (same condition, ECB fix) failed val in E023. In
  E024 the normal-date control was +0.901 (CI incl 0) and all dates +1.562, so the conditioning is not shown to matter; 2018-2019
  were negative. ~200 val events x SD ~25 pips -> SE ~1.8 pips: a val mean near the dev +3.0 could give WEAK, not SIGNAL. The rule
  is not loosened for this.
- **Why val is clean for this statistic:** E017 computed the unconditional long 12:00-17:00 NY leg on val (WEAK, as one leg of
  home-hours). No vol-conditional 11:05-16:00 NY signed return has been computed on val.
- **Why now:** only `ready` backlog item (B20v, fixed in E024's methodology before data).
