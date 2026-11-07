# E001 Conclusion (2026-11-07)

## Decision: **NONE** (pre-registered rule applied as written)
No predictor met even one part of the SIGNAL rule: none had Bonferroni p < 0.05 in dev, none had unadjusted p < 0.05 in val,
and none had mean signed pips > 1.0 in both blocks. The unconditional benchmark was also indistinguishable from zero.

**H0 is not rejected.** Over 2015-2023 (dev + val), simple Asian/London session structure gave no detectable
information about the direction of the EUR/USD 08:00-12:00 New York session.

## What this does and does not rule out
- **Rules out (for this window and these predictors):** using London direction, Asian direction, the Asian-range break
  side, held breaks, faded false breaks, or Asia/London agreement as a directional bias for the whole US morning.
- **Does not rule out:**
  - Shorter outcome windows (e.g. 08:00-09:00 or post-08:30 data). The master prompt targets short holds, and a 4-hour
    window can average a short-lived effect away. That is a different outcome variable and needs its own experiment.
  - Conditional effects (volatility regime, event days). Testing these on the same dev/val data is exploratory and
    must carry the full multiple-testing count.
  - Strategies that trade **inside London** (S001 Asian range breakout), which do not depend on a US-session bias.
- Absence of evidence at these sample sizes: with about 1,550 dev days, a true hit rate of 52-53% would often go undetected.
  Effects that small would be unlikely to survive costs on a once-a-day trade anyway (mean |US return| should be checked against the roughly 1-pip round-trip cost).

## What worked
- The pipeline ran end to end on GitHub Actions in about 24 minutes, including Dukascopy's bot protection.
- Data quality passed the gate on the first attempt.

## What failed
- The hypothesis, for this formulation.
- The exploratory breakdowns from the methodology were not automated; they still need doing (labelled exploratory).

## Unexpected
- `london_ret_sign` in dev leaned slightly towards **reversal** (hit rate 48.3%, IC -0.037), but not significantly, and val leaned the other way (50.9%, IC +0.025). This is the instability you would expect from noise.
- No time-of-day drift despite Breedon & Ranaldo (2013). Their sample ended in 2007 and measured local trading hours, not our window. The effect may have faded, or our window may not line up with it.

## Implications
| Strategy | Effect |
|---|---|
| S003 London-to-US continuation | Its core premise (London direction carries into the US morning) shows no support. Deprioritised; keep only as a conditional variant if a later short-window experiment finds signal. |
| S002 London false-break reversal | `lon_false_break_fade` shows no signal. Deprioritised. |
| S006 US early momentum | Untouched by E001; it uses information from inside the US session. |
| S001 Asian range breakout | Untouched by E001 (it trades within London). Next candidate. |

## Next experiment (recommendation)
1. **E004:** S001 Asian range breakout on dev with full costs. It tests a separate hypothesis (continuation within London) and is the most-cited retail setup.
2. **E006:** E001 predictors with a **short outcome window** (08:00-09:00 NY, and 08:35-09:30 to skip the release jump). One variable changed: the outcome window.
3. E001 exploratory breakdowns (year, regime, fix split), labelled exploratory.
