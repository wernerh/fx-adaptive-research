# E006 Hypothesis

**H1:** at least one E001 predictor predicts the sign of a SHORT early-US-session return.
**H0:** hit rate = 50% and mean signed return = 0 for every predictor in both windows.

**Parent:** E001. **Variable changed (one):** the outcome window, from 08:00-12:00 NY to:
- `us_0800_0900`: 08:00-09:00 New York (first hour, includes the 08:30 releases)
- `us_0835_0930`: 08:35-09:30 New York (skips the release jump itself)

Predictors and features are unchanged from E001 (all known before 08:00 NY).
**Why:** E001 found nothing over 4 hours, but the master prompt targets short holds, and a brief effect could be averaged away over a long window.
