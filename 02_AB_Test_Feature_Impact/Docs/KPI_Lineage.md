# KPI lineage and business rules

SQL dialect: SQLite 3.25+; tested runtime recorded in the manifest. Each result name maps to a named section in `SQL/analysis.sql`. Additional statistical estimates are computed in `portfolio/metrics.py` and reconciled in `portfolio/run.py`.

| Metric | Calculation / denominator | Result file | Interpretation |
| --- | --- | --- | --- |
| conversion_rate | SUM(converted) / COUNT(sessions), within arm | variant_summary.csv | Assumes independent sessions for inference. |
| absolute lift | Variant B conversion rate − Control rate | additional_metrics.json | Multiply by 100 to express percentage points. |
| relative lift | Absolute lift / Control rate | additional_metrics.json | Undefined if Control rate is zero. |
| difference confidence interval | Newcombe difference interval using Wilson arm intervals, 95% | additional_metrics.json | Unadjusted single primary contrast. |
| p_value | Two-sided pooled two-proportion z-test | additional_metrics.json | Not a probability the hypothesis is true. |
| srm_p_value_50_50 | Chi-square goodness-of-fit to equal assignment | additional_metrics.json | 50:50 allocation is an explicit assumption. |
