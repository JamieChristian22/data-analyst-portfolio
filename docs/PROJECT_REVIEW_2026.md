# Project review: StreamFlow SaaS analytics

## Interview walkthrough (5–7 minutes)

**Business problem.** Identify where users drop out of onboarding and how that behavior relates to subscriptions and supplied churn labels.

**Data and scope.** This is a simulated portfolio dataset. Confirm the exact source tables, observation window, and grain in the project SQL before discussing the numbers.

**Analysis sequence**
1. Inspect source keys, missing values, duplicates, and event timestamps.
2. Define users, paying users, snapshot MRR, churn-label rate, and funnel conversion with explicit denominators.
3. Trace onboarding steps chronologically per user; distinguish missing events from actual drop-off.
4. Reconcile SQL aggregates against independent Python calculations and saved outputs.
5. Segment drop-off by meaningful dimensions only when sample sizes support comparisons.

**Decision recommendation.** Investigate the largest verified onboarding transition loss first. Design an experiment before claiming that a product change improves activation.

**Important limitations.** Snapshot MRR is not recognized revenue. A supplied churn label is not necessarily an observed cancellation. Correlation does not establish causation. Synthetic data cannot prove real business impact.

## Reviewer challenge questions

- What is the denominator for each funnel rate?
- How are repeated or out-of-order events handled?
- Can paying-user counts be reproduced from raw subscriptions?
- Which results are sensitive to the analysis window?
- What minimum sample size and guardrail metrics would an experiment need?

## Evidence checklist

- [ ] Link exact source SQL query and output CSV
- [ ] Link Python reconciliation or unit test
- [ ] Record dataset snapshot/version and execution command
- [ ] Include at least one failed/edge-case validation
- [ ] Explain a decision that would change if assumptions change

This walkthrough is an interview aid, not evidence that an additional analysis or experiment has been executed.
