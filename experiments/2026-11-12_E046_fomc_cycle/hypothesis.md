# E046 Hypothesis: even- vs odd-week FOMC cycle, EUR/USD daily (B54), dev only (pre-registered 2026-11-12 R110, before any run)

- **H1 (B54):** on the dev block, a position s = +1 on trading dates in FOMC-cycle weeks 2, 4, 6 and s = -1 in weeks -1, 1, 3, 5
  (week 0 excluded), entered at 20:00 NY at the start of trading date D and exited at 16:55 NY on D, earns a mean signed mid return
  > 1 pip per date.
- **H0:** the mean signed return per date is zero.
- **Mechanism [PUB for equities only; EUR/USD is our extension]:** Cieslak, Morse & Vissing-Jorgensen (2014 draft, VERIFIED partial,
  research/academic_studies.md): risk-asset returns are high in even FOMC-cycle weeks and flat/negative in odd weeks, also for
  non-US equities in USD; Fed news arrives in even weeks. Our reading: even-week Fed news flow is on average accommodative / risk-on,
  which weakens the USD. Sign fixed in the backlog (R109) before data; no FX evidence in the text read.
- **Parent experiment / variable changed:** none (new family: FOMC-cycle calendar partition). Week 0 holds the statement day,
  tested in E013 (SIGNAL dev) / E014 (NONE val) and E040 (post-FOMC window): excluded here.
- **Contamination note:** no other FOMC-cycle partition has been computed in this repo (grep R109). The 20:00 -> 16:55 NY hold was
  used in E044 (different trading-date alignment; unconditional mean known as descriptive only). Dev usable.
- **Calendar label:** this *is* a calendar effect; if it ever became a lead, it is the strategy itself (LEAD criterion 4).
- **Prior expectation:** weak. 264 registered trials: a single p just under 0.05 is expected noise (lesson R092), hence B55 val.
- **Why now:** top `ready` backlog item after the R109 refill; no research-batch run queued or in progress.
