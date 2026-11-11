# E043 Conclusion (2026-11-11, R098)

## Decision: **NONE on dev** (pre-registered rule, applied exactly). **Not a LEAD.**
Rule: < 300 tested events -> NONE; SIGNAL if mean signed > 1.0 pip AND date-cluster bootstrap 95% CI lower > 0 AND one-sided t
p < 0.05 (1 trial); WEAK if mean > 0 and (CI lower > 0 or t p < 0.05); else NONE.
- B48: n 1896 events (1160 dates), mean -0.693 pips, CI (-1.607, 0.251), t p 0.9238 -> **NONE**.
- LEAD condition 1 fails. No notification.

## Reading the result (cautions, no new numbers)
- After a 5-minute EUR/USD jump, the 60-minute fade from t+10 earns nothing; the point estimate is slightly negative, i.e. the
  move tends to persist a little, mostly in 2015 (-4.33) and in the largest-|L| tercile. Net of SPEC 4 costs it is -1.178 pips.
- The only reversal visible is inside the skipped bar (t+5 -> t+10, +0.491 pips, CI excludes 0). It is under one pip, gross of
  spread, and sits in the 5 minutes the design deliberately skipped to avoid a same-quote fill. It is descriptive only; trading it
  would be a new trial chosen after seeing data (lesson R076) and is not queued.
- Release-proxy events (08:25-08:50 NY, 13.5% of events) also show no reversal (-2.123), consistent with E026 (no continuation, faint
  reversal at 2 h) being noise. Xiao, Yin & Zhao (2020) is about US equity ETFs; this does not refute it.

## Next
B48 closed NONE (rejected_hypotheses.md); B49 closed unearned (0 trials). No dev re-test with other thresholds, holds, entry lags,
the opposite sign or |L| subsets. No `ready` item remains: next run is a backlog refill.
