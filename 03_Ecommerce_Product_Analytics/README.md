# Ecommerce funnel and merchandise concentration

**Data provenance:** supplied simulated portfolio CSVs. No external client or production outcome is implied.

## Decision question

Which device/channel combinations lose cart sessions, and how concentrated is SKU revenue?

## Headline interpretation

Observed session conversion is 12.15%; cart abandonment is 64.24%. The top 20% of SKUs contribute 31.42% of recorded order revenue. These outputs replace the earlier untraceable 68% concentration claim.

## Computed findings

### Summary

| sessions | cart_sessions | purchases | conversion_rate | cart_abandonment_rate | revenue | average_order_value |
| --- | --- | --- | --- | --- | --- | --- |
| 25000 | 8492 | 3037 | 0.12148 | 0.642369 | 198,586 | 65.3889 |

Full output: [Results/summary.csv](Results/summary.csv).

### Funnel By Segment

| device | channel | sessions | carts | purchases | conversion_rate | cart_abandonment_rate |
| --- | --- | --- | --- | --- | --- | --- |
| Desktop | Paid Social | 2247 | 807 | 322 | 0.143302 | 0.600991 |
| Desktop | Paid Search | 3448 | 1238 | 475 | 0.137761 | 0.616317 |
| Desktop | Email | 1739 | 616 | 239 | 0.137435 | 0.612013 |
| Desktop | Affiliate | 1201 | 466 | 153 | 0.127394 | 0.671674 |
| Desktop | Organic | 3452 | 1229 | 431 | 0.124855 | 0.649308 |
| Mobile | Affiliate | 1232 | 416 | 153 | 0.124188 | 0.632212 |
| Mobile | Paid Search | 3669 | 1190 | 424 | 0.115563 | 0.643697 |
| Mobile | Email | 1817 | 573 | 199 | 0.109521 | 0.652705 |
| Mobile | Organic | 3788 | 1221 | 407 | 0.107445 | 0.666667 |
| Mobile | Paid Social | 2407 | 736 | 234 | 0.0972165 | 0.682065 |

Full output: [Results/funnel_by_segment.csv](Results/funnel_by_segment.csv).

### Sku Pareto

| sku | revenue | rank | sku_count | total_revenue | cumulative_revenue | cumulative_share | in_top_20_percent |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SKU-0028 | 1,249.99 | 1 | 400 | 198,586 | 1,249.99 | 0.00629445 | 1 |
| SKU-0143 | 992.65 | 2 | 400 | 198,586 | 2,242.64 | 0.011293 | 1 |
| SKU-0081 | 948.51 | 3 | 400 | 198,586 | 3,191.15 | 0.0160694 | 1 |
| SKU-0339 | 930.7 | 4 | 400 | 198,586 | 4,121.85 | 0.020756 | 1 |
| SKU-0104 | 920.64 | 5 | 400 | 198,586 | 5,042.49 | 0.025392 | 1 |
| SKU-0344 | 903.81 | 6 | 400 | 198,586 | 5,946.3 | 0.0299432 | 1 |
| SKU-0122 | 896.86 | 7 | 400 | 198,586 | 6,843.16 | 0.0344594 | 1 |
| SKU-0273 | 889.1 | 8 | 400 | 198,586 | 7,732.26 | 0.0389366 | 1 |
| SKU-0234 | 879.2 | 9 | 400 | 198,586 | 8,611.46 | 0.0433639 | 1 |
| SKU-0047 | 876.01 | 10 | 400 | 198,586 | 9,487.47 | 0.0477751 | 1 |

Full output: [Results/sku_pareto.csv](Results/sku_pareto.csv).

### Discount Association

| device | category | discount_applied | orders | average_order_value | average_units |
| --- | --- | --- | --- | --- | --- |
| Desktop | Apparel | 0 | 283 | 67.8994 | 2.02473 |
| Desktop | Apparel | 1 | 163 | 61.8226 | 1.9816 |
| Desktop | Beauty | 0 | 203 | 67.0589 | 2.02463 |
| Desktop | Beauty | 1 | 98 | 62.7128 | 1.96939 |
| Desktop | Electronics | 0 | 210 | 68.075 | 1.9619 |
| Desktop | Electronics | 1 | 123 | 61.9149 | 1.96748 |
| Desktop | Fitness | 0 | 120 | 71.3069 | 1.95 |
| Desktop | Fitness | 1 | 64 | 60.4198 | 2.04688 |
| Desktop | Home | 0 | 225 | 67.9237 | 1.96444 |
| Desktop | Home | 1 | 131 | 63.7812 | 1.96183 |

Full output: [Results/discount_association.csv](Results/discount_association.csv).

## Additional calculations

```json

{
  "top_20_percent_sku_revenue_share": 0.31417248085690647,
  "rfm_status": "Not computed: no stable customer ID; session_id is not a customer proxy."
}

```

## Recommendation

Prioritize segments with both substantial session volume and high abandonment. Validate checkout friction with UX evidence; use SKU concentration to guide inventory review, not automatic assortment cuts.

## Limits and assumptions

Each order row is one purchased session in this supplied dataset. This is a dataset contract, not a universal ecommerce model. No customer ID exists, so customer RFM and repeat-purchase claims are intentionally omitted. Discount comparisons are observational and may reflect product/segment selection.

## Reproduction

From the repository root: `python -m portfolio.run --project 03_Ecommerce_Product_Analytics`.

Each named query in `SQL/analysis.sql` writes a corresponding results CSV. The Python runner independently reconciles headline metrics and ordered funnels. See `Results/validation.json` for checks and `Results/quality.json` for source diagnostics.

## Existing BI workbooks

The original Power BI/Tableau dashboards are retained as separate-data legacy assets. The Excel summaries have been corrected. Native-file inspection confirms that the legacy Power BI/Tableau dashboards use different datasets. Corrected Excel summaries reconcile to the canonical CSVs; see the native verification report for engine-specific evidence. Use `Results/` and `REPORT.html` for the canonical analysis. See `Docs/Dashboard_Reconciliation.md` before presenting a legacy screenshot as evidence.

## Validation

20 blocking checks passed. Source limitations remain documented; a passing technical check does not establish causal validity.
