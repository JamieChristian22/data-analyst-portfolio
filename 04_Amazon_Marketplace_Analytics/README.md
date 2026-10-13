# Marketplace revenue and source reconciliation

**Data provenance:** supplied simulated portfolio CSVs. No external client or production outcome is implied.

## Decision question

How concentrated is recorded seller revenue, and what prevents financial reconciliation?

## Headline interpretation

The source records 1,830,085.36 in revenue across 24,000 sale rows. 9,019 rows differ from price × units by more than 0.011. The top ten sellers contribute 8.44%. The data do not establish platform commission revenue or order counts.

## Computed findings

### Summary

| sales_rows | units | recorded_revenue | price_times_units | revenue_discrepancy_rows | sellers |
| --- | --- | --- | --- | --- | --- |
| 24000 | 48063 | 1.83009e+06 | 1.90115e+06 | 9019 | 316 |

Full output: [Results/summary.csv](Results/summary.csv).

### Seller Concentration

| seller_id | revenue | rank | total_revenue | revenue_share |
| --- | --- | --- | --- | --- |
| 223 | 19,882.1 | 1 | 1.83009e+06 | 0.010864 |
| 264 | 17,618.5 | 2 | 1.83009e+06 | 0.00962712 |
| 247 | 15,950.7 | 3 | 1.83009e+06 | 0.00871582 |
| 114 | 15,485.4 | 4 | 1.83009e+06 | 0.00846156 |
| 307 | 15,376 | 5 | 1.83009e+06 | 0.00840182 |
| 269 | 14,661.2 | 6 | 1.83009e+06 | 0.00801123 |
| 86 | 14,459.6 | 7 | 1.83009e+06 | 0.00790107 |
| 283 | 13,732 | 8 | 1.83009e+06 | 0.00750345 |
| 61 | 13,720.3 | 9 | 1.83009e+06 | 0.00749709 |
| 218 | 13,522.1 | 10 | 1.83009e+06 | 0.0073888 |

Full output: [Results/seller_concentration.csv](Results/seller_concentration.csv).

### Category Performance

| category | recorded_revenue | units | sales_rows |
| --- | --- | --- | --- |
| Home | 416,940 | 10548 | 5268 |
| Electronics | 415,820 | 10891 | 5404 |
| Sports | 388,528 | 10387 | 5203 |
| Beauty | 330,136 | 8639 | 4324 |
| Toys | 278,660 | 7598 | 3801 |

Full output: [Results/category_performance.csv](Results/category_performance.csv).

### Stock Status Association

| category | price_band | in_stock | listings | mean_recorded_revenue |
| --- | --- | --- | --- | --- |
| Beauty | 50 to 99.99 | 0 | 17 | 0 |
| Beauty | 50 to 99.99 | 1 | 91 | 1,819.68 |
| Beauty | Under 50 | 0 | 25 | 0 |
| Beauty | Under 50 | 1 | 198 | 831.033 |
| Electronics | 100+ | 1 | 1 | 4,048.2 |
| Electronics | 50 to 99.99 | 0 | 15 | 0 |
| Electronics | 50 to 99.99 | 1 | 109 | 1,951.91 |
| Electronics | Under 50 | 0 | 27 | 0 |
| Electronics | Under 50 | 1 | 253 | 786.614 |
| Home | 100+ | 1 | 3 | 3,879.18 |

Full output: [Results/stock_status_association.csv](Results/stock_status_association.csv).

## Additional calculations

```json

{
  "top_10_seller_revenue_share": 0.08437196612512107,
  "seller_hhi": 42.394608986337744
}

```

## Recommendation

Resolve the difference between recorded revenue and price × units with a source owner before financial use. Review seller exposure by revenue share. Stock-status comparisons are diagnostic associations only.

## Limits and assumptions

The supplied data do not identify orders, fees, Prime membership or seller tiers. Sales row count is not order count. Recorded revenue is not labeled platform revenue or GMV. Snapshot stock status is not historical inventory. Repeated fact rows are retained because there is no sale ID; no causal lost-revenue estimate is justified.

## Reproduction

From the repository root: `python -m portfolio.run --project 04_Amazon_Marketplace_Analytics`.

Each named query in `SQL/analysis.sql` writes a corresponding results CSV. The Python runner independently reconciles headline metrics and ordered funnels. See `Results/validation.json` for checks and `Results/quality.json` for source diagnostics.

## Existing BI workbooks

The original Power BI/Tableau dashboards are retained as separate-data legacy assets. The Excel summaries have been corrected. Native-file inspection confirms that the legacy Power BI/Tableau dashboards use different datasets. Corrected Excel summaries reconcile to the canonical CSVs; see the native verification report for engine-specific evidence. Use `Results/` and `REPORT.html` for the canonical analysis. See `Docs/Dashboard_Reconciliation.md` before presenting a legacy screenshot as evidence.

## Validation

19 blocking checks passed. Source limitations remain documented; a passing technical check does not establish causal validity.
