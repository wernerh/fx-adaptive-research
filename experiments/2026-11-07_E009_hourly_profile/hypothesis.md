# E009 Hypothesis: hourly return profile scan (pre-registered 2026-11-07, before any run)

- **Type:** EXPLORATORY scan (hypothesis generation), dev block only. No result of this experiment can be a SIGNAL or a lead.
- **H1 (generic):** some clock hours (UTC or New York), weekday x hour combinations, or month-end x hour combinations carry a
  persistent mean EUR/USD mid drift of at least 1 pip per hour.
- **H0:** every cell's mean hourly return is zero.
- **Mechanism [PUB, background]:** currencies tend to depreciate during their own region's trading hours (Breedon & Ranaldo 2013,
  cited in research/academic_studies.md); fixing flows and month-end rebalancing (Evans 2018; Krohn, Mueller & Whelan 2024)
  concentrate order flow at known clock times. E007 found the London-fix windows too small; this scan maps all hours at once.
- **Parent experiment / variable changed:** none (new question: unconditional time-of-day drift across all hours).
- **Why now:** backlog B3 is the top `ready` item (docs/AUTONOMOUS_PROTOCOL.md step 3).
