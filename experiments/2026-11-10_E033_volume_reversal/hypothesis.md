# E033 Hypothesis: volume-conditioned next-day reversal (B28) and continuation (B29), dev only (pre-registered 2026-11-10 R069, before any run)

- **H1a (B28):** on dev trading dates D whose unexpected volume UV(D) is in the low tercile of its rolling past-only distribution,
  a position -sign(R(D)) held from 20:00 NY on D to 16:55 NY on D+1 earns a mean signed mid return > 1 pip (next-day reversal
  after a low-volume move: non-informational price pressure).
- **H1b (B29):** on dev dates with UV(D) in the high tercile, a position +sign(R(D)) over the same hold earns a mean signed mid
  return > 1 pip (next-day continuation after a high-volume move: informed trading revealed by volume).
- **H0 (each):** the mean signed return is zero.
- **Mechanism [PUB, secondary source]:** Cespa, Gargano, Riddiough & Sarno, "Foreign exchange volume" (RFS; JBS summary opened R068;
  journal volume/pages **UNVERIFIED**): abnormally low unexpected volume -> "a return reversal over the following day"; the
  reversal "weakens and moves toward a next-day continuation ... when volume is particularly high" (cf. Campbell-Grossman-Wang;
  Llorente-Michaely-Saar-Wang). Details: research/backlog.md B28, B29.
- **Volume proxy (limitation):** their volume is CLS settlement volume; ours is Dukascopy's single-venue tick-volume field
  (`volume`, from `bid_volume` in data.py). A null result here does not refute the published CLS result.
- **Parent experiment / variable changed:** none formally; new conditioning variable (volume, never used by any experiment).
  Relatives: E021 (dev, large |16:00->16:00| move reversal 20:00 -> 10:45 NY, NONE, signed -2.55 i.e. slight continuation), E028/E029.
- **Contamination:** E021 published a dev reading on large-move days, which overlap high-UV days; B29's prior is partly contaminated
  (E021's continuation-leaning reading). The overlap share and the result excluding E021-large days are reported (descriptive).
- **Prior expectation (written before data):** low. ~21 h hold, SD roughly 40-45 pips, n ~380 per arm -> SE ~2.2 pips; a SIGNAL
  needs a mean of roughly 4.5+ pips. The volume proxy weakens the link to the published mechanism. B29 prior lower than B28.
- **LEAD status:** a dev SIGNAL is not a LEAD; it earns B28v / B29v (val, its own pre-registered experiment).
- **Why now:** top `ready` backlog items (B28, B29, added R068); run together as one experiment, 2 trials (precedent E012).
