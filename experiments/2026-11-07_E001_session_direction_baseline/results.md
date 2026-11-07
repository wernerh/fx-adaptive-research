# E001 Results

**Run:** GitHub Actions run 42391610826, 2026-11-07. Data commit 7cf2fc6. Blocks: dev and val only. **OOS not touched.**
**Raw outputs:** `backtests/validation_reports/E001_results.json`, `E001_results.txt`, `data_quality_2015-01-01_2026-10-30.json`

## Data
- 4,405,240 one-minute bid/ask bars, 2015-01-01 to 2026-10-30
- Missing trading minutes: 0.869% (gate: < 1%) -> **pass**
- Crossed quotes: 0; bad OHLC: 0
- Spread (pips): median 0.3, p95 0.8, p99 2.7
- Trading days: dev 1,556; val 637

## Script output (verbatim)
```
block            predictor  n_days  n_active  coverage  hit_rate    hit_rate_ci95  binom_p  mean_signed_pips mean_signed_ci95_block_boot  spearman_ic  spearman_p  binom_p_bonferroni
  dev   unconditional_long    1556      1556     1.000    0.5096 (0.4848, 0.5344)   0.4622             0.593             (-1.173, 2.683)          NaN         NaN                 1.0
  dev      london_ret_sign    1556      1555     0.999    0.4830 (0.4582, 0.5078)   0.1873            -1.217             (-3.188, 0.753)      -0.0371      0.1430                 1.0
  dev        asia_ret_sign    1556      1553     0.998    0.5145 (0.4896, 0.5393)   0.2642             0.550             (-1.394, 2.184)       0.0275      0.2783                 1.0
  dev       lon_break_side    1556      1503     0.966    0.4997 (0.4744, 0.5249)   1.0000            -0.182             (-2.328, 1.855)      -0.0090      0.7215                 1.0
  dev       lon_break_held    1556      1037     0.666    0.4908 (0.4605, 0.5212)   0.5762             0.041              (-2.434, 2.16)      -0.0201      0.4282                 1.0
  dev lon_false_break_fade    1556       466     0.299    0.4807  (0.4357, 0.526)   0.4310             0.677             (-2.261, 4.863)      -0.0137      0.5892                 1.0
  dev    asia_london_agree    1556       781     0.502    0.4968 (0.4618, 0.5318)   0.8862            -0.706             (-3.385, 1.902)      -0.0076      0.7637                 1.0
  val   unconditional_long     637       637     1.000    0.4819 (0.4434, 0.5207)   0.3834             0.713              (-1.844, 3.16)          NaN         NaN                 1.0
  val      london_ret_sign     637       636     0.998    0.5094 (0.4706, 0.5481)   0.6627            -0.213             (-3.582, 2.951)       0.0253      0.5243                 1.0
  val        asia_ret_sign     637       636     0.998    0.5079 (0.4691, 0.5466)   0.7212             0.490              (-2.51, 3.395)       0.0118      0.7669                 1.0
  val       lon_break_side     637       619     0.972    0.5202 (0.4808, 0.5593)   0.3347            -0.265             (-2.824, 2.203)       0.0303      0.4450                 1.0
  val       lon_break_held     637       423     0.664    0.5177  (0.4702, 0.565)   0.4961            -0.159             (-3.362, 3.075)       0.0363      0.3608                 1.0
  val lon_false_break_fade     637       196     0.308    0.4745 (0.4057, 0.5442)   0.5204             0.494             (-3.192, 5.115)      -0.0008      0.9840                 1.0
  val    asia_london_agree     637       307     0.482    0.5212 (0.4654, 0.5764)   0.4935             0.338             (-4.617, 4.885)       0.0272      0.4926                 1.0
```

## Reading the table
- Hit rates range from 0.4745 to 0.5212; every Wilson 95% CI contains 0.50.
- Smallest unadjusted binomial p: 0.1873 (dev, `london_ret_sign`, which points the **wrong** way, hit rate 0.4830). Every Bonferroni-adjusted p = 1.0.
- Every block-bootstrap 95% CI for mean signed pips contains zero.
- `unconditional_long`: +0.593 pips (dev) and +0.713 pips (val) per day, both CIs include zero. No detectable US-session drift.
- No predictor has the same sign of mean signed pips above 1.0 in both blocks.
- Pre-registered exploratory breakdowns (by year, by Asian range tercile, by weekday, pre/post 4pm fix) were **not run** in this workflow; see conclusion.
