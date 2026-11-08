# E012 Hypothesis: NY 18:00 hour long drift on trading-date Wednesday and Thursday, val confirmation (pre-registered 2026-11-08, before any run)

- **H1 (B9):** on FX trading dates that are Wednesdays, the EUR/USD mid return over 18:00-19:00 America/New_York is positive, > 1 pip on average.
- **H1 (B10):** the same for trading-date Thursdays.
- **H0:** mean signed (long) return is zero.
- **Origin [EXP, dev-derived]:** E009 exploratory scan (192 cells, dev) flagged two CANDIDATE cells under its pre-registered rule:
  Wed_ny_18 +1.333 pips, CI (0.703, 2.055), t p 2.0e-5, n 312; Thu_ny_18 +1.240 pips, CI (0.749, 2.024), t p 9.5e-5, up-share 0.654, n 313
  (backtests/validation_reports/E009_results.json). Pooled ny_18 (all weekdays) +0.866 pips, up-share 0.595 (NONE, below 1 pip).
- **Mechanism [hypothesis, unverified]:** post-roll (17:00 NY) liquidity rebuild / early Asia-Pacific (Sydney, Wellington) flow.
  **Main alternative (artifact):** spreads are widest just after the 17:00 roll and normalise during 18:00-19:00; if the ask side
  normalises faster or slower than the bid, the *mid* drifts with no tradable move. A pooled up-share of 0.595 across all weekdays
  fits this artifact as well as a real drift. The bid/ask cost check is designed to separate the two.
- **Parent experiment / variable changed:** E009; variable changed = block (dev -> val), cells fixed in advance. Backlog B9 and B10
  ("may share one experiment run but are 2 trials").
- **Prior expectation:** low-moderate. Two cells selected from 192 on dev regress towards the pooled +0.87 even if real, and val
  (2021-2023) is a different regime.
- **Why now:** top `ready` backlog item (B9), with B10 sharing the run as the backlog allows.
