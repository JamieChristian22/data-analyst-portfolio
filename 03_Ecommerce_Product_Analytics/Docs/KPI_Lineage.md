# KPI lineage and business rules

SQL dialect: SQLite 3.25+; tested runtime recorded in the manifest. Each result name maps to a named section in `SQL/analysis.sql`. Additional statistical estimates are computed in `portfolio/metrics.py` and reconciled in `portfolio/run.py`.

| Metric | Calculation / denominator | Result file | Interpretation |
| --- | --- | --- | --- |
| conversion_rate | SUM(purchased) / COUNT(web sessions) | summary.csv | Session denominator, not users. |
| cart_abandonment_rate | 1 − purchased sessions / cart sessions | summary.csv | Verified purchased implies cart. |
| average_order_value | SUM(order_value) / COUNT(order rows) | summary.csv | One order per purchased session is validated here. |
| SKU top-20% share | Revenue of ceil(0.2 × distinct SKUs) top SKUs / total order revenue | additional_metrics.json | Ranking ties broken by SKU for determinism. |
| discount association | AOV grouped by device, category and observed discount flag | discount_association.csv | Not a causal discount effect; no customer RFM is computed. |
