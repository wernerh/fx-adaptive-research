# E007 Hypothesis: London 4pm fix reversal (pre-registered 2026-11-07, before any run)

- **H1:** around the WM/Reuters 4pm London fix the USD appreciates into the fix and depreciates after it. For EUR/USD:
  mid return over 15:00-16:00 Europe/London is negative on average (pre), and over 16:00-17:00 Europe/London positive (post).
  The effect is expected to be stronger on the last trading day of the month (month-end rebalancing flows).
- **H0:** the mean signed return (short pre / long post) is zero.
- **Mechanism [PUB]:** Krohn, Mueller & Whelan (2024, Journal of Finance) document USD appreciation into the fix and reversal
  after; Evans (2018, Journal of Banking & Finance) finds high volatility and negative autocorrelation around the fix,
  strongest at month end. Citations as listed in research/academic_studies.md.
- **Parent experiment / variable changed:** none (new information source: calendar/fixing flow instead of session-price structure).
  The 16:00 London fix sits at 11:00 NY, inside the US window tested in E001 (SPEC 2 confound note; SPEC 8 E005).
- **Why now:** backlog B1 (top `ready` item); R002 decision log recommended pivoting to scheduled-flow effects after E001/E004/E006.
