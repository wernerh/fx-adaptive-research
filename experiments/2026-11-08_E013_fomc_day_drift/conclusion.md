# E013 Conclusion (2026-11-08, R020)

## Decision: **SIGNAL on dev** (pre-registered rule, applied exactly). **Not a lead yet.**
Rule: SIGNAL if mean > 10.0 pips AND block-bootstrap (block 4) 95% CI lower > 0 AND one-sided t p < 0.05.
- Long EUR/USD 16:00 NY (prev business day) -> 16:00 NY (scheduled FOMC statement day): n 47, mean +21.28 pips, median +28.3,
  hit 0.617, t p 0.029, CI (2.75, 38.16) -> **SIGNAL**.
- Cost check passes on dev (net +20.81 at SPEC 4, +20.57 at costs x1.5; median entry spread 0.2 pips), but per
  docs/AUTONOMOUS_PROTOCOL.md a LEAD also needs a pre-registered val confirmation. Per the methodology: SIGNAL -> pre-register B11v
  (val only, same window and rule, 1 trial).

## Reading the result (cautions, no new numbers)
- Direction matches the published mechanism (USD weaker on scheduled FOMC days; Mueller, Tahbaz-Salehi & Vedolin 2017) and the
  non-FOMC benchmark in the same window is flat (-0.39 pips, CI includes 0), so it is not general USD drift over dev.
- The evidence is thin: CI lower bound 2.7 pips, p 0.029 on one trial out of 227 dev trials so far. Per-meeting SD (75 pips) is
  larger than on other days (56), and one meeting (2015-03-18, +248 pips) is large. Per-year means are positive in 5 of 6 years
  (2018 -1.5).
- About 8 of the 21 pips come in 13:00-16:00 NY on statement day (n.s. alone); the rest accrues earlier in the window.
- Val power is low: the val block has roughly 20 scheduled meetings. With an SD near 75 pips, val can only confirm a mean of roughly
  35 pips or more under the same rule. A val NONE/WEAK would therefore not disprove a smaller effect, but the rule stays as written.

## Next
Pre-register **B11v** (E014): same window, same rule (mean > 10 pips, block-4 CI lower > 0, one-sided t p < 0.05), val block only,
1 trial, date file `data/calendars/fomc_dates.csv` (val dates already fetched and validated). LEAD only if val SIGNAL and SPEC 4 and
costs x1.5 net > 0.
