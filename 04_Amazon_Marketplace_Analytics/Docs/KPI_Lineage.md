# KPI lineage and business rules

SQL dialect: SQLite 3.25+; tested runtime recorded in the manifest. Each result name maps to a named section in `SQL/analysis.sql`. Additional statistical estimates are computed in `portfolio/metrics.py` and reconciled in `portfolio/run.py`.

| Metric | Calculation / denominator | Result file | Interpretation |
| --- | --- | --- | --- |
| recorded_revenue | SUM(sales.revenue) | summary.csv | Not labeled GMV or platform commission revenue. |
| sales_rows | COUNT(sales rows) | summary.csv | Not an order count; no order ID. |
| revenue discrepancy | ABS(recorded revenue − price × units) > 0.011 | summary.csv | Tolerance slightly above one cent; cause unknown. |
| top-ten share | Top ten seller recorded revenue / total recorded revenue | additional_metrics.json | Ranks derived from supplied seller IDs. |
| seller HHI | 10000 × SUM(seller revenue share squared) | additional_metrics.json | Descriptive concentration measure, not a regulatory conclusion. |
| stock association | Mean recorded listing revenue, including zero-sale listings, by category/price band/stock flag | stock_status_association.csv | No causal lost-sales estimate. |
