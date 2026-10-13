# Verified result-to-visual mapping

Use the exported **Results tables** as aggregate data sources. They already contain metric denominators and segmentation. Do not sum rates; recompute ratios from numerator and denominator when rolling up segments.

- `conversion_rate` → `Results/variant_summary.csv`. Assumes independent sessions for inference.
- `absolute lift` → `Results/additional_metrics.json`. Multiply by 100 to express percentage points.
- `relative lift` → `Results/additional_metrics.json`. Undefined if Control rate is zero.
- `difference confidence interval` → `Results/additional_metrics.json`. Unadjusted single primary contrast.
- `p_value` → `Results/additional_metrics.json`. Not a probability the hypothesis is true.
- `srm_p_value_50_50` → `Results/additional_metrics.json`. 50:50 allocation is an explicit assumption.

The self-contained `REPORT.html` renders the same named-query outputs. Legacy workbook fields and screenshots are not certified by this mapping. See `Dashboard_Reconciliation.md`.
