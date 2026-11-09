# E023 Hypothesis: pre-ECB-fix USD appreciation on high-volatility dates, VAL confirmation of E022 (pre-registered 2026-11-09 R044, before any run)

- **H1 (B19v):** on val trading dates D whose previous trading date had a large EUR/USD mid range (RNG(D-1), 17:00 -> 17:00 NY,
  strictly above the 67th percentile of the 60 valid trading dates before D-1), a short EUR/USD position from 02:00 NY to 08:15 NY
  on D earns a mean signed mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Parent experiment:** E022 (B19), dev SIGNAL (marginal): n 473, mean +3.646 pips, block-boot CI (0.011, 7.751), one-sided t p
  0.0133 (backtests/validation_reports/E022_results.json, run 42585915012). **Variable changed (one):** block (dev -> val).
- **Mechanism [PUB]:** as E022 (Krohn, Mueller & Whelan, USD appreciates ahead of the major fixes; vol-state amplification and the
  2:00-8:15 a.m. ET window UNVERIFIED, model summary only).
- **Prior expectation (written before data):** low-to-moderate. The dev CI lower bound was barely above 0; the normal-date control was
  also positive (+1.731, CI incl 0), so the conditioning is not shown to matter. ~190 val events x SD ~30-36 pips -> SE ~2.2-2.6
  pips: a val mean near the dev +3.6 would most likely give WEAK, not SIGNAL. The rule is not loosened for this.
- **Why val is clean for this statistic:** E017 computed the unconditional short 03:00-08:00 NY leg on val (+1.776, as one leg of
  home-hours). No vol-conditional 02:00-08:15 NY signed return has been computed on val.
- **Why now:** top `ready` backlog item (B19v, ranked above B20 in R043, reason in agent_decision_log.md).
