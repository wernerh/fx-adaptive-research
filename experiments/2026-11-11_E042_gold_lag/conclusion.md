# E042 Conclusion (2026-11-11, R095)

## Decision: **NONE on dev** (pre-registered rule `gold_lag.decide_b46` = `decide_b34`, applied exactly). **Not a LEAD.**
Rule: data gate first; < 500 tested dates -> NONE; SIGNAL if mean > 1.0 pip AND block-20 bootstrap CI lower > 0 AND one-sided t
p < 0.05; WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- Data gate pass (0.9897 of dates with both gold quotes).
- B46: n 1533, mean -1.407 pips, CI (-4.415, 0.939), t p 0.8352 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- The pre-registered sign (partial reversal of the same-day gold/EUR co-move, from Apergis's short-run coefficients) has a negative
  point estimate; the lagged correlation is near zero (0.0058). There is no next-day information in the daily gold return on dev.
- Gold and EUR/USD co-move strongly on the same day (corr 0.4026, the common USD factor), but that co-move does not carry into the
  next day. This matches Basnarkov et al. (most daily FX lags absent) and lesson R081 (lagged cross-market claims are weak priors).
- The opposite-sign continuation mean (+1.407) is reported only; testing it would be a new trial chosen after seeing data (lesson
  R076) and is not queued. Gold and oil signals are nearly uncorrelated on common dates (0.0329), so E041 and E042 are close to
  independent tests, both NONE.
- Apergis is about AUD/USD (a commodity currency); this does not refute it.

## Next
B46 closed NONE (rejected_hypotheses.md); B47 closed unearned (0 trials). No dev re-test with other lags, windows, |G| filters,
the opposite sign or silver. No `ready` item remains: next run is a backlog refill.
