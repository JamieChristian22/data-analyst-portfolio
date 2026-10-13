# Verified result-to-visual mapping

Use the exported **Results tables** as aggregate data sources. They already contain metric denominators and segmentation. Do not sum rates; recompute ratios from numerator and denominator when rolling up segments.

- `recorded_revenue` → `Results/summary.csv`. Not labeled GMV or platform commission revenue.
- `sales_rows` → `Results/summary.csv`. Not an order count; no order ID.
- `revenue discrepancy` → `Results/summary.csv`. Tolerance slightly above one cent; cause unknown.
- `top-ten share` → `Results/additional_metrics.json`. Ranks derived from supplied seller IDs.
- `seller HHI` → `Results/additional_metrics.json`. Descriptive concentration measure, not a regulatory conclusion.
- `stock association` → `Results/stock_status_association.csv`. No causal lost-sales estimate.

The self-contained `REPORT.html` renders the same named-query outputs. Legacy workbook fields and screenshots are not certified by this mapping. See `Dashboard_Reconciliation.md`.
