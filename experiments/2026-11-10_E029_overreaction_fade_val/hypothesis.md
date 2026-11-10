# E029 Hypothesis: next-morning fade after an overreaction day (val only; pre-registered 2026-11-10 R058, before any run)

- **H1 (B24):** on val trading dates D (Mon-Thu) whose EUR/USD open-to-close mid move R(D) (17:00 NY open of D -> 16:55 NY on D)
  lies strictly outside mean +/- 2 SD of R over the 60 valid val dates before D (past only), a position against the direction of
  R(D) - mean from 17:05 NY (start of the next trading date, after the roll) to 02:00 NY on the next trading date earns a mean signed
  mid return > 1 pip per event.
- **H0:** the mean signed return per event is zero.
- **Mechanism [PUB]:** Caporale & Plastun (2019, Brunel WP 19-09; entry in research/academic_studies.md, opened R055): after an
  EURUSD overreaction day prices "move in the opposite direction on the following day" from the start of the day to the start of the
  European session; their Strategy 2 passed for positive days (t 2.45) and failed for negative days (t 1.23), no costs. Data-clock to
  NY mapping is our assumption (**UNVERIFIED**). Every parameter was fixed in the backlog (R055) before any data.
- **Parent experiment / variable changed:** none formally. New variable: fading the overnight session after a same-day 2-SD
  open-to-close move. Relatives: E021 (dev; 16:00 -> 16:00 NY p80 move, fade 20:00 NY -> 10:45 NY next date, NONE) and E028 (dev;
  intraday continuation on 17:00 -> 12:00 NY 2-SD days, NONE).
- **Why val only:** E021 logged on dev, as descriptive, the 16:00 -> 20:00 NY move after large 16:00 -> 16:00 days (+1.666 pips
  reversal, p 0.034). It overlaps this hold (17:05 -> 20:00 NY), so dev is contaminated; the clean test is val.
- **Why val is clean for this statistic:** no val experiment has conditioned an overnight return on the previous day's move. E012
  (val) computed unconditional long 18:00 -> 19:00 NY on Wed/Thu; E017 (val) the unconditional 03:00 -> 08:00 and 12:00 -> 17:00 NY
  legs; E023/E025 (val) conditioned 02:00 -> 08:15 and 11:05 -> 16:00 NY on the unsigned prior-date range. None is this statistic.
- **Prior expectation (written before data):** low. ~620 val dates - 60 burn-in, 2-SD tail, Fridays excluded -> roughly 15-35
  events; overnight SD on large-move days ~15-20 pips -> SE ~3-5 pips, so only a mean of roughly +8 pips or more clears the CI bar.
  E021 on dev found no next-session reversal. A NONE does not rule out a small effect.
- **LEAD status:** a val-only SIGNAL cannot meet the LEAD definition (no clean dev pass). It would be logged, and any further test
  (OOS) needs a human decision (AUTONOMOUS_PROTOCOL). No notification on any outcome of this experiment alone.
- **Why now:** top (only) `ready` backlog item (B24); B23 closed in R057.
