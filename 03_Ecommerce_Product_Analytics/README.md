
# 🛒 Ecommerce Product Analytics | Conversion, Customer Behavior & Revenue Performance

### SQL • Python • Funnel Analysis • Power BI • Revenue Analytics • Data Quality

**An end-to-end ecommerce analytics case study investigating website conversion, shopping cart abandonment, customer-session behavior, product revenue concentration, and discount-related performance using reproducible SQL and Python analysis.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Power BI](https://img.shields.io/badge/Power_BI-Native_Asset-F2C811)
![Analytics](https://img.shields.io/badge/Ecommerce-Product_Analytics-blueviolet)
![Validation](https://img.shields.io/badge/Validation-20%2F20-success)
![Dataset](https://img.shields.io/badge/Dataset-Simulated-orange)

**Analyst:** Jamie Christian  
**Project:** 03 — Ecommerce Product Analytics  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Jamie Christian](https://www.linkedin.com/in/jamiechristian2/)

---

## 📌 Executive Summary

This project analyzes a simulated ecommerce business to understand customer purchasing behavior, conversion performance, shopping cart abandonment, and revenue distribution across products.

Using **25,000 website sessions and 3,037 associated order records**, the analysis applies SQL, Python, data quality validation, and business intelligence principles to uncover performance patterns and identify opportunities for further investigation.

The project focuses on five business questions:

1. How effectively do website sessions convert into purchases?
2. Where does shopping cart abandonment occur?
3. How does conversion performance differ by device and acquisition channel?
4. How concentrated is recorded revenue among top-performing products?
5. How do observed discounts relate to order values and purchasing patterns?

### Key Results

| Business Metric | Verified Result |
|---|---:|
| 👥 Website Sessions | 25,000 |
| 🛒 Sessions with Cart Activity | 8,492 |
| 💳 Purchases | 3,037 |
| 📈 Session Conversion Rate | 12.15% |
| 📉 Cart Abandonment Rate | 64.24% |
| 💰 Recorded Order Revenue | 198,586.00 |
| 🧾 Average Order Value | 65.39 |
| 📦 Distinct Product SKUs | 400 |
| 🏆 Revenue Share of Top 20% of SKUs | 31.42% |
| ✅ Runtime Validation Checks | 20 passed |

**Data transparency:** This analysis uses supplied simulated datasets. Revenue values are expressed in unspecified dataset currency units. No real company sales, production deployment, or realized business improvements are claimed.

### Primary Findings

**1. Shopping cart abandonment is substantial.** Of the 8,492 sessions with cart activity, 3,037 resulted in a purchase, producing a 64.24% abandonment rate under the dataset's validated funnel definition.

**2. Conversion performance varies across acquisition channels and devices.** Desktop Paid Social sessions convert at approximately 14.33%, compared with 9.72% for Mobile Paid Social sessions.

**3. Product revenue is distributed across a broad assortment.** The top 20% of SKUs contribute approximately 31.42% of recorded order revenue, rather than the 80% sometimes associated with a conventional Pareto pattern.

**4. Discount-related comparisons require caution.** Differences in average order value between discounted and non-discounted transactions are observational and cannot establish the causal effects of promotions.

### Business Conclusion

The analysis identifies **checkout friction, mobile-session performance, and product revenue distribution** as useful areas for further investigation.

Rather than assuming the causes of observed differences, the project provides a reproducible analytical foundation for prioritizing usability research, instrumentation review, merchandising analysis, and controlled experimentation.

---

## 📚 Table of Contents

1. [Business Problem](#-business-problem)
2. [Dataset Overview](#-dataset-overview)
3. [Technical Stack](#-technical-stack)
4. [End-to-End Workflow](#-end-to-end-analytical-workflow)
5. [KPI Definitions](#-kpi-definitions--business-rules)
6. [Analysis 1: Conversion Performance](#-analysis-1-ecommerce-conversion-performance)
7. [Analysis 2: Cart Abandonment](#-analysis-2-shopping-cart-abandonment)
8. [Analysis 3: Device & Channel Performance](#-analysis-3-device--acquisition-channel-performance)
9. [Analysis 4: Product Revenue Concentration](#-analysis-4-product-revenue--sku-pareto-analysis)
10. [Analysis 5: Discount Associations](#-analysis-5-discount--order-value-analysis)
11. [SQL Implementation](#-sql-implementation)
12. [Business Recommendations](#-business-recommendations)
13. [Data Quality & Validation](#-data-quality--validation)
14. [Power BI & Excel Assets](#-business-intelligence--dashboard-assets)
15. [Project Structure](#-project-structure)
16. [Reproduction Guide](#-reproduce-the-analysis)
17. [Limitations](#-limitations--future-improvements)
18. [Project Takeaways](#-project-takeaways)

---

## 🎯 Business Problem

### Business Context

Ecommerce businesses rely on website traffic, product discovery, customer engagement, and successful checkout completion to generate revenue.

However, attracting visitors does not guarantee that those visitors will complete purchases.

Customers may browse products, add items to their carts, and leave before checkout is completed.

At the same time, businesses must understand how different acquisition channels, devices, products, and promotional strategies contribute to overall performance.

Without reliable analytics, companies may struggle to identify which operational or customer-experience problems deserve priority.

### Business Scenario

A simulated ecommerce platform wants to evaluate purchasing performance across its website.

The business has collected session-level behavioral data and associated order records.

Its analytics team needs to answer questions about conversion efficiency, checkout progression, product performance, and discount associations.

### Primary Business Question

**Where is the ecommerce purchasing process losing potential transactions, and which customer-session segments and products deserve further business investigation?**

### Business Objectives

| Objective | Analytical Focus | Decision Support |
|---|---|---|
| Evaluate Conversion | Website sessions vs. purchases | Establish purchasing efficiency |
| Analyze Cart Abandonment | Cart sessions vs. completed purchases | Identify funnel friction |
| Compare Customer Sessions | Device and acquisition channel | Prioritize segment-level investigation |
| Analyze Revenue | Recorded orders and average order value | Understand commercial performance |
| Evaluate Product Concentration | Revenue by SKU | Support assortment review |
| Examine Discounts | Discount flags and order values | Identify questions for promotion testing |
| Validate Reporting | Data contracts and KPI reconciliation | Improve metric reliability |

### Project Goal

Build a reproducible ecommerce analytics workflow that transforms raw website and order records into traceable KPIs, validates the resulting calculations, and communicates findings that can support responsible business decisions.

---

## 🗄️ Dataset Overview

The project uses two related simulated datasets containing **28,037 source rows**.

### Source Tables

| Dataset | Records | Purpose |
|---|---:|---|
| `web_sessions_raw.csv` | 25,000 | Website activity, device, channel, cart and purchase indicators |
| `orders_raw.csv` | 3,037 | Purchased sessions, product SKUs, discounts and order values |
| **Total** | **28,037** | **Two connected analytical datasets** |

### Dataset 1 — Website Sessions

Each record represents one website session.

| Column | Type | Description |
|---|---|---|
| `session_id` | Integer | Unique session identifier |
| `session_date` | Date | Recorded session date |
| `device` | Text | Device category |
| `channel` | Text | Customer acquisition channel |
| `added_to_cart` | Binary | Whether the session added an item to the cart |
| `purchased` | Binary | Whether the session completed a purchase |

**Analytical Uses**

- Website conversion measurement
- Cart activity analysis
- Cart abandonment reporting
- Device performance
- Acquisition-channel comparison
- Funnel segmentation

### Dataset 2 — Orders

Contains the associated order record for each purchased session under the supplied dataset contract.

| Column | Type | Description |
|---|---|---|
| `session_id` | Integer | Associated purchased session |
| `session_date` | Date | Order-associated session date |
| `device` | Text | Device category |
| `channel` | Text | Acquisition channel |
| `sku` | Text | Product identifier |
| `category` | Text | Product category |
| `discount_applied` | Binary | Whether a discount flag was recorded |
| `order_value` | Numeric | Recorded order value |
| `units` | Integer | Number of units in the supplied order row |

**Analytical Uses**

- Revenue calculations
- Average order value
- Product performance
- SKU concentration
- Discount-related comparisons
- Order-to-session reconciliation

### Data Relationships

The datasets connect through `session_id`.

**Website Sessions (1) → (0 or 1) Orders**

The repository validates one order record per purchased session for this particular dataset.

This is a documented source contract, not an assumption that all real ecommerce businesses have only one order per session.

### Data Grain

Understanding data grain prevents inaccurate calculations.

**Session grain:** One record per website session.

**Order grain:** One order record per purchased session.

**Product grain:** One SKU is recorded per supplied order row.

**Customer grain:** Not available.

A session identifier is not equivalent to a stable customer identifier. Consequently, the dataset cannot support validated customer-level repeat-purchase or RFM analysis.

### Supporting Documentation

[📘 Data Dictionary](Docs/Data_Dictionary.md) | [📂 Raw Data](Data/raw) | [📂 Clean Data](Data/clean)

---

## 🛠️ Technical Stack

| Category | Technology | Application |
|---|---|---|
| Programming | Python 3.12 | Data validation, processing and reconciliation |
| Query Language | SQL | Business metrics and analytical queries |
| Database | SQLite | Relational analytical execution |
| Data Analysis | pandas | Independent KPI calculations |
| Data Preparation | Python | Schema validation and normalization |
| Product Analytics | Funnel and segmentation analysis | Conversion and purchasing behavior |
| Revenue Analytics | Aggregations and rankings | Product concentration and order metrics |
| BI Assets | Power BI | Existing native dashboard and model inspection |
| Spreadsheet Analysis | Excel | Corrected source-aligned summaries |
| Reporting | HTML and CSV | Analytical reporting artifacts |
| Automated Testing | Python unittest | Unit and integration verification |
| Data Integrity | SHA-256 manifests | Evidence and source traceability |
| Version Control | Git and GitHub | Repository history and reproducibility |

### SQL Competencies

- `INNER JOIN` and `LEFT JOIN`
- Conditional aggregation
- `GROUP BY`
- Common Table Expressions
- Window functions
- `ROW_NUMBER()`
- Cumulative revenue calculations
- `CASE` expressions
- Subqueries
- Safe division with `NULLIF`
- Revenue ranking
- Segment-level metrics

### Python Competencies

- CSV data processing
- DataFrame transformations
- Data type and range validation
- Independent SQL reconciliation
- Metric calculation
- Source relationship verification
- Automated reporting
- Reproducible analysis
- Unit and integration testing

### Business Analytics Competencies

- KPI definition and documentation
- Conversion funnel reporting
- Ecommerce performance evaluation
- Product concentration analysis
- Revenue analysis
- Customer-session segmentation
- Discount association analysis
- Data quality investigation
- Evidence-based recommendations

---

## 🔄 End-to-End Analytical Workflow

The project follows an analytical pipeline that connects business requirements with verified results.

### Phase 1 — Define Business Requirements

Establish the questions being answered, relevant populations, and KPI definitions.

**Deliverable:** Defined analytical objectives and business rules.

### Phase 2 — Inspect Source Data

Examine source records and verify:

- Required fields
- Session identifiers
- Source types
- Date formats
- Binary outcome fields
- Order relationships
- Revenue fields
- Available segmentation dimensions

**Deliverable:** Data dictionary and source contracts.

### Phase 3 — Validate & Transform

Apply supported normalization and validation rules.

The pipeline checks for invalid records and inconsistent relationships rather than silently fixing source data.

**Deliverable:** Regenerated clean datasets.

### Phase 4 — Execute SQL Analysis

Compute:

- Overall conversion
- Cart abandonment
- Revenue
- Average order value
- Device/channel performance
- SKU revenue ranking
- Discount associations

**Deliverable:** Named SQL query outputs.

### Phase 5 — Reconcile Using Python

Independently calculate headline metrics and compare them with SQL results.

**Deliverable:** Recorded numerical verification.

### Phase 6 — Interpret Results

Examine commercial and customer-experience implications without claiming unsupported causal explanations.

**Deliverable:** Business findings and recommendations.

### Phase 7 — Generate Reports

Publish reproducible analytical outputs, quality reports, and evidence manifests.

**Deliverable:** CSV result files and offline HTML reporting.

### Workflow Summary

**Raw Sessions & Orders → Data Validation → Clean Tables → SQLite → Analytical Queries → Python Reconciliation → Results & Reporting → Business Recommendations**

---

## 📐 KPI Definitions & Business Rules

### Primary KPI Framework

| KPI | Calculation | Interpretation |
|---|---|---|
| Total Sessions | Count of website sessions | Total observed website activity |
| Cart Sessions | Sum of `added_to_cart` | Sessions with recorded cart activity |
| Purchases | Sum of `purchased` | Completed purchase sessions |
| Conversion Rate | Purchases ÷ Sessions | Overall session purchasing rate |
| Cart Abandonment Rate | 1 − Purchases ÷ Cart Sessions | Proportion of cart sessions without a completed purchase |
| Total Revenue | Sum of `order_value` | Recorded order revenue |
| Average Order Value | Total Revenue ÷ Number of Orders | Average recorded value per order |
| SKU Revenue | Sum of order values by SKU | Product-level contribution |
| Top 20% SKU Share | Revenue from highest-ranked 20% of SKUs ÷ Total Revenue | Merchandise concentration |
| Discounted Order AOV | Average order value where discount flag = 1 | Observed discounted-order performance |

### Important Business Rules

**Session-Based Conversion**

Conversion uses website sessions as the denominator, not unique customers.

**Purchase Requires Cart**

The dataset contract validates that purchased sessions contain the expected cart activity.

**One Order per Purchased Session**

The supplied order records reconcile to purchase sessions.

**Revenue Definition**

Revenue comes from the recorded `order_value` field. Refunds, taxes, shipping, and recognized revenue treatment are not independently available.

**SKU Ranking**

Product concentration uses SKU-level revenue, descending rank order, deterministic SKU tie-breaking, and the top 20% of distinct SKUs.

**Discount Comparisons**

Discount status is an observed attribute, not a randomized treatment.

### KPI Reference

[📘 KPI Lineage Documentation](Docs/KPI_Lineage.md)

---

## 📈 Analysis 1: Ecommerce Conversion Performance

### Business Question

What percentage of website sessions result in completed purchases?

### Verified Performance

| Metric | Result |
|---|---:|
| Total Website Sessions | 25,000 |
| Sessions with Cart Activity | 8,492 |
| Completed Purchases | 3,037 |
| Session Conversion Rate | 12.15% |
| Cart Activity Rate | 33.97% |
| Recorded Revenue | 198,586.00 |
| Average Order Value | 65.39 |

### Conversion Rate Formula

\[
\text{Conversion Rate}=\frac{\text{Purchases}}{\text{Website Sessions}}\times100
\]

\[
=\frac{3,037}{25,000}\times100
\]

**Conversion Rate: 12.15%**

### Finding 1 — Most Website Sessions Do Not Convert

Approximately 12.15% of observed sessions result in a completed purchase.

This describes the observed session conversion baseline.

It does not establish whether performance is strong or weak relative to a valid industry benchmark, because no directly comparable external benchmark is included.

### Finding 2 — About One-Third of Sessions Reach Cart Activity

Of 25,000 sessions, 8,492 include recorded cart activity.

**Cart Activity Rate: 33.97%**

This indicates that a sizable portion of sessions records purchasing intent through cart interaction, but many still do not result in orders.

### Finding 3 — Revenue and Average Order Value Are Traceable

The 3,037 purchased sessions correspond to 3,037 validated order rows.

Total recorded revenue is 198,586.00.

\[
\text{AOV}=\frac{\text{Total Revenue}}{\text{Orders}}
\]

**Average Order Value: 65.39**

### Business Interpretation

The observed conversion and cart metrics provide a baseline for investigating customer-session progression.

A useful next step is to identify which segments experience higher abandonment and whether the measurement represents actual checkout friction, price comparison, or other behavior.

**Evidence:** [Overall Ecommerce Summary](Results/summary.csv)

---

## 🛒 Analysis 2: Shopping Cart Abandonment

### Business Question

How frequently do sessions with cart activity end without a recorded purchase?

### Funnel Results

| Funnel Stage | Sessions | Share of Total Sessions |
|---|---:|---:|
| Website Session | 25,000 | 100.00% |
| Added to Cart | 8,492 | 33.97% |
| Completed Purchase | 3,037 | 12.15% |

### Cart Completion

\[
\text{Cart Completion Rate}=\frac{3,037}{8,492}\times100
\]

**Cart Completion Rate: 35.76%**

### Cart Abandonment

\[
\text{Cart Abandonment Rate}=1-\frac{\text{Purchases}}{\text{Cart Sessions}}
\]

\[
=1-\frac{3,037}{8,492}
\]

**Cart Abandonment Rate: 64.24%**

### Finding 1 — Most Cart Sessions Do Not Complete Purchasing

Of the 8,492 sessions with cart activity, 5,455 do not contain a completed purchase.

This produces the observed 64.24% cart-abandonment rate.

### Finding 2 — The Cart-to-Purchase Transition Deserves Investigation

The observed drop-off identifies a potentially valuable area for product and checkout research.

Possible explanations include:

- Unexpected shipping or checkout costs
- Payment friction
- Account creation requirements
- Checkout usability
- Product comparison behavior
- Customers intentionally saving items for later

These are **hypotheses**, not proven findings from the supplied data.

### Finding 3 — Abandoned Carts Are Not Equal to Lost Revenue

The dataset does not establish what cart contents would have cost or whether abandoned sessions would have purchased without friction.

Therefore, multiplying abandoned carts by average order value would not produce a defensible causal lost-revenue estimate.

### Recommended Investigation

Review checkout instrumentation and customer feedback to distinguish intentional nonpurchase behavior from technical or usability barriers.

A future controlled experiment could test a specific checkout improvement and measure its effect on completed purchases.

**Evidence:** [Funnel by Segment](Results/funnel_by_segment.csv)

---

## 📱 Analysis 3: Device & Acquisition Channel Performance

### Business Question

Which device and marketing-channel combinations show the strongest and weakest observed session conversion?

### Verified Segment Results

| Device | Channel | Sessions | Purchases | Conversion | Cart Abandonment |
|---|---|---:|---:|---:|---:|
| Desktop | Paid Social | 2,247 | 322 | 14.33% | 60.10% |
| Desktop | Paid Search | 3,448 | 475 | 13.78% | 61.63% |
| Desktop | Email | 1,739 | 239 | 13.74% | 61.20% |
| Desktop | Affiliate | 1,201 | 153 | 12.74% | 67.17% |
| Desktop | Organic | 3,452 | 431 | 12.49% | 64.93% |
| Mobile | Affiliate | 1,232 | 153 | 12.42% | 63.22% |
| Mobile | Paid Search | 3,669 | 424 | 11.56% | 64.37% |
| Mobile | Email | 1,817 | 199 | 10.95% | 65.27% |
| Mobile | Organic | 3,788 | 407 | 10.74% | 66.67% |
| Mobile | Paid Social | 2,407 | 234 | 9.72% | 68.21% |

### Finding 1 — Desktop Paid Social Has the Highest Observed Conversion

Desktop Paid Social has a conversion rate of approximately **14.33%**, the highest among the ten displayed segments.

This indicates relatively strong observed purchase completion within that segment.

It does not prove the traffic source itself causes higher conversion.

### Finding 2 — Mobile Paid Social Has the Lowest Observed Conversion

Mobile Paid Social converts at approximately **9.72%** and has an abandonment rate of **68.21%**.

It combines substantial session volume with comparatively weak observed purchasing performance.

This makes it a useful candidate for further investigation.

### Finding 3 — Device Differences Are Worth Exploring

For Paid Social traffic:

- Desktop conversion: 14.33%
- Mobile conversion: 9.72%

The difference is approximately **4.61 percentage points**.

Potential contributing factors might include differences in intent, page design, device usability, or traffic composition.

The current observational analysis cannot distinguish these mechanisms.

### Finding 4 — Mobile Organic Also Has Elevated Abandonment

Mobile Organic sessions exhibit an observed cart-abandonment rate of **66.67%**.

Given the segment's 3,788 sessions, it deserves consideration alongside Mobile Paid Social when planning usability research.

### Business Interpretation

The segment data suggest that investigating mobile purchasing experiences may be useful.

However, device and channel differences are not randomized comparisons, so they should not be presented as causal effects.

### Recommended Analysis

A follow-up investigation could evaluate:

- Checkout errors by device
- Page responsiveness
- Payment-method availability
- Cart-to-checkout progression
- Acquisition-source intent
- Customer-experience feedback
- Mobile-specific checkout tests

**Evidence:** [Complete Device & Channel Analysis](Results/funnel_by_segment.csv)

---

## 📦 Analysis 4: Product Revenue & SKU Pareto Analysis

### Business Question

How concentrated is recorded ecommerce revenue among the highest-performing product SKUs?

### Business Context

Product revenue concentration analysis helps businesses understand whether sales depend on a narrow group of products or are distributed across a broader assortment.

The project uses SQL window functions to rank SKUs by recorded revenue.

### SKU Overview

| Metric | Verified Result |
|---|---:|
| Distinct SKUs | 400 |
| Top 20% of SKUs | 80 |
| Total Recorded Revenue | 198,586.00 |
| Top 20% SKU Revenue Share | 31.42% |

### Pareto Methodology

1. Aggregate recorded revenue by SKU.
2. Rank SKUs in descending revenue order.
3. Use SKU identifiers to break revenue ties consistently.
4. Compute cumulative revenue using a SQL window function.
5. Select the top 20% of distinct SKUs.
6. Divide their combined revenue by total revenue.

### Verified Leading SKUs

| Rank | Product SKU | Recorded Revenue |
|---|---|---:|
| 1 | SKU-0028 | 1,249.99 |
| 2 | SKU-0143 | 992.65 |
| 3 | SKU-0081 | 948.51 |
| 4 | SKU-0339 | 930.70 |
| 5 | SKU-0104 | 920.64 |
| 6 | SKU-0344 | 903.81 |
| 7 | SKU-0122 | 896.86 |
| 8 | SKU-0273 | 889.10 |
| 9 | SKU-0234 | 879.20 |
| 10 | SKU-0047 | 876.01 |

### Finding 1 — The Highest-Revenue SKU Is SKU-0028

SKU-0028 contributes 1,249.99 in recorded revenue.

This makes it the highest-ranked product under the saved aggregation.

Additional inventory and profitability information would be needed to evaluate its broader commercial importance.

### Finding 2 — Top-SKU Revenue Concentration Is Moderate

The top 80 SKUs account for **31.42% of recorded revenue**.

This does not resemble a strong 80/20 revenue-concentration relationship.

The remaining 80% of SKUs collectively account for approximately 68.58% of recorded revenue.

### Finding 3 — Product Performance Should Not Be Evaluated Solely by Revenue

Revenue does not reveal:

- Product profitability
- Gross margin
- Inventory holding costs
- Stockout frequency
- Return rates
- Customer demand trends
- Acquisition costs

A SKU contributing more revenue may not necessarily be more profitable.

### Business Recommendation

Use SKU concentration as an initial diagnostic for merchandising and inventory review.

Do not automatically discontinue lower-ranked products or prioritize top sellers without evaluating profitability, availability, and customer demand.

**Evidence:** [SKU Pareto Results](Results/sku_pareto.csv)

---

## 🏷️ Analysis 5: Discount & Order Value Analysis

### Business Question

How do observed order values and quantities differ between discounted and non-discounted purchases?

### Analytical Approach

The project compares order records by:

- Device
- Product category
- Discount flag

It then calculates:

- Number of orders
- Average order value
- Average units per order

### Selected Verified Results

| Device | Category | Discount Applied | Orders | Average Order Value |
|---|---|---|---:|---:|
| Desktop | Apparel | No | 283 | 67.90 |
| Desktop | Apparel | Yes | 163 | 61.82 |
| Desktop | Beauty | No | 203 | 67.06 |
| Desktop | Beauty | Yes | 98 | 62.71 |
| Desktop | Electronics | No | 210 | 68.08 |
| Desktop | Electronics | Yes | 123 | 61.91 |
| Desktop | Fitness | No | 120 | 71.31 |
| Desktop | Fitness | Yes | 64 | 60.42 |
| Desktop | Home | No | 225 | 67.92 |
| Desktop | Home | Yes | 131 | 63.78 |

### Finding 1 — Discounted Orders Show Lower AOV in Selected Segments

Across the displayed Desktop categories, orders with discount flags exhibit lower average recorded order values than those without discounts.

This is a descriptive relationship.

### Finding 2 — Lower AOV Does Not Establish Discount Ineffectiveness

A promotional campaign might have different goals, including:

- Increasing conversion
- Encouraging first purchases
- Improving inventory turnover
- Acquiring new customers
- Increasing overall order volume

Average order value alone cannot determine whether a discount accomplishes those goals.

### Finding 3 — Selection Effects Matter

Discounted and non-discounted purchases may involve different products, customer populations, or buying intentions.

Because discounts were not assigned through a documented randomized experiment, the observed differences cannot be interpreted as causal promotional effects.

### Recommended Follow-Up

A stronger promotional evaluation would require:

- Verified discount amounts
- Product-level margin data
- Eligibility and exposure information
- Comparable treatment/control populations
- Clear campaign objectives
- Incremental revenue or margin measurement

**Evidence:** [Discount Association Results](Results/discount_association.csv)

---

## 💻 SQL Implementation

The project contains executable SQLite SQL queries rather than disconnected illustrative scripts.

### Query 1 — Ecommerce Performance Summary

```sql
SELECT
    COUNT(*) AS sessions,
    SUM(added_to_cart) AS cart_sessions,
    SUM(purchased) AS purchases,

    AVG(1.0 * purchased) AS conversion_rate,

    1.0 - SUM(1.0 * purchased)
        / NULLIF(SUM(added_to_cart), 0)
        AS cart_abandonment_rate,

    (
        SELECT SUM(order_value)
        FROM orders_clean
    ) AS revenue,

    (
        SELECT AVG(order_value)
        FROM orders_clean
    ) AS average_order_value

FROM web_sessions_clean;
```

**SQL Concepts Demonstrated**

- Aggregate functions
- Scalar subqueries
- Conversion calculations
- Safe division
- Consistent KPI denominators

**Business Application**

Creates a unified performance summary across website activity, purchases, and recorded revenue.

### Query 2 — Conversion and Abandonment by Segment

```sql
SELECT
    device,
    channel,

    COUNT(*) AS sessions,
    SUM(added_to_cart) AS carts,
    SUM(purchased) AS purchases,

    AVG(1.0 * purchased)
        AS conversion_rate,

    1.0 - SUM(1.0 * purchased)
        / NULLIF(SUM(added_to_cart), 0)
        AS cart_abandonment_rate

FROM web_sessions_clean

GROUP BY
    device,
    channel

ORDER BY conversion_rate DESC;
```

**SQL Concepts Demonstrated**

- Multi-dimensional segmentation
- Aggregation
- Derived performance measures
- SQL grouping
- Comparative analysis

**Business Application**

Highlights device and acquisition-channel combinations with different observed conversion and abandonment patterns.

### Query 3 — Product Revenue Ranking and Cumulative Share

```sql
WITH revenue AS (
    SELECT
        sku,
        SUM(order_value) AS revenue

    FROM orders_clean

    GROUP BY sku
),

ranked AS (
    SELECT
        *,

        ROW_NUMBER() OVER (
            ORDER BY revenue DESC, sku
        ) AS rank,

        COUNT(*) OVER ()
            AS sku_count,

        SUM(revenue) OVER ()
            AS total_revenue,

        SUM(revenue) OVER (
            ORDER BY revenue DESC, sku
            ROWS UNBOUNDED PRECEDING
        ) AS cumulative_revenue

    FROM revenue
)

SELECT
    *,

    cumulative_revenue
        / NULLIF(total_revenue, 0)
        AS cumulative_share,

    (
        rank <= (sku_count + 4) / 5
    ) AS in_top_20_percent

FROM ranked

ORDER BY rank;
```

**SQL Concepts Demonstrated**

- Common Table Expressions
- `ROW_NUMBER()`
- Window functions
- Cumulative sums
- Revenue ranking
- Partition-independent totals
- Deterministic tie-breaking

**Business Application**

Supports reproducible SKU revenue concentration analysis.

### Query 4 — Discount-Related Order Performance

```sql
SELECT
    device,
    category,
    discount_applied,

    COUNT(*) AS orders,

    AVG(order_value)
        AS average_order_value,

    AVG(1.0 * units)
        AS average_units

FROM orders_clean

GROUP BY
    device,
    category,
    discount_applied

ORDER BY
    device,
    category,
    discount_applied;
```

**SQL Concepts Demonstrated**

- Conditional grouping
- Category segmentation
- Average metric calculation
- Promotional data analysis

**Business Application**

Enables descriptive comparisons of orders with and without observed discounts.

**Complete Implementation:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Python Analysis & Metric Reconciliation

Python supports the pipeline by validating source data, running analytical transformations, and independently checking selected SQL results.

### Primary Python Responsibilities

**Data Preparation**

- Read source CSVs
- Validate required schemas
- Normalize supported values
- Check primary keys and relationships
- Produce cleaned tables

**Analytical Reconciliation**

- Verify session counts
- Verify purchase counts
- Recalculate conversion rates
- Reconcile cart-abandonment calculations
- Reconcile recorded revenue
- Recalculate average order value
- Verify top-20% SKU revenue share

**Reporting**

- Generate result files
- Preserve quality diagnostics
- Record validation outcomes
- Track source and output hashes
- Produce offline analytical reports

### Independent Metric Verification

The portfolio compares selected SQL outputs against separate pandas calculations.

This helps identify errors caused by inconsistent populations, incorrect denominators, inappropriate joins, or mismatched aggregation logic.

### Supporting Files

[🐍 Python Entry Point](Python/analysis.py) | [📊 Additional Metrics](Results/additional_metrics.json) | [✅ Validation Evidence](Results/validation.json)

---

## 💡 Business Recommendations

The project converts descriptive observations into priorities for future business investigation.

### Recommendation Matrix

| Priority | Recommendation | Supporting Evidence | Proposed Validation |
|---|---|---|---|
| High | Investigate cart-to-purchase friction | 64.24% cart abandonment | Checkout instrumentation and user research |
| High | Examine Mobile Paid Social experience | 9.72% conversion, 68.21% abandonment | Device-level usability testing |
| Medium | Evaluate Mobile Organic purchasing journey | 66.67% abandonment | Review checkout errors and customer feedback |
| Medium | Assess SKU revenue distribution | Top 20% contributes 31.42% | Add margin and inventory data |
| Medium | Evaluate promotional effectiveness | Observational AOV differences | Controlled discount experiment |

### Proposed 30/60/90-Day Plan

These are recommended actions for a business using similar analytics, not completed production interventions.

**Days 1–30 — Investigate**

- Validate purchasing event instrumentation.
- Review mobile checkout behavior.
- Identify key checkout failure categories.
- Assess available inventory and product-margin information.
- Confirm the objectives of discount programs.

**Days 31–60 — Design Improvements**

- Select a specific checkout-friction hypothesis.
- Define a controlled experiment.
- Establish primary conversion and guardrail metrics.
- Prepare improved product performance reporting.
- Specify promotional evaluation criteria.

**Days 61–90 — Evaluate**

- Review experimental results if a valid intervention has been tested.
- Compare conversion changes with uncertainty estimates.
- Assess revenue and margin implications.
- Investigate segment-specific results.
- Recommend further iteration based on the evidence.

### Business Decision Framework

Before implementing any change, stakeholders should establish:

1. **Problem:** What specific customer or operational issue is being addressed?
2. **Baseline:** Which current metrics define performance?
3. **Hypothesis:** Why might the intervention improve the outcome?
4. **Measurement:** What constitutes success?
5. **Validation:** How will a causal effect be evaluated?
6. **Decision:** What evidence is required to adopt, modify, or reject the change?

---

## ✅ Data Quality & Validation

### Validation Overview

This project documents **20 passing runtime checks** covering source integrity, relationships, query execution, and metric reconciliation.

### Verified Quality Summary

| Quality Indicator | Recorded Result |
|---|---:|
| Website Source Records | 25,000 |
| Order Source Records | 3,037 |
| Total Source Records | 28,037 |
| Missing Required Cells | 0 |
| Exact-Repeated Source Rows | 0 |
| Runtime Validation Checks | 20 |
| Recorded Runtime Status | Passed |

### Validation Coverage

**1. Source Schema Integrity**

Checks the required structure, data types, and value constraints of both datasets.

**2. Session Key Validation**

Requires unique session identifiers where declared as primary keys.

**3. Purchase-to-Cart Consistency**

Verifies that purchased sessions contain the expected cart indicator.

**4. Order Relationship Validation**

Checks one order record per purchased session under the dataset's contract.

**5. Cross-Table Consistency**

Verifies matching session date, device, and acquisition channel between associated records.

**6. SQL Execution**

Executes all four named analytical queries.

**7. Independent KPI Reconciliation**

Checks headline metrics, including sessions, carts, purchases, conversion, abandonment, revenue, and average order value.

**8. Product Concentration Reconciliation**

Independently checks the revenue share attributed to the top 20% of SKUs.

### Validation Results

| Evidence | Purpose |
|---|---|
| [validation.json](Results/validation.json) | Project runtime check results |
| [quality.json](Results/quality.json) | Source quality diagnostics |
| [manifest.json](Results/manifest.json) | Input, code, and output provenance |
| [query_plans.json](Results/query_plans.json) | SQLite execution plans |
| [additional_metrics.json](Results/additional_metrics.json) | Supplementary analytical outputs |

### Validation Boundary

Passing technical checks supports reproducible calculation and documented data integrity.

It does not prove the causes of cart abandonment, discount effectiveness, customer retention, profitability, or projected business impact.

---

## 📊 Business Intelligence & Dashboard Assets

The repository includes Power BI and Excel assets alongside the canonical SQL/Python reporting pipeline.

### Existing Assets

| Asset | Purpose | Location |
|---|---|---|
| Excel Analytical Model | Source-aligned summary workbook | [Excel Model](Excel/03_Ecommerce_Product_Analytics_Model.xlsx) |
| Power BI Workbook | Preserved legacy BI dashboard | [Power BI PBIX](Dashboard/Ecommerce_Product_Analytics.pbix) |
| Dashboard Documentation | Describes native report asset | [Dashboard README](Dashboard/README.md) |
| Funnel Image | Existing visualization asset | [Funnel Image](Images/ecommerce_funnel.png) |
| HTML Report | Canonical offline analytical report | [REPORT.html](REPORT.html) |

### Native Workbook Verification

The portfolio's native-file audit found that the original Ecommerce Power BI workbook uses a different source structure and data grain from the canonical web sessions and orders datasets.

Its embedded model contains customer, order, payment, product, and session-related structures that are not equivalent to the current canonical CSV inputs.

This distinction is documented rather than hidden.

### Verified Work

- Canonical SQL and Python metric reconciliation
- Corrected source-aligned Excel summaries
- Excel formula and recalculation evidence
- Native Power BI source inspection
- Documented workbook/source mismatches
- Legacy Power BI measure baselines and verification scripts

### Outstanding Native Verification

Full Power BI Desktop DAX execution, canonical model rebuilding, visual refresh, and page-by-page acceptance have not been claimed as completed.

The existing dashboard should therefore not be presented as proof that every canonical SQL/Python result is displayed accurately.

### Recommended Source-Aligned Dashboard Design

**Executive Overview**

Sessions, purchases, conversion, cart abandonment, recorded revenue, and average order value.

**Conversion Analysis**

Session and cart progression with breakdowns by device and acquisition channel.

**Product Performance**

Top SKUs, cumulative revenue, and revenue concentration.

**Promotional Analysis**

Average order values and unit counts by observed discount category.

**Data Quality**

Source counts, reconciliation checks, and refresh-validation status.

These are recommendations for a rebuilt, verified dashboard, not claims about the existing PBIX.

### Supporting Verification

[Dashboard Reconciliation](Docs/Dashboard_Reconciliation.md) | [Dashboard Field Mapping](Docs/Dashboard_Field_Mapping.md) | [Connection Guide](Docs/Connect_To_Dashboard.md) | [Native Verification Report](../verification/native/README.md)

---

## 📂 Project Structure

```text
03_Ecommerce_Product_Analytics/
│
├── Data/
│   ├── raw/
│   │   ├── web_sessions_raw.csv
│   │   └── orders_raw.csv
│   └── clean/
│       ├── web_sessions_clean.csv
│       └── orders_clean.csv
│
├── SQL/
│   └── analysis.sql
│
├── Python/
│   └── analysis.py
│
├── Excel/
│   └── 03_Ecommerce_Product_Analytics_Model.xlsx
│
├── Dashboard/
│   ├── Ecommerce_Product_Analytics.pbix
│   └── README.md
│
├── Images/
│   └── ecommerce_funnel.png
│
├── Results/
│   ├── summary.csv
│   ├── funnel_by_segment.csv
│   ├── sku_pareto.csv
│   ├── discount_association.csv
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

The project shares processing, validation, SQL execution, and reporting components with the parent portfolio.

---

## ▶️ Reproduce the Analysis

### Prerequisites

- Python 3.12
- Git
- Python package installation capability

The core analytical workflow does not require a paid BI license, cloud subscription, or externally hosted database.

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

### Step 4 — Run the Ecommerce Project

```bash
python -m portfolio.run --project 03_Ecommerce_Product_Analytics
```

The pipeline regenerates analytical outputs, local execution artifacts, validation records, and reporting evidence.

### Step 5 — Execute Automated Tests

```bash
python -m unittest discover -s tests -v
```

This runs the shared portfolio test suite, including data-integrity and numerical validation scenarios.

### Step 6 — Review Generated Results

Navigate to:

`03_Ecommerce_Product_Analytics/Results/`

Important outputs include:

- `summary.csv`
- `funnel_by_segment.csv`
- `sku_pareto.csv`
- `discount_association.csv`
- `additional_metrics.json`
- `validation.json`

### Step 7 — Open the Analytical Report

Open:

`03_Ecommerce_Product_Analytics/REPORT.html`

Download or clone the repository to view the offline HTML report locally.

GitHub's file viewer may display the HTML source rather than the rendered report.

### Reproducibility Guidance

The project maintains source and output manifests for traceability.

After any failed execution, do not rely on potentially stale result files. Correct the issue, rerun successfully, and review current validation records.

**Full Instructions:** [Portfolio Runbook](../docs/RUNBOOK.md)

---

## ⚠️ Limitations & Future Improvements

### Current Limitations

**1. Simulated Data**

The analyses represent supplied portfolio datasets rather than a real operational ecommerce business.

**2. Missing Customer Identifiers**

Stable customer IDs are unavailable.

Therefore, customer RFM, repeat-purchase frequency, and true customer lifetime value cannot be calculated reliably.

**3. Simplified Order Grain**

The dataset represents one order per purchased session and one SKU per supplied order row. Real ecommerce data may have multiple orders, order lines, and partial transactions.

**4. Incomplete Checkout Instrumentation**

The data provide cart and purchase indicators but not a complete sequence of checkout events or reasons for nonpurchase.

**5. No Causal Evidence for Discount Effects**

Discount assignments are observational.

**6. Revenue Definition Limitations**

Refunds, recognized revenue, taxes, shipping, margins, and currency codes are not independently established.

**7. No Proven Cart-Recovery Revenue**

Recorded abandoned carts cannot automatically be treated as recoverable revenue.

**8. Native Power BI Source Mismatch**

The preserved PBIX uses different underlying datasets and requires separate canonical model verification.

### Potential Future Enhancements

- Customer-level identity and purchase history
- RFM segmentation after customer IDs become available
- Checkout-stage event instrumentation
- Cart abandonment by checkout step
- Product-level contribution margin
- Inventory and stockout analysis
- Refund and return-rate reporting
- Campaign acquisition cost integration
- Controlled mobile-checkout experimentation
- Promotion effectiveness testing
- Cohort-based purchasing analysis
- Validated source-aligned Power BI dashboards
- Automated Power BI model acceptance

These are future analytical opportunities, not completed implementation claims.

---

## 🧠 Project Takeaways

### Technical Skills Demonstrated

- SQL-based ecommerce analysis
- Relational data modeling and joins
- Window functions and ranking
- Cumulative revenue calculations
- Python data validation
- Numerical metric reconciliation
- Conversion and funnel analytics
- Product segmentation
- Revenue analysis
- Data quality controls
- Automated testing
- Reproducible reporting

### Business Skills Demonstrated

- Translating business questions into defined KPIs
- Evaluating purchasing performance
- Identifying high-priority segments for investigation
- Interpreting customer-session behavior
- Assessing product revenue distribution
- Recognizing observational limitations
- Communicating analytical findings clearly
- Developing testable business recommendations

### Final Conclusion

The Ecommerce Product Analytics project identifies three central findings:

**First**, 12.15% of recorded website sessions result in purchases, while 64.24% of sessions reaching cart activity do not complete a purchase.

**Second**, device and acquisition-channel performance differs, with Mobile Paid Social exhibiting relatively low observed conversion and comparatively high cart abandonment.

**Third**, the highest-ranked 20% of product SKUs contribute 31.42% of recorded revenue, indicating a broader revenue distribution than a strong 80/20 concentration pattern.

These findings provide direction for checkout investigation, mobile experience research, and merchandising analysis.

The results are supported by reproducible SQL, independent Python checks, and documented source contracts.

**The central lesson is that valuable ecommerce analytics requires more than finding low conversion rates. It requires understanding measurement definitions, tracing the evidence, recognizing limitations, and translating results into responsible business decisions.**

---

## 📚 Supporting Documentation & Evidence

| Resource | Description |
|---|---|
| [Data Dictionary](Docs/Data_Dictionary.md) | Source schemas and data contracts |
| [KPI Lineage](Docs/KPI_Lineage.md) | Metric calculations and business definitions |
| [SQL Analysis](SQL/analysis.sql) | Executable analytical queries |
| [Python Analysis](Python/analysis.py) | Project execution entry point |
| [Summary Results](Results/summary.csv) | Overall ecommerce KPIs |
| [Segment Funnel Results](Results/funnel_by_segment.csv) | Conversion and abandonment by segment |
| [SKU Pareto Analysis](Results/sku_pareto.csv) | Product revenue rankings |
| [Discount Analysis](Results/discount_association.csv) | Observed promotional comparisons |
| [Additional Metrics](Results/additional_metrics.json) | Top-SKU concentration and RFM status |
| [Quality Evidence](Results/quality.json) | Source quality diagnostics |
| [Validation Evidence](Results/validation.json) | Runtime checks and results |
| [Offline Report](REPORT.html) | Canonical analytical report |
| [Native Workbook Verification](../verification/native/README.md) | Excel and Power BI verification status |

---

## 👨‍💻 About the Analyst

**Jamie Christian**

Data Analytics | Business Intelligence | SQL | Python | Product Analytics

I focus on transforming data into reliable business insights, identifying performance patterns, validating analytical outputs, and communicating findings that support decision-making.

My professional interests include Data Analytics, Business Intelligence, Product Analytics, Customer Behavior, Revenue Reporting, and Business Operations.

📧 [Email](mailto:Jamiechristian331@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/jamiechristian2/)  
💻 [GitHub](https://github.com/JamieChristian22)

### 🔗 Explore More Projects

[⬅️ Back to Main Data Analyst Portfolio](../README.md)

[🧪 Previous Project: A/B Testing & Feature Impact](../02_AB_Test_Feature_Impact/README.md)

[📦 Next Project: Marketplace Revenue & Seller Analytics](../04_Amazon_Marketplace_Analytics/README.md)

---

**🛒 Ecommerce Product Analytics | Built by Jamie Christian**

*SQL-driven analysis. Python-validated metrics. Actionable business insights. Reproducible evidence.*
