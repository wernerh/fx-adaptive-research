# E048 Hypothesis: 1-hour swing-level breakout, 5-minute break-and-retest entry (B58), dev only (pre-registered 2026-11-13 R154, before any run)

- **H1 (B58):** on the dev block, when a UTC 1-hour EUR/USD bar closing between 07:00 London and 12:00 New York closes above the
  highest high (below the lowest low) of the previous 24 clock hours, and price then retests that level on a 5-minute bar
  (5m low within 1 pip of the level and 5m close still beyond it) within 120 minutes without first closing back through it, a
  position in the breakout direction entered at the retest bar's close and held 60 minutes earns a mean signed mid return > 1 pip
  per trade.
- **H0:** the mean signed return per trade is zero.
- **Origin [HUMAN / PRACTITIONER]:** the human asked on 2026-11-13 (R153) for "the one hour breakout strategy with a set resistance
  ... then drop down to lower time frame for the trade" and left the definitions to the agent; they were fixed in the backlog (R153)
  before any data was seen. No published EUR/USD evidence is claimed.
- **Mechanism (practitioner reading, not verified):** a close beyond a widely visible swing level triggers stop and breakout orders;
  a shallow retest that holds marks resting demand/supply at the old level, so the move continues.
- **Parent experiment / variable changed:** none (new family: 24-hour swing-level breakouts with a lower-timeframe retest entry).
  Fill/exclusion machinery reused unchanged from E045/E047 (`round_numbers.build_trades`), hold 60 minutes.
- **Contamination note:** related, already-tested families: Asian-range breakout (E004, rejected), round-number touch fade (E045,
  NONE), pivot R1/S1 continuation (E047, NONE, -0.187). None of them used a 24-hour swing level or a retest entry; none was used to
  fix this rule. No B58 statistic has been computed in this repo. Dev usable.
- **Prior expectation:** low (technical-rule profits in developed FX largely gone: Neely-Weller 2011, Coakley-Marzano-Nankervis 2016,
  both in research/academic_studies.md; E004/E047 negative). ~267 registered trials after this one, so a single p just under 0.05
  is expected noise (lesson R092); hence the separate B58v val confirmation.
- **Why now:** top `ready` backlog item (human-directed, ranked first in R153); last research-batch run 43291084015 (E047) recorded;
  nothing queued or in progress.
