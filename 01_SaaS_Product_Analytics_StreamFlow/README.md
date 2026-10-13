
# 📈 SaaS Product Analytics | StreamFlow

### Customer Activation • Subscription Revenue • Onboarding Funnels • Churn Analysis

**An end-to-end SQL and Python analytics case study examining how SaaS customers activate, progress through onboarding, contribute subscription revenue, and exhibit retention-related behavior.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Analytics](https://img.shields.io/badge/Product-Analytics-blueviolet)
![Data Quality](https://img.shields.io/badge/Validation-19%2F19-success)
![Dataset](https://img.shields.io/badge/Data-Simulated-orange)

**Created by:** Jamie Christian  
**Project:** 01 — SaaS Product Analytics  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Jamie Christian](https://www.linkedin.com/in/jamiechristian2/)

---

## 📌 Executive Summary

StreamFlow is a simulated Software-as-a-Service (SaaS) product analytics case study designed to investigate customer onboarding, subscription performance, user activity, and churn-related indicators.

The project demonstrates how a Data Analyst can use SQL, Python, data quality checks, and business intelligence principles to transform raw SaaS data into reliable metrics and actionable recommendations.

The analysis focuses on four questions:

1. Where do customers experience the greatest onboarding drop-off?
2. How is monthly recurring revenue distributed across subscription tiers?
3. What does the supplied churn indicator reveal about paying subscribers?
4. What additional evidence is required before making product or retention decisions?

### Key Results

| Business Metric | Verified Result |
|---|---:|
| 👥 Total Users | 1,500 |
| 💳 Paying Subscribers | 698 |
| 💰 Monthly Recurring Revenue Snapshot | 189,975.00 |
| 📅 Annualized Revenue Snapshot | 2,279,700.00 |
| 📉 Paying-User Churn Label Rate | 21.06% |
| 🚧 First Onboarding Transition Drop-Off | 62.59% |
| 🏢 Enterprise Share of MRR | 83.80% |
| ✅ Project Validation Checks | 19 passed |

**Data disclosure:** This project uses supplied simulated datasets. Currency units are unspecified, and the results are not claims about a real business, production system, or achieved customer outcomes.

### Primary Finding

The largest early onboarding loss occurs between **Step 1: Account** and **Step 2: Workspace**, where 62.59% of users reaching Step 1 do not satisfy the next ordered stage.

At the same time, Enterprise subscriptions contribute approximately 83.80% of total recorded MRR, highlighting substantial subscription-revenue concentration.

Together, these findings identify two areas deserving further investigation: **early product activation and revenue concentration**.

---

## 📚 Table of Contents

1. [Business Problem](#-business-problem)
2. [Dataset Overview](#-dataset-overview)
3. [Technical Stack](#-technical-stack)
4. [Analytical Workflow](#-end-to-end-analytical-workflow)
5. [KPI Definitions](#-kpi-definitions--business-rules)
6. [Analysis 1: SaaS Revenue](#-analysis-1-saas-subscription-revenue)
7. [Analysis 2: Onboarding Funnel](#-analysis-2-customer-onboarding-funnel)
8. [Analysis 3: Churn](#-analysis-3-customer-churn--engagement)
9. [SQL Implementation](#-sql-implementation)
10. [Business Recommendations](#-business-recommendations)
11. [Data Quality & Validation](#-data-quality--validation)
12. [Business Intelligence Assets](#-business-intelligence--dashboard-assets)
13. [Project Structure](#-project-structure)
14. [Reproduction Guide](#-reproduce-the-analysis)
15. [Limitations & Future Improvements](#-limitations--future-improvements)
16. [Project Takeaways](#-project-takeaways)

---

## 🎯 Business Problem

### Business Context

For subscription-based software businesses, customer acquisition alone does not guarantee sustainable growth.

Users must successfully complete onboarding, experience product value, and continue using the service for subscription revenue to remain dependable.

Analytics teams therefore need accurate measurements of:

- Customer onboarding progression
- Product activation behavior
- Subscription-tier performance
- Monthly recurring revenue
- Churn-related outcomes
- Product engagement
- Revenue concentration
- Data quality and metric reliability

Poorly defined metrics or inaccurate event data can lead teams to invest in the wrong product improvements.

### Business Objectives

| Objective | Analytical Question | Expected Decision Support |
|---|---|---|
| Improve Activation | Where do users leave the onboarding funnel? | Prioritize usability investigation |
| Understand Revenue | Which subscription tiers generate the most MRR? | Assess revenue concentration |
| Examine Churn | What is the supplied churn rate among paying users? | Establish descriptive retention-related indicators |
| Evaluate Engagement | How does product activity relate to churn labels? | Determine whether deeper analysis is possible |
| Validate Reporting | Are source records and KPI calculations consistent? | Improve reporting confidence |

### Analytical Goal

Develop a reproducible analytical workflow that converts raw SaaS records into traceable business metrics and provides recommendations grounded in the available evidence.

---

## 🗄️ Dataset Overview

The project uses three related simulated datasets containing **32,175 source rows**.

### Source Tables

| Dataset | Rows | Purpose |
|---|---:|---|
| `users_raw.csv` | 1,500 | Customer attributes, signup dates, plans, and acquisition channels |
| `subscriptions_raw.csv` | 1,500 | Subscription snapshots, MRR, seats, and churn labels |
| `events_raw.csv` | 29,175 | Onboarding actions and product activity |
| **Total** | **32,175** | **Three analytical source tables** |

### 1. Users Dataset

Contains account-level details used to understand customer composition and establish valid onboarding observation windows.

**Important fields:**

- `user_id` — Unique user identifier
- `signup_date` — Account creation date
- `country` — Supplied country code
- `acquisition_channel` — Acquisition category
- `plan_tier` — Free, Starter, Pro, or Enterprise

**Analytical purpose:** Customer segmentation, signup timing, and user-level relationships.

### 2. Subscriptions Dataset

Provides subscription and outcome fields used to calculate revenue snapshots and churn-label rates.

**Important fields:**

- `user_id` — User relationship key
- `plan_tier` — Subscription category
- `mrr` — Supplied monthly revenue snapshot
- `seats` — Subscription seat count
- `completed_step2` — Recorded Step 2 completion flag
- `churned_within_90d` — Supplied churn outcome label
- `first_payment_date` — Recorded payment date

**Analytical purpose:** Subscription reporting, plan performance, and churn-related comparisons.

### 3. Events Dataset

Contains recorded customer interactions with the simulated SaaS application.

**Important fields:**

- `user_id` — User associated with the event
- `event_date` — Day-level event date
- `event_group` — Onboarding or Product
- `event_name` — Recorded user activity

**Analytical purpose:** Ordered funnel construction, workflow engagement, and event-quality investigation.

### Data Relationships

The analysis uses `user_id` to relate account information, subscription information, and product events.

**Users (1) → (1) Subscriptions**

**Users (1) → (Many) Events**

These relationships are checked through data-contract and referential-integrity validation.

### Source Documentation

[📘 Data Dictionary](Docs/Data_Dictionary.md) | [📂 Raw Data](Data/raw) | [📂 Clean Data](Data/clean)

---

## 🛠️ Technical Stack

| Category | Technology | Application |
|---|---|---|
| Programming | Python 3.12 | Data processing, validation, reconciliation |
| Query Language | SQL | KPI calculations and analytical queries |
| Database | SQLite | Local relational analysis |
| Data Analysis | pandas | Independent calculations and comparisons |
| Data Preparation | Python | Type normalization and schema validation |
| Statistical Reasoning | Descriptive metrics | Rates, proportions, and observational analysis |
| Reporting | HTML and CSV | Analytical results and offline reports |
| Spreadsheet Reporting | Excel | Validated summary formulas |
| Visualization Assets | Tableau | Legacy workbook and source-aligned Hyper extract |
| Quality Assurance | Python unittest | Automated testing |
| Version Control | Git and GitHub | Repository history and project management |
| Reproducibility | SHA-256 manifests | Input, code, and output traceability |

### SQL Skills Demonstrated

- Table relationships and joins
- Aggregate functions
- Conditional aggregation
- Common Table Expressions
- Subqueries
- Chronological event selection
- `CASE` expressions
- `GROUP BY`
- `NULLIF` for safe division
- Date filtering
- Multi-stage funnel calculations

### Python Skills Demonstrated

- Data import and transformation
- Data-type validation
- Reusable analytical processing
- SQL result reconciliation
- Automated data-quality checks
- Test execution
- Report generation
- Reproducible output management

---

## 🔄 End-to-End Analytical Workflow

The project follows a structured analytics process that connects source data to business findings.

### Phase 1 — Business Requirements

Define the business questions, reporting objectives, user populations, and metric definitions.

**Deliverable:** Documented analytical scope and KPI rules.

### Phase 2 — Data Inspection

Review raw files to identify:

- Dataset grain
- Available fields
- Primary keys and relationships
- Required columns
- Date types
- Duplicate considerations
- Missing context

**Deliverable:** Source data dictionary and validation contracts.

### Phase 3 — Cleaning & Transformation

Normalize supported field types and prepare cleaned analytical datasets.

Controls include:

- Required-value validation
- Numeric range checks
- Date parsing
- Boolean normalization
- Key uniqueness checks
- Relationship validation
- Source anomaly reporting

Original raw datasets are preserved.

**Deliverable:** Regenerated clean CSV files.

### Phase 4 — SQL Analytics

Load the cleaned records into SQLite and execute named analytical queries.

Main analyses:

1. Subscription summary
2. Revenue by plan
3. Ordered onboarding funnel
4. Product activity and churn-label association

**Deliverable:** SQL-generated result tables.

### Phase 5 — Independent Python Validation

Compare headline SQL calculations with independently computed Python results.

Checks cover revenue totals, subscriber counts, churn rates, funnel counts, and selected activity calculations.

**Deliverable:** Validation records and reproducibility evidence.

### Phase 6 — Business Interpretation

Identify meaningful patterns and distinguish observed results from explanations requiring further investigation.

**Deliverable:** Findings, limitations, and recommendations.

### Phase 7 — Reporting

Generate saved results and offline analytical reports.

**Deliverable:** CSV outputs, HTML report, and evidence manifests.

### Pipeline Summary

**Raw CSVs → Data Contracts → Clean CSVs → SQLite → SQL KPIs → Python Reconciliation → Saved Results → Business Interpretation**

---

## 📐 KPI Definitions & Business Rules

Well-defined metrics are essential to producing consistent analytical results.

| KPI | Definition | Important Business Rule |
|---|---|---|
| Total Users | Count of supplied user records | One user per declared user key |
| Paying Subscribers | Count of subscription rows with MRR greater than zero | Free subscriptions excluded |
| Snapshot MRR | Sum of supplied MRR values | Revenue snapshot, not recognized revenue |
| Snapshot ARR | Snapshot MRR × 12 | Annualization, not a verified forecast |
| Paying Churn Label Rate | Paying users with churn label ÷ all paying users | Supplied label, not reconstructed lifecycle churn |
| Onboarding Stage Reach | Users successfully completing the ordered path to a stage | Preceding stages must be satisfied |
| Onboarding Drop-Off | 1 − next-stage users ÷ current-stage users | Uses eligible chronological stage counts |
| Revenue Share | Plan MRR ÷ total snapshot MRR | Uses all supplied subscription rows |
| Workflow Activity Group | Workflow Run count within the 90-day observation window | Descriptive association only |

### Important Metric Distinctions

**MRR vs. Recognized Revenue**

The supplied MRR field represents a subscription snapshot. It does not verify payment collection, accounting recognition, or actual historical recurring revenue.

**Churn Label vs. Observed Customer Churn**

The dataset contains a supplied churn outcome indicator but lacks the complete subscription lifecycle needed to independently reconstruct cohort churn.

**Event Reach vs. Ordered Funnel Completion**

A customer recording an event does not automatically demonstrate successful completion of earlier funnel steps. The ordered funnel respects date eligibility and required transitions.

Full definitions: [KPI Lineage](Docs/KPI_Lineage.md)

---

## 💰 Analysis 1: SaaS Subscription Revenue

### Business Question

Which subscription tiers contribute the most monthly recurring revenue, and how concentrated is that revenue?

### Revenue Performance

| Subscription Tier | Users | Snapshot MRR | MRR Share |
|---|---:|---:|---:|
| 🏢 Enterprise | 92 | 159,201 | 83.80% |
| 💼 Pro | 264 | 20,856 | 10.98% |
| 🌱 Starter | 342 | 9,918 | 5.22% |
| 🆓 Free | 802 | 0 | 0.00% |
| **Total** | **1,500** | **189,975** | **100%** |

### Finding 1 — Enterprise Drives Most Revenue

Enterprise subscribers represent a relatively small portion of the total customer population but contribute approximately **83.80% of recorded monthly revenue**.

**Interpretation:** Subscription revenue is highly concentrated in the Enterprise plan.

This may make enterprise retention and revenue continuity important areas for investigation.

However, subscription values alone cannot establish true account-level revenue risk without additional historical and contractual information.

### Finding 2 — Free Accounts Form the Largest User Segment

The Free tier contains 802 users, approximately 53.47% of the recorded population.

This represents a substantial nonpaying segment.

**Potential business investigation:** Determine whether Free-tier customers experience activation barriers that prevent upgrades.

The present dataset does not establish free-to-paid conversion trajectories or identify the cause of nonpayment.

### Finding 3 — Starter and Pro Contribute Smaller Revenue Shares

Starter and Pro together contribute approximately 16.20% of total recorded MRR.

Additional information about customer needs, feature usage, pricing, upgrades, and downgrades would help evaluate opportunities within these tiers.

### Business Recommendation

Prioritize an analysis of Enterprise revenue concentration and collect reliable account-level renewal history before estimating retention risk.

Separately, evaluate whether Free and Starter customers face measurable activation barriers.

**SQL Evidence:** [Revenue by Tier](Results/revenue_by_tier.csv)

---

## 🚀 Analysis 2: Customer Onboarding Funnel

### Business Question

Where do users fail to progress through the onboarding experience?

### Onboarding Stages

The supplied events describe a five-step sequence:

**Account → Workspace → Integration → First Workflow → Invite Team**

The SQL analysis evaluates whether users reach each step in valid chronological order.

### Verified Funnel Results

| Stage | Users | Retained From Previous Stage |
|---|---:|---:|
| Step 1: Account | 1,088 | Baseline |
| Step 2: Workspace | 407 | 37.41% |
| Step 3: Integration | 123 | 30.22% |
| Step 4: First Workflow | 34 | 27.64% |
| Step 5: Invite Team | 9 | 26.47% |

### Transition Analysis

| Transition | Users Lost | Drop-Off |
|---|---:|---:|
| Account → Workspace | 681 | 62.59% |
| Workspace → Integration | 284 | 69.78% |
| Integration → First Workflow | 89 | 72.36% |
| First Workflow → Invite Team | 25 | 73.53% |

### Finding 1 — Significant Loss During Initial Setup

Among 1,088 users reaching Account, only 407 reach Workspace in the valid ordered sequence.

**62.59% fail to progress to the next stage.**

This suggests that the workspace setup process warrants investigation.

Possible hypotheses include confusing setup instructions, technical friction, or limited perceived value, but these explanations have not been established by the supplied data.

### Finding 2 — Drop-Off Continues Through Advanced Activation

Only 123 users reach Integration after completing the preceding eligible stages.

Just 34 progress through First Workflow, and 9 reach Invite Team.

This suggests limited completion of the entire recorded onboarding path.

However, later steps may differ in business importance, and some users may not need every step to achieve product value.

### Finding 3 — Full-Funnel Completion Is Limited

Nine of the 1,088 Step 1 users reach the final stage of the ordered funnel, approximately **0.83%**.

This is a descriptive funnel-completion statistic.

It should not automatically be interpreted as the percentage of customers achieving product value or becoming paying subscribers.

### Recommended Investigation

**Priority 1 — Account-to-Workspace Experience**

Review product instrumentation, onboarding instructions, and qualitative feedback to investigate early setup barriers.

**Priority 2 — Workspace-to-Integration Transition**

Determine whether integration requirements are understandable, accessible, and relevant for different customer types.

**Priority 3 — First Workflow Activation**

Investigate whether users can successfully complete a meaningful initial workflow.

**Priority 4 — Validate Activation Definitions**

Confirm whether Invite Team belongs in a universal required funnel or represents an optional collaborative behavior.

### Measurement Plan

If a product team implements an onboarding change, evaluate:

- Eligible users reaching each stage
- Conditional transition rates
- Time to activation
- Workflow completion
- Subsequent product activity
- Relevant retention guardrails

Use a properly controlled experiment before attributing observed changes to the intervention.

**SQL Evidence:** [Onboarding Funnel Results](Results/onboarding_funnel.csv)

---

## 📉 Analysis 3: Customer Churn & Engagement

### Business Question

What does the supplied churn indicator reveal about paying customers, and how does observed workflow activity relate to churn?

### Recorded Churn Metrics

| Metric | Result |
|---|---:|
| Paying Users | 698 |
| Paying-User Churn Label Rate | 21.06% |
| Churn Indicator | `churned_within_90d` |
| Population | Subscriptions with MRR greater than zero |

### Finding 1 — The Supplied Churn Label Rate Is 21.06%

Approximately 21.06% of paying users have a positive churn label in the supplied snapshot.

This provides a descriptive outcome indicator.

It is not a fully reconstructed subscription churn rate because cancellation events, complete cohort windows, and billing lifecycle records are unavailable.

### Finding 2 — Engagement Comparison Is Limited

The analysis defines a power-user threshold of at least 20 Workflow Run events within the first 90 days after signup.

The saved results contain one observed group:

| Engagement Group | Paying Users | Churn Label Rate |
|---|---:|---:|
| Under 20 Workflow Runs | 698 | 21.06% |

No paying users appear in the 20-or-more-run group under the defined activity window.

**Analytical implication:** The data do not support a comparison between high-activity and low-activity paying users using this threshold.

The analysis should not claim that power users churn less when a comparable power-user group is absent.

### Finding 3 — Data Availability Limits Causal Interpretation

Product activity and churn outcomes can be affected by many factors, including account age, customer needs, subscription terms, and incomplete observation periods.

The dataset does not contain sufficient information to isolate those mechanisms.

### Recommended Next Steps

- Establish complete customer lifecycle records.
- Verify churn label construction.
- Introduce consistent observation periods.
- Review whether the engagement threshold fits observed activity distributions.
- Investigate retention by appropriate customer cohorts.
- Test activation interventions before claiming churn reduction.

**SQL Evidence:** [Power User Association](Results/power_user_association.csv)

---

## 💻 SQL Implementation

The project uses executable SQLite queries rather than static examples detached from the underlying analysis.

### Example 1 — Subscription Revenue Summary

The following query is drawn from the project's executable SQL analysis.

```sql
SELECT
    COUNT(*) AS users,
    SUM(mrr > 0) AS paying_users,
    SUM(mrr) AS snapshot_mrr,
    SUM(mrr) * 12 AS snapshot_arr,

    1.0 * SUM(
        CASE
            WHEN mrr > 0
            THEN churned_within_90d
            ELSE 0
        END
    ) / NULLIF(SUM(mrr > 0), 0)
      AS paying_churn_label_rate

FROM subscriptions_clean;
```

**SQL Concepts Demonstrated**

- Aggregate functions
- Conditional calculation
- Business-rule filtering
- Numerical type handling
- Safe denominator calculation

**Business Application**

Creates a consistent summary of subscription population, revenue, and churn-label reporting.

### Example 2 — Revenue by Subscription Tier

```sql
SELECT
    plan_tier,
    COUNT(*) AS users,
    SUM(mrr) AS snapshot_mrr,

    1.0 * SUM(mrr)
        / NULLIF(
            (SELECT SUM(mrr)
             FROM subscriptions_clean),
            0
        ) AS mrr_share

FROM subscriptions_clean

GROUP BY plan_tier

ORDER BY snapshot_mrr DESC;
```

**SQL Concepts Demonstrated**

- Grouped aggregation
- Scalar subqueries
- Calculated proportions
- Result ordering
- Revenue segmentation

**Business Application**

Identifies the contribution of each subscription tier to overall recorded revenue.

### Example 3 — Chronological Onboarding Logic

The ordered funnel uses a sequence of Common Table Expressions.

A representative transition from Account to Workspace uses the following logic:

```sql
WITH s0 AS (
    SELECT
        user_id,
        signup_date AS reached
    FROM users_clean
),

s1 AS (
    SELECT
        p.user_id,

        (
            SELECT MIN(e.event_date)
            FROM events_clean e
            WHERE e.user_id = p.user_id
              AND e.event_name = 'Step 1: Account'
              AND e.event_date >= p.reached
        ) AS reached

    FROM s0 p
    WHERE p.reached IS NOT NULL
),

s2 AS (
    SELECT
        p.user_id,

        (
            SELECT MIN(e.event_date)
            FROM events_clean e
            WHERE e.user_id = p.user_id
              AND e.event_name = 'Step 2: Workspace'
              AND e.event_date >= p.reached
        ) AS reached

    FROM s1 p
    WHERE p.reached IS NOT NULL
)

SELECT
    COUNT(reached) AS workspace_users
FROM s2;
```

**SQL Concepts Demonstrated**

- Common Table Expressions
- Correlated subqueries
- Date comparisons
- Chronological eligibility
- User-level progression
- Conditional stage completion

**Business Application**

Avoids incorrectly counting later onboarding actions without confirming the preceding eligible stage.

The complete implementation extends the sequence through all five onboarding stages.

**Explore the Full SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 💡 Business Recommendations

The analysis produces actionable investigation priorities without treating simulated descriptive findings as realized business results.

| Priority | Recommendation | Supporting Evidence | Proposed Validation |
|---|---|---|---|
| High | Investigate Workspace setup friction | 62.59% first-transition drop-off | Usability study and controlled experiment |
| High | Assess Enterprise revenue exposure | 83.80% MRR concentration | Contract and renewal cohort review |
| Medium | Examine Integration activation | Low ordered progression to Integration | Product event and qualitative analysis |
| Medium | Redefine useful engagement thresholds | No paying users reach 20+ Workflow Runs | Engagement distribution assessment |
| Medium | Improve churn measurement | Supplied 21.06% churn-label rate | Reconstruct churn from lifecycle events |

### Recommended 30/60/90-Day Analytical Roadmap

These are proposed next steps, not completed business interventions.

**Days 1–30 — Diagnose**

- Review onboarding instrumentation.
- Validate whether required stages match customer workflows.
- Conduct user interviews around initial setup.
- Investigate historical subscription and renewal data availability.

**Days 31–60 — Design & Test**

- Establish baseline activation KPIs.
- Specify the onboarding improvement hypothesis.
- Define an experiment assignment unit and guardrails.
- Prepare the analysis and measurement plan.

**Days 61–90 — Evaluate**

- Analyze experiment results if a valid test is conducted.
- Review primary and guardrail metrics.
- Estimate uncertainty.
- Present evidence-based recommendations for the next iteration.

### Expected Decision Value

A well-instrumented onboarding analysis can help product teams prioritize investigation, reduce reporting ambiguity, and design more informative experiments.

No specific revenue gain or churn improvement is projected as achieved.

---

## ✅ Data Quality & Validation

### Why Validation Matters

Business decisions depend on the integrity of both source records and analytical transformations.

This project includes documented validation across source schemas, relationships, query execution, and metric reconciliation.

### Verified Quality Summary

| Quality Metric | Recorded Evidence |
|---|---:|
| User Records | 1,500 |
| Subscription Records | 1,500 |
| Event Records | 29,175 |
| Missing Required Cells | 0 |
| Exact-Repeated Event Rows | 481 |
| Free Accounts with Positive Churn Label | 218 |
| Events Before Signup | 0 |
| Step 2 Flag/Event Disagreements | 0 |
| Runtime Validation Checks | 19 passed |

### Key Quality Decisions

**1. Preserve Repeated Event Rows**

The source contains 481 exact-repeat event rows, but no stable event identifiers.

Repeated records cannot safely be classified as ingestion duplicates rather than legitimate activity.

The workflow preserves and reports them instead of silently removing them.

**2. Exclude Free Accounts from Paying Churn**

A total of 218 Free-tier accounts carry positive churn labels.

They are not included in the paying-user churn denominator or numerator because the reported KPI is specifically defined for paying subscribers.

**3. Enforce Relationship Integrity**

User and subscription keys are validated to prevent invalid joins and inconsistent subscription reporting.

**4. Independently Reconcile Metrics**

Selected SQL calculations are recomputed in Python to identify disagreements in metric definitions or implementation.

**5. Preserve Source Traceability**

Evidence manifests associate analytical outputs with original sources, code, and execution metadata.

### Validation Outputs

| Evidence File | Purpose |
|---|---|
| [validation.json](Results/validation.json) | Records passing technical and reconciliation checks |
| [quality.json](Results/quality.json) | Data quality findings and source anomalies |
| [manifest.json](Results/manifest.json) | Hashes and execution provenance |
| [query_plans.json](Results/query_plans.json) | SQLite query-plan information |
| [additional_metrics.json](Results/additional_metrics.json) | Supplementary computed metrics |

**Validation Status:** The repository records 19 passing runtime checks for this case study.

These checks demonstrate defined execution and reconciliation behavior, not independent validation of every possible business interpretation.

---

## 📊 Business Intelligence & Dashboard Assets

The project includes Excel, Tableau, and offline reporting assets to support multiple ways of inspecting the analytical work.

### Available Files

| Asset | Location | Purpose |
|---|---|---|
| Excel Model | [Excel Workbook](Excel/01_SaaS_Product_Analytics_StreamFlow_Model.xlsx) | Source-aligned analytical summaries |
| Tableau Workbook | [Dashboard Folder](Dashboard/) | Preserved legacy dashboard |
| Validated Tableau Extract | [Validated_Analysis.hyper](Dashboard/Validated_Analysis.hyper) | Canonical source/result tables for dashboard rebuilding |
| Dashboard Image | [Images Folder](Images/) | Screenshot of the legacy dashboard |
| Offline Analytical Report | [REPORT.html](REPORT.html) | Canonical SQL/Python findings |

### Native Workbook Verification Status

A native-file audit identified a source mismatch between the original Tableau workbook and the canonical analysis datasets.

The original Tableau workbook contains a different event population and schema from the three canonical project CSVs.

For that reason:

- The original dashboard is preserved as a legacy asset.
- Its screenshot is not presented as verification of the canonical KPI values.
- A source-aligned Tableau Hyper extract is provided.
- The Excel summary has documented formula and source-alignment checks.
- Tableau Desktop rebuild, refresh, and visual acceptance remain outstanding.

### Dashboard Validation Guidance

Before presenting a refreshed native Tableau dashboard as the canonical analysis:

1. Connect to the validated source/result tables.
2. Rebuild measures using documented KPI definitions.
3. Compare totals against saved result CSVs.
4. Test filters, tooltips, aggregations, and calculated fields.
5. Record visual and numerical acceptance evidence.

**Documentation:** [Dashboard Reconciliation](Docs/Dashboard_Reconciliation.md) | [Field Mapping](Docs/Dashboard_Field_Mapping.md) | [Connection Guide](Docs/Connect_To_Dashboard.md)

**Portfolio Evidence:** [Native Workbook Verification](../verification/native/README.md)

---

## 📂 Project Structure

```text
01_SaaS_Product_Analytics_StreamFlow/
│
├── Data/
│   ├── raw/
│   └── clean/
│
├── SQL/
│   └── analysis.sql
│
├── Python/
│   └── analysis.py
│
├── Excel/
│   └── 01_SaaS_Product_Analytics_StreamFlow_Model.xlsx
│
├── Dashboard/
│   ├── README.md
│   ├── Validated_Analysis.hyper
│   └── Product Analytics Dashboard...twbx
│
├── Images/
│   └── Product Analytics Dashboard...png
│
├── Results/
│   ├── summary.csv
│   ├── revenue_by_tier.csv
│   ├── onboarding_funnel.csv
│   ├── power_user_association.csv
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

The project is part of a larger portfolio with shared execution, transformation, statistical, testing, and reporting modules.

---

## ▶️ Reproduce the Analysis

### Prerequisites

- Python 3.12
- Git
- Python package installation capability

The core project does not require a cloud subscription, external database server, or paid BI application.

### Step 1 — Clone the Repository

```bash
git clone https://github.com/JamieChristian22/data-analyst-portfolio.git

cd data-analyst-portfolio
```

### Step 2 — Create a Virtual Environment

```bash
python -m venv .venv
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4 — Run the SaaS Project

```bash
python -m portfolio.run --project 01_SaaS_Product_Analytics_StreamFlow
```

### Step 5 — Run the Automated Tests

```bash
python -m unittest discover -s tests -v
```

The test command runs the repository's shared test suite, not only SaaS-specific checks.

### Step 6 — Inspect Results

Review the generated files in:

`01_SaaS_Product_Analytics_StreamFlow/Results/`

Open the local `REPORT.html` for the canonical analytical report.

GitHub displays HTML file source rather than always rendering it as an interactive local page, so clone or download the repository for offline viewing.

### Validation Guidance

Successful execution should produce current validation records and a corresponding manifest.

After a failed run, treat previous reports or partially regenerated outputs as potentially stale until execution succeeds again.

For troubleshooting, see the [Portfolio Runbook](../docs/RUNBOOK.md).

---

## ⚠️ Limitations & Future Improvements

### Current Analytical Limitations

**1. Simulated Source Data**

All datasets were supplied as portfolio inputs. Results do not describe an actual deployed SaaS business.

**2. Snapshot Revenue**

MRR and ARR reflect supplied subscription values rather than verified realized revenue, payment collections, or historical financial performance.

**3. Incomplete Customer Lifecycle**

The available fields do not support independent reconstruction of churn from full cancellation and renewal histories.

**4. Limited Event Granularity**

Events are recorded at day-level precision, and stable event identifiers are unavailable.

**5. Engagement Comparison Constraints**

All paying users fall below the current 20-workflow-run threshold, preventing a meaningful high-versus-low engagement comparison.

**6. Observational Analysis**

Customer activity, onboarding progression, and churn labels cannot by themselves prove causal relationships.

**7. Dashboard Source Mismatch**

The preserved legacy Tableau dashboard uses different source data from the canonical CSV analysis and requires rebuilding before it can represent the verified canonical metrics.

### Future Enhancements

Potential next iterations include:

- Cohort-based retention analysis using complete customer histories
- Time-to-activation measurements using more precise timestamps
- Free-to-paid conversion tracking
- Subscription upgrade and downgrade analytics
- Revenue concentration by customer account
- Experiment-ready onboarding measurement
- Activity segmentation using data-supported thresholds
- A fully refreshed, source-aligned Tableau dashboard with visual acceptance evidence

These are planned analytical opportunities, not capabilities claimed as already implemented.

---

## 🧠 Project Takeaways

### Technical Skills Demonstrated

This case study provides evidence of practical experience with:

- SQL data extraction and aggregation
- Relational data analysis
- Python-based validation
- Data cleaning and quality assessment
- Chronological funnel construction
- Subscription-revenue calculations
- KPI documentation and lineage
- Reproducible analytical workflows
- Automated testing
- Reporting and interpretation

### Business Skills Demonstrated

The analysis also demonstrates:

- Translating business questions into analytical requirements
- Prioritizing findings by decision relevance
- Identifying risks in reported metrics
- Distinguishing descriptive patterns from causal claims
- Explaining technical limitations to business stakeholders
- Developing measurable follow-up recommendations

### Final Conclusion

The StreamFlow analysis identifies significant early onboarding drop-off, substantial Enterprise revenue concentration, and a supplied paying-user churn-label rate of 21.06%.

The results suggest that onboarding instrumentation, customer activation, Enterprise revenue exposure, and churn measurement deserve further investigation.

Just as importantly, the project demonstrates how to recognize when source limitations make an apparently attractive conclusion unsupported.

**The objective is not simply to calculate KPIs, but to produce metrics that can be explained, traced, validated, and responsibly used in business decisions.**

---

## 📚 Supporting Documentation

| Documentation | Description |
|---|---|
| [Data Dictionary](Docs/Data_Dictionary.md) | Source fields, data types, keys, and validation rules |
| [KPI Lineage](Docs/KPI_Lineage.md) | Metric formulas, denominators, and source relationships |
| [Dashboard Reconciliation](Docs/Dashboard_Reconciliation.md) | Native asset alignment and outstanding acceptance work |
| [Dashboard Field Mapping](Docs/Dashboard_Field_Mapping.md) | Fields used for reporting integration |
| [Dashboard Connection Guide](Docs/Connect_To_Dashboard.md) | Connecting BI assets to source data |
| [SQL Analysis](SQL/analysis.sql) | Executable analytical queries |
| [Python Analysis](Python/analysis.py) | Project Python entry point |
| [Quality Results](Results/quality.json) | Source diagnostics |
| [Validation Results](Results/validation.json) | Project check evidence |
| [Offline Report](REPORT.html) | Generated analytical report |

---

## 👨‍💻 About the Analyst

**Jamie Christian**  
Data Analytics | Business Intelligence | SQL | Python | Business Analysis

I focus on using data to solve business problems, evaluate performance, improve reporting reliability, and communicate meaningful findings.

My analytical interests include product analytics, customer behavior, business intelligence, operational performance, and data-driven decision support.

📧 [Email](mailto:Jamiechristian331@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/jamiechristian2/)  
💻 [GitHub Profile](https://github.com/JamieChristian22)

### 🔗 Explore More Projects

[⬅️ Back to Data Analyst Portfolio](../README.md)

---

**📈 StreamFlow SaaS Product Analytics | Built by Jamie Christian**

*SQL-driven insights. Python-verified metrics. Transparent analytical decisions.*
