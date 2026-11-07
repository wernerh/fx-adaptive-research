# E001 Hypothesis

**H1:** At least one simple pre-US-session predictor built from Asian and London structure predicts the sign of the
EUR/USD US-session return (08:00 to 12:00 New York) better than chance.

**H0:** Hit rate = 50% and mean signed return = 0 for every predictor.

Predictors (fixed before seeing data; defined in `src/fxresearch/predictive.py`):
0. `unconditional_long`: always +1. **Benchmark**, because published work finds time-of-day drift in FX
   (Breedon & Ranaldo 2013). A conditional predictor only adds value if it beats this.
1. `london_ret_sign`: sign of London session return
2. `asia_ret_sign`: sign of Asian session return
3. `lon_break_side`: side of the Asian range London breaks first
4. `lon_break_held`: break side, only if London closes outside the Asian range
5. `lon_false_break_fade`: opposite of break side, only if London closes back inside
6. `asia_london_agree`: London sign, only when Asia and London agree

**Why this experiment first:** if none of these has signal, the session-based strategies in the registry have no
foundation and backtesting them would mostly fit noise.
