
# 📦 Amazon Marketplace Analytics | Revenue, Seller Performance & Data Quality

### SQL • Python • Marketplace Analytics • Financial Reconciliation • Business Intelligence

**An end-to-end marketplace analytics case study examining recorded sales performance, product categories, seller revenue concentration, inventory-status associations, and financial data quality through reproducible SQL and Python analysis.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Power BI](https://img.shields.io/badge/Power_BI-Native_Asset-F2C811)
![Analytics](https://img.shields.io/badge/Marketplace-Analytics-blueviolet)
![Validation](https://img.shields.io/badge/Validation-19%2F19-success)
![Dataset](https://img.shields.io/badge/Dataset-Simulated-orange)

**Analyst:** Jamie Christian  
**Project:** 04 — Amazon Marketplace Analytics  
**Portfolio:** [Data Analyst Portfolio](../README.md)  
**LinkedIn:** [Jamie Christian](https://www.linkedin.com/in/jamiechristian2/)

---

## 📌 Executive Summary

This project analyzes a simulated Amazon-style ecommerce marketplace to understand sales performance, seller revenue concentration, product category contributions, inventory-status associations, and financial data inconsistencies.

Using **24,000 sales records and 1,800 product listings**, the project applies SQL, Python, relational data validation, and analytical reporting to transform source datasets into traceable business metrics.

Unlike a traditional sales dashboard that focuses exclusively on revenue totals, this case study emphasizes **financial reconciliation, source-data reliability, and responsible business interpretation**.

The analysis examines five major business questions:

1. How much revenue is recorded across the marketplace dataset?
2. Which product categories contribute the most recorded revenue?
3. How concentrated is revenue among individual sellers?
4. What discrepancies exist between recorded revenue and calculated price multiplied by units?
5. What can current stock-status data reveal, and what additional information is required before making inventory decisions?

### Key Results

| Business Metric | Verified Result |
|---|---:|
| 📦 Product Listings | 1,800 |
| 🛒 Sales Records | 24,000 |
| 📊 Units Recorded | 48,063 |
| 👥 Distinct Sellers | 316 |
| 💰 Recorded Revenue | 1,830,085.36 |
| 🧮 Price × Units Total | 1,901,153.19 |
| ⚠️ Revenue Discrepancy Rows | 9,019 |
| 📈 Top 10 Sellers' Revenue Share | 8.44% |
| 📉 Seller Concentration HHI | 42.39 |
| ✅ Runtime Validation Checks | 19 passed |

**Data disclosure:** The project uses supplied simulated portfolio datasets. Despite the Amazon Marketplace project title, no Amazon transaction records, verified company performance, or actual marketplace outcomes are claimed.

Revenue is expressed in unspecified dataset currency units.

### Primary Findings

**1. Revenue reconciliation is the most important data-quality issue.**

Recorded revenue totals 1,830,085.36, while multiplying recorded unit prices by units sold produces 1,901,153.19.

The difference between these totals is **71,067.83**, and 9,019 sales rows have individual discrepancies exceeding the documented tolerance.

Because the data do not provide discount, tax, fee, or accounting rules explaining these differences, they must remain unresolved until the underlying business definitions can be confirmed.

**2. Seller revenue is distributed across a broad seller population.**

The ten highest-revenue sellers contribute approximately 8.44% of recorded revenue.

The seller concentration calculation produces an HHI of approximately 42.39 on the standard 0–10,000 scale.

**3. Home and Electronics lead recorded category revenue.**

Home contributes 416,940.49, followed closely by Electronics at 415,820.13.

**4. Stock-status comparisons require careful interpretation.**

The data include an undated stock-status snapshot, preventing reliable conclusions about historical stockouts or lost sales.

### Business Conclusion

The strongest immediate recommendation is to **investigate and resolve revenue-definition inconsistencies before relying on the source for financial reporting**.

The seller, category, and inventory analyses provide additional insight into marketplace performance, but their interpretation must respect the underlying data limitations.

---

## 📚 Table of Contents

1. [Business Problem](#-business-problem)
2. [Dataset Overview](#-dataset-overview)
3. [Technical Stack](#-technical-stack)
4. [Analytical Workflow](#-end-to-end-analytical-workflow)
5. [KPI Definitions](#-kpi-definitions--business-rules)
6. [Analysis 1: Revenue Performance](#-analysis-1-marketplace-revenue-performance)
7. [Analysis 2: Revenue Reconciliation](#-analysis-2-financial-revenue-reconciliation)
8. [Analysis 3: Seller Concentration](#-analysis-3-seller-performance--revenue-concentration)
9. [Analysis 4: Category Performance](#-analysis-4-product-category-performance)
10. [Analysis 5: Inventory Associations](#-analysis-5-inventory--stock-status-associations)
11. [SQL Implementation](#-sql-implementation)
12. [Business Recommendations](#-business-recommendations)
13. [Data Quality & Validation](#-data-quality--validation)
14. [Business Intelligence Assets](#-business-intelligence--dashboard-assets)
15. [Project Structure](#-project-structure)
16. [Reproduction Guide](#-reproduce-the-analysis)
17. [Limitations](#-limitations--future-improvements)
18. [Project Takeaways](#-project-takeaways)

---

## 🎯 Business Problem

### Business Context

Online marketplaces connect multiple sellers with customers across different product categories.

Managing marketplace performance requires more than tracking sales totals.

Business teams need reliable information about:

- Recorded revenue
- Product performance
- Seller contributions
- Marketplace revenue concentration
- Sales volumes
- Listing availability
- Inventory relationships
- Financial reconciliation
- Data quality and reporting integrity

Incorrect sales definitions or unexplained revenue discrepancies can undermine financial reporting and lead to unreliable operational decisions.

### Business Scenario

A simulated marketplace operates across multiple product categories and contains hundreds of independent sellers.

Its analytics team receives product listing data and sales records.

The business needs to evaluate marketplace performance and determine whether the available financial and operational metrics are suitable for decision-making.

### Primary Business Question

**How is recorded marketplace revenue distributed across sellers and product categories, and what data-quality issues prevent confident financial and operational reporting?**

### Business Objectives

| Objective | Analytical Focus | Decision Support |
|---|---|---|
| Measure Revenue | Recorded sales revenue | Establish commercial baseline |
| Evaluate Seller Performance | Seller-level revenue | Understand revenue distribution |
| Analyze Categories | Revenue and units by category | Support merchandising review |
| Reconcile Financial Data | Recorded revenue vs. price × units | Investigate reporting discrepancies |
| Examine Availability | Stock snapshot and listing performance | Identify further inventory questions |
| Validate Data Integrity | Source contracts and relationships | Increase reporting reliability |

### Project Goal

Develop a reproducible marketplace analytics framework that produces verifiable performance metrics, detects financial inconsistencies, and translates observations into responsible business recommendations.

---

## 🗄️ Dataset Overview

The project uses two related simulated datasets containing **25,800 source records**.

### Source Tables

| Dataset | Records | Purpose |
|---|---:|---|
| `listings_raw.csv` | 1,800 | Product listing, seller, category, price, rating, and stock attributes |
| `sales_raw.csv` | 24,000 | Recorded sale activity, units, revenue, and associated listing information |
| **Total** | **25,800** | **Two analytical source tables** |

### Dataset 1 — Listings

Contains product-level attributes for the marketplace listings.

| Column | Data Type | Description |
|---|---|---|
| `listing_id` | Integer | Unique product listing identifier |
| `seller_id` | Integer | Seller associated with the listing |
| `category` | Text | Product category |
| `price` | Numeric | Supplied listing price |
| `rating` | Numeric | Rating on a 0–5 scale |
| `in_stock` | Binary | Undated stock-status snapshot |

**Analytical Uses**

- Product category segmentation
- Seller-to-listing relationships
- Listing-price bands
- Stock-status comparisons
- Product-level revenue association

### Dataset 2 — Sales

Contains recorded sale activity linked to marketplace listings.

| Column | Data Type | Description |
|---|---|---|
| `sale_date` | Date | Recorded sale date |
| `listing_id` | Integer | Associated product listing |
| `units_sold` | Integer | Units recorded in the sale row |
| `seller_id` | Integer | Seller identifier |
| `price` | Numeric | Supplied unit price |
| `rating` | Numeric | Recorded rating |
| `in_stock` | Binary | Supplied stock snapshot |
| `category` | Text | Product category |
| `revenue` | Numeric | Recorded revenue value |

### Data Relationship

The datasets connect through `listing_id`.

**Listings (1) → (Many) Sales Records**

The analytical workflow checks listing references and the consistency of shared seller, category, price, rating, and stock fields.

### Data Grain

**Listing Grain**

One record per unique `listing_id`.

**Sales Grain**

One recorded sale row without a supplied unique sale identifier.

**Seller Grain**

Multiple listings and sales records may belong to the same `seller_id`.

### Important Grain Limitations

A sales row is not necessarily a complete customer order.

The dataset does not provide:

- Unique order identifiers
- Customer identifiers
- Transaction fees
- Verified platform commission rates
- Refund histories
- Full inventory movement histories

Consequently, the project avoids interpreting sales-row counts as order counts or recorded revenue as platform commission income.

### Supporting Documentation

[📘 Data Dictionary](Docs/Data_Dictionary.md) | [📂 Raw Data](Data/raw) | [📂 Cleaned Data](Data/clean)

---

## 🛠️ Technical Stack

| Category | Technology | Application |
|---|---|---|
| Programming | Python 3.12 | Data processing and analytical reconciliation |
| Query Language | SQL | Marketplace performance queries |
| Database | SQLite | Relational data analysis |
| Data Analysis | pandas | Independent KPI verification |
| Data Cleaning | Python | Type normalization and validation |
| Financial Analytics | SQL and Python | Revenue comparison and discrepancy detection |
| Concentration Analysis | SQL window functions | Seller ranking and revenue share |
| Business Intelligence | Power BI | Legacy native workbook and verification preparation |
| Spreadsheet Reporting | Excel | Corrected source-aligned analytical model |
| Reporting | HTML and CSV | Offline reports and results |
| Automated Testing | Python unittest | Data contract and integration checks |
| Data Traceability | SHA-256 | Source and output evidence |
| Version Control | Git and GitHub | Repository management |

### SQL Competencies Demonstrated

- Relational joins
- Aggregation functions
- Common Table Expressions
- Window functions
- `ROW_NUMBER()`
- Seller ranking
- Conditional categorization
- `CASE WHEN`
- `LEFT JOIN`
- `COALESCE`
- `NULLIF`
- Data reconciliation
- Grouped performance reporting

### Python Competencies Demonstrated

- CSV processing
- Type and range validation
- Relationship verification
- Independent metric calculation
- Source-quality diagnostics
- Automated analytical checks
- Reproducible report generation
- Data integrity monitoring

### Business Analytics Competencies

- Financial metric reconciliation
- Marketplace reporting
- Seller performance analysis
- Revenue concentration
- Category performance
- Inventory-status diagnostics
- Business rule documentation
- Data governance and analytical judgment

---

## 🔄 End-to-End Analytical Workflow

The project follows a reproducible process connecting raw records to business reporting.

### Phase 1 — Define Business Requirements

Identify reporting objectives, relevant business entities, required metrics, and their limitations.

**Deliverable:** KPI definitions and business questions.

### Phase 2 — Inspect Source Data

Review:

- Listing identifiers
- Seller identifiers
- Product categories
- Sale records
- Prices
- Quantities
- Recorded revenue
- Stock indicators
- Data relationships

**Deliverable:** Data dictionary and source contracts.

### Phase 3 — Validate & Transform

Apply documented data normalization while preserving source values and anomalies.

Validation includes:

- Required columns
- Data types
- Numeric ranges
- Unique declared listing keys
- Relationship integrity
- Shared-field consistency
- Null checks
- Duplicate diagnostics

**Deliverable:** Clean analytical datasets and quality records.

### Phase 4 — SQL Analytics

Run named queries for:

1. Marketplace revenue summary
2. Seller concentration
3. Product category performance
4. Inventory-status associations

**Deliverable:** Saved SQL result tables.

### Phase 5 — Python Reconciliation

Independently verify selected SQL outputs and headline financial metrics.

**Deliverable:** Validation records.

### Phase 6 — Business Interpretation

Evaluate the commercial significance of results while accounting for missing transaction and inventory context.

**Deliverable:** Findings and recommended investigations.

### Phase 7 — Reporting & Evidence

Generate result CSVs, data-quality reports, query plans, hashes, and an offline analytical report.

**Deliverable:** Reproducible technical and analytical evidence.

### Pipeline Architecture

**Raw Listings & Sales → Data Contracts → Clean Tables → SQLite Analysis → Python Reconciliation → Quality Evidence → Reporting → Business Recommendations**

---

## 📐 KPI Definitions & Business Rules

| KPI | Calculation | Interpretation |
|---|---|---|
| Sales Records | Count of sales rows | Not necessarily customer orders |
| Units Recorded | Sum of `units_sold` | Total recorded unit activity |
| Recorded Revenue | Sum of `revenue` | Source-defined revenue |
| Calculated Price × Units | Sum of `price × units_sold` | Independent arithmetic comparison |
| Revenue Discrepancy Rows | Count where absolute row difference exceeds 0.011 | Records needing explanation |
| Distinct Sellers | Unique seller IDs in sales | Sellers represented in recorded activity |
| Seller Revenue Share | Seller revenue ÷ total recorded revenue | Individual seller contribution |
| Top 10 Seller Share | Combined revenue of ten highest sellers ÷ total recorded revenue | Revenue concentration |
| Seller HHI | 10,000 × sum of squared seller revenue shares | Descriptive concentration index |
| Category Revenue | Sum of recorded revenue by category | Category contribution |
| Mean Listing Revenue | Mean recorded revenue across listings in a group | Descriptive listing comparison |

### Financial Definition Boundaries

**Recorded Revenue**

Uses `sales.revenue` exactly as provided.

**Price × Units**

Represents a separate arithmetic calculation using recorded unit prices and quantities.

**Revenue Discrepancy**

Indicates that two source-related calculations differ beyond a small tolerance.

It does not automatically establish an accounting error, discount, commission, or missing payment.

**Marketplace Commission Revenue**

Cannot be calculated reliably because commission rules and fee structures are unavailable.

**Gross Merchandise Value**

Not independently established by the source documentation.

**Order Count**

Cannot be derived reliably because order identifiers are absent.

### KPI Documentation

[📘 KPI Lineage](Docs/KPI_Lineage.md)

---

## 💰 Analysis 1: Marketplace Revenue Performance

### Business Question

What is the recorded commercial activity across the supplied marketplace sales data?

### Verified Summary

| Metric | Result |
|---|---:|
| Sales Records | 24,000 |
| Units Recorded | 48,063 |
| Recorded Revenue | 1,830,085.36 |
| Calculated Price × Units | 1,901,153.19 |
| Sellers | 316 |
| Listings | 1,800 |

### Finding 1 — The Dataset Records Substantial Sales Activity

The supplied source contains 24,000 sales rows representing 48,063 recorded units.

The aggregate recorded revenue is **1,830,085.36**.

This forms the source-defined revenue baseline for seller and category analysis.

### Finding 2 — Revenue Totals Depend on Business Definitions

The source provides both `revenue` and sufficient data to calculate `price × units_sold`.

These values do not reconcile to the same total.

The analysis therefore preserves the recorded revenue metric for descriptive reporting while separately identifying the discrepancy.

### Finding 3 — Revenue Must Not Be Relabeled Without Evidence

Although the project models marketplace activity, the source does not establish whether recorded revenue represents gross merchandise sales, net merchandise revenue, platform fees, or another accounting category.

It would be incorrect to relabel the figure as verified Amazon revenue or platform profit.

### Business Interpretation

The dataset supports marketplace performance reporting using supplied revenue definitions.

However, financial reconciliation must be resolved before the results can be used as an authoritative financial source.

**Evidence:** [Marketplace Summary](Results/summary.csv)

---

## 🧮 Analysis 2: Financial Revenue Reconciliation

### Business Question

Why does recorded revenue differ from the arithmetic result of price multiplied by recorded units?

### Verified Reconciliation

| Financial Measure | Result |
|---|---:|
| Recorded Revenue | 1,830,085.36 |
| Calculated Price × Units | 1,901,153.19 |
| Difference in Totals | 71,067.83 |
| Sales Records | 24,000 |
| Rows Exceeding Difference Tolerance | 9,019 |
| Share of Rows Flagged | 37.58% |

### Reconciliation Formula

**Calculated Revenue per Row = Price × Units Sold**

**Absolute Difference = |Recorded Revenue − Calculated Revenue|**

A sales row is flagged when:

`ABS(revenue - price * units_sold) > 0.011`

This tolerance is slightly greater than one cent in the dataset's unspecified currency units.

### Finding 1 — Material Reconciliation Differences Exist

The arithmetic total exceeds recorded revenue by **71,067.83**.

This does not automatically mean revenue is understated.

The two metrics may have different business definitions or source-generation rules.

### Finding 2 — More Than One-Third of Sales Rows Are Flagged

Of 24,000 sales records, 9,019 exceed the discrepancy threshold.

This indicates that the difference is not confined to one isolated row.

### Finding 3 — The Root Cause Is Not Established

Possible explanations to investigate include:

- Discount treatment
- Net versus gross sales definitions
- Tax or shipping treatment
- Seller-related fees
- Refund adjustments
- Price snapshot timing
- Source-generation logic

These are hypotheses requiring external business rules or source-owner confirmation.

The repository does not establish which explanation is correct.

### Finding 4 — Preserving Both Values Protects Analytical Integrity

The pipeline retains both recorded and arithmetic revenue values.

It does not replace recorded revenue with a calculated value or silently force the figures to match.

This preserves the evidence needed for subsequent investigation.

### Financial Reconciliation Investigation

A responsible workflow would include:

**Step 1 — Confirm Metric Definitions**

Identify what each financial field is intended to represent.

**Step 2 — Inspect Source Lineage**

Determine how prices, quantities, and revenue were generated.

**Step 3 — Investigate Flagged Records**

Evaluate discrepancy patterns by date, listing, seller, and category.

**Step 4 — Obtain Missing Business Rules**

Request relevant fee, discount, refund, and pricing documentation.

**Step 5 — Establish a Reconciliation Policy**

Define expected calculations, acceptable rounding tolerances, and documented exceptions.

**Step 6 — Implement Regression Checks**

Automate reconciliations only after the approved business definition is known.

### Business Recommendation

**Treat source revenue definitions as unresolved for authoritative financial use until the discrepancies are explained.**

Descriptive portfolio analysis can proceed with explicit labeling, but the results should not be presented as audited financial reporting.

**Evidence:** [Revenue Summary](Results/summary.csv) | [Data Quality Report](Results/quality.json)

---

## 👥 Analysis 3: Seller Performance & Revenue Concentration

### Business Question

How much recorded revenue comes from the highest-performing sellers, and how concentrated is marketplace activity?

### Seller Overview

| Metric | Verified Result |
|---|---:|
| Distinct Sellers | 316 |
| Highest-Revenue Seller | Seller 223 |
| Highest Seller Revenue | 19,882.06 |
| Highest Seller Share | 1.09% |
| Top 10 Seller Revenue Share | 8.44% |
| Seller HHI | 42.39 |

### Top 10 Sellers by Recorded Revenue

| Rank | Seller ID | Recorded Revenue |
|---|---|---:|
| 1 | 223 | 19,882.06 |
| 2 | 264 | 17,618.46 |
| 3 | 247 | 15,950.69 |
| 4 | 114 | 15,485.38 |
| 5 | 307 | 15,376.04 |
| 6 | 269 | 14,661.24 |
| 7 | 86 | 14,459.63 |
| 8 | 283 | 13,731.95 |
| 9 | 61 | 13,720.32 |
| 10 | 218 | 13,522.13 |

### Finding 1 — Seller 223 Is the Highest-Revenue Seller

Seller 223 generates 19,882.06 in recorded revenue.

This represents approximately **1.09% of total recorded marketplace revenue**.

The seller is the highest-ranked contributor, but not a dominant revenue source within the supplied data.

### Finding 2 — Top Sellers Contribute a Limited Share

The ten highest-revenue sellers collectively account for approximately **8.44%** of recorded revenue.

This suggests that revenue is broadly distributed across participating sellers rather than concentrated primarily in a small top-ten group.

### Finding 3 — HHI Supports a Low-Concentration Description

The Herfindahl-Hirschman Index summarizes concentration by squaring individual revenue shares and summing them.

**Formula:**

`Seller HHI = 10,000 × SUM(seller_revenue_share²)`

**Calculated HHI: 42.39**

This is low on the conventional 0–10,000 index scale.

However, the result is a concentration measure for the supplied seller revenue distribution. It is not a regulatory market-definition analysis or a determination of competition.

### Finding 4 — Revenue Ranking Is Not Profitability Ranking

A seller generating high revenue is not necessarily producing:

- High gross margin
- High platform commission income
- Strong customer satisfaction
- Low return rates
- Sustainable long-term performance

The data do not include sufficient information to evaluate those characteristics.

### Business Recommendation

Use seller revenue concentration to understand exposure and identify sellers requiring deeper review.

Future reporting should incorporate historical revenue, seller retention, fee structures, profitability, and category participation before making resource-allocation decisions.

**Evidence:** [Seller Concentration](Results/seller_concentration.csv) | [Additional Metrics](Results/additional_metrics.json)

---

## 🏷️ Analysis 4: Product Category Performance

### Business Question

Which product categories contribute the most recorded sales revenue and units?

### Verified Category Results

| Category | Recorded Revenue | Units | Sales Rows |
|---|---:|---:|---:|
| 🏠 Home | 416,940.49 | 10,548 | 5,268 |
| 💻 Electronics | 415,820.13 | 10,891 | 5,404 |
| 🏅 Sports | 388,528.46 | 10,387 | 5,203 |
| 💄 Beauty | 330,135.80 | 8,639 | 4,324 |
| 🧸 Toys | 278,660.48 | 7,598 | 3,801 |
| **Total** | **1,830,085.36** | **48,063** | **24,000** |

### Finding 1 — Home Leads Recorded Revenue

Home generates **416,940.49**, the highest category revenue in the supplied dataset.

Its performance makes it a reasonable candidate for deeper merchandising and seller analysis.

### Finding 2 — Electronics Leads Recorded Unit Volume

Electronics accounts for 10,891 units, more than any other listed category.

However, Home generates slightly higher recorded revenue.

This illustrates why unit volume and revenue should be evaluated as distinct performance indicators.

### Finding 3 — Sports Is Another Major Revenue Contributor

Sports generates 388,528.46, ranking third in recorded revenue.

It also represents more than 10,000 recorded units.

### Finding 4 — Category Revenue Alone Is Insufficient for Inventory Decisions

Revenue performance does not establish:

- Product profitability
- Inventory cost
- Seller fees
- Customer return rates
- Stockout frequency
- Demand seasonality
- Marketing investment

Category rankings should therefore serve as the beginning of operational investigation, not the final basis for investment.

### Business Recommendations

**Home:** Investigate category profitability and seller contribution.

**Electronics:** Compare revenue, unit volumes, product availability, and margin characteristics.

**Sports:** Evaluate whether revenue is concentrated within a small group of listings or distributed broadly.

**Beauty and Toys:** Review product mix, listing availability, and underlying demand before proposing assortment changes.

**Evidence:** [Category Performance](Results/category_performance.csv)

---

## 📦 Analysis 5: Inventory & Stock-Status Associations

### Business Question

How does recorded listing revenue differ across product categories, price bands, and supplied stock-status flags?

### Available Stock Information

The listing dataset includes an `in_stock` indicator.

However, the value represents an **undated stock snapshot**, not a history of inventory levels at the moment each sale occurred.

### Analytical Approach

The SQL query:

1. Aggregates recorded revenue by listing.
2. Joins the results to the complete listing population.
3. Groups listings by category, price band, and stock flag.
4. Includes zero-sale listings using `COALESCE`.
5. Calculates average recorded revenue for each group.

### Price Bands

| Price Band | Definition |
|---|---|
| Under 50 | Listing price below 50 |
| 50 to 99.99 | Listing price at least 50 and below 100 |
| 100+ | Listing price at least 100 |

### Selected Verified Results

| Category | Price Band | Stock Flag | Listings | Mean Recorded Revenue |
|---|---|---|---:|---:|
| Beauty | 50–99.99 | Out of Stock | 17 | 0.00 |
| Beauty | 50–99.99 | In Stock | 91 | 1,819.68 |
| Electronics | 50–99.99 | Out of Stock | 15 | 0.00 |
| Electronics | 50–99.99 | In Stock | 109 | 1,951.91 |
| Home | 50–99.99 | In Stock | 106 | 1,927.04 |
| Sports | 50–99.99 | In Stock | 95 | 1,846.42 |
| Toys | 50–99.99 | In Stock | 74 | 1,860.65 |

### Finding 1 — Stock-Flag Groups Differ Descriptively

The output shows differences in mean recorded revenue between groups of listings based on the supplied stock snapshot.

These are descriptive associations.

### Finding 2 — Historical Availability Cannot Be Established

The quality report flags 2,936 sales rows associated with listings whose supplied stock field indicates out of stock.

This does not prove those sales occurred while the listings were unavailable.

The snapshot could have been recorded after the transactions, and no historical inventory timestamps are provided.

### Finding 3 — Lost-Sales Estimates Are Unsupported

A zero-revenue listing or out-of-stock indicator cannot automatically be converted into lost sales.

Doing so would require additional information such as:

- Historical inventory levels
- Dates of stockout events
- Customer demand during unavailable periods
- Product views and conversion opportunities
- Restock dates
- Substitution behavior

### Business Recommendation

Use the stock-status analysis as a data-quality and operational diagnostic.

Obtain time-stamped inventory history before estimating the financial effects of stockouts or designing inventory replenishment recommendations.

**Evidence:** [Stock Status Associations](Results/stock_status_association.csv)

---

## 💻 SQL Implementation

The project contains four executable, named SQLite analytical queries in `SQL/analysis.sql`.

### Query 1 — Marketplace Revenue Summary

```sql
SELECT
    COUNT(*) AS sales_rows,
    SUM(units_sold) AS units,
    SUM(revenue) AS recorded_revenue,

    SUM(price * units_sold)
        AS price_times_units,

    SUM(
        ABS(revenue - price * units_sold) > 0.011
    ) AS revenue_discrepancy_rows,

    COUNT(DISTINCT seller_id) AS sellers

FROM sales_clean;
```

**SQL Concepts Demonstrated**

- Aggregate functions
- Distinct counts
- Arithmetic expressions
- Boolean conditional counts
- Financial reconciliation

**Business Application**

Creates the central marketplace financial summary while identifying records that do not satisfy the arithmetic revenue comparison.

### Query 2 — Seller Revenue Concentration

```sql
WITH seller AS (
    SELECT
        seller_id,
        SUM(revenue) AS revenue

    FROM sales_clean

    GROUP BY seller_id
),

ranked AS (
    SELECT
        *,

        ROW_NUMBER() OVER (
            ORDER BY revenue DESC, seller_id
        ) AS rank,

        SUM(revenue) OVER ()
            AS total_revenue

    FROM seller
)

SELECT
    *,

    revenue / NULLIF(total_revenue, 0)
        AS revenue_share

FROM ranked

ORDER BY rank;
```

**SQL Concepts Demonstrated**

- Common Table Expressions
- `ROW_NUMBER()`
- Window aggregation
- Deterministic ranking
- Seller-level grouping
- Safe division

**Business Application**

Calculates individual seller contributions and supports concentration analysis.

### Query 3 — Product Category Performance

```sql
SELECT
    category,

    SUM(revenue)
        AS recorded_revenue,

    SUM(units_sold)
        AS units,

    COUNT(*)
        AS sales_rows

FROM sales_clean

GROUP BY category

ORDER BY recorded_revenue DESC;
```

**SQL Concepts Demonstrated**

- Grouped aggregation
- Category segmentation
- Revenue and unit comparisons
- Ranking through sorting

**Business Application**

Summarizes recorded sales performance across marketplace product categories.

### Query 4 — Stock-Status Associations

```sql
WITH r AS (
    SELECT
        listing_id,
        SUM(revenue) AS revenue

    FROM sales_clean

    GROUP BY listing_id
)

SELECT
    l.category,

    CASE
        WHEN l.price < 50
            THEN 'Under 50'
        WHEN l.price < 100
            THEN '50 to 99.99'
        ELSE '100+'
    END AS price_band,

    l.in_stock,

    COUNT(*) AS listings,

    AVG(
        COALESCE(r.revenue, 0)
    ) AS mean_recorded_revenue

FROM listings_clean l

LEFT JOIN r
    USING(listing_id)

GROUP BY
    l.category,
    price_band,
    l.in_stock

ORDER BY
    l.category,
    price_band,
    l.in_stock;
```

**SQL Concepts Demonstrated**

- Common Table Expressions
- `LEFT JOIN`
- Conditional classification
- `CASE WHEN`
- `COALESCE`
- Grouped averages
- Inclusion of zero-sale listings

**Business Application**

Creates an inventory-related descriptive summary while maintaining the complete listing population.

### SQL Design Principles

The analysis emphasizes:

- Consistent metric definitions
- Correct entity relationships
- Explicit denominators
- Safe arithmetic
- Reproducible query results
- Traceable business logic
- Independent numerical reconciliation

**Complete SQL Source:** [SQL/analysis.sql](SQL/analysis.sql)

---

## 🐍 Python Analysis & Metric Reconciliation

Python supports the project by validating inputs, reproducing selected calculations independently, and generating quality and reporting evidence.

### Data Processing

The workflow validates:

- Required source fields
- Supported data types
- Numeric ranges
- Listing keys
- Referential integrity
- Shared-field consistency

### Independent KPI Reconciliation

The Python validation checks selected headline metrics, including:

- Sales-record counts
- Recorded units
- Revenue totals
- Price-times-units calculations
- Discrepancy counts
- Distinct seller counts
- Top-ten seller revenue concentration

### Seller Concentration Metric

The project also calculates a Herfindahl-Hirschman Index from seller revenue shares.

**Formula:**

`HHI = 10,000 × SUM((seller_revenue / total_revenue)²)`

**Verified Result: 42.3946**

The HHI is descriptive for the supplied seller-revenue population.

### Reporting Outputs

Python supports the generation and verification of:

- Analytical CSV files
- Data quality diagnostics
- Validation records
- Additional metrics
- Query execution plans
- Source/output evidence manifests
- Offline HTML reports

**Supporting Code:** [Python Project Entry Point](Python/analysis.py) | [Additional Metrics](Results/additional_metrics.json)

---

## 💡 Business Recommendations

The strongest recommendations arise from the verified financial and operational data limitations.

### Recommendation Matrix

| Priority | Recommendation | Supporting Evidence | Proposed Validation |
|---|---|---|---|
| Critical | Reconcile recorded revenue definitions | 9,019 flagged rows | Source-owner and accounting-rule investigation |
| High | Establish trustworthy financial reporting rules | 71,067.83 aggregate difference | Approved metric specifications |
| High | Investigate inventory snapshot inconsistencies | 2,936 flagged sales rows | Historical stock records |
| Medium | Review seller revenue distribution | Top 10 share of 8.44% | Seller cohorts and historical reporting |
| Medium | Examine category economics | Home and Electronics lead revenue | Add margin and cost data |
| Medium | Improve transaction traceability | Missing unique sale/order IDs | Strengthen source event and transaction design |

### Proposed 30/60/90-Day Analytical Plan

These are recommended future business activities, not completed interventions.

**Days 1–30 — Investigate Financial Definitions**

- Review recorded revenue calculations.
- Inspect flagged rows.
- Confirm pricing and discount rules.
- Identify relevant source owners.
- Validate listing and seller relationships.
- Document unresolved reporting assumptions.

**Days 31–60 — Improve Data Quality**

- Establish an approved revenue reconciliation policy.
- Add stable transaction identifiers to future source data.
- Define acceptable discrepancies and exceptions.
- Develop time-aware inventory reporting requirements.
- Improve metric ownership and documentation.

**Days 61–90 — Strengthen Marketplace Reporting**

- Build source-aligned financial dashboards.
- Add historical seller performance.
- Integrate category profitability where available.
- Track reconciliation exceptions over time.
- Validate reporting output against approved business definitions.

### Decision Framework

Before using the results for operational or financial decisions, stakeholders should confirm:

**Metric Definition → Source Accuracy → Relationship Integrity → Reconciliation → Business Context → Approved Reporting**

---

## ✅ Data Quality & Validation

### Quality Assurance Overview

The project documents **19 passing runtime validation checks** across source contracts, relationships, SQL execution, and independent metric reconciliation.

### Verified Quality Results

| Quality Indicator | Recorded Result |
|---|---:|
| Listing Records | 1,800 |
| Sales Records | 24,000 |
| Total Source Rows | 25,800 |
| Missing Required Cells | 0 |
| Exact-Repeated Sales Rows | 140 |
| Revenue Discrepancy Rows | 9,019 |
| Sales Rows Flagged Against Stock Snapshot | 2,936 |
| Runtime Validation Checks | 19 |
| Runtime Status | Passed |

### Validation Categories

**1. Schema and Type Integrity**

Checks required fields, expected data types, value constraints, and declared listing keys.

**2. Relationship Integrity**

Verifies that sales records reference valid listings.

**3. Shared Attribute Consistency**

Checks that sale/listing seller, category, price, rating, and stock attributes agree under the source contracts.

**4. SQL Execution**

Runs all four named analytical queries.

**5. Revenue Reconciliation**

Calculates recorded revenue and price-times-units totals.

**6. Seller Metric Reconciliation**

Verifies distinct seller counts and top-ten seller revenue share.

**7. Duplicate Diagnostics**

Quantifies repeated sales rows without assuming they are illegitimate transactions.

**8. Source Traceability**

Uses evidence manifests to associate input data, code, and results with file hashes.

### Important Data Quality Decisions

**Preserve Repeated Sales Rows**

The source contains 140 exact-repeated sales rows.

Because no stable unique sale ID exists, identical records may represent legitimate repeated transactions or ingestion duplication.

The workflow quantifies and preserves them rather than silently deleting them.

**Preserve Revenue Differences**

The pipeline reports 9,019 rows exceeding the arithmetic discrepancy tolerance.

It does not automatically overwrite recorded revenue.

**Do Not Infer Historical Stockouts**

The stock indicator lacks event-time context.

The pipeline therefore does not convert the 2,936 flagged rows into proven stockout violations or lost-revenue estimates.

**Differentiate Technical Validation from Business Validity**

A passing technical check confirms the implemented validation conditions were satisfied.

It does not prove that source financial definitions are correct or that the dataset supports causal business conclusions.

### Evidence Files

| File | Purpose |
|---|---|
| [validation.json](Results/validation.json) | Runtime validation checks |
| [quality.json](Results/quality.json) | Data anomalies and source limitations |
| [manifest.json](Results/manifest.json) | Source, code, and result traceability |
| [query_plans.json](Results/query_plans.json) | Local SQLite execution plans |
| [additional_metrics.json](Results/additional_metrics.json) | Seller concentration calculations |

**Validation Status:** 19 documented runtime checks passed.

**Business Data Status:** Revenue definitions and historical inventory interpretation remain unresolved.

---

## 📊 Business Intelligence & Dashboard Assets

The project includes Power BI, Excel, and HTML reporting artifacts in addition to its SQL/Python pipeline.

### Existing Assets

| Asset | Purpose | Location |
|---|---|---|
| Excel Model | Source-aligned analytical summary | [Excel Workbook](Excel/04_Amazon_Marketplace_Analytics_Model.xlsx) |
| Power BI Report | Preserved legacy marketplace dashboard | [Power BI Dashboard](Dashboard/Amazon_Marketplace_Analytics_Dashboard.pbix) |
| Dashboard Documentation | Native asset status | [Dashboard README](Dashboard/README.md) |
| Dashboard Image | Existing visual reference | [Marketplace Dashboard Image](Images/amazon_marketplace_dashboard.png) |
| HTML Report | Canonical SQL/Python findings | [REPORT.html](REPORT.html) |

### Native Workbook Verification

The existing Power BI workbook contains a different embedded dataset from the canonical marketplace CSV analysis.

The audited legacy model includes approximately 85,000 `fact_orders` records, while the canonical analysis contains 24,000 sales rows.

These are different source populations and business grains.

Consequently, the legacy Power BI workbook must not be presented as fully verified visual evidence of the canonical SQL/Python results.

### Completed Verification Evidence

- Canonical SQL execution and metric reconciliation
- Corrected Excel analytical summaries
- Excel formula verification and recalculation evidence
- Power BI native-file inspection
- Extracted model and relationship information
- Independent legacy-measure baselines
- Runnable DAX verification queries

### Outstanding Desktop Acceptance

Power BI Desktop DAX execution, source-aligned model rebuilding, native report refresh, and page-level visual acceptance remain outstanding.

A DAX test against the legacy model would validate that model's own measure expectations, not establish alignment with unrelated canonical CSVs.

### Recommended Canonical Dashboard Pages

**Page 1 — Marketplace Executive Overview**

Recorded revenue, units, sales-row counts, sellers, listing counts, and reconciliation indicators.

**Page 2 — Seller Performance**

Top-seller ranking, individual revenue shares, concentration metrics, and seller comparisons.

**Page 3 — Category Performance**

Revenue, units, and sales activity by product category.

**Page 4 — Revenue Quality**

Recorded versus calculated revenue, discrepancy totals, flagged rows, and exception patterns.

**Page 5 — Inventory Diagnostics**

Listing stock flags, price bands, category groupings, and source limitations.

These pages represent a recommended source-aligned design, not a claim that they are already implemented and verified in the legacy PBIX.

### Verification Documentation

[Dashboard Reconciliation](Docs/Dashboard_Reconciliation.md) | [Field Mapping](Docs/Dashboard_Field_Mapping.md) | [Connection Guide](Docs/Connect_To_Dashboard.md) | [Native Workbook Verification](../verification/native/README.md)

---

## 📂 Project Structure

```text
04_Amazon_Marketplace_Analytics/
│
├── Data/
│   ├── raw/
│   │   ├── listings_raw.csv
│   │   └── sales_raw.csv
│   └── clean/
│       ├── listings_clean.csv
│       └── sales_clean.csv
│
├── SQL/
│   └── analysis.sql
│
├── Python/
│   └── analysis.py
│
├── Excel/
│   └── 04_Amazon_Marketplace_Analytics_Model.xlsx
│
├── Dashboard/
│   ├── Amazon_Marketplace_Analytics_Dashboard.pbix
│   └── README.md
│
├── Images/
│   └── amazon_marketplace_dashboard.png
│
├── Results/
│   ├── summary.csv
│   ├── seller_concentration.csv
│   ├── category_performance.csv
│   ├── stock_status_association.csv
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

The project uses shared processing, SQL execution, validation, and reporting components from the parent Data Analyst Portfolio.

---

## ▶️ Reproduce the Analysis

### Prerequisites

- Python 3.12
- Git
- Python package installation capability

The verified core analytical workflow requires no paid database subscription, cloud account, or native BI license.

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

### Step 4 — Run the Marketplace Analysis

```bash
python -m portfolio.run --project 04_Amazon_Marketplace_Analytics
```

This executes the project's analytical workflow and regenerates the associated outputs.

### Step 5 — Run Automated Tests

```bash
python -m unittest discover -s tests -v
```

The test command runs the shared portfolio test suite.

### Step 6 — Review the Outputs

Navigate to:

`04_Amazon_Marketplace_Analytics/Results/`

Important outputs include:

- `summary.csv`
- `seller_concentration.csv`
- `category_performance.csv`
- `stock_status_association.csv`
- `additional_metrics.json`
- `quality.json`
- `validation.json`

### Step 7 — Open the Offline Report

Open:

`04_Amazon_Marketplace_Analytics/REPORT.html`

Download or clone the repository to view the rendered report locally.

GitHub may display the HTML source rather than the rendered report.

### Reproducibility Guidance

The pipeline records validation evidence and file hashes.

If execution fails, previously generated outputs may be stale or partial. Rerun successfully and verify current evidence before using the results.

For further instructions, consult the [Portfolio Reproduction Runbook](../docs/RUNBOOK.md).

---

## ⚠️ Limitations & Future Improvements

### Current Analytical Limitations

**1. Simulated Portfolio Dataset**

No actual Amazon customer records, company revenues, or production marketplace transactions are represented.

**2. Missing Unique Sale and Order IDs**

Sales rows cannot reliably be equated with distinct customer orders.

**3. Unresolved Revenue Definitions**

Recorded revenue differs from the arithmetic price-times-units total.

Without business rules, the discrepancy cannot be conclusively categorized.

**4. Missing Fee and Commission Information**

The data do not support valid platform commission income or fee calculations.

**5. Incomplete Inventory History**

An undated stock snapshot cannot establish historical stock availability or lost sales.

**6. Repeated Sales Records**

Exact-repeat rows are preserved because unique sale identifiers are unavailable.

**7. Incomplete Seller Economics**

Costs, profitability, fees, returns, and seller operating histories are not supplied.

**8. No Reliable GMV Classification**

The source does not independently establish an accounting definition of gross merchandise value.

**9. Power BI Source Mismatch**

The preserved native dashboard uses a different source population and requires further validation.

### Future Enhancements

Potential improvements include:

- Stable transaction identifiers
- Documented gross and net revenue definitions
- Fee and commission schedules
- Discount and refund reconciliation
- Automated financial exception reporting
- Historical seller revenue trends
- Seller cohort analysis
- Product profitability reporting
- Historical inventory movement tracking
- Time-aware stockout analysis
- Marketplace return-rate analysis
- Margin-based category evaluation
- Source-aligned Power BI semantic model
- Native DAX verification and dashboard acceptance

These are proposed enhancements and are not claimed as already implemented.

---

## 🧠 Project Takeaways

### Technical Skills Demonstrated

- SQL-based marketplace analysis
- Financial reconciliation
- Relational data modeling
- Seller revenue ranking
- Window functions
- Common Table Expressions
- Python data validation
- Independent metric reconciliation
- Data quality diagnostics
- Revenue concentration calculations
- Automated verification
- Reproducible reporting

### Business Skills Demonstrated

- Translating financial reporting questions into metrics
- Identifying source inconsistencies
- Evaluating seller performance
- Understanding marketplace revenue exposure
- Comparing category contributions
- Recognizing limitations in operational data
- Communicating financial uncertainty
- Prioritizing business investigations
- Developing accountable reporting recommendations

### Final Conclusion

This marketplace analytics project identifies three central findings:

**First**, the source records 1,830,085.36 in revenue, but 9,019 sales rows differ from the corresponding price-times-units calculation beyond the documented tolerance.

**Second**, the top ten sellers contribute only 8.44% of recorded revenue, showing a relatively broad seller revenue distribution within the supplied dataset.

**Third**, Home and Electronics lead category revenue, while undated stock information prevents defensible historical stockout or lost-sales conclusions.

The analysis demonstrates that business reporting must connect technical calculations with reliable definitions, clear lineage, and data-quality controls.

**The central lesson is that accurate financial and operational analytics requires more than calculating revenue totals. It requires reconciling competing metrics, preserving source evidence, validating assumptions, and communicating what the data can—and cannot—support.**

---

## 📚 Supporting Documentation & Evidence

| Resource | Description |
|---|---|
| [Data Dictionary](Docs/Data_Dictionary.md) | Source schemas, identifiers, and contracts |
| [KPI Lineage](Docs/KPI_Lineage.md) | Revenue definitions and calculations |
| [SQL Analysis](SQL/analysis.sql) | Executable marketplace queries |
| [Python Analysis](Python/analysis.py) | Project Python entry point |
| [Marketplace Summary](Results/summary.csv) | Overall sales and revenue metrics |
| [Seller Concentration](Results/seller_concentration.csv) | Seller rankings and revenue shares |
| [Category Performance](Results/category_performance.csv) | Category revenue and unit summaries |
| [Stock Status Analysis](Results/stock_status_association.csv) | Listing stock associations |
| [Additional Metrics](Results/additional_metrics.json) | Seller HHI and top-ten revenue concentration |
| [Quality Evidence](Results/quality.json) | Source discrepancies and warnings |
| [Validation Evidence](Results/validation.json) | Runtime checks |
| [Offline Report](REPORT.html) | Canonical analytical results |
| [Native Workbook Verification](../verification/native/README.md) | Excel and Power BI verification status |

---

## 👨‍💻 About the Analyst

**Jamie Christian**

Data Analytics | Business Intelligence | SQL | Python | Business Analysis

I focus on transforming complex data into reliable business metrics, identifying reporting inconsistencies, evaluating operational performance, and communicating insights that support informed decision-making.

My professional interests include Data Analytics, Business Intelligence, Financial Reporting, Revenue Operations, Business Analysis, and Data Quality.

📧 [Email](mailto:Jamiechristian331@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/jamiechristian2/)  
💻 [GitHub](https://github.com/JamieChristian22)

### 🔗 Explore More Projects

[⬅️ Back to Main Data Analyst Portfolio](../README.md)

[🛒 Previous Project: Ecommerce Product Analytics](../03_Ecommerce_Product_Analytics/README.md)

[🔍 Next Project: User Journey Analytics](../05_User_Journey_Analytics/README.md)

---

**📦 Amazon Marketplace Analytics | Built by Jamie Christian**

*SQL-driven marketplace insights. Python-verified reporting. Financial reconciliation. Transparent business analysis.*
