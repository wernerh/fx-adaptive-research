# E040 Hypothesis: post-FOMC reversal of the pre-statement EUR/USD drift, 12-24 h after the statement, dev only (pre-registered 2026-11-11 R089, before any run)

- **H1 (B43):** on scheduled dev FOMC statement dates t, the EUR/USD mid move P from 16:00 NY on the previous business day to 13:55 NY
  on t (the pre-statement drift) is partly reversed between 02:00 NY and 14:00 NY on t+1 (12-24 h after the 14:00 NY statement):
  mean of -sign(P) x (mid 14:00 NY t+1 - mid 02:00 NY t+1) > 1 pip per event.
- **H0:** the mean signed return per event is zero (no reversal in the 12-24 h window).
- **Mechanism [PUB, abstract only]:** Lee & Wang (2025, RAPS 15(3-4) 247-287; research/academic_studies.md, VERIFIED (abstract only)):
  post-FOMC currency returns are "mostly realized between 12 and 24 hours after FOMC announcements", "cancelling out approximately
  65% of positive pre-FOMC announcement drifts". Currency set, sign convention and EUR magnitude UNVERIFIED, so the test is symmetric
  in the sign of the drift (reversal of whichever direction P took).
- **Parent experiment / variable changed:** none (new target window on a known event). Relatives: E013/E014 measured the FOMC-day
  window 16:00 t-1 -> 16:00 t only; this is a new conditional target (t+1, 02:00 -> 14:00 NY) that has never been computed.
- **Prior:** weak to moderate; underpowered (~48 dev events, SE ~5 pips). A NONE does not rule out the published effect.
- **Why now:** top `ready` backlog item after the R088 refill; no research-batch run queued or in progress (last run 42960104359
  recorded as E039 in R087).
