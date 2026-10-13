
# 🧪 A/B Testing & Feature Impact Analysis

### Experimentation • Conversion Optimization • Statistical Inference • Product Analytics

**An end-to-end SQL and Python analytics project evaluating experimental conversion performance, statistical significance, customer behavior, and evidence-based feature rollout decisions.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Statistics](https://img.shields.io/badge/Statistics-Hypothesis_Testing-blueviolet)
![Confidence](https://img.shields.io/badge/Confidence_Interval-95%25-blue)
![Validation](https://img.shields.io/badge/Validation-20%2F20-success)
![Dataset](https://img.shields.io/badge/Dataset-Simulated-orange)

**Analyst:** Jamie Christian  
**Project:** 02 — A/B Test Feature Impact  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Jamie Christian](https://www.linkedin.com/in/jamiechristian2/)

---

## 📌 Executive Summary

This project evaluates the performance of a simulated A/B experiment comparing an existing product experience (**Control**) with an alternative experience (**Variant B**).

The objective is to determine whether Variant B demonstrates higher session conversion, estimate the uncertainty surrounding that difference, and identify additional evidence needed before an organization could make a responsible product rollout decision.

Using **12,000 simulated session observations**, SQL-based analysis, Python statistical calculations, and independent validation, the project examines:

- Conversion rates across experimental groups
- Absolute and relative conversion lift
- Statistical significance and confidence intervals
- Sample allocation balance
- Bounce rates and user engagement
- Revenue per session
- Device and acquisition-source segments
- Experiment validity and decision risks

### Key Findings

| Experiment Metric | Verified Result |
|---|---:|
| 👥 Total Sessions | 12,000 |
| 🔵 Control Conversion Rate | 19.84% |
| 🟢 Variant B Conversion Rate | 23.08% |
| 📈 Absolute Conversion Lift | +3.24 percentage points |
| 🚀 Relative Conversion Lift | +16.33% |
| 📊 95% Confidence Interval | +1.77 to +4.71 percentage points |
| 🧪 Two-Sided p-value | 0.0000154 |
| ⚖️ 50:50 Sample-Ratio Test p-value | 0.8124 |
| ✅ Runtime Validation Checks | 20 passed |

### Primary Finding

Variant B demonstrates a **3.24-percentage-point increase in observed session conversion**, equivalent to approximately **16.33% relative lift** over Control.

The unadjusted 95% confidence interval for the conversion-rate difference lies above zero, and the two-sided statistical test produces a small p-value under its assumptions.

However, the dataset does not include stable user identifiers, the actual assignment mechanism, or complete experiment governance information.

**Analytical conclusion:** Variant B is promising within the simulated dataset, but the results are insufficient to authorize a real product rollout or establish actual causal business impact.

> **Data transparency:** This case study uses supplied simulated portfolio data. It does not represent a live company experiment, verified production deployment, or realized business outcome.

---

## 📚 Table of Contents

1. [Business Problem](#-business-problem)
2. [Dataset Overview](#-dataset-overview)
3. [Technical Stack](#-technical-stack)
4. [Analytical Workflow](#-end-to-end-analytical-workflow)
5. [Experimental Design](#-experimental-design--hypotheses)
6. [KPI Definitions](#-kpi-definitions--measurement-framework)
7. [Conversion Analysis](#-analysis-1-conversion-rate-performance)
8. [Statistical Significance](#-analysis-2-statistical-significance--confidence-intervals)
9. [Sample Allocation](#-analysis-3-sample-ratio--assignment-balance)
10. [Engagement & Guardrails](#-analysis-4-engagement-revenue--guardrail-metrics)
11. [Segment Analysis](#-analysis-5-device--traffic-source-segmentation)
12. [SQL Implementation](#-sql-implementation)
13. [Business Recommendations](#-business-recommendations)
14. [Data Quality & Validation](#-data-quality--validation)
15. [BI & Dashboard Assets](#-business-intelligence--dashboard-assets)
16. [Repository Structure](#-project-structure)
17. [Reproduction](#-reproduce-the-analysis)
18. [Limitations](#-limitations--future-improvements)
19. [Project Takeaways](#-project-takeaways)

---

## 🎯 Business Problem

### Business Context

Digital product teams frequently introduce new features, designs, onboarding experiences, and user-interface changes to improve customer behavior and business performance.

However, implementing a new feature does not automatically mean it produces better outcomes.

An observed improvement may result from natural statistical variation, differences in user populations, measurement errors, or experiment-design problems.

Organizations need a reliable experimentation framework to distinguish promising changes from unsupported conclusions.

### Business Scenario

A simulated digital platform is evaluating two versions of a product experience:

**Control — Existing Experience**

Represents the baseline experience against which performance is measured.

**Variant B — Alternative Experience**

Represents a proposed change intended to improve session conversion.

The supplied dataset does not describe the precise feature modification, so the project does not assume a particular interface, pricing change, or product intervention.

### Primary Business Question

**Does Variant B achieve a higher session conversion rate than Control, and how strong is the statistical evidence supporting that difference?**

### Supporting Questions

1. How large is the conversion-rate difference?
2. Is the observed difference statistically distinguishable from zero under the assumed model?
3. How precise is the estimated improvement?
4. Are experimental group sizes consistent with an assumed 50:50 allocation?
5. Do bounce rates, engagement, and revenue per session move in potentially favorable directions?
6. Are segment-level patterns consistent enough to justify additional investigation?
7. What experiment-design limitations prevent a confident rollout decision?

### Business Objectives

| Objective | Analytical Focus | Decision Support |
|---|---|---|
| Measure Feature Impact | Control vs. Variant B conversion | Evaluate observed performance |
| Assess Statistical Uncertainty | Confidence interval and hypothesis test | Quantify uncertainty |
| Check Assignment Balance | Sample-ratio diagnostic | Detect allocation concerns |
| Examine User Experience | Bounce and engagement metrics | Identify potential guardrail issues |
| Evaluate Monetization | Revenue per session | Explore commercial implications |
| Understand Segments | Device and source comparisons | Identify follow-up questions |
| Ensure Analytical Reliability | Data contracts and metric reconciliation | Validate reporting accuracy |

---

## 🗄️ Dataset Overview

### Dataset Summary

The analysis uses one simulated session-level CSV containing **12,000 records**.

| Property | Description |
|---|---|
| Source File | `ab_sessions_raw.csv` |
| Cleaned File | `ab_sessions_clean.csv` |
| Source Records | 12,000 |
| Declared Primary Key | `session_id` |
| Experimental Groups | Control and Variant B |
| Observation Unit | Session |
| Date Granularity | Day |
| Data Type | Simulated portfolio data |

### Source Columns

| Column | Data Type | Description |
|---|---|---|
| `session_id` | Integer | Unique session identifier |
| `session_date` | Date | Recorded session date |
| `variant` | Text | Control or Variant B |
| `device` | Text | User device category |
| `source` | Text | Acquisition or traffic source |
| `converted` | Binary | Session conversion indicator |
| `engagement_score` | Numeric | Supplied engagement measure |
| `bounce` | Binary | Bounce indicator |
| `revenue` | Numeric | Recorded session revenue |

### Important Dataset Characteristics

**Session-Level Grain**

Each row represents a session, not necessarily a distinct individual.

**Binary Conversion**

`converted = 1` identifies a converted session, while `converted = 0` identifies a session without the recorded conversion.

**Traffic Source**

The dataset supports comparisons across source categories such as Email, Organic, Paid, and Referral.

**Engagement Score**

The engagement variable is numerical, but its measurement scale and construction are not independently documented.

**Revenue**

Revenue is reported in unspecified dataset currency units. It should not be presented as verified company revenue.

**Missing Assignment Metadata**

The dataset lacks stable user IDs and the experiment assignment log, making it impossible to independently establish whether observations represent independent, correctly randomized experimental units.

### Supporting Data Documentation

[📘 Data Dictionary](Docs/Data_Dictionary.md) | [📂 Original Dataset](Data/raw) | [📂 Cleaned Dataset](Data/clean)

---

## 🛠️ Technical Stack

| Category | Technology | Application |
|---|---|---|
| Programming | Python 3.12 | Statistical calculations and automated analysis |
| Query Language | SQL | Data aggregation and performance analysis |
| Database | SQLite | Executable experiment queries |
| Data Analysis | pandas | Independent calculation and reconciliation |
| Statistical Testing | Two-Proportion Z-Test | Primary conversion-rate comparison |
| Confidence Intervals | Newcombe-Wilson Method | Difference interval estimation |
| Assignment Diagnostics | Chi-Square Goodness-of-Fit | Assumed sample-ratio assessment |
| Spreadsheet Reporting | Excel | Validated analytical summaries |
| BI Data Sources | Tableau Hyper | Source-aligned reporting extract |
| Reporting | CSV and HTML | Saved analytical results |
| Testing | Python unittest | Statistical and integration checks |
| Source Integrity | SHA-256 | Reproducibility and evidence traceability |
| Version Control | Git and GitHub | Repository management |

### Technical Competencies Demonstrated

**SQL**

Aggregation, grouping, conditional metric calculation, segment analysis, date-based reporting, and null-safe numerical operations.

**Python**

Statistical calculations, confidence intervals, data processing, analytical reconciliation, reproducibility, and automated verification.

**Statistics**

Hypothesis testing, statistical significance, absolute and relative effects, interval estimation, experimental assumptions, and sample-ratio diagnostics.

**Business Analytics**

Metric selection, conversion optimization, product performance interpretation, guardrail evaluation, and rollout decision support.

---

## 🔄 End-to-End Analytical Workflow

The project follows a structured experimentation-analysis workflow.

### Phase 1 — Define the Decision

Identify the business question, comparison groups, primary outcome, supplementary metrics, and required evidence.

**Output:** Experiment measurement framework.

### Phase 2 — Validate the Dataset

Inspect and validate:

- Required fields
- Session identifiers
- Experiment labels
- Binary conversion values
- Numeric ranges
- Date formats
- Missing or duplicated records
- Source limitations

**Output:** Data quality and contract validation.

### Phase 3 — Prepare the Data

Apply documented normalization rules without inventing missing experiment metadata or modifying raw source records.

**Output:** Reproducible cleaned dataset.

### Phase 4 — Execute SQL Analysis

Calculate:

- Experimental group sizes
- Conversion counts
- Conversion rates
- Bounce rates
- Mean engagement
- Revenue per session
- Segment conversion rates
- Daily assignment summaries

**Output:** Named SQL result tables.

### Phase 5 — Run Statistical Analysis

Use Python to calculate:

- Absolute conversion lift
- Relative conversion lift
- Confidence interval for the conversion difference
- Two-sided two-proportion z-test
- 50:50 sample-ratio diagnostic

**Output:** Statistical estimates and experiment decision record.

### Phase 6 — Reconcile Results

Independently compare headline SQL outputs with Python calculations.

**Output:** Validation evidence.

### Phase 7 — Interpret the Findings

Assess the direction and magnitude of the findings while acknowledging unverified randomization, independence, and decision guardrails.

**Output:** Business interpretation and recommendations.

### Phase 8 — Generate Reports

Export result CSVs, statistical metrics, quality records, and a self-contained offline report.

**Output:** Reproducible analytical evidence.

### Workflow Architecture

**Raw CSV → Schema Validation → Clean CSV → SQLite Analysis → Statistical Inference → Independent Reconciliation → Reporting → Decision Review**

---

## 🧪 Experimental Design & Hypotheses

### Experiment Groups

| Group | Description | Sessions |
|---|---|---:|
| Control | Existing experience | 5,987 |
| Variant B | Alternative experience | 6,013 |
| **Total** | **All observations** | **12,000** |

The group sizes are close to equal, but balanced counts alone do not establish valid randomization.

### Primary Outcome

**Session Conversion Rate**

The percentage of recorded sessions resulting in a conversion.

### Statistical Hypotheses

Let:

- \(p_C\) = true Control conversion probability
- \(p_B\) = true Variant B conversion probability

**Null Hypothesis (H₀)**

There is no difference in conversion probability between groups.

\[
H_0: p_B - p_C = 0
\]

**Alternative Hypothesis (H₁)**

The conversion probabilities differ.

\[
H_1: p_B - p_C \neq 0
\]

The implemented primary significance test is **two-sided**, rather than a one-sided test that assumes improvement.

### Significance Threshold

For conventional interpretation, the project uses:

\[
\alpha = 0.05
\]

The associated unadjusted confidence level is 95%.

### Important Assumptions

The inferential procedure assumes that:

- Observations can be treated as independent Bernoulli trials.
- Each session belongs to one observed experiment group.
- The conversion outcome has a consistent definition.
- Allocation and exposure did not introduce unmodeled systematic bias.
- The comparison was not selectively chosen after repeated significance checks.

Several of these assumptions cannot be verified using the supplied fields.

---

## 📐 KPI Definitions & Measurement Framework

| Metric | Definition | Business Interpretation |
|---|---|---|
| Sessions | Count of observations within a group | Sample size |
| Conversions | Sum of positive conversion indicators | Recorded successful outcomes |
| Conversion Rate | Conversions ÷ Sessions | Primary performance KPI |
| Absolute Lift | Variant B rate − Control rate | Difference in percentage points |
| Relative Lift | Absolute lift ÷ Control rate | Proportional improvement |
| Bounce Rate | Bounced sessions ÷ Sessions | Descriptive user-experience indicator |
| Mean Engagement | Average engagement score | Descriptive engagement comparison |
| Revenue per Session | Total revenue ÷ Sessions | Commercial outcome indicator |
| Confidence Interval | Interval for conversion-rate difference | Estimation uncertainty |
| p-value | Probability, under the null and model assumptions, of a test statistic at least as extreme as observed | Significance evidence |
| Sample-Ratio p-value | Goodness-of-fit diagnostic against assumed allocation | Detects unusual group imbalance |

### Primary and Secondary Metrics

**Primary metric:** Session conversion rate.

**Supporting exploratory metrics:** Bounce rate, engagement score, and revenue per session.

**Diagnostic metric:** Sample-ratio mismatch test.

Supporting metrics are not treated as independently proven improvements because formal multiple-outcome inference and predefined guardrail thresholds are unavailable.

---

## 📈 Analysis 1: Conversion Rate Performance

### Business Question

Did Variant B generate a higher percentage of converting sessions than Control?

### Verified Results

| Metric | Control | Variant B |
|---|---:|---:|
| Sessions | 5,987 | 6,013 |
| Conversions | 1,188 | 1,388 |
| Conversion Rate | 19.84% | 23.08% |
| Non-Converting Sessions | 4,799 | 4,625 |

### Finding 1 — Variant B Has a Higher Observed Conversion Rate

Control converts at approximately **19.84%**, while Variant B converts at **23.08%**.

The difference is positive in the supplied session-level data.

### Finding 2 — Absolute Lift

Absolute lift measures the difference between conversion probabilities.

\[
\text{Absolute Lift}=p_B-p_C
\]

Using the recorded values:

\[
0.230833-0.198430=0.032403
\]

**Absolute Lift: +3.24 percentage points**

This is not a 3.24% relative increase. It is the difference between two percentages.

### Finding 3 — Relative Lift

Relative lift compares the absolute difference against the Control baseline.

\[
\text{Relative Lift}=\frac{p_B-p_C}{p_C}
\]

\[
=\frac{0.230833-0.198430}{0.198430}
\]

**Relative Lift: +16.33%**

### Business Interpretation

Within the supplied dataset, Variant B converts a larger proportion of sessions.

This is a promising descriptive result and motivates deeper evaluation.

It does not independently prove that the alternative feature causes higher conversion in a real user population.

### Evidence

[📊 Variant Summary](Results/variant_summary.csv)

---

## 📊 Analysis 2: Statistical Significance & Confidence Intervals

### Business Question

How much statistical uncertainty surrounds the observed conversion difference?

### Statistical Test

The project applies a two-sided pooled two-proportion z-test to compare the observed session conversion rates.

### Verified Test Results

| Statistical Metric | Result |
|---|---:|
| Absolute Difference | 0.032403 |
| Relative Lift | 16.33% |
| Two-Sided p-value | 0.0000154243 |
| Confidence Level | 95% |
| Lower Difference Bound | +1.77 percentage points |
| Upper Difference Bound | +4.71 percentage points |

### Finding 1 — Small p-value

The observed p-value is approximately:

\[
p=0.0000154
\]

Under the assumed model, this is below the conventional significance threshold of 0.05.

**Statistical interpretation:** The observed conversion difference is inconsistent with the equal-proportions null hypothesis under the test assumptions.

The p-value is not the probability that the null hypothesis is true, and it is not proof that the experiment was randomized correctly.

### Finding 2 — Positive Confidence Interval

The project uses the Newcombe method based on Wilson intervals to estimate the conversion-rate difference.

**95% Confidence Interval: +1.77 to +4.71 percentage points**

The interval excludes zero.

This supports a positive session-level difference under the assumed independent-trial model.

### Finding 3 — Statistical vs. Business Significance

A low p-value alone does not establish whether a feature is commercially valuable.

A deployment decision may also require:

- Business-defined minimum meaningful lift
- Acquisition and implementation costs
- Product reliability
- Customer experience considerations
- Revenue and retention guardrails
- Experiment duration
- Correct randomization
- Verified user-level exposure

### Interpretation Summary

**What the statistical results support:** A positive conversion-rate difference in the simulated session sample under the specified independent-trial assumptions.

**What they do not establish:** Valid real-world randomization, a causal feature effect, production readiness, or guaranteed future performance.

### Evidence

[🧪 Statistical Calculations](Results/additional_metrics.json)

---

## ⚖️ Analysis 3: Sample Ratio & Assignment Balance

### Business Question

Are the group sizes unusually different from an assumed equal allocation?

### Observed Sample Distribution

| Group | Sessions | Share |
|---|---:|---:|
| Control | 5,987 | 49.89% |
| Variant B | 6,013 | 50.11% |
| Total | 12,000 | 100% |

### Expected Allocation

Under an assumed 50:50 allocation:

| Group | Expected Sessions |
|---|---:|
| Control | 6,000 |
| Variant B | 6,000 |

### Statistical Diagnostic

The portfolio uses a chi-square goodness-of-fit test to examine whether the observed allocation is unusually imbalanced under the assumed equal split.

**Sample-Ratio Test p-value: 0.8124**

### Interpretation

The observed group counts do not provide evidence of a sample-ratio mismatch against the assumed 50:50 design.

However:

**A non-significant sample-ratio diagnostic does not verify the randomization process.**

The actual allocation configuration, assignment units, exposure logging, and user-level assignment records are unavailable.

### Recommended Validation

Before operational use, an experimentation team should confirm:

1. The intended allocation ratio.
2. The unit of randomization.
3. Whether individual users could appear in both groups.
4. Whether assignment and exposure logs are complete.
5. Whether filtering introduced unequal exclusions.

---

## 💼 Analysis 4: Engagement, Revenue & Guardrail Metrics

The experiment includes additional measures that can help assess whether higher conversion coincides with potentially favorable user behavior.

These are descriptive comparisons, not separately validated causal effects.

### Performance Comparison

| Metric | Control | Variant B |
|---|---:|---:|
| Bounce Rate | 43.33% | 38.18% |
| Mean Engagement Score | 53.00 | 60.29 |
| Total Recorded Revenue | 49,719.70 | 58,527.50 |
| Revenue per Session | 8.30 | 9.73 |

### Finding 1 — Lower Observed Bounce Rate

Variant B has an approximately **5.14-percentage-point lower bounce rate** than Control.

This may warrant investigating whether the alternative experience is associated with improved session engagement.

The comparison does not establish that Variant B caused lower bouncing.

### Finding 2 — Higher Mean Engagement Score

Variant B has an average engagement score of approximately 60.29 compared with 53.00 for Control.

Because the source does not independently specify the engagement scale or measurement construction, this difference should be interpreted cautiously.

### Finding 3 — Higher Recorded Revenue per Session

Revenue per session increases from approximately 8.30 for Control to 9.73 for Variant B.

**Observed Difference: Approximately 1.43 dataset currency units per session.**

This is potentially relevant to business evaluation.

However, the repository does not establish a statistically validated treatment effect on revenue per session or demonstrate the accounting meaning of the revenue field.

### Guardrail Considerations

| Metric | Direction Observed | Interpretation |
|---|---|---|
| Conversion | Higher for Variant B | Favorable primary metric |
| Bounce | Lower for Variant B | Potentially favorable |
| Engagement | Higher for Variant B | Exploratory |
| Revenue per Session | Higher for Variant B | Exploratory commercial signal |

### Recommendation

Keep conversion as the primary metric while formally defining guardrails before any future live experiment.

Do not present descriptive movement in supporting metrics as proof of statistically significant improvements.

**Evidence:** [Variant Summary](Results/variant_summary.csv)

---

## 📱 Analysis 5: Device & Traffic Source Segmentation

### Business Question

Do conversion patterns differ across device types and acquisition channels?

### Analytical Approach

SQL groups sessions by:

- Device
- Traffic source
- Experiment variant

For each combination, the analysis calculates:

- Session count
- Conversion count
- Conversion rate

### Selected Verified Segment Results

| Segment | Control Conversion | Variant B Conversion |
|---|---:|---:|
| Desktop — Email | 18.54% | 22.00% |
| Desktop — Organic | 21.27% | 24.53% |
| Desktop — Paid | 18.43% | 23.88% |
| Desktop — Referral | 20.00% | 24.73% |
| Mobile — Email | 19.67% | 23.36% |

### Finding 1 — Positive Descriptive Differences Across Selected Segments

Variant B shows higher conversion rates in each selected segment above.

This pattern is useful for identifying where additional experimentation could be informative.

It does not establish that every segment experienced a statistically significant treatment effect.

### Finding 2 — Traffic Source May Matter

Different acquisition channels can contain users with different intentions, needs, or purchasing behavior.

A segmented analysis helps identify heterogeneity, but does not automatically explain its causes.

### Finding 3 — Segment Analysis Requires Additional Controls

Subgroup comparisons introduce additional uncertainty and multiple-testing concerns.

A formal segment-effect investigation would require:

- Predefined hypotheses
- Adequate subgroup sample sizes
- Confidence intervals for treatment differences
- Interaction testing
- Multiple-testing considerations
- Verified randomization and exposure information

### Recommendation

Use the current results as exploratory evidence.

For a future live experiment, establish a small set of preselected segment hypotheses instead of treating every favorable subgroup result as a proven effect.

**Evidence:** [Complete Segment Results](Results/segment_conversion.csv)

---

## 💻 SQL Implementation

This project uses named executable SQL queries stored in `SQL/analysis.sql`.

### Query 1 — Experimental Group Summary

```sql
SELECT
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions,
    AVG(1.0 * converted) AS conversion_rate,
    AVG(1.0 * bounce) AS bounce_rate,
    AVG(engagement_score) AS mean_engagement,
    SUM(revenue) AS revenue,
    AVG(revenue) AS revenue_per_session

FROM ab_sessions_clean

GROUP BY variant

ORDER BY variant;
```

**SQL Concepts Demonstrated**

- Grouped aggregation
- Binary outcome averaging
- Calculated KPIs
- Revenue aggregation
- Result ordering

**Business Application**

Produces the central experiment-performance table used to compare Control and Variant B.

### Query 2 — Conversion by Device and Acquisition Source

```sql
SELECT
    device,
    source,
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions,
    AVG(1.0 * converted) AS conversion_rate

FROM ab_sessions_clean

GROUP BY
    device,
    source,
    variant

ORDER BY
    device,
    source,
    variant;
```

**SQL Concepts Demonstrated**

- Multi-dimensional grouping
- Segment-level KPIs
- Conditional population comparisons
- Granular business reporting

**Business Application**

Supports exploratory assessment of conversion patterns across device and acquisition categories.

### Query 3 — Daily Assignment and Conversions

```sql
SELECT
    session_date,
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions

FROM ab_sessions_clean

GROUP BY
    session_date,
    variant

ORDER BY
    session_date,
    variant;
```

**SQL Concepts Demonstrated**

- Date-based aggregation
- Group comparisons
- Time-series reporting preparation
- Experiment diagnostic reporting

**Business Application**

Provides daily observations that can be used to investigate allocation patterns and changes in recorded outcomes.

### Technical Design Principles

The SQL implementation emphasizes:

- Named, reproducible queries
- Consistent KPI denominators
- SQLite-compatible execution
- Numerical results suitable for independent Python checks
- Output files that can be traced back to source inputs

**Full SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Python Statistical Analysis

Python supports the statistical inference and reconciliation stages beyond the descriptive SQL reporting.

### Primary Statistical Calculations

**Conversion Probability**

\[
p=\frac{\text{Conversions}}{\text{Sessions}}
\]

**Absolute Lift**

\[
\Delta=p_B-p_C
\]

**Relative Lift**

\[
L=\frac{p_B-p_C}{p_C}
\]

**Pooled Proportion Under the Null**

\[
\hat p=\frac{x_B+x_C}{n_B+n_C}
\]

**Two-Proportion Z Statistic**

\[
z=\frac{p_B-p_C}
{\sqrt{\hat p(1-\hat p)(1/n_B+1/n_C)}}
\]

The primary test is two-sided.

### Confidence Interval Method

The project uses a **Newcombe-Wilson difference interval**, which derives a confidence interval for the difference between two independent proportions from Wilson score intervals.

This is distinct from simply applying a symmetric normal interval to the observed difference.

### Statistical Output

The analysis exports `Results/additional_metrics.json`, containing:

- Group sample sizes
- Conversion probabilities
- Absolute lift
- Relative lift
- Confidence interval bounds
- Two-sided p-value
- Sample-ratio diagnostic
- Confidence level
- Experiment decision note

### Independent Metric Reconciliation

The runner compares selected SQL values with independently computed Python results.

This reduces the risk of reporting discrepancies from inconsistent filters, denominators, or implementations.

**Supporting Code:** [Project Python Entry Point](Python/analysis.py)

---

## 💡 Business Recommendations

### Decision Summary

| Evaluation Area | Assessment |
|---|---|
| Primary Conversion Result | Positive observed lift |
| Statistical Evidence | Significant under specified assumptions |
| Confidence Interval | Entirely positive under assumed model |
| Assumed Sample Balance | No detected 50:50 mismatch |
| Supporting Metrics | Descriptively favorable |
| Randomization Verification | Incomplete |
| Independent User Assignment | Unverified |
| Production Rollout Authorization | Not supported |

### Recommendation 1 — Validate Experiment Assignment

**Priority: High**

Confirm the randomization unit, exposure rules, assignment logs, and intended allocation before relying on inferential conclusions.

Without that information, session-level observations may overstate the effective sample size.

### Recommendation 2 — Verify Primary Conversion Measurement

**Priority: High**

Confirm that conversion events are defined consistently across groups and that user exposure and outcomes are correctly attributed.

### Recommendation 3 — Establish Business Guardrails

**Priority: High**

Define acceptable thresholds for bounce behavior, revenue performance, reliability, and other relevant business outcomes.

### Recommendation 4 — Investigate Segment Heterogeneity

**Priority: Medium**

Identify whether selected device or traffic-source differences justify future pre-registered hypotheses.

### Recommendation 5 — Use a Controlled Rollout Framework

**Priority: Medium**

If a future live experiment passes validity checks, evaluate phased deployment with appropriate monitoring and rollback criteria.

### Proposed 30/60/90-Day Evaluation Plan

These are proposed actions for a real experimentation program, not completed implementations.

**Days 1–30 — Validate Measurement**

- Audit assignment and exposure data.
- Confirm the unit of randomization.
- Establish stable user identifiers.
- Document conversion-event definitions.
- Define minimum business-relevant lift and guardrails.

**Days 31–60 — Execute Valid Experimentation**

- Predefine hypotheses and evaluation criteria.
- Calculate sample size based on the business-relevant effect.
- Control experiment duration and stopping rules.
- Monitor assignment integrity and data quality.

**Days 61–90 — Evaluate and Decide**

- Analyze the preselected primary comparison.
- Review guardrails and uncertainty.
- Evaluate any planned subgroup interactions.
- Recommend launch, iteration, or rejection based on complete evidence.

### Final Product Decision

**Do not authorize a real rollout based solely on this simulated session-level dataset.**

The statistical findings warrant further investigation but do not replace valid experiment design, production measurement, or business risk evaluation.

---

## ✅ Data Quality & Validation

### Validation Overview

The project includes documented automated checks across source contracts, SQL execution, and independent metric reconciliation.

### Verified Data Quality

| Data Quality Indicator | Result |
|---|---:|
| Source Rows | 12,000 |
| Cleaned Rows | 12,000 |
| Missing Required Cells | 0 |
| Exact-Repeat Source Rows | 0 |
| Declared Primary Key | `session_id` |
| Experiment Arms | 2 |
| Runtime Checks | 20 |
| Runtime Validation Status | Passed |

### Validation Areas

**1. Schema Integrity**

Ensures required columns and supported data types match the source contract.

**2. Required Values**

Rejects missing required fields.

**3. Primary Key Integrity**

Checks uniqueness of the declared session identifier.

**4. Experiment Group Validity**

Confirms that the cleaned analysis contains the expected two experiment arms.

**5. SQL Execution**

Executes all three named analytical queries.

**6. Headline Metric Reconciliation**

Independently verifies group-level results, including session counts, conversions, rates, revenue, and engagement summaries.

**7. Statistical Test Coverage**

The shared portfolio test suite covers statistical boundaries, inference behavior, and selected integrity scenarios.

**8. Source and Output Traceability**

SHA-256 manifests associate data, code, and generated outputs.

### Known Semantic Limitation

The data quality report flags all 12,000 session records as affected by the missing randomization-unit context.

This does not mean 12,000 individual records are malformed.

It means that **the independence and allocation assumptions required for causal experiment interpretation cannot be independently validated**.

### Evidence Files

| File | Purpose |
|---|---|
| [validation.json](Results/validation.json) | Documented runtime checks |
| [quality.json](Results/quality.json) | Data quality and source limitations |
| [manifest.json](Results/manifest.json) | Reproducibility hashes and software metadata |
| [query_plans.json](Results/query_plans.json) | Local SQLite execution plans |
| [additional_metrics.json](Results/additional_metrics.json) | Statistical estimates and decision record |

**Verification boundary:** Passing technical checks does not independently validate randomization, session independence, experiment governance, or causal identification.

---

## 📊 Business Intelligence & Dashboard Assets

The repository contains analytical reporting assets in addition to its SQL and Python outputs.

### Available Assets

| Asset | Purpose | File |
|---|---|---|
| Excel Model | Corrected source-aligned analytical summary | [Excel Workbook](Excel/02_AB_Test_Feature_Impact_Model.xlsx) |
| Tableau Workbook | Preserved legacy experiment dashboard | [Dashboard Folder](Dashboard/) |
| Tableau Hyper Extract | Source-aligned canonical reporting data | [Validated Extract](Dashboard/Validated_Analysis.hyper) |
| Dashboard Image | Legacy visualization reference | [Images Folder](Images/) |
| Offline Analytical Report | Canonical analytical findings | [REPORT.html](REPORT.html) |

### Native Workbook Verification

The native-file audit found that the original Tableau workbook contains **12 aggregated experiment rows**, while the canonical SQL/Python analysis is based on **12,000 session-level observations**.

These assets have different data grains, populations, and source structures.

Therefore, the legacy dashboard screenshot is not presented as verification of the current canonical experiment results.

### Verified Work

- Canonical SQL/Python metric reconciliation
- Corrected Excel summary formulas
- Documented Excel recalculation evidence
- Source-aligned Tableau Hyper extract
- Hyper table readback verification
- Workbook source auditing

### Outstanding Acceptance

Full Tableau Desktop refresh, reconstructed visuals, filters, calculated fields, and visual acceptance have not been reported as completed.

### Recommended Dashboard Views

For a future source-aligned dashboard, useful visuals would include:

**Experiment Scorecard**

Conversion rates, sample sizes, absolute lift, relative lift, and the primary confidence interval.

**Variant Performance**

Side-by-side conversion, bounce, engagement, and revenue-per-session comparisons.

**Segment Performance**

Device and traffic-source conversion tables with sample-size context.

**Daily Diagnostics**

Group counts and conversion summaries over the recorded observation dates.

**Experiment Decision Panel**

Statistical findings, assumptions, validity gates, and final evaluation status.

These are design recommendations and should not be interpreted as already completed Tableau visuals.

### Supporting Documentation

[Dashboard Reconciliation](Docs/Dashboard_Reconciliation.md) | [Dashboard Field Mapping](Docs/Dashboard_Field_Mapping.md) | [Connection Guide](Docs/Connect_To_Dashboard.md) | [Native Workbook Verification](../verification/native/README.md)

---

## 📂 Project Structure

```text
02_AB_Test_Feature_Impact/
│
├── Data/
│   ├── raw/
│   │   └── ab_sessions_raw.csv
│   └── clean/
│       └── ab_sessions_clean.csv
│
├── SQL/
│   └── analysis.sql
│
├── Python/
│   └── analysis.py
│
├── Excel/
│   └── 02_AB_Test_Feature_Impact_Model.xlsx
│
├── Dashboard/
│   ├── README.md
│   ├── Validated_Analysis.hyper
│   └── Experiment _ A-B Test _ Feature Impact Dashboard.twbx
│
├── Images/
│   └── Experiment _ A-B Test _ Feature Impact Dashboard.png
│
├── Results/
│   ├── variant_summary.csv
│   ├── segment_conversion.csv
│   ├── daily_assignment.csv
│   ├── additional_metrics.json
│   ├── quality.json
│   ├── validation.json
│   ├── query_plans.json
│   └── manifest.json
│
├── Docs/
│   ├── Data_Dictionary.md
│   ├── KPI_Lineage.md
│   ├── Dashboard_Reconciliation.md
│   ├── Dashboard_Field_Mapping.md
│   └── Connect_To_Dashboard.md
│
├── REPORT.html
└── README.md
```

The project uses shared modules from the parent repository for data processing, statistical calculations, SQL execution, and reporting.

---

## ▶️ Reproduce the Analysis

### Prerequisites

- Python 3.12
- Git
- Python package installation capability

The verified core workflow does not require a cloud account, paid database service, or licensed BI application.

### Step 1 — Clone the Portfolio

```bash
git clone https://github.com/JamieChristian22/data-analyst-portfolio.git
cd data-analyst-portfolio
```

### Step 2 — Create a Python Environment

```bash
python -m venv .venv
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4 — Execute the A/B Testing Project

```bash
python -m portfolio.run --project 02_AB_Test_Feature_Impact
```

This generates the project’s analytical outputs, statistical calculations, and execution evidence.

### Step 5 — Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

The test command executes the portfolio-wide test suite.

### Step 6 — Review the Results

Navigate to:

`02_AB_Test_Feature_Impact/Results/`

Review:

- `variant_summary.csv`
- `segment_conversion.csv`
- `daily_assignment.csv`
- `additional_metrics.json`
- `validation.json`

### Step 7 — Open the Offline Report

Open:

`02_AB_Test_Feature_Impact/REPORT.html`

Download or clone the project to view the rendered offline report locally.

GitHub may display HTML source rather than presenting the rendered report.

### Reproducibility Guidance

The project recreates local analytical outputs from the supplied data and code.

After a failed run, do not assume previously generated result files represent a current validated execution. Rerun successfully and check the current manifest and validation evidence.

For additional help, see the [Portfolio Runbook](../docs/RUNBOOK.md).

---

## ⚠️ Limitations & Future Improvements

### Current Analytical Limitations

**1. Simulated Data**

The results describe a portfolio dataset, not an actual company experiment.

**2. Unknown Randomization Unit**

Stable user IDs and assignment logs are not supplied.

A single individual may theoretically contribute multiple sessions, violating independent-trial assumptions.

**3. Unverified Intended Allocation**

The 50:50 sample-ratio diagnostic assumes an intended equal split. The actual assignment configuration is unavailable.

**4. Unverified Exposure and Stopping Rules**

The source does not establish exposure quality, sequential testing behavior, or whether the experiment followed a predetermined stopping rule.

**5. Multiple Comparisons**

Segment results and supporting outcome metrics are exploratory. No familywise multiple-testing adjustment has been applied.

**6. Incomplete Business Context**

The exact product change, implementation costs, and minimum commercially meaningful effect are not documented.

**7. Unspecified Revenue Units**

Revenue values lack a verified currency code and accounting definition.

**8. Native Dashboard Source Mismatch**

The preserved legacy Tableau workbook uses a different dataset from the canonical analysis, and full Desktop acceptance remains outstanding.

### Future Analytical Enhancements

Potential improvements include:

- User-level assignment and exposure tracking
- Power and sample-size calculations
- Minimum detectable effect documentation
- Experiment pre-registration
- User-clustered or otherwise design-appropriate inference
- Revenue-per-session uncertainty estimation
- Guardrail thresholds
- Predefined segment interaction testing
- Sequential testing controls
- Long-term retention measurement
- Source-aligned native dashboard acceptance
- Formal decision records for live experimentation

These are future opportunities, not completed project features.

---

## 🧠 Project Takeaways

### Technical Skills Demonstrated

This project provides evidence of work with:

- SQL-based experiment reporting
- Python statistical analysis
- Conversion-rate calculations
- Hypothesis testing
- Confidence interval estimation
- Sample-ratio diagnostics
- Device and traffic-source segmentation
- Numerical reconciliation
- Data cleaning and source validation
- Reproducible analytics
- Automated testing
- Analytical reporting

### Business Skills Demonstrated

The case study also emphasizes:

- Connecting statistical findings to business questions
- Distinguishing absolute and relative performance changes
- Evaluating uncertainty rather than relying on point estimates
- Recognizing limitations in experimental design
- Avoiding unsupported causal conclusions
- Identifying decision-critical information gaps
- Developing actionable validation and experimentation plans

### Final Conclusion

The simulated experiment shows a higher observed conversion rate for Variant B:

**Control: 19.84% → Variant B: 23.08%**

This represents a **3.24-percentage-point absolute increase** and a **16.33% relative increase**, with a positive unadjusted 95% confidence interval under the specified independent-trial model.

Supporting descriptive metrics also move in potentially favorable directions.

Nevertheless, a complete production decision would require verified assignment design, user-level independence, exposure records, guardrails, and business context.

**The central lesson is that strong experimentation analysis combines accurate calculations, appropriate uncertainty estimates, validated data, and responsible decision-making.**

---

## 📚 Supporting Documentation & Evidence

| Resource | Description |
|---|---|
| [Data Dictionary](Docs/Data_Dictionary.md) | Dataset fields, source contracts, and data types |
| [KPI Lineage](Docs/KPI_Lineage.md) | Metric formulas, assumptions, and result mapping |
| [SQL Analysis](SQL/analysis.sql) | Executable experiment queries |
| [Python Analysis](Python/analysis.py) | Project Python entry point |
| [Variant Summary](Results/variant_summary.csv) | Main experiment KPIs |
| [Segment Conversion](Results/segment_conversion.csv) | Device and acquisition-source breakdowns |
| [Daily Assignment](Results/daily_assignment.csv) | Daily sample and conversion counts |
| [Statistical Metrics](Results/additional_metrics.json) | Lift, interval estimates, and diagnostic tests |
| [Quality Report](Results/quality.json) | Dataset quality and semantic limitations |
| [Validation Report](Results/validation.json) | Runtime verification evidence |
| [Offline Report](REPORT.html) | Generated canonical analysis |
| [Native Workbook Verification](../verification/native/README.md) | Spreadsheet and Tableau source verification |

---

## 👨‍💻 About the Analyst

**Jamie Christian**

Data Analytics | Business Intelligence | SQL | Python | Product Analytics

I focus on translating business questions into measurable analytical problems, validating data, evaluating performance, and communicating reliable insights.

My interests include experimentation, customer behavior, business intelligence, data quality, operational analysis, and evidence-based product decisions.

📧 [Email](mailto:Jamiechristian331@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/jamiechristian2/)  
💻 [GitHub Profile](https://github.com/JamieChristian22)

### 🔗 Explore the Portfolio

[⬅️ Back to Main Data Analyst Portfolio](../README.md)

[📈 Previous Project: SaaS Product Analytics](../01_SaaS_Product_Analytics_StreamFlow/README.md)

[🛒 Next Project: Ecommerce Product Analytics](../03_Ecommerce_Product_Analytics/README.md)

---

**🧪 A/B Testing & Feature Impact Analysis | Built by Jamie Christian**

*Statistically informed decisions. Reproducible analysis. Transparent evidence.*
