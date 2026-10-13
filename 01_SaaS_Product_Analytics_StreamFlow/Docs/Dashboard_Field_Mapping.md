# Verified result-to-visual mapping

Use the exported **Results tables** as aggregate data sources. They already contain metric denominators and segmentation. Do not sum rates; recompute ratios from numerator and denominator when rolling up segments.

- `snapshot_mrr` → `Results/summary.csv`. Snapshot only; not verified active MRR.
- `snapshot_arr` → `Results/summary.csv`. Annualization, not recognized revenue.
- `paying_churn_label_rate` → `Results/summary.csv`. Free rows excluded; label is not independently reconstructed.
- `ordered onboarding` → `Results/onboarding_funnel.csv`. Same-day ties allowed; earliest eligible retry used.
- `power-user association` → `Results/power_user_association.csv`. Includes zero-activity users in comparison; correlation only.

The self-contained `REPORT.html` renders the same named-query outputs. Legacy workbook fields and screenshots are not certified by this mapping. See `Dashboard_Reconciliation.md`.
