
# 🔍 User Journey Analytics | Customer Behavior, Conversion Funnels & Event Tracking

### SQL • Python • Customer Analytics • Funnel Analysis • Behavioral Segmentation • Data Quality

**An end-to-end customer journey analytics case study examining user behavior, purchasing activity, chronological funnel progression, returning-user conversion, and event-tracking reliability through reproducible SQL and Python analysis.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Tableau](https://img.shields.io/badge/Tableau-Native_Asset-E97627)
![Analytics](https://img.shields.io/badge/Customer-Journey_Analytics-blueviolet)
![Validation](https://img.shields.io/badge/Validation-15%2F15-success)
![Dataset](https://img.shields.io/badge/Dataset-Simulated-orange)

**Analyst:** Jamie Christian  
**Project:** 05 — User Journey Analytics  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Jamie Christian](https://www.linkedin.com/in/jamiechristian2/)

---

## 📌 Executive Summary

This project examines the behavior of users progressing through a simulated ecommerce customer journey, from initial landing-page activity to purchasing.

Using **6,000 user records and 17,354 recorded journey events**, the analysis applies SQL, Python, chronological event validation, behavioral segmentation, and reproducible reporting to understand user activity and identify limitations in funnel measurement.

A central focus of the project is distinguishing **observed event participation** from **valid chronological funnel completion**.

The analysis answers five major business questions:

1. How many users have recorded purchase events?
2. How many users complete a valid, date-ordered purchasing journey?
3. How does purchasing differ between returning and non-returning users?
4. How much time elapses between first observation and purchase?
5. What data-quality issues prevent reliable interpretation of customer abandonment?

### Key Results

| Business Metric | Verified Result |
|---|---:|
| 👥 Total Users | 6,000 |
| 📋 Journey Event Records | 17,354 |
| 💳 Users with Purchase Events | 627 |
| 📈 Observed Purchase Rate | 10.45% |
| 🔁 Returning-User Purchase Rate | 16.20% |
| 🆕 Non-Returning-User Purchase Rate | 8.26% |
| ⏱️ Median Days to Purchase | 7 |
| 📅 90th Percentile Days to Purchase | 12 |
| ⚠️ Users with Adjacent-Stage Date Inversions | 3,296 |
| 🔎 Complete Six-Stage Ordered Paths | 0 |
| ✅ Runtime Validation Checks | 15 passed |

**Data disclosure:** This project uses supplied simulated portfolio datasets. The findings do not represent actual customer behavior, real company transactions, or verified production outcomes.

### Primary Findings

**1. The dataset records 627 purchasers.**

Among 6,000 users, 627 have an observed Purchase event, representing a **10.45% observed purchase rate**.

**2. Returning users exhibit higher observed purchase rates.**

Returning users have a 16.20% recorded purchase rate compared with 8.26% among non-returning users.

This is an observational difference, not proof that returning status causes higher purchasing.

**3. Chronological funnel completion differs dramatically from event reach.**

Although 627 users have recorded Purchase events, no user satisfies the complete six-stage date-ordered funnel.

This discrepancy reveals an important measurement problem rather than demonstrating that customers never purchased.

**4. Event-date inconsistencies affect interpretation.**

A total of 3,296 users have at least one adjacent-stage date inversion.

These inconsistencies prevent the strict funnel from being interpreted as a reliable measure of actual customer abandonment.

### Business Conclusion

The project's most important recommendation is to **investigate event instrumentation, stage completeness, and timestamp reliability before using ordered-funnel results to diagnose checkout performance**.

The case study demonstrates why technically correct calculations can still produce misleading business interpretations when source chronology is unreliable.

---

## 📚 Table of Contents

1. [Business Problem](#-business-problem)
2. [Dataset Overview](#-dataset-overview)
3. [Technical Stack](#-technical-stack)
4. [Analytical Workflow](#-end-to-end-analytical-workflow)
5. [KPI Definitions](#-kpi-definitions--business-rules)
6. [Analysis 1: Purchase Activity](#-analysis-1-overall-purchase-activity)
7. [Analysis 2: Stage Reach](#-analysis-2-customer-journey-stage-reach)
8. [Analysis 3: Ordered Funnel](#-analysis-3-chronological-customer-journey-funnel)
9. [Analysis 4: Returning Users](#-analysis-4-returning-vs-non-returning-user-conversion)
10. [Analysis 5: Time to Purchase](#-analysis-5-time-to-purchase)
11. [Analysis 6: Event Quality](#-analysis-6-event-tracking--chronological-data-quality)
12. [SQL Implementation](#-sql-implementation)
13. [Business Recommendations](#-business-recommendations)
14. [Data Quality & Validation](#-data-quality--validation)
15. [Tableau & Excel Assets](#-business-intelligence--dashboard-assets)
16. [Project Structure](#-project-structure)
17. [Reproduction Guide](#-reproduce-the-analysis)
18. [Limitations](#-limitations--future-improvements)
19. [Project Takeaways](#-project-takeaways)

---

## 🎯 Business Problem

### Business Context

Digital businesses need to understand how users navigate websites and applications before completing meaningful actions such as purchases, registrations, or subscriptions.

Customer journey analytics helps teams investigate:

- Product discovery
- Browsing behavior
- Engagement with product pages
- Shopping cart activity
- Checkout progression
- Purchase conversion
- Returning-user behavior
- Time required to convert

However, measuring a customer journey accurately requires more than counting individual events.

Events must be associated with the correct users, ordered appropriately, and interpreted in the context of reliable tracking.

Incomplete or inconsistent event chronology can make a funnel appear to lose customers who actually completed purchases.

### Business Scenario

A simulated ecommerce platform has collected user information and recorded events representing stages of a purchasing journey.

The analytics team wants to evaluate conversion and identify potential friction points.

Before interpreting those funnel results, however, it must determine whether recorded events support a valid chronological path.

### Primary Business Question

**How does observed customer purchasing behavior compare with a strictly ordered conversion funnel, and what do discrepancies reveal about the reliability of customer journey tracking?**

### Business Objectives

| Objective | Analytical Focus | Decision Support |
|---|---|---|
| Measure Purchasing | Users with Purchase events | Establish observed conversion |
| Understand Journey Reach | Participation in individual stages | Assess tracked customer activity |
| Analyze Funnel Progression | Chronologically valid transitions | Evaluate ordered-path eligibility |
| Compare User Groups | Returning vs. non-returning users | Identify behavioral associations |
| Analyze Conversion Timing | First-seen date to first purchase | Describe purchasing timelines |
| Evaluate Tracking Quality | Invalid event ordering | Identify instrumentation concerns |
| Validate Reporting | SQL/Python reconciliation | Improve analytical reliability |

### Project Goal

Build a reproducible behavioral analytics workflow that produces traceable customer journey metrics while clearly separating legitimate purchasing observations from potentially unreliable chronological funnel conclusions.

---

## 🗄️ Dataset Overview

The project uses two simulated source datasets containing **23,354 total records**.

### Source Tables

| Dataset | Records | Purpose |
|---|---:|---|
| `users_raw.csv` | 6,000 | User attributes, first-seen dates, devices, and returning status |
| `journey_events_raw.csv` | 17,354 | Recorded customer journey events and dates |
| **Total** | **23,354** | **Two related analytical datasets** |

### Dataset 1 — Users

Contains one record per user.

| Column | Data Type | Description |
|---|---|---|
| `user_id` | Integer | Unique dataset-local user identifier |
| `first_seen_date` | Date | First recorded observation date |
| `traffic_source` | Text | Supplied traffic-source category |
| `device` | Text | Recorded device category |
| `is_returning` | Binary | Supplied returning-user indicator |

**Analytical Uses**

- Population measurement
- Returning-user segmentation
- Behavioral comparisons
- Initial observation dates
- User-to-event relationships

### Dataset 2 — Journey Events

Contains recorded customer actions associated with the purchasing journey.

| Column | Data Type | Description |
|---|---|---|
| `user_id` | Integer | User associated with the event |
| `event_date` | Date | Recorded event date |
| `journey_stage` | Text | Named journey stage |
| `stage_order` | Integer | Nominal stage-order identifier |

**Analytical Uses**

- Stage reach analysis
- Chronological funnel construction
- Purchase identification
- Event ordering validation
- Time-to-purchase analysis

### Source Journey Stages

The source includes seven event labels:

1. Landing
2. Browse
3. Product View
4. Add to Cart
5. Checkout
6. Purchase
7. Signup

### Important Stage Definition

The canonical commerce funnel uses the first six stages:

**Landing → Browse → Product View → Add to Cart → Checkout → Purchase**

**Signup is reported separately.**

Its source ordinal does not establish that signup must universally occur after purchase.

Treating Signup as a mandatory final commerce stage would impose an unsupported business rule.

### Data Relationships

The datasets connect through `user_id`.

**Users (1) → (Many) Journey Events**

The workflow validates user relationships and checks the compatibility of stage names and nominal stage-order values.

### Data Grain

**Users:** One record per `user_id`.

**Journey Events:** One row per supplied user-stage event observation, without a stable event identifier.

**Dates:** Day-level records without precise event timestamps.

### Data Limitations

The dataset does not provide:

- Event timestamps with hour, minute, or second precision
- Stable event IDs
- Session identifiers
- Explicit user-journey session boundaries
- Experiment assignment information
- Full lifecycle tracking
- Verified acquisition dates
- Complete follow-up windows

These limitations directly affect chronological funnel interpretation.

### Supporting Documentation

[📘 Data Dictionary](Docs/Data_Dictionary.md) | [📂 Raw Data](Data/raw) | [📂 Clean Data](Data/clean)

---

## 🛠️ Technical Stack

| Category | Technology | Application |
|---|---|---|
| Programming | Python 3.12 | Data preparation, validation, and metrics |
| Query Language | SQL | Funnel analysis and behavioral queries |
| Database | SQLite | Relational analytical execution |
| Data Analysis | pandas | Independent calculations |
| Behavioral Analytics | Customer journey analysis | Event reach and progression |
| Temporal Analysis | SQLite date functions | Chronological validation |
| Segmentation | SQL aggregation | Returning-user conversion |
| Statistics | Descriptive quantiles | Time-to-purchase distributions |
| Business Intelligence | Tableau | Native workbook and verified Hyper source |
| Spreadsheet Reporting | Excel | Source-aligned summaries |
| Reporting | HTML and CSV | Analytical results |
| Automated Testing | Python unittest | Data and calculation checks |
| Reproducibility | SHA-256 manifests | Input/output traceability |
| Version Control | Git and GitHub | Repository management |

### SQL Competencies Demonstrated

- `INNER JOIN`
- `LEFT JOIN`
- Common Table Expressions
- Correlated subqueries
- `COUNT(DISTINCT)`
- `MIN()`
- Grouped aggregations
- Conditional filtering
- Date comparisons
- `julianday()`
- Ordered-stage calculations
- Funnel construction
- User-level analysis

### Python Competencies Demonstrated

- CSV processing
- Schema and type validation
- DataFrame analysis
- Independent SQL reconciliation
- Chronological data checks
- Statistical quantiles
- Automated report generation
- Reproducible pipelines
- Source and output integrity checks

### Business Analytics Competencies

- Customer journey measurement
- Funnel analytics
- Purchase conversion
- Behavioral segmentation
- Time-to-conversion analysis
- Event instrumentation diagnostics
- KPI documentation
- Data quality investigation
- Analytical decision-making

---

## 🔄 End-to-End Analytical Workflow

The project follows a structured analytical process connecting raw customer events to validated business insights.

### Phase 1 — Define Business Questions

Identify the decisions that customer journey analysis should support.

Establish the difference between observed participation in a stage and successful completion of a chronological path.

**Deliverable:** Analytical objectives and KPI definitions.

### Phase 2 — Inspect Source Data

Review:

- User identifiers
- First-seen dates
- Returning status
- Stage labels
- Event dates
- Nominal stage order
- Source relationships
- Available temporal precision

**Deliverable:** Data dictionary and validation contracts.

### Phase 3 — Validate & Transform

Apply documented normalization and integrity checks.

The workflow preserves recorded source events rather than modifying dates to force a preferred funnel result.

**Deliverable:** Reproducible cleaned datasets.

### Phase 4 — Execute SQL Analysis

Calculate:

- User counts
- Observed purchase rates
- Individual stage reach
- Chronologically ordered funnel counts
- Returning-user conversion
- Time to first valid recorded purchase

**Deliverable:** Named analytical result tables.

### Phase 5 — Validate Chronological Logic

Compare stage ordering and identify temporal inconsistencies.

Distinguish events that exist from events satisfying a valid ordered journey.

**Deliverable:** Chronological diagnostics and quality findings.

### Phase 6 — Reconcile Using Python

Independently verify selected SQL metrics and ordered-path calculations.

**Deliverable:** Validation evidence.

### Phase 7 — Interpret Business Findings

Evaluate customer behavior while acknowledging source-tracking limitations and the risk of incorrect abandonment conclusions.

**Deliverable:** Findings and business recommendations.

### Phase 8 — Generate Reports

Create saved results, quality reports, manifests, and offline analytical reporting.

**Deliverable:** Traceable analytical evidence.

### Pipeline Architecture

**Raw Users & Events → Schema Validation → Clean Data → SQLite → Stage Reach & Ordered Funnel → Python Reconciliation → Data Quality Review → Business Reporting**

---

## 📐 KPI Definitions & Business Rules

Accurate customer journey analysis depends on defining the population, event conditions, and chronological requirements.

| KPI | Calculation | Interpretation |
|---|---|---|
| Total Users | Count of user records | Overall observed population |
| Observed Purchasers | Distinct users with a Purchase event | Unordered purchase reach |
| Observed Purchase Rate | Purchasers ÷ Total Users | Descriptive purchase participation |
| Stage Reach | Distinct users recording each stage | Stage presence, regardless of earlier stages |
| Ordered Funnel | Users satisfying every required preceding stage in date order | Strict path eligibility |
| Returning-User Purchase Rate | Returning purchasers ÷ Returning users | Descriptive segment conversion |
| Non-Returning Purchase Rate | Non-returning purchasers ÷ Non-returning users | Descriptive comparison baseline |
| Days to Purchase | First valid Purchase date − First-seen date | Observed elapsed days |
| Median Days to Purchase | 50th percentile of valid observed elapsed days | Descriptive central tendency |
| P90 Days to Purchase | 90th percentile of valid observed elapsed days | Upper observed timing percentile |
| Adjacent-Stage Inversion | Later nominal stage has an earlier recorded date | Tracking or source chronology diagnostic |

### Essential Metric Distinctions

**Observed Purchase vs. Ordered Purchase**

An observed Purchase event establishes that the source contains a Purchase record for the user.

It does not automatically establish that the user satisfies every preceding stage of a strict funnel.

**Stage Reach vs. Funnel Progression**

Stage reach counts distinct users who have a particular event.

Ordered progression requires qualifying events to occur in a valid sequence.

**First Seen vs. Acquired**

The `first_seen_date` represents the first recorded observation, not necessarily the date the customer was originally acquired.

**Time to Purchase vs. Complete Conversion-Time Distribution**

Time-to-purchase statistics describe users with observed valid purchases. They do not account for nonpurchasers whose outcomes may be right-censored.

### KPI Documentation

[📘 KPI Lineage](Docs/KPI_Lineage.md)

---

## 💳 Analysis 1: Overall Purchase Activity

### Business Question

How many users have recorded purchasing activity in the supplied journey data?

### Verified Purchase Summary

| KPI | Result |
|---|---:|
| Total Users | 6,000 |
| Users with Purchase Events | 627 |
| Users Without Observed Purchase Events | 5,373 |
| Observed Purchase Rate | 10.45% |

### Purchase Rate Formula

`Observed Purchase Rate = Distinct Purchasers / Total Users`

`627 / 6,000 × 100 = 10.45%`

### Finding 1 — Recorded Purchases Exist

The dataset contains Purchase events for 627 distinct users.

This establishes a nonzero observed purchaser population.

### Finding 2 — Most Users Lack a Recorded Purchase Event

A total of 5,373 users do not have a Purchase event in the supplied records.

This is a descriptive observation.

It does not establish that all of those users permanently abandoned the platform.

Some users may have shorter available observation periods or activity not represented in the dataset.

### Finding 3 — Purchase Reach Must Be Preserved

Even if a strict chronological funnel produces zero complete paths, the 627 observed purchase records remain valid observations of source event presence.

Analytical logic should not erase these observations merely because the tracking sequence is inconsistent.

### Business Interpretation

The observed purchase rate establishes a useful descriptive baseline.

Before using it as a production conversion KPI, a business should verify event completeness, customer identity, observation windows, and purchase-event definitions.

**Evidence:** [Purchase Summary](Results/summary.csv)

---

## 🧭 Analysis 2: Customer Journey Stage Reach

### Business Question

How many unique users have recorded activity at each journey stage, regardless of whether preceding stages were completed?

### Verified Stage Reach

| Journey Stage | Unique Users | Share of Total Users |
|---|---:|---:|
| Landing | 6,000 | 100.00% |
| Browse | 4,346 | 72.43% |
| Product View | 2,923 | 48.72% |
| Add to Cart | 1,883 | 31.38% |
| Checkout | 1,174 | 19.57% |
| Purchase | 627 | 10.45% |
| Signup | 401 | 6.68% |

### Finding 1 — Landing Is Recorded for All Users

All 6,000 users have a Landing event.

This establishes complete Landing-stage reach within the supplied population.

It does not independently verify that every event was instrumented accurately.

### Finding 2 — Later Stages Have Smaller Observed Populations

Recorded stage reach decreases from Landing to Purchase.

However, these numbers represent independent stage presence rather than verified step-by-step transitions.

### Finding 3 — Purchase and Signup Are Different Behaviors

The source contains 627 users with Purchase events and 401 users with Signup events.

Signup is not required as the final step of the six-stage commerce journey.

A user may have recorded purchasing activity without a corresponding Signup event.

The underlying business rules do not establish that such activity is invalid.

### Why Stage Reach Matters

Stage reach is useful for determining which actions were recorded at all.

It provides a diagnostic comparison against strict funnel results.

If users appear at Purchase but not in a valid ordered path, the discrepancy may signal incomplete instrumentation, unexpected ordering, or an overly restrictive funnel definition.

**Evidence:** [Stage Reach Results](Results/stage_reach.csv)

---

## 🚦 Analysis 3: Chronological Customer Journey Funnel

### Business Question

How many users satisfy the complete purchasing journey in valid chronological order?

### Defined Funnel

**Landing → Browse → Product View → Add to Cart → Checkout → Purchase**

Each user must satisfy the preceding stage before becoming eligible for the next.

### Verified Ordered Funnel

| Stage | Eligible Users | Retention From Previous Stage |
|---|---:|---:|
| Landing | 6,000 | Baseline |
| Browse | 2,304 | 38.40% |
| Product View | 590 | 25.61% |
| Add to Cart | 102 | 17.29% |
| Checkout | 12 | 11.76% |
| Purchase | 0 | 0.00% |

### Ordered Transition Diagnostics

| Transition | Users Not Progressing | Conditional Loss |
|---|---:|---:|
| Landing → Browse | 3,696 | 61.60% |
| Browse → Product View | 1,714 | 74.39% |
| Product View → Add to Cart | 488 | 82.71% |
| Add to Cart → Checkout | 90 | 88.24% |
| Checkout → Purchase | 12 | 100.00% |

**Important:** These percentages describe loss of *eligible ordered paths*. They must not be interpreted as proven customer abandonment rates because the source chronology contains substantial inconsistencies.

### Finding 1 — Ordered Funnel Counts Differ Sharply From Stage Reach

Stage reach identifies 4,346 users with Browse events.

The ordered funnel identifies only 2,304 users who have an eligible Browse event following Landing.

This difference demonstrates the effect of adding chronological requirements.

### Finding 2 — Chronological Restrictions Continue Reducing Eligibility

Only 590 users satisfy the path through Product View.

Only 102 satisfy the path through Add to Cart.

Only 12 satisfy the path through Checkout.

These are counts of users meeting the specified event sequence, not independently established counts of customers who experienced each real business step.

### Finding 3 — No Complete Six-Stage Path Exists

The strict ordered funnel reports zero users reaching Purchase after satisfying every earlier required stage.

This contrasts with the 627 users who have recorded Purchase events.

### Critical Interpretation

**Zero valid complete ordered paths does not mean zero actual purchases.**

It means no user satisfies this particular six-stage chronological rule in the supplied data.

Possible explanations include:

- Incomplete event instrumentation
- Inconsistent event timestamps
- Missing intermediate stages
- Synthetic source-generation artifacts
- Different valid customer journeys
- Incorrect assumptions about required stages

The current dataset cannot establish which explanation accounts for every discrepancy.

### Finding 4 — The 100% Final Transition Loss Is a Tracking Diagnostic

The ordered funnel shows 12 eligible users at Checkout and zero at Purchase.

The resulting 100% conditional loss is mathematically correct for the defined strict path.

However, it is **not a valid claim that 100% of real customers abandon checkout**.

The overall source includes 627 Purchase events.

### Business Recommendation

Investigate tracking quality and journey definitions before using the strict funnel to identify product friction.

Only after verifying event coverage and chronology should funnel losses be used to prioritize checkout improvements.

**Evidence:** [Ordered Funnel Results](Results/ordered_funnel.csv)

---

## 🔁 Analysis 4: Returning vs. Non-Returning User Conversion

### Business Question

How does observed purchasing differ between users labeled as returning and users not labeled as returning?

### Verified Results

| User Group | Users | Purchasers | Observed Purchase Rate |
|---|---:|---:|---:|
| Non-Returning | 4,346 | 359 | 8.26% |
| Returning | 1,654 | 268 | 16.20% |
| **Total** | **6,000** | **627** | **10.45%** |

### Finding 1 — Returning Users Have Higher Observed Purchase Rates

Returning users have a 16.20% observed purchase rate.

Non-returning users have an 8.26% observed purchase rate.

The descriptive difference is approximately **7.94 percentage points**.

### Finding 2 — Returning-User Purchase Rate Is Approximately 1.96 Times Higher

The ratio of observed purchase rates is:

`16.20% / 8.26% ≈ 1.96`

Returning users are associated with approximately 1.96 times the observed purchase rate of non-returning users in the supplied data.

### Finding 3 — The Relationship Is Observational

The dataset does not establish that returning status causes higher conversion.

Potential contributing differences include:

- Prior experience with the product
- User intent
- Traffic acquisition source
- Device characteristics
- Selection effects
- Unequal observation windows

The supplied returning flag also lacks an independently verified lookback definition.

### Finding 4 — The Result Suggests a Useful Segmentation Question

Returning status may be relevant when exploring customer purchasing behavior.

However, the current project cannot establish why the groups differ or which interventions would improve conversion.

### Recommended Follow-Up

With richer tracking data, a business could examine:

- Purchase rates by first-visit cohort
- Returning frequency
- Acquisition channel
- Time since previous visit
- Number of prior sessions
- Device usage
- Customer purchase history

A reliable customer-lifecycle model would be required before extending the analysis to retention or lifetime value.

**Evidence:** [Returning-User Conversion](Results/returning_user_conversion.csv)

---

## ⏱️ Analysis 5: Time to Purchase

### Business Question

How much time elapses between a user's first recorded observation and their first valid observed Purchase event?

### Measurement Definition

`Days to Purchase = First Valid Purchase Date − First-Seen Date`

The calculation uses day-level dates.

Purchase events must occur on or after the user's `first_seen_date`.

### Verified Results

| Time Metric | Result |
|---|---:|
| Median Days to Purchase | 7 |
| 90th Percentile Days to Purchase | 12 |
| Date Precision | Days |
| Population | Users with valid observed Purchase dates |

### Finding 1 — Median Observed Purchase Time Is Seven Days

Among users with valid observed purchases, the median elapsed time from first observation to purchase is seven days.

This describes the middle of the observed purchaser distribution.

### Finding 2 — P90 Observed Purchase Time Is Twelve Days

The 90th percentile is twelve days.

Under the project's quantile method, approximately 90% of the analyzed observed purchaser elapsed times are at or below this value.

### Finding 3 — Time to Purchase Is Conditional on Purchasing

The calculation does not estimate how long all customers would take to purchase.

Users without observed purchases are excluded from the purchaser-specific elapsed-time distribution.

### Finding 4 — Observation Windows Affect Interpretation

Users first observed near the end of the dataset's available period may have less opportunity to register a later purchase.

This is a potential right-censoring problem.

Without a defined common follow-up horizon or survival-analysis approach, the reported quantiles should remain descriptive.

### Recommended Follow-Up

Future reporting could add:

- Fixed follow-up windows
- First-seen cohort analysis
- Kaplan-Meier time-to-event estimation
- Censoring indicators
- Device/source stratification
- Longer-term purchase observation

These methods require suitable event coverage and definitions.

**Evidence:** [Time-to-Purchase Results](Results/time_to_purchase.csv) | [Additional Metrics](Results/additional_metrics.json)

---

## ⚠️ Analysis 6: Event Tracking & Chronological Data Quality

### Business Question

Do recorded journey events support a consistent, reliable ordering of customer actions?

### Verified Quality Findings

| Data Quality Metric | Recorded Result |
|---|---:|
| User Records | 6,000 |
| Event Records | 17,354 |
| Users with Adjacent-Stage Date Inversions | 3,296 |
| Share of User Population with Inversions | 54.93% |
| Events Before First-Seen Date | 0 |
| Complete Ordered Six-Stage Paths | 0 |
| Users with Purchase Events | 627 |

### Finding 1 — More Than Half the Users Have Stage-Date Inversions

The source-quality report identifies **3,296 users** with at least one adjacent-stage date inversion.

An inversion occurs when a later nominal journey stage has an earlier recorded date than its preceding stage under the diagnostic's comparison rules.

This affects approximately 54.93% of the user population.

### Finding 2 — Valid Stage Labels Do Not Guarantee Valid Chronology

The repository verifies that the source contains known stage labels and consistent nominal stage-order values.

However, those labels cannot repair event dates that contradict the expected journey sequence.

A correctly labeled event can still be chronologically inconsistent.

### Finding 3 — Same-Day Events Have Limited Ordering Precision

The supplied event dates do not include times of day.

The ordered funnel permits events on the same date to satisfy successive stages.

This is a documented rule, but it does not prove which event actually occurred first within that day.

### Finding 4 — Strict Funnel Results Are Highly Sensitive to Source Chronology

The gap between 627 observed purchasers and zero complete ordered purchasers demonstrates that the chronological requirements cannot be treated as ordinary behavioral attrition without investigation.

This is one of the most important analytical findings in the project.

### Root-Cause Investigation Framework

**Step 1 — Validate Event Definitions**

Confirm what each recorded stage is intended to represent.

**Step 2 — Inspect Event Timestamp Generation**

Determine whether event dates originate from actual user activity, ingestion time, transformation logic, or synthetic generation.

**Step 3 — Check Missing Stage Events**

Investigate whether some users can legitimately skip stages or whether required events were never recorded.

**Step 4 — Examine Temporal Inversions**

Identify affected users and compare nominal stage order with observed dates.

**Step 5 — Define Valid Journey Variants**

Determine which stages are universally required and which are optional.

**Step 6 — Improve Instrumentation**

Capture stable event identifiers, timestamp precision, session context, and event-source metadata.

**Step 7 — Rebuild the Ordered Funnel**

Recalculate valid paths after the approved tracking definitions and data quality issues have been addressed.

### Recommended Decision

**Do not use the current strict ordered-funnel loss percentages as verified business abandonment metrics.**

Use them as a diagnostic for source chronology and event coverage until the instrumentation can be validated.

**Evidence:** [Data Quality Results](Results/quality.json) | [Ordered Funnel](Results/ordered_funnel.csv)

---

## 💻 SQL Implementation

The project uses five executable SQLite queries stored in `SQL/analysis.sql`.

### Query 1 — Observed Purchase Rate

```sql
SELECT
    COUNT(*) AS users,

    (
        SELECT COUNT(DISTINCT user_id)
        FROM journey_events_clean
        WHERE journey_stage = 'Purchase'
    ) AS purchasers,

    1.0 * (
        SELECT COUNT(DISTINCT user_id)
        FROM journey_events_clean
        WHERE journey_stage = 'Purchase'
    ) / NULLIF(COUNT(*), 0)
        AS observed_purchase_rate

FROM users_clean;
```

**SQL Concepts Demonstrated**

- Subqueries
- `COUNT(DISTINCT)`
- Aggregate functions
- Safe division
- User-level conversion reporting

**Business Application**

Measures unique users with recorded Purchase events without imposing unsupported chronological requirements.

### Query 2 — Chronological Funnel Logic

The ordered funnel uses a series of Common Table Expressions to identify the earliest eligible event at each stage.

The following excerpt demonstrates the initial transitions.

```sql
WITH s0 AS (
    SELECT
        user_id,
        first_seen_date AS reached
    FROM users_clean
),

s1 AS (
    SELECT
        p.user_id,

        (
            SELECT MIN(e.event_date)
            FROM journey_events_clean e
            WHERE e.user_id = p.user_id
              AND e.journey_stage = 'Landing'
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
            FROM journey_events_clean e
            WHERE e.user_id = p.user_id
              AND e.journey_stage = 'Browse'
              AND e.event_date >= p.reached
        ) AS reached

    FROM s1 p
    WHERE p.reached IS NOT NULL
),

s3 AS (
    SELECT
        p.user_id,

        (
            SELECT MIN(e.event_date)
            FROM journey_events_clean e
            WHERE e.user_id = p.user_id
              AND e.journey_stage = 'Product View'
              AND e.event_date >= p.reached
        ) AS reached

    FROM s2 p
    WHERE p.reached IS NOT NULL
)

SELECT
    COUNT(reached) AS users_through_product_view
FROM s3;
```

The complete source extends this method through Add to Cart, Checkout, and Purchase.

**SQL Concepts Demonstrated**

- Multiple Common Table Expressions
- Correlated subqueries
- Earliest eligible event selection
- Date comparisons
- User-level progression
- Chronological filtering

**Business Application**

Prevents a later-stage event from being treated as a valid transition unless earlier required stages have been satisfied.

### Query 3 — Returning-User Conversion

```sql
WITH p AS (
    SELECT DISTINCT
        user_id

    FROM journey_events_clean

    WHERE journey_stage = 'Purchase'
)

SELECT
    u.is_returning,

    COUNT(*) AS users,

    COUNT(p.user_id)
        AS purchasers,

    1.0 * COUNT(p.user_id)
        / COUNT(*) AS purchase_rate

FROM users_clean u

LEFT JOIN p
    USING(user_id)

GROUP BY u.is_returning

ORDER BY u.is_returning;
```

**SQL Concepts Demonstrated**

- Common Table Expressions
- `DISTINCT`
- `LEFT JOIN`
- Grouped aggregation
- Binary segmentation

**Business Application**

Compares recorded purchasing participation across supplied returning-user groups.

### Query 4 — Time to Purchase

```sql
SELECT
    u.user_id,

    MIN(e.event_date)
        AS first_purchase_date,

    julianday(MIN(e.event_date))
        - julianday(u.first_seen_date)
        AS days_to_purchase

FROM users_clean u

JOIN journey_events_clean e
    USING(user_id)

WHERE e.journey_stage = 'Purchase'
  AND e.event_date >= u.first_seen_date

GROUP BY u.user_id

ORDER BY u.user_id;
```

**SQL Concepts Demonstrated**

- Relational joins
- Date functions
- Earliest-event selection
- Grouped aggregation
- Temporal filtering

**Business Application**

Calculates elapsed days from first observation to the first valid recorded purchase for each eligible user.

### Query 5 — Journey Stage Reach

```sql
SELECT
    journey_stage,

    COUNT(DISTINCT user_id)
        AS users

FROM journey_events_clean

GROUP BY journey_stage

ORDER BY users DESC;
```

**SQL Concepts Demonstrated**

- Distinct user counts
- Stage-level aggregation
- Behavioral segmentation
- Results ordering

**Business Application**

Provides independent stage participation counts for comparison with strict ordered-funnel results.

### Technical Design Principles

The implementation emphasizes:

- Consistent analytical grain
- Explicit population definitions
- Chronological eligibility
- Preservation of original event records
- Reproducible SQL execution
- Independent Python verification
- Transparent handling of source limitations

**Complete SQL:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Python Analysis & Metric Reconciliation

Python supports source processing, numerical validation, temporal analysis, and report generation.

### Data Preparation

The pipeline validates:

- Required fields
- Supported data types
- User identifiers
- Event relationships
- Date formats
- Known journey stage labels
- Nominal stage-order values

### Independent Metric Verification

Selected SQL results are independently recomputed in Python.

The reconciliation covers:

- Total users
- Unique purchasers
- Observed purchase rate
- Ordered funnel counts
- Time-to-purchase calculations

### Statistical Quantiles

Python calculates descriptive quantiles for elapsed days to purchase using pandas' linear quantile method.

**Median: 7 days**

**P90: 12 days**

These calculations are conditional on valid observed purchasers and do not account for censoring.

### Data Quality Assessment

The workflow records temporal inconsistencies and preserves the underlying event data.

It does not rewrite event dates to create a more favorable funnel result.

### Reporting Evidence

The project produces:

- SQL result CSVs
- Additional metric records
- Data quality diagnostics
- Validation results
- Query plans
- SHA-256 evidence manifests
- Offline HTML reporting

**Supporting Code:** [Python Entry Point](Python/analysis.py) | [Additional Metrics](Results/additional_metrics.json)

---

## 💡 Business Recommendations

The project's recommendations prioritize measurement reliability before product optimization.

### Recommendation Matrix

| Priority | Recommendation | Supporting Evidence | Proposed Validation |
|---|---|---|---|
| Critical | Investigate chronological event inconsistencies | 3,296 users with inversions | Timestamp and pipeline audit |
| Critical | Reconcile observed purchases with strict funnel | 627 observed vs. 0 ordered purchasers | Event coverage and stage-rule review |
| High | Validate required funnel stages | Large differences between reach and ordered paths | Product journey specification |
| High | Improve event instrumentation | Day-level dates and no event IDs | Capture precise timestamps and event identifiers |
| Medium | Investigate returning-user behavior | 16.20% vs. 8.26% purchase rates | Comparable user cohorts |
| Medium | Improve time-to-purchase measurement | Median 7 days, P90 12 days | Fixed follow-up and censoring-aware analysis |
| Medium | Rebuild source-aligned Tableau reporting | Legacy/native source mismatch | Tableau Desktop acceptance |

### Proposed 30/60/90-Day Analytical Plan

These are recommended actions for a business facing similar data issues, not completed production work.

**Days 1–30 — Validate Tracking**

- Audit event definitions.
- Identify source timestamps and transformation rules.
- Investigate users with date inversions.
- Confirm required and optional journey stages.
- Establish event instrumentation ownership.
- Document current reporting limitations.

**Days 31–60 — Improve Measurement**

- Introduce more precise timestamps.
- Add stable event identifiers.
- Establish session and user identity rules.
- Implement chronological data quality checks.
- Redefine conversion and funnel populations.
- Test source-aligned analytical outputs.

**Days 61–90 — Rebuild Reporting**

- Recalculate validated customer journeys.
- Compare event reach with ordered progression.
- Analyze returning-user cohorts.
- Evaluate time-to-event methods.
- Rebuild the canonical dashboard.
- Develop controlled UX hypotheses using trustworthy funnel data.

### Decision Framework

A product team should establish:

**Reliable Events → Valid Stage Definitions → Correct Chronology → Verified Funnel → Business Interpretation → Controlled Intervention**

Without reliable tracking, it may be inappropriate to use observed funnel losses as the justification for product changes.

---

## ✅ Data Quality & Validation

### Validation Overview

The project documents **15 passing runtime checks** covering source integrity, event definitions, SQL execution, and independent metric reconciliation.

### Verified Quality Summary

| Quality Indicator | Recorded Result |
|---|---:|
| User Records | 6,000 |
| Journey Event Records | 17,354 |
| Total Source Rows | 23,354 |
| Missing Required Cells | 0 |
| Exact-Repeated Source Rows | 0 |
| Events Before First-Seen Date | 0 |
| Users with Adjacent-Stage Inversions | 3,296 |
| Runtime Validation Checks | 15 |
| Runtime Status | Passed |

### Validation Coverage

**1. Schema Integrity**

Checks the required structure and field types for users and journey events.

**2. User-Key Integrity**

Verifies unique declared user keys.

**3. Referential Integrity**

Checks that events reference valid users.

**4. Stage Vocabulary**

Validates recognized journey stage labels.

**5. Nominal Stage Order**

Checks consistency between stage labels and their supplied ordinal values.

**6. SQL Execution**

Executes all five named analytical queries.

**7. Observed Purchase Reconciliation**

Verifies users, purchasers, and observed purchase rate.

**8. Ordered Funnel Reconciliation**

Independently checks the chronological funnel results.

**9. Time-to-Purchase Reconciliation**

Validates elapsed-time calculations.

### Why Validation Can Pass Despite Chronology Problems

The technical checks confirm that the data satisfy the implemented contracts and that the relevant calculations reconcile.

The 3,296 users with date inversions represent a documented semantic data-quality problem, not a hidden test failure.

A dataset can have valid columns, acceptable values, and correct SQL calculations while still being unsuitable for a particular business interpretation.

This distinction is a central lesson of the case study.

### Evidence Files

| Evidence File | Purpose |
|---|---|
| [validation.json](Results/validation.json) | Runtime checks |
| [quality.json](Results/quality.json) | Source chronology and quality diagnostics |
| [manifest.json](Results/manifest.json) | Source and output hashes |
| [query_plans.json](Results/query_plans.json) | SQLite query execution information |
| [additional_metrics.json](Results/additional_metrics.json) | Time quantiles and strict-path diagnostic |

**Validation Status:** 15 documented runtime checks passed.

**Business Interpretation Status:** Strict funnel abandonment remains unreliable because of source chronology inconsistencies.

---

## 📊 Business Intelligence & Dashboard Assets

The project includes Tableau, Excel, and offline reporting assets.

### Available Assets

| Asset | Purpose | Location |
|---|---|---|
| Excel Model | Corrected source-aligned analytical summary | [Excel Workbook](Excel/05_User_Journey_Analytics_Model.xlsx) |
| Tableau Workbook | Preserved legacy journey dashboard | [Tableau Workbook](Dashboard/User_Journey_Tableau_Dashboard.twbx) |
| Tableau Hyper Extract | Source-aligned reporting data | [Validated Extract](Dashboard/Validated_Analysis.hyper) |
| Journey Image | Existing visual reference | [Journey Image](Images/user_journey.png) |
| HTML Report | Canonical SQL/Python analysis | [REPORT.html](REPORT.html) |

### Native Workbook Verification

The original Tableau workbook contains a different dataset from the canonical analysis.

The native audit identifies approximately 4,066 extracted user-journey records in the legacy workbook, compared with the canonical project's 6,000 users and 17,354 journey events.

These are distinct source populations and schemas.

The legacy dashboard is preserved as a separate-data artifact.

It is not certified as a refreshed visualization of the canonical analysis.

### Completed Verification Evidence

- Canonical SQL/Python metric reconciliation
- Corrected Excel summary formulas
- Excel recalculation evidence
- Native Tableau source inspection
- Source-aligned Tableau Hyper extract
- Cell-level extract readback verification

### Outstanding Native Acceptance

A complete Tableau Desktop rebuild, visual refresh, filter inspection, and page-level acceptance have not been claimed as completed.

Opening or querying a Hyper extract does not establish that a Tableau dashboard has been visually validated.

### Recommended Canonical Dashboard Pages

**Page 1 — Executive Customer Overview**

Total users, observed purchasers, observed purchase rate, returning-user breakdown, and tracking-quality status.

**Page 2 — Journey Stage Reach**

Individual stage participation across Landing, Browse, Product View, Add to Cart, Checkout, Purchase, and Signup.

**Page 3 — Ordered Funnel Diagnostics**

Chronologically eligible users at each required stage.

Display a clear warning that strict path losses are not validated business abandonment.

**Page 4 — Returning-User Behavior**

Observed purchase rates by returning status with user and purchaser counts.

**Page 5 — Time-to-Purchase Analysis**

Descriptive elapsed-time distributions and percentile summaries for valid observed purchasers.

**Page 6 — Event Data Quality**

Date inversions, missing instrumentation concerns, chronology checks, and outstanding data-quality issues.

These represent a recommended design for future verified Tableau reporting, not a claim that the current legacy workbook contains those completed views.

### Verification Documentation

[Dashboard Reconciliation](Docs/Dashboard_Reconciliation.md) | [Field Mapping](Docs/Dashboard_Field_Mapping.md) | [Connection Guide](Docs/Connect_To_Dashboard.md) | [Native Workbook Verification](../verification/native/README.md)

---

## 📂 Project Structure

```text
05_User_Journey_Analytics/
│
├── Data/
│   ├── raw/
│   │   ├── users_raw.csv
│   │   └── journey_events_raw.csv
│   └── clean/
│       ├── users_clean.csv
│       └── journey_events_clean.csv
│
├── SQL/
│   └── analysis.sql
│
├── Python/
│   └── analysis.py
│
├── Excel/
│   └── 05_User_Journey_Analytics_Model.xlsx
│
├── Dashboard/
│   ├── README.md
│   ├── User_Journey_Tableau_Dashboard.twbx
│   └── Validated_Analysis.hyper
│
├── Images/
│   └── user_journey.png
│
├── Results/
│   ├── summary.csv
│   ├── ordered_funnel.csv
│   ├── returning_user_conversion.csv
│   ├── time_to_purchase.csv
│   ├── stage_reach.csv
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

The project uses shared data processing, SQL execution, validation, and reporting components from the parent Data Analyst Portfolio.

---

## ▶️ Reproduce the Analysis

### Prerequisites

- Python 3.12
- Git
- Python package installation capability

The core analytical workflow does not require paid software, an external database server, or a cloud subscription.

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

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4 — Execute the User Journey Project

```bash
python -m portfolio.run --project 05_User_Journey_Analytics
```

This regenerates the project's cleaned data, analytical results, validation records, and reporting evidence.

### Step 5 — Execute Automated Tests

```bash
python -m unittest discover -s tests -v
```

This command runs the shared portfolio test suite rather than only the User Journey project's runtime checks.

### Step 6 — Inspect Generated Results

Navigate to:

`05_User_Journey_Analytics/Results/`

Important outputs include:

- `summary.csv`
- `ordered_funnel.csv`
- `stage_reach.csv`
- `returning_user_conversion.csv`
- `time_to_purchase.csv`
- `quality.json`
- `validation.json`

### Step 7 — Review the Offline Report

Open:

`05_User_Journey_Analytics/REPORT.html`

Download or clone the repository to view the rendered report locally.

GitHub's file viewer may display HTML source rather than the intended offline report.

### Reproducibility Guidance

The pipeline generates source and output evidence manifests.

After failed execution, previously generated reports or partial results should not be assumed current.

Correct the issue, rerun successfully, and review the regenerated validation records.

**Full Instructions:** [Portfolio Reproduction Runbook](../docs/RUNBOOK.md)

---

## ⚠️ Limitations & Future Improvements

### Current Analytical Limitations

**1. Simulated Source Data**

The dataset represents a portfolio exercise, not a live ecommerce tracking system.

**2. Day-Level Event Dates**

The source cannot establish exact within-day event order.

**3. No Stable Event IDs**

The data do not support independent event-level identity or full deduplication reasoning.

**4. No Session Boundaries**

The dataset cannot establish whether all journey steps occurred within one session or across multiple sessions.

**5. Substantial Chronological Inconsistency**

3,296 users have adjacent-stage date inversions.

**6. Strict Funnel Completion Is Not Behavioral Abandonment**

Zero complete ordered paths cannot be interpreted as zero purchases or universal checkout abandonment.

**7. Observational Returning-User Comparisons**

Returning status is not randomly assigned, and its underlying lookback definition is unavailable.

**8. Incomplete Follow-Up**

Time-to-purchase estimates do not account for censoring.

**9. First-Seen Dates Are Not Verified Acquisition Dates**

The available date represents recorded first observation.

**10. Legacy Tableau Source Mismatch**

The original Tableau workbook uses different source data from the canonical SQL/Python analysis.

### Future Enhancements

Potential next iterations include:

- High-precision event timestamps
- Stable event identifiers
- Session identifiers
- Verified user identity stitching
- Journey sessionization
- Validated event ordering
- Alternative customer-path analysis
- Optional-versus-required stage definitions
- Cohort-based conversion reporting
- Censoring-aware survival analysis
- Returning-user behavior by cohort
- Acquisition-source analysis
- Device-level journey segmentation
- Checkout instrumentation validation
- Controlled UX experimentation
- Source-aligned Tableau dashboard acceptance

These are future opportunities and are not represented as already implemented.

---

## 🧠 Project Takeaways

### Technical Skills Demonstrated

- SQL-based behavioral analytics
- Relational data analysis
- Chronological funnel construction
- Common Table Expressions
- Correlated subqueries
- Date arithmetic
- User-level segmentation
- Python metric reconciliation
- Statistical quantiles
- Source data validation
- Automated checks
- Reproducible reporting

### Business Skills Demonstrated

- Translating customer behavior questions into metrics
- Defining conversion populations
- Distinguishing event reach from valid progression
- Identifying tracking-quality problems
- Avoiding misleading abandonment conclusions
- Evaluating returning-user associations
- Interpreting purchase timelines
- Communicating measurement uncertainty
- Designing responsible analytical follow-up plans

### Final Conclusion

The User Journey Analytics project reveals four important findings.

**First**, the simulated dataset contains 627 observed purchasers among 6,000 users, corresponding to a **10.45% observed purchase rate**.

**Second**, returning users have a higher recorded purchase rate than non-returning users, although the relationship is observational rather than causal.

**Third**, the strict chronological funnel reports zero complete six-stage paths despite hundreds of recorded purchases.

**Fourth**, 3,296 users have date-ordering inconsistencies, providing strong evidence that event chronology must be investigated before funnel losses are interpreted as real customer abandonment.

These results demonstrate how SQL, Python, and data quality validation can reveal meaningful differences between reported customer activity and the reliability of the tracking system used to measure it.

**The central lesson is that reliable customer journey analysis requires more than counting events. It requires valid event definitions, accurate chronology, consistent customer identification, reproducible calculations, and business interpretations that reflect the quality of the available evidence.**

---

## 📚 Supporting Documentation & Evidence

| Resource | Description |
|---|---|
| [Data Dictionary](Docs/Data_Dictionary.md) | Source columns, types, and validation contracts |
| [KPI Lineage](Docs/KPI_Lineage.md) | Metric calculations and business rules |
| [SQL Analysis](SQL/analysis.sql) | Executable behavioral analysis |
| [Python Analysis](Python/analysis.py) | Project Python entry point |
| [Purchase Summary](Results/summary.csv) | Overall observed purchasing |
| [Stage Reach](Results/stage_reach.csv) | Independent stage participation |
| [Ordered Funnel](Results/ordered_funnel.csv) | Strict chronological progression |
| [Returning-User Analysis](Results/returning_user_conversion.csv) | Purchase rates by returning status |
| [Time-to-Purchase Analysis](Results/time_to_purchase.csv) | User-level elapsed purchase times |
| [Additional Metrics](Results/additional_metrics.json) | Timing percentiles and ordered-path diagnostics |
| [Data Quality Report](Results/quality.json) | Chronological source issues |
| [Validation Evidence](Results/validation.json) | Recorded runtime checks |
| [Offline Report](REPORT.html) | Canonical analytical report |
| [Native Workbook Verification](../verification/native/README.md) | Excel and Tableau evidence and limitations |

---

## 👨‍💻 About the Analyst

**Jamie Christian**

Data Analytics | Business Intelligence | SQL | Python | Customer Analytics

I focus on transforming raw information into reliable business metrics, evaluating user behavior, validating analytical results, and communicating evidence-based insights that support informed decision-making.

My professional interests include Data Analytics, Business Intelligence, Product Analytics, Customer Behavior, Business Analysis, and Data Quality.

📧 [Email](mailto:Jamiechristian331@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/jamiechristian2/)  
💻 [GitHub](https://github.com/JamieChristian22)

### 🔗 Explore More Projects

[⬅️ Back to Main Data Analyst Portfolio](../README.md)

[📦 Previous Project: Amazon Marketplace Analytics](../04_Amazon_Marketplace_Analytics/README.md)

[📈 Project 01: SaaS Product Analytics](../01_SaaS_Product_Analytics_StreamFlow/README.md)

[🧪 Project 02: A/B Testing & Feature Impact](../02_AB_Test_Feature_Impact/README.md)

[🛒 Project 03: Ecommerce Product Analytics](../03_Ecommerce_Product_Analytics/README.md)

---

**🔍 User Journey Analytics | Built by Jamie Christian**

*SQL-driven customer insights. Python-validated metrics. Reliable event analysis. Evidence-based business decisions.*
