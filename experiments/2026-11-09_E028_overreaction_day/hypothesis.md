# E028 Hypothesis: intraday continuation on overreaction days (dev only; pre-registered 2026-11-09 R056, before any run)

- **H1 (B23):** on trading dates D whose EUR/USD mid move from the 17:00 NY open of D to 12:00 NY on D, r(D), lies strictly
  outside mean +/- 2 SD of r over the 60 valid dates before D (past only), a position in the direction of r(D) - mean from 12:00 NY to
  16:30 NY on D earns a mean signed mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** Caporale & Plastun (2019, Brunel WP 19-09; entry in research/academic_studies.md, opened R055): on EURUSD
  overreaction days "prices tend to change in the direction of the overreaction during the overreaction day"; their Strategy 1 follows
  the move from an intraday identification hour to day end, no costs. Their trigger uses the full-day return (not known in real time);
  this version uses only information known at entry. Data-clock to NY mapping is our assumption (**UNVERIFIED**). Every parameter was
  fixed in the backlog (R055) before any data.
- **Parent experiment / variable changed:** none formally. New variable: conditioning the afternoon return on the same day's
  17:00 -> 12:00 NY move being a 2-SD tail (relatives E021 full-day reversal with next-day hold; E024/E025 prior-day range, unsigned).
- **Prior expectation:** low. Long run of NONE/WEAK on dev; two dev SIGNALs (E022, E024) failed val. ~45-75 events, 4.5 h SD on
  large-move days ~20-25 pips -> SE ~3 pips; roughly +6 pips needed to clear the CI bar. A NONE does not rule out a small effect.
- **Why dev is clean:** no 12:00 -> 16:30 NY return signed by the same-day 17:00 -> 12:00 NY move has been computed on dev
  (E024/E025 were long-only on prior-day range; E021 conditioned on 16:00 -> 16:00 with a next-day hold).
- **Why now:** top `ready` backlog item (B23; ranked above B24 in R055, agent_decision_log.md).
