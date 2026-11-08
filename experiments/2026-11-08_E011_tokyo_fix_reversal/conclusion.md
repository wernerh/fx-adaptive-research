# E011 Conclusion (2026-11-08)

## Decision: **WEAK** (pre-registered rule, applied exactly)
Rule per test: SIGNAL if mean signed > 1.0 pip AND block-bootstrap CI lower > 0 AND binomial p < 0.025;
WEAK if mean signed > 0 and (CI lower > 0 or p < 0.05); else NONE.
- `tky_pre_all`: mean +0.32 pips (< 1.0), CI (-0.10, 0.76) includes 0, binom p 0.021 < 0.05 -> **WEAK**.
- `tky_post_all`: mean +0.79 pips (< 1.0), CI (0.32, 1.17) lower > 0, binom p 0.0026 < 0.025 -> fails only the 1.0-pip size bar -> **WEAK**.
Per the pre-registration, WEAK does **not** go to val. **B5v is not queued.** No lead.

## What we learned
- Unlike London (E007) and ECB (E010), the Tokyo-fix version shows a **frequency** effect, not a tail effect: hit rates 0.53/0.54
  in the predicted direction for both windows. It is the most consistent of the three fix tests, but still sub-pip per hour.
- Post-fix hour (USD down after 09:55 JST): +0.79 pips mid, and the descriptive bid/ask check gives +0.48 pips net, +0.32 at costs x1.5
  (median entry spread 0.2 pips). This is descriptive only and on dev only; it is **not** a lead and does not reopen the val question.
  Recording it so a future, separately justified pre-registration (e.g. fresh data) can cite it as a dev observation, with the 226-trial
  multiple-testing context.
- Pre-fix hour: +0.32 pips mid, negative after costs. Not tradable.
- Asian-hours spreads at these times were narrower than feared (median 0.2-0.4 pips on Dukascopy).

## Next
B5 done. Next ready backlog item: B9 (NY 18:00 Wednesday drift, val only).
