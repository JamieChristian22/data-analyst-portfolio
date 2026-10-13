# Verified result-to-visual mapping

Use the exported **Results tables** as aggregate data sources. They already contain metric denominators and segmentation. Do not sum rates; recompute ratios from numerator and denominator when rolling up segments.

- `observed_purchase_rate` → `Results/summary.csv`. Unordered reach; varying follow-up.
- `ordered_funnel` → `Results/ordered_funnel.csv`. Strict tracking diagnostic; distinguish from stage reach.
- `returning conversion` → `Results/returning_user_conversion.csv`. Descriptive association.
- `time to purchase` → `Results/time_to_purchase.csv`. Conditional on observed purchasers; not survival analysis.
- `p50 / p90` → `Results/additional_metrics.json`. No correction for right censoring.

The self-contained `REPORT.html` renders the same named-query outputs. Legacy workbook fields and screenshots are not certified by this mapping. See `Dashboard_Reconciliation.md`.
