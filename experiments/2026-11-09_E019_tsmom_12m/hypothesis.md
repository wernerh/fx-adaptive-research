# E019 Hypothesis: time-series momentum, 12-month lookback, daily hold (dev only; pre-registered 2026-11-09 R034, before any run)

- **H1 (B16):** on each trading date D, holding EUR/USD in the direction of its trailing 252-trading-date mid change
  (16:00 NY to 16:00 NY) from 16:00 NY on D to 16:00 NY on the next trading date earns a mean daily signed mid return > 1 pip.
- **H0:** the mean daily signed return is zero.
- **Mechanism [PUB]:** "persistence in returns for one to 12 months that partially reverses over longer horizons" across 58 futures
  including currencies, attributed to initial under-reaction and delayed over-reaction (Moskowitz, Ooi & Pedersen 2012, JFE 104(2),
  228-250, DOI 10.1016/j.jfineco.2011.11.003; abstract opened 2026-11-08 R031). Evidence is portfolio-level; one pair over ~5 test
  years has low power.
- **Parent experiment / variable changed:** none (new mechanism: multi-day trend; all of E001-E018 are intraday or event windows).
- **Prior expectation:** low. Single pair, short sample, the 1-pip daily bar needs ~10%/yr.
- **Why dev is clean:** no daily-horizon or multi-day trend statistic has been computed on dev (E001-E018 are intraday/event).
- **Why now:** top `ready` backlog item (B16, added R031); B15 closed in R033.
