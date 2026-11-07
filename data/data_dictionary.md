# Data dictionary

## Canonical 1-minute bars: `data/processed/eurusd_m1.parquet` (git-ignored)

| Column | Type | Meaning |
|---|---|---|
| index `ts` | datetime64[ns, UTC] | Bar OPEN time, UTC |
| bid_open/high/low/close | float | Bid OHLC |
| ask_open/high/low/close | float | Ask OHLC |
| volume | int | Tick volume (count of quote updates), NOT traded volume |

Mid is derived as (bid+ask)/2. 1 pip = 0.0001.

## Sources
| Source | Use | Caveats |
|---|---|---|
| Dukascopy historical (via `dukascopy-node`) | Primary research data, 2015+ | Single-venue ECN quotes; spreads tighter than many retail brokers; tick volume only |
| Broker paper feed (e.g. OANDA/MT5) | Paper trading, spread realism checks | Compare spreads against Dukascopy before trusting backtests |
| Economic calendar | Event filter | TBD; must have historical timestamps in UTC and an importance rating |

## Daily features (`fxresearch.features.daily_features`)
Indexed by trading date (17:00 New York roll).
- `asia_*`, `london_*`: open/high/low/close/range_pips/ret_pips/close_loc per session
- `atr_pips_prior`: mean daily range of the 14 PRIOR trading days
- `asia_range_atr`, `london_range_atr`: range / prior ATR
- `lon_break_side` (+1/-1/0), `lon_broke_both`, `lon_closed_inside_asia`, `lon_break_time`
- `prev_day_high`, `prev_day_low`
- `y_us_*`: US session OUTCOMES. Never usable as signal inputs.
