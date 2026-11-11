# E041 Hypothesis: lagged daily WTI return -> next-day EUR/USD (B45), dev only (pre-registered 2026-11-11 R091, before any run)

- **H1 (B45):** on every valid dev trading date D, a position +sign(O(D)) in EUR/USD held from 16:05 Europe/London on D to 16:00
  London on the next valid trading date earns a mean signed mid return > 1 pip per date, where O(D) = ln(WTI CFD mid at 16:00 London
  on D) - ln(WTI CFD mid at 16:00 London on the previous valid trading date) (oil up -> USD weaker -> long EUR/USD).
- **H0:** the mean signed return per date is zero.
- **Mechanism [PUB, partial text; EUR is our extension]:** Ferraro, Rogoff & Rossi (NBER WP 17998, 2012; JIMF 2015; ~45% of the
  text opened R088): daily oil price changes forecast commodity-currency exchange rates (CAD/USD main result), and "the predictive
  ability of the lagged realized oil prices is more ephemeral" (verbatim). No EUR result is published; the sign used here (oil up ->
  USD weaker -> EUR/USD up) was stated in the backlog (R088) before any data. The contemporaneous correlation is reported descriptively.
- **Parent experiment / variable changed:** none formally. New conditioning variable: lagged daily WTI return. Hold window identical
  to E037 (16:05 London D -> 16:00 London next date), signal different.
- **Prior expectation:** weak (lesson R081: published lags are often absorbed the same day). A clean NONE closes the line.
- **Why dev is clean:** no oil series has been used in this repo before.
- **Why now:** top `ready` backlog item after E040 (B43 NONE, B44 closed unearned); no research-batch run queued or in progress.
