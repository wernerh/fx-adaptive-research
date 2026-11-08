# E013 Hypothesis: FOMC statement-day long EUR/USD (pre-registered 2026-11-08, before any run and before the date file exists)

- **H1 (B11):** over the 24 hours from 16:00 America/New_York on the business day before a **scheduled** FOMC statement to
  16:00 NY on the statement day, EUR/USD (mid) rises on average, by more than 10 pips.
- **H0:** mean long return over that window is zero.
- **Mechanism [PUB]:** short-USD positions earn higher excess returns on scheduled FOMC announcement days, read as compensation
  for monetary-policy uncertainty (Mueller, Tahbaz-Salehi & Vedolin 2017, JF, DOI 10.1111/jofi.12499; research/academic_studies.md,
  R016). Karnaukh (2018 WP) reports a 5-10 bp USD drift into neutral meetings.
- **Parent experiment / variable changed:** none (new information source: scheduled policy events). Follows the E012 lesson
  (target event mechanisms or liquid hours; 16:00 NY entry/exit is a liquid time with spreads far below the window's sd).
- **Prior expectation:** low-moderate. The published effect is strongest for high-yielders; EUR had a negative rate differential
  vs USD for most of 2015-2020. With n ~48 and a daily sd of ~40-50 pips, only a mean of roughly +12 pips or more can clear the bar,
  so NONE does not rule out the published few-bp effect.
- **Calendar label:** this *is* the event effect (not a fix or rollover hour).
- **Why now:** top `ready` backlog item (B11) after R016 refill.
