# E051 Hypothesis: random-forest classifier on 10 lagged daily returns, next-day EUR/USD direction (B62), dev only (pre-registered 2026-11-16 R212, before any run)

- **H1 (B62):** on the dev block (test dates 2016-2020), going long (short) EUR/USD from 16:00 NY on D to 16:00 NY on D+1 when a
  random forest (51 trees) trained walk-forward on the 10 most recent daily 16:00 NY log returns predicts P(up) > 0.5 (< 0.5) earns
  a mean signed mid return > 1 pip per day.
- **H0:** the mean daily signed return is zero.
- **Origin [PUB, weak]:** Theofilatos, Likothanassis & Karathanasopoulos (ETASR 2012, opened R211, entry in
  research/academic_studies.md): Random Forest on 10 lagged daily EUR/USD returns, always-in-market long/short, 53.5% hit rate and
  7.28%/yr after ~1 pip costs, 2009-2010 test sample.
- **Mechanism (story):** short-horizon nonlinear return dependence (e.g. reversal after large moves, continuation after small ones)
  that a linear AR or a sign-of-past-return rule misses.
- **Parent experiment / variable changed:** none (new family: ML classifier on lagged returns). Timing, return definition, walk-forward
  schedule (first fit to 2015-12-31, refit every 21 trading dates) and decision rule follow E050 (B60) / E019 (B16).
- **Simplifications vs the paper (stated now):** library-default hyperparameters (the paper's GA-tuned settings are not reported; no
  tuning here), 16:00 NY daily close instead of the paper's daily close, expanding window instead of the paper's fixed split.
- **Contamination note:** daily 16:00 NY returns on dev were used by E019, E037, E041, E050; no lagged-return classifier or AR model has
  been fitted on dev in this repo. Dev usable.
- **Prior expectation:** weak. Single short published sample (2009-2010), small journal, no replication. Published 8.29%/yr gross is
  ~3.7 pips/day, only just above the detection limit (CI half-width ~2.5-3 pips with n ~1,290); a NONE does not rule out a smaller
  effect. ~270 registered trials after this one (lesson R092): a single p just under 0.05 is expected noise, hence the separate B63
  val confirmation.
- **Why now:** top `ready` backlog item (B62, added R211); last research-batch run 43817068619 (E050) recorded R210; nothing queued
  or in progress.
