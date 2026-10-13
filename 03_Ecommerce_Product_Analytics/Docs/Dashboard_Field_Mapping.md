# Verified result-to-visual mapping

Use the exported **Results tables** as aggregate data sources. They already contain metric denominators and segmentation. Do not sum rates; recompute ratios from numerator and denominator when rolling up segments.

- `conversion_rate` → `Results/summary.csv`. Session denominator, not users.
- `cart_abandonment_rate` → `Results/summary.csv`. Verified purchased implies cart.
- `average_order_value` → `Results/summary.csv`. One order per purchased session is validated here.
- `SKU top-20% share` → `Results/additional_metrics.json`. Ranking ties broken by SKU for determinism.
- `discount association` → `Results/discount_association.csv`. Not a causal discount effect; no customer RFM is computed.

The self-contained `REPORT.html` renders the same named-query outputs. Legacy workbook fields and screenshots are not certified by this mapping. See `Dashboard_Reconciliation.md`.
