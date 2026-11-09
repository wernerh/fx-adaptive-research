# E024 Conclusion (2026-11-09, R047)

## Decision: **SIGNAL on dev** (pre-registered rule `vol_state_london.decide_b20`, applied exactly). **Not a LEAD yet.**
Rule: SIGNAL if mean > 1.0 pip AND block-bootstrap CI lower > 0 AND one-sided t p < 0.05; WEAK if mean > 0 and
(CI lower > 0 or p < 0.05); else NONE.
- Mean +2.983 pips (> 1.0), CI (0.566, 4.847) lower > 0, one-sided t p 0.0053 (< 0.05) -> **SIGNAL**.
- Cost check positive (descriptive): SPEC 4 net +2.515, costs x1.5 +2.281 pips per event.
- Not driven by FOMC days (12 events; excluding them +3.143, CI lower 0.787).
- LEAD definition (docs/AUTONOMOUS_PROTOCOL.md) needs a separate pre-registered val confirmation. Per the methodology, the next step is
  **B20v**: the identical rule on the val block as its own experiment (1 val trial). No notification.

## Reading the result (cautions, no new numbers)
- **Stronger than E022 but same caveat:** CI lower 0.566 and p 0.0053 are clearer than E022's (0.011, p 0.013), yet with ~238
  registered trials one dev SIGNAL at p 0.005 can still be chance. E022 (same condition, other fix) failed val in E023.
- **Conditioning vs. unconditional drift:** all post-burn-in dates are also positive (+1.562, CI excludes 0); the normal-date control
  is +0.901 (CI includes 0). The high-vs-normal difference was not tested and is not established; part of the result may be the
  unconditional post-fix EUR-up drift reported in the published source.
- **Uneven over time:** 2018 and 2019 were negative; 2015, 2016 and 2020 carry the mean. Weekday splits are post-hoc and not evidence.
- **Val contamination note for B20v:** E017 already computed the unconditional long 12:00-17:00 NY leg on val (WEAK). No vol-conditional
  11:05-16:00 NY return has been computed on val, so B20v's exact statistic is unseen, but a related window was.
- **Power note for B20v (stated before val data):** ~200 val events x SD ~25 pips -> SE ~1.8 pips; a val mean near the dev +3.0 could
  give WEAK rather than SIGNAL. The rule is not loosened.

## Next
Queue B20v (val confirmation, rule unchanged, val-only burn-in as in E023).
