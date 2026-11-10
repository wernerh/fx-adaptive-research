# E037 Hypothesis: relative equity performance -> next-day EUR/USD, daily (B35) and 20-date smoothed (B36), dev only (pre-registered 2026-11-10 R080, before any run)

- **H1a (B35):** on every valid dev trading date D, a position -sign(S1(D)) in EUR/USD held from 16:05 Europe/London on D to 16:00
  London on the next valid trading date earns a mean signed mid return > 1 pip per date, where S1(D) = log return of the EU Stocks 50
  CFD mid minus log return of the US 500 CFD mid, each from 16:00 London on the previous valid trading date to 16:00 London on D
  (US equities outperformed -> long EUR/USD; EU outperformed -> short).
- **H1b (B36):** the same trade with position -sign(S20(D)), S20 = the same relative log return measured from 16:00 London on the
  valid trading date 20 places before D, earns a mean signed mid return > 1 pip per date.
- **H0 (each arm):** the mean signed return per date is zero.
- **Mechanism [PUB, contemporaneous only]:** Hau & Rey (2006, RFS 19(1), abstract opened R079): higher home equity returns relative
  to foreign returns go with a home-currency depreciation (portfolio rebalancing under incomplete FX hedging) at daily, monthly and
  quarterly frequencies. Camanho, Hau & Rey (2022, RFS 35(11), abstract opened R079): funds rebalance after excess foreign returns.
  **This is a lagged extension, not a replication:** if rebalancing flows are spread over the following day, yesterday's relative equity
  return predicts EUR/USD today with the same sign. Effect size not published. All parameters were fixed in the backlog (R079) before
  any data.
- **Parent experiment / variable changed:** none formally. New conditioning variable: daily (B35) and 20-date (B36) relative EU vs US
  equity return. Relative: E034 (B30, month-to-date relative equity return on 71 month-ends only).
- **Prior expectation:** weak. A clean NONE is informative and closes the line.
- **Why dev is clean:** E034 reported corr(S, move) on 71 month-ends with a month-to-date signal only; the daily lagged statistic has
  never been computed. E019 (TSMOM) and E021 use EUR/USD's own past moves, not equity data.
- **Caution (lesson R078):** E035/B33, also a 20-date smoothed sign held one day, was SIGNAL on dev and NONE on val. A B36 SIGNAL alone
  means little; only B37 (val) counts.
- **Why now:** top `ready` backlog items (B35, B36) after the R079 refill; no research-batch run queued or in progress.
