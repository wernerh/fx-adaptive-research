# E026 Hypothesis: post-08:30 NY release-window continuation, calendar-free (dev only; pre-registered 2026-11-09 R051, before any run)

- **H1 (B21):** on trading dates D whose 08:30 -> 08:45 NY EUR/USD mid move J(D) is large (|J(D)| strictly above the 90th
  percentile of |J| over the 60 valid dates before D, past only), a position in the direction of J(D) from 08:45 NY to 10:45 NY on D
  earns a mean signed mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** macro news reaches exchange rates partly through subsequent order flow (Evans & Lyons 2008, JFE 88(1), 26-50:
  about two-thirds of the news effect via order flow; Love & Payne 2008, JFQA 43(2), 467-488: about one third of price-relevant
  information incorporated via trading); both VERIFIED (abstract) in research/academic_studies.md R050. Neither paper states a
  tradable post-release drift or its horizon (**UNVERIFIED**); the continuation hypothesis and every parameter were fixed in the
  backlog (R050) before any data, not taken from the papers.
- **Parent experiment / variable changed:** none formally. New variable relative to E006 (08:35-09:30 NY window with E001 session
  predictors): conditioning on the 08:30-08:45 jump itself. Calendar-free route to the release question B12 could not test.
- **Prior expectation:** low to moderate. Long run of NONE/WEAK on dev; two dev SIGNALs (E022, E024) failed val. ~145 events, 2 h SD
  after a large release move ~20-25 pips -> SE ~1.8-2.1 pips; roughly +4 pips needed to clear the CI bar. A NONE does not rule out a
  small effect.
- **Why dev is clean:** E006 tested 08:35-09:30 NY with session predictors, not the 08:30 jump; E009 scanned unconditional hour means.
  No return conditional on the 08:30-08:45 move has been computed on dev.
- **Why now:** top `ready` backlog item (B21; ranked above B22 in R050, agent_decision_log.md).
