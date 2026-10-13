# Experiment measurement and rollout judgment

**Data provenance:** supplied simulated portfolio CSVs. No external client or production outcome is implied.

## Decision question

Does Variant B show higher session conversion, and how uncertain is the estimated difference?

## Headline interpretation

Control converts at 19.84% and Variant B at 23.08%: +3.24 percentage points, or 16.33% relative lift. The unadjusted 95% difference interval is 1.77 to 4.71 percentage points. Statistical inference remains conditional on unverified session independence.

## Computed findings

### Variant Summary

| variant | sessions | conversions | conversion_rate | bounce_rate | mean_engagement | revenue | revenue_per_session |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Control | 5987 | 1188 | 0.19843 | 0.433272 | 52.9966 | 49,719.7 | 8.30462 |
| Variant B | 6013 | 1388 | 0.230833 | 0.381839 | 60.2906 | 58,527.5 | 9.73349 |

Full output: [Results/variant_summary.csv](Results/variant_summary.csv).

### Segment Conversion

| device | source | variant | sessions | conversions | conversion_rate |
| --- | --- | --- | --- | --- | --- |
| Desktop | Email | Control | 426 | 79 | 0.185446 |
| Desktop | Email | Variant B | 409 | 90 | 0.220049 |
| Desktop | Organic | Control | 1072 | 228 | 0.212687 |
| Desktop | Organic | Variant B | 1109 | 272 | 0.245266 |
| Desktop | Paid | Control | 917 | 169 | 0.184297 |
| Desktop | Paid | Variant B | 963 | 230 | 0.238837 |
| Desktop | Referral | Control | 290 | 58 | 0.2 |
| Desktop | Referral | Variant B | 279 | 69 | 0.247312 |
| Mobile | Email | Control | 427 | 84 | 0.196721 |
| Mobile | Email | Variant B | 428 | 100 | 0.233645 |

Full output: [Results/segment_conversion.csv](Results/segment_conversion.csv).

### Daily Assignment

| session_date | variant | sessions | conversions |
| --- | --- | --- | --- |
| 2025-06-01 | Control | 107 | 19 |
| 2025-06-01 | Variant B | 96 | 19 |
| 2025-06-02 | Control | 96 | 23 |
| 2025-06-02 | Variant B | 84 | 20 |
| 2025-06-03 | Control | 99 | 17 |
| 2025-06-03 | Variant B | 109 | 31 |
| 2025-06-04 | Control | 103 | 22 |
| 2025-06-04 | Variant B | 113 | 25 |
| 2025-06-05 | Control | 99 | 19 |
| 2025-06-05 | Variant B | 79 | 13 |

Full output: [Results/daily_assignment.csv](Results/daily_assignment.csv).

## Additional calculations

```json

{
  "experiment": {
    "control_n": 5987,
    "treatment_n": 6013,
    "control_rate": 0.19842993151828964,
    "treatment_rate": 0.23083319474471978,
    "absolute_lift": 0.03240326322643014,
    "relative_lift": 0.16329826341467782,
    "difference_ci_low": 0.01771561966720977,
    "difference_ci_high": 0.04707410353407348,
    "p_value": 1.5424301091656673e-05,
    "srm_p_value_50_50": 0.8123880360341355,
    "confidence_level": 0.95,
    "decision": "Do not authorize rollout from simulated session-level evidence; verify randomization, user independence and business guardrails."
  }
}

```

## Recommendation

Use conversion as the primary metric; investigate bounce, revenue per session and engagement as guardrails. Verify assignment unit, exposure, intended allocation and experiment duration before a real rollout. Segment results are exploratory.

## Limits and assumptions

Simulated session observations lack stable user IDs and assignment logs. The two-sided pooled z-test and Newcombe-Wilson interval assume independent trials. The sample-ratio test assumes 50:50 allocation. No claim of actual causal business impact is made; repeated peeking and multiple comparisons are not corrected.

## Reproduction

From the repository root: `python -m portfolio.run --project 02_AB_Test_Feature_Impact`.

Each named query in `SQL/analysis.sql` writes a corresponding results CSV. The Python runner independently reconciles headline metrics and ordered funnels. See `Results/validation.json` for checks and `Results/quality.json` for source diagnostics.

## Existing BI workbooks

The original Power BI/Tableau dashboards are retained as separate-data legacy assets. The Excel summaries have been corrected. Native-file inspection confirms that the legacy Power BI/Tableau dashboards use different datasets. Corrected Excel summaries reconcile to the canonical CSVs; see the native verification report for engine-specific evidence. Use `Results/` and `REPORT.html` for the canonical analysis. See `Docs/Dashboard_Reconciliation.md` before presenting a legacy screenshot as evidence.

## Validation

20 blocking checks passed. Source limitations remain documented; a passing technical check does not establish causal validity.
