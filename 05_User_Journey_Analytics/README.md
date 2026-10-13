# Ordered user journey and conversion friction

**Data provenance:** supplied simulated portfolio CSVs. No external client or production outcome is implied.

## Decision question

How many users complete an ordered commerce path, and how does observed conversion differ by returning status?

## Headline interpretation

There are 627 observed purchasers among 6,000 users (10.45%). No user satisfies the entire six-step date-ordered path in the supplied records. This conflicts with purchase reach and signals source sequencing problems; it is not evidence of zero actual purchases or 100% business checkout abandonment.

## Computed findings

### Summary

| users | purchasers | observed_purchase_rate |
| --- | --- | --- |
| 6000 | 627 | 0.1045 |

Full output: [Results/summary.csv](Results/summary.csv).

### Ordered Funnel

| step | stage | users |
| --- | --- | --- |
| 1 | Landing | 6000 |
| 2 | Browse | 2304 |
| 3 | Product View | 590 |
| 4 | Add to Cart | 102 |
| 5 | Checkout | 12 |
| 6 | Purchase | 0 |

Full output: [Results/ordered_funnel.csv](Results/ordered_funnel.csv).

### Returning User Conversion

| is_returning | users | purchasers | purchase_rate |
| --- | --- | --- | --- |
| 0 | 4346 | 359 | 0.0826047 |
| 1 | 1654 | 268 | 0.162031 |

Full output: [Results/returning_user_conversion.csv](Results/returning_user_conversion.csv).

### Time To Purchase

| user_id | first_purchase_date | days_to_purchase |
| --- | --- | --- |
| 17 | 2025-06-15 | 2 |
| 22 | 2025-08-25 | 2 |
| 24 | 2025-07-27 | 9 |
| 27 | 2025-11-23 | 3 |
| 32 | 2025-04-24 | 7 |
| 41 | 2025-12-10 | 0 |
| 74 | 2025-05-16 | 12 |
| 86 | 2025-12-04 | 1 |
| 89 | 2025-03-29 | 1 |
| 107 | 2025-05-28 | 12 |

Full output: [Results/time_to_purchase.csv](Results/time_to_purchase.csv).

### Stage Reach

| journey_stage | users |
| --- | --- |
| Landing | 6000 |
| Browse | 4346 |
| Product View | 2923 |
| Add to Cart | 1883 |
| Checkout | 1174 |
| Purchase | 627 |
| Signup | 401 |

Full output: [Results/stage_reach.csv](Results/stage_reach.csv).

## Additional calculations

```json

{
  "p50_days_to_purchase": 7.0,
  "p90_days_to_purchase": 12.0,
  "ordered_path_loss_after_checkout": 1.0,
  "signup_handling": "Signup is reported separately; source ordinal 7 is not treated as a universal post-purchase requirement. Ordered-path loss is a tracking/sequence diagnostic, not validated checkout abandonment."
}

```

## Recommendation

Compare overall purchase reach with the stricter ordered funnel and investigate missing or out-of-order tracking. Diagnose the largest eligible transition drop before proposing a UX test.

## Limits and assumptions

Source dates have day granularity; same-day steps are allowed and cannot establish within-day order. Signup is separate from the six-step commerce funnel. First-seen cohorts have different follow-up durations, so conversion and time-to-purchase are descriptive, not censoring-adjusted causal measures.

## Reproduction

From the repository root: `python -m portfolio.run --project 05_User_Journey_Analytics`.

Each named query in `SQL/analysis.sql` writes a corresponding results CSV. The Python runner independently reconciles headline metrics and ordered funnels. See `Results/validation.json` for checks and `Results/quality.json` for source diagnostics.

## Existing BI workbooks

The original Power BI/Tableau dashboards are retained as separate-data legacy assets. The Excel summaries have been corrected. Native-file inspection confirms that the legacy Power BI/Tableau dashboards use different datasets. Corrected Excel summaries reconcile to the canonical CSVs; see the native verification report for engine-specific evidence. Use `Results/` and `REPORT.html` for the canonical analysis. See `Docs/Dashboard_Reconciliation.md` before presenting a legacy screenshot as evidence.

## Validation

15 blocking checks passed. Source limitations remain documented; a passing technical check does not establish causal validity.
