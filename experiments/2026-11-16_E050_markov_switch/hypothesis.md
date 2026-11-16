# E050 Hypothesis: 2-state Markov switching expected-return rule, daily EUR/USD (B60), dev only (pre-registered 2026-11-16 R209, before any run)

- **H1 (B60):** on the dev block (test dates 2016-2020), going long (short) EUR/USD from 16:00 NY on D to 16:00 NY on D+1 when the
  8-day expected return of a 2-state Markov switching model (switching mean and variance, fitted walk-forward on daily 16:00 NY log
  returns up to D) is positive (negative) earns a mean signed mid return > 1 pip per day.
- **H0:** the mean daily signed return is zero.
- **Origin [PUB]:** Dueker & Neely (St. Louis Fed WP 2001-021 / JBF; opened R208, verbatim in research/academic_studies.md): a
  Markov switching model of daily excess FX returns traded on the sign of its average expected return over eight days earns positive
  out-of-sample returns net of 10 bp costs (DEM/EUR, JPY, CHF, GBP vs USD, to 2005). Parikakis & Merika (2009, abstract only)
  report out-of-sample gains for EUR/USD with this rule family.
- **Mechanism:** persistent mean/volatility regimes ("long swings") that filtered regime probabilities pick up early.
- **Parent experiment / variable changed:** none (new family: regime-model expected-return signal). Timing, return definition,
  exclusions-style and decision rule follow E019 (B16, 12-month TSMOM, NONE).
- **Simplifications vs the paper (stated now):** spot only (no interest differential; carry not in data), 2 states, Gaussian errors,
  no kurtosis switching, constant transition matrix.
- **Contamination note:** daily 16:00 NY returns on dev were used by E019 (sign of 252-day return), E037, E041; no regime model or
  multi-day expected-return statistic has been computed on dev in this repo. Dev usable.
- **Prior expectation:** weak. Published sample ends 2005 (technical-rule decay, Neely-Weller-Ulrich 2009); the published gain is
  ~5.27%/yr ≈ 2 pips/day, close to the detection limit (CI half-width ~2.5-3 pips with n ~1,290). A NONE does not rule it out.
  ~269 registered trials after this one (lesson R092): a single p just under 0.05 is expected noise, hence the separate B61 val
  confirmation.
- **Why now:** top `ready` backlog item (B60, added R208); last research-batch run 43541310326 (E049) recorded; nothing queued or in
  progress.
