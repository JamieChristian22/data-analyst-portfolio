# KPI lineage and business rules

SQL dialect: SQLite 3.25+; tested runtime recorded in the manifest. Each result name maps to a named section in `SQL/analysis.sql`. Additional statistical estimates are computed in `portfolio/metrics.py` and reconciled in `portfolio/run.py`.

| Metric | Calculation / denominator | Result file | Interpretation |
| --- | --- | --- | --- |
| observed_purchase_rate | Distinct users with Purchase / all users | summary.csv | Unordered reach; varying follow-up. |
| ordered_funnel | Unique users satisfying all six stages in nondecreasing date order after first_seen | ordered_funnel.csv | Strict tracking diagnostic; distinguish from stage reach. |
| returning conversion | Distinct purchasers / all users, separately by supplied returning flag | returning_user_conversion.csv | Descriptive association. |
| time to purchase | First valid purchase date − first_seen_date | time_to_purchase.csv | Conditional on observed purchasers; not survival analysis. |
| p50 / p90 | Pandas linear quantile of observed valid days-to-purchase | additional_metrics.json | No correction for right censoring. |
