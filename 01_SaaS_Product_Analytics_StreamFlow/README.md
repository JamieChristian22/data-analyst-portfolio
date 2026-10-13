# SaaS activation and revenue quality

**Data provenance:** supplied simulated portfolio CSVs. No external client or production outcome is implied.

## Decision question

Where does onboarding lose users, and how do observed activity and churn labels differ?

## Headline interpretation

The supplied subscription snapshot totals 189,975.00 MRR across 698 paying users. The paying-user churn label rate is 21.06%. Ordered Step 1-to-Step 2 loss is 62.59%; this is a descriptive funnel result, not a measured intervention outcome.

## Computed findings

### Summary

| users | paying_users | snapshot_mrr | snapshot_arr | paying_churn_label_rate |
| --- | --- | --- | --- | --- |
| 1500 | 698 | 189,975 | 2.2797e+06 | 0.210602 |

Full output: [Results/summary.csv](Results/summary.csv).

### Revenue By Tier

| plan_tier | users | snapshot_mrr | mrr_share |
| --- | --- | --- | --- |
| Enterprise | 92 | 159,201 | 0.83801 |
| Pro | 264 | 20,856 | 0.109783 |
| Starter | 342 | 9,918 | 0.0522069 |
| Free | 802 | 0 | 0 |

Full output: [Results/revenue_by_tier.csv](Results/revenue_by_tier.csv).

### Onboarding Funnel

| step | stage | users |
| --- | --- | --- |
| 1 | Step 1: Account | 1088 |
| 2 | Step 2: Workspace | 407 |
| 3 | Step 3: Integration | 123 |
| 4 | Step 4: First Workflow | 34 |
| 5 | Step 5: Invite Team | 9 |

Full output: [Results/onboarding_funnel.csv](Results/onboarding_funnel.csv).

### Power User Association

| activity_group | paying_users | churn_label_rate |
| --- | --- | --- |
| Under 20 runs | 698 | 0.210602 |

Full output: [Results/power_user_association.csv](Results/power_user_association.csv).

## Additional calculations

```json

{
  "onboarding_step2_conditional_dropoff": 0.6259191176470589
}

```

## Recommendation

Investigate the largest ordered onboarding drop-off with usability research. Treat activity/churn comparisons as associations; propose a randomized onboarding experiment before claiming retention impact.

## Limits and assumptions

MRR/ARR are supplied snapshots, not recognized revenue or verified active run rates. Churn is a supplied 90-day label, not an independently reconstructed cohort outcome. Free users are excluded from paying churn. Repeated daily events are retained because event IDs are absent. Activity uses [signup, signup + 90 days); incomplete follow-up and reverse causality limit interpretation.

## Reproduction

From the repository root: `python -m portfolio.run --project 01_SaaS_Product_Analytics_StreamFlow`.

Each named query in `SQL/analysis.sql` writes a corresponding results CSV. The Python runner independently reconciles headline metrics and ordered funnels. See `Results/validation.json` for checks and `Results/quality.json` for source diagnostics.

## Existing BI workbooks

The original Power BI/Tableau dashboards are retained as separate-data legacy assets. The Excel summaries have been corrected. Native-file inspection confirms that the legacy Power BI/Tableau dashboards use different datasets. Corrected Excel summaries reconcile to the canonical CSVs; see the native verification report for engine-specific evidence. Use `Results/` and `REPORT.html` for the canonical analysis. See `Docs/Dashboard_Reconciliation.md` before presenting a legacy screenshot as evidence.

## Validation

19 blocking checks passed. Source limitations remain documented; a passing technical check does not establish causal validity.
