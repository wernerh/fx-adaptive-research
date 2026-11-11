# E042 Hypothesis: lagged daily gold return -> next-day EUR/USD (B46), dev only (pre-registered 2026-11-11 R094, before any run)

- **H1 (B46):** on every valid dev trading date D, a position -sign(G(D)) in EUR/USD held from 16:05 Europe/London on D to 16:00
  London on the next valid trading date earns a mean signed mid return > 1 pip per date, where G(D) = ln(XAU/USD mid at 16:00
  London on D) - ln(XAU/USD mid at 16:00 London on the previous valid trading date) (gold up -> EUR/USD down next day: partial
  reversal of the same-day USD co-move).
- **H0:** the mean signed return per date is zero.
- **Mechanism [PUB, AUD/USD only; EUR is our extension]:** Apergis (2014, International Review of Economics & Finance 29, 75-82):
  daily gold prices forecast AUD/USD out of sample; author-manuscript Table 3 prints negative short-run coefficients on lagged gold
  returns (lag 1 -0.328, t -4.34). Sign fixed from those printed coefficients in the backlog (R093) before any data; the paper's
  quote direction for AUD is UNVERIFIED (lesson R081). Prior weak.
- **Parent experiment / variable changed:** E041 (B45). One variable changed: the source market (WTI CFD -> XAU/USD), and with it
  the sign taken from the source paper. Hold window, quotes, exclusions, gate and rule identical to E041.
- **Contamination note:** no gold series has been used in this repo. The target window equals E041's (and E037's), whose
  unconditional and oil-signed dev means are known (E041: +2.306 pips with oil continuation sign, NONE). Gold and WTI are both
  USD-priced, so G is likely positively correlated with E041's O; E041's positive oil-continuation mean would, if anything, favour
  the opposite (continuation) sign for gold. The sign here is the paper's, not chosen from E041.
- **Prior expectation:** weak (lesson R081; Basnarkov et al.: most daily-and-shorter FX lags absent). A clean NONE closes the line.
- **Why now:** top `ready` backlog item after E041 (B45 NONE) and the R093 refill; no research-batch run queued or in progress.
