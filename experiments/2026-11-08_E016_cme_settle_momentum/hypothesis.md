# E016 Hypothesis: intraday momentum into the CME FX futures settlement shows up in spot EUR/USD (pre-registered 2026-11-08 R026, before any run and before the settlement file exists)

- **H1 (B13):** on weekday trading dates, the EUR/USD mid return over the last 30 minutes before the CME FX futures daily
  settlement time S (America/Chicago) has the same sign as the return from the 17:00 NY roll to S - 30 min:
  mean of sign(r1) x r2 > 1.0 pip.
- **H0:** mean signed return is zero (no intraday momentum into the settlement).
- **Mechanism [PUB]:** across 60+ futures including currencies, the rest-of-day return predicts the last-30-minute return before
  the futures close; attributed to gamma hedging by option market makers and leveraged products (Baltussen, Da, Lammers &
  Martens 2021, JFE, DOI 10.1016/j.jfineco.2021.04.029; research/academic_studies.md, VERIFIED (abstract) 2026-11-07).
  Hedging in 6E futures should pass to spot by arbitrage.
- **Parent experiment / variable changed:** none (new mechanism: futures-settlement hedging flow).
- **Prior expectation:** low-to-moderate. Published on futures, not spot; spot EUR/USD is much deeper than 6E, so any
  transmitted effect should be smaller. E007/E010/E011 found sub-pip time-of-day effects, so the 1-pip bar may bind.
- **Contamination note:** E009 scanned unconditional hourly means on dev; this conditional (sign-agreement) statistic was not
  computed there, so dev is still usable for this test.
- **Calendar label:** futures-settlement effect; not the London 4pm fix (11:00 NY) or the 17:00 NY roll.
- **Why now:** top `ready` backlog item (B13) after the R025 refill.
