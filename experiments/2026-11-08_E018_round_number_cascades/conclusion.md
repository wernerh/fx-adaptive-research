# E018 Conclusion (2026-11-08, R033)

## Decision: **NONE on dev** (pre-registered B1 rule, `fixes.decide(res, n_trials=1)`, applied exactly). **No lead.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.05; WEAK if mean > 0 and (CI lower > 0 or p < 0.05); else NONE.
- Mean -0.128 pips (not > 0), CI (-0.989, 0.714) includes 0, binomial p 0.280 -> **NONE**.
- Per the methodology, B15 is closed for this definition; no re-test with other horizons, offsets or level steps on dev.
- Cost check also negative: SPEC 4 net -0.628, costs x1.5 -0.879.

## Reading the result (cautions, no new numbers)
- No continuation after first crossings of 00/50 levels on 2015-2020 EUR/USD at 15, 60 or 120 minutes. Only 2015 was positive.
- The control levels (23/73) show a negative mean with CI below 0 (a mild reversal after any first level crossing); round levels are
  +0.675 pips better than control. This is descriptive only; a "reversal after first crossing" reading or a "round minus control" test
  would be new hypotheses needing their own pre-registration on fresh data (dev now seen for this line).
- Up/down asymmetry (down +0.786, up -1.006) mirrors the dev-period EUR/USD downtrend plus mean reversion; not a trial.
- Consistent with the 1990s stop-loss cascade effect (Osler 2002/2005) being absent or arbitraged away in the electronic market.

## Next
B15 closed (recorded in knowledge/rejected_hypotheses.md). Next `ready` item: B16 (12-month TSMOM, daily hold, dev).
