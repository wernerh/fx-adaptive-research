# Data quality reports

Paste the JSON from `scripts/ingest_dukascopy.py` here with the date and source each time data is refreshed.

### 2026-11-07: Dukascopy EUR/USD m1 bid+ask, 2015-01-01 to 2026-10-30 (GitHub Actions run 42391610826)
```json
{
  "first_bar": "2015-01-01 22:00:00+00:00",
  "last_bar": "2026-10-30 20:59:00+00:00",
  "bars": 4405240,
  "weekend_bars": 1,
  "missing_trading_minutes": 38601,
  "missing_pct": 0.869,
  "crossed_quotes": 0,
  "zero_spread_bars": 0,
  "spread_pips_median": 0.3,
  "spread_pips_p95": 0.8,
  "spread_pips_p99": 2.7,
  "bad_ohlc": 0,
  "source": "Dukascopy via dukascopy-node, 1-minute bid and ask"
}
```
Gate: missing < 1% -> **pass** (0.869%). One weekend bar retained (harmless; excluded from sessions).
