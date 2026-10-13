 
# 📊 Data Analyst Portfolio | Jamie Christian

**Data Analytics • SQL • Python • Excel • Business Intelligence • Statistical Analysis**

**Turning complex datasets into actionable business insights through reproducible analysis, data quality validation, statistical reasoning, and decision-focused reporting.**

[![Validate analysis](https://github.com/JamieChristian22/data-analyst-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/JamieChristian22/data-analyst-portfolio/actions/workflows/validate.yml)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-4479A1)
![Projects](https://img.shields.io/badge/Analytics_Projects-5-success)
![Testing](https://img.shields.io/badge/Automated_Tests-35-informational)

🌐 [LinkedIn](https://www.linkedin.com/in/jamiechristian2/) | 💻 [GitHub](https://github.com/JamieChristian22) | 📧 [Email](mailto:Jamiechristian331@gmail.com)

---

## 👨‍💻 About This Portfolio

Welcome to my Data Analyst Portfolio, a collection of five end-to-end analytical projects demonstrating my ability to transform raw datasets into reliable metrics, uncover business trends, investigate data-quality issues, and communicate findings that support informed decisions.

My approach combines technical execution with business reasoning. Rather than reporting numbers without context, I focus on understanding how metrics are defined, validating their accuracy, interpreting uncertainty, and translating results into practical recommendations.

The portfolio demonstrates hands-on work with:

- **SQL:** Data extraction, joins, filtering, aggregations, CTEs, window functions, analytical queries, and performance inspection.
- **Python:** pandas-based transformation, statistical calculations, automated analysis, testing, and reporting.
- **Data Cleaning & ETL:** Schema validation, type normalization, relationship checks, reproducible transformations, and source-to-output traceability.
- **Exploratory Data Analysis:** Pattern identification, segmentation, performance comparisons, funnel analysis, and concentration analysis.
- **Statistical Analysis:** Hypothesis testing, confidence intervals, conversion analysis, and experimental interpretation.
- **Business Intelligence:** KPI documentation, report reconciliation, Excel validation, Tableau extracts, and Power BI measure-verification artifacts.
- **Data Quality:** Duplicate analysis, integrity testing, chronological validation, and metric reconciliation.
- **Business Communication:** Executive-friendly findings, transparent assumptions, analytical recommendations, and supporting documentation.

**Data transparency:** The projects use supplied simulated portfolio datasets. Results describe those datasets and are not represented as real client outcomes, deployed production systems, or realized business improvements.

---

## 🚀 Portfolio at a Glance

| Portfolio Metric | Documented Evidence |
|---|---|
| End-to-end analytics projects | 5 |
| Original source records | 121,366 rows across 10 CSV files |
| Runtime validation checks | 93 |
| Automated unit/integration tests | 35 |
| Analytical approaches | SQL, Python, descriptive statistics, experiment inference |
| Reporting | Offline HTML reports, CSV results, Excel summaries, BI verification artifacts |
| Reproducibility | Python 3.12, SQLite, pinned dependencies |
| Evidence tracking | SHA-256 manifests and saved validation results |

These checks validate defined technical and analytical behaviors; they do not establish production deployment, external business impact, or completed native Power BI/Tableau Desktop acceptance.

### Quick Navigation

- 📂 [Explore the Five Analytics Projects](#-featured-data-analytics-projects)
- 🛠️ [Technical Skills & Tools](#-technical-skills--tools)
- 🔄 [End-to-End Analytics Workflow](#-end-to-end-data-analytics-workflow)
- ✅ [Testing & Validation](#-data-quality-testing--validation)
- 📊 [Business Intelligence & Native Workbook Verification](#-business-intelligence--native-workbook-verification)
- 💻 [Run the Portfolio Locally](#-reproduce-the-portfolio)
- 📚 [Technical Documentation](#-documentation--supporting-evidence)

---

## 📁 Featured Data Analytics Projects

Five case studies showcase business-oriented analytics across SaaS, experimentation, ecommerce, marketplace operations, and user behavior.

### 01 | 📈 SaaS Product Analytics — StreamFlow

**Focus:** Customer Activation, Subscription Revenue, Onboarding Funnels & Churn Analysis

**Business Question**

Where do users experience the greatest onboarding friction, and how do subscription activity and supplied churn indicators relate to customer behavior?

**Analytical Approach**

- Analyzed user, subscription, and event-level information.
- Used SQL to summarize subscription revenue, customer segments, and onboarding progression.
- Evaluated activation stages through chronological funnel analysis.
- Examined the relationship between user activity and supplied churn labels.
- Reconciled core metrics through independent Python calculations.

**Key Findings**

| KPI | Result |
|---|---:|
| Total Users | 1,500 |
| Paying Users | 698 |
| Snapshot Monthly Recurring Revenue | 189,975.00 |
| Snapshot Annualized Revenue | 2,279,700.00 |
| Paying-User Churn Label Rate | 21.06% |
| Step 1 to Step 2 Onboarding Drop-Off | 62.59% |

Revenue is expressed in unspecified dataset currency units. The annualized revenue figure is calculated from the subscription snapshot, not independently verified recognized revenue.

**Business Interpretation**

The highest early onboarding loss suggests that workspace setup deserves additional investigation. Usability research, event instrumentation review, and a controlled onboarding experiment would help determine whether a product change improves activation.

**Skills Demonstrated:** SQL aggregation, retention-related descriptive analysis, revenue metrics, ordered funnel construction, KPI reconciliation, and business recommendations.

**Project Resources**

[📖 Case Study](01_SaaS_Product_Analytics_StreamFlow/README.md) | [💻 SQL Analysis](01_SaaS_Product_Analytics_StreamFlow/SQL/analysis.sql) | [📊 Results](01_SaaS_Product_Analytics_StreamFlow/Results) | [📄 Offline Report](01_SaaS_Product_Analytics_StreamFlow/REPORT.html)

---

### 02 | 🧪 A/B Testing — Feature Impact Analysis

**Focus:** Hypothesis Testing, Conversion Optimization & Experiment Evaluation

**Business Question**

Does Variant B demonstrate a higher session conversion rate than the control group, and how confident can we be in the observed difference?

**Analytical Approach**

- Analyzed 12,000 simulated session-level observations.
- Compared conversion performance between experimental groups.
- Applied a two-sided two-proportion z-test.
- Calculated a Newcombe-Wilson 95% confidence interval.
- Evaluated relative and absolute conversion lift.
- Examined segment performance and supporting guardrail metrics.
- Documented assumptions about randomization and independence.

**Key Findings**

| KPI | Result |
|---|---:|
| Control Sessions | 5,987 |
| Variant B Sessions | 6,013 |
| Control Conversion Rate | 19.84% |
| Variant B Conversion Rate | 23.08% |
| Absolute Conversion Lift | +3.24 percentage points |
| Relative Conversion Lift | +16.33% |
| 95% Confidence Interval for Difference | +1.77 to +4.71 percentage points |
| Two-Sided p-value | Approximately 0.0000154 |

**Business Interpretation**

Variant B exhibits a higher conversion rate in the supplied data. However, a statistically significant result does not independently justify a product launch.

Before a real rollout, the experiment would require verification of assignment units, randomization integrity, independence assumptions, duration, and operational guardrails.

**Skills Demonstrated:** A/B testing, statistical inference, Python, SQL, experiment reporting, conversion analysis, and evidence-based decision-making.

**Project Resources**

[📖 Case Study](02_AB_Test_Feature_Impact/README.md) | [💻 SQL Analysis](02_AB_Test_Feature_Impact/SQL/analysis.sql) | [📊 Results](02_AB_Test_Feature_Impact/Results) | [📄 Offline Report](02_AB_Test_Feature_Impact/REPORT.html)

---

### 03 | 🛒 Ecommerce Product Analytics

**Focus:** Conversion Funnels, Cart Abandonment, Customer Sessions & Product Performance

**Business Question**

Which ecommerce segments demonstrate the greatest purchasing friction, and how is revenue distributed across products?

**Analytical Approach**

- Examined website sessions and associated purchase records.
- Analyzed conversion and cart-abandonment metrics.
- Compared purchasing behavior by device and acquisition channel.
- Evaluated SKU-level revenue concentration using a Pareto-style analysis.
- Investigated discount associations without assuming causation.
- Verified funnel definitions and result calculations.

**Key Findings**

| KPI | Result |
|---|---:|
| Website Sessions | 25,000 |
| Purchases | 3,037 |
| Session Conversion Rate | 12.15% |
| Cart Abandonment Rate | 64.24% |
| Recorded Order Revenue | 198,586 |
| Average Order Value | 65.39 |
| Revenue Share of Top 20% of SKUs | 31.42% |

**Business Interpretation**

Cart abandonment represents an area worth investigating, particularly within segments combining substantial traffic and higher abandonment rates.

SKU concentration also provides a basis for reviewing product exposure, assortment, and merchandising priorities.

These findings identify where investigation could be valuable. They do not independently establish the causes of abandonment or the revenue impact of a proposed intervention.

**Skills Demonstrated:** SQL joins, customer-session analysis, segmentation, conversion metrics, revenue analysis, data visualization preparation, and KPI validation.

**Project Resources**

[📖 Case Study](03_Ecommerce_Product_Analytics/README.md) | [💻 SQL Analysis](03_Ecommerce_Product_Analytics/SQL/analysis.sql) | [📊 Results](03_Ecommerce_Product_Analytics/Results) | [📄 Offline Report](03_Ecommerce_Product_Analytics/REPORT.html)

---

### 04 | 📦 Marketplace Analytics — Revenue & Seller Performance

**Focus:** Marketplace Reporting, Seller Concentration, Revenue Reconciliation & Data Quality

**Business Question**

How is recorded marketplace revenue distributed across sellers, and what data-quality discrepancies prevent full financial reconciliation?

**Analytical Approach**

- Analyzed marketplace sales records and seller relationships.
- Computed category-level performance and seller concentration.
- Compared recorded revenue against unit price multiplied by quantity.
- Identified discrepancies that require source-owner investigation.
- Evaluated inventory-status associations.
- Preserved source anomalies rather than silently changing revenue totals.

**Key Findings**

| KPI | Result |
|---|---:|
| Sales Records | 24,000 |
| Units | 48,063 |
| Sellers | 316 |
| Recorded Revenue | 1,830,085.36 |
| Revenue Discrepancy Rows | 9,019 |
| Top 10 Sellers' Revenue Share | 8.44% |

**Business Interpretation**

The revenue discrepancies demonstrate why financial metrics require source reconciliation before operational use.

The analysis preserves recorded revenue rather than assuming an undocumented commission, discount, or fee formula.

Seller concentration provides additional insight into marketplace revenue exposure.

**Important Limitation:** A sales record is not necessarily an order, and recorded revenue cannot be assumed to represent marketplace commission income.

**Skills Demonstrated:** SQL, financial data analysis, data integrity, reconciliation, seller segmentation, anomaly detection, and operational reporting.

**Project Resources**

[📖 Case Study](04_Amazon_Marketplace_Analytics/README.md) | [💻 SQL Analysis](04_Amazon_Marketplace_Analytics/SQL/analysis.sql) | [📊 Results](04_Amazon_Marketplace_Analytics/Results) | [📄 Offline Report](04_Amazon_Marketplace_Analytics/REPORT.html)

---

### 05 | 🔍 User Journey Analytics

**Focus:** Customer Behavior, Funnel Progression, Event Tracking & Chronological Data Quality

**Business Question**

How does observed purchasing activity compare with a strictly date-ordered conversion funnel, and what do discrepancies reveal about event tracking?

**Analytical Approach**

- Analyzed user activity across successive journey stages.
- Distinguished stage reach from chronological funnel completion.
- Validated event-date ordering and eligible transitions.
- Compared purchase behavior by returning-user status.
- Examined time-to-purchase distributions.
- Identified issues preventing trustworthy interpretation of strict-funnel abandonment.

**Key Findings**

| KPI | Result |
|---|---:|
| Users | 6,000 |
| Observed Purchasers | 627 |
| Observed Purchase Rate | 10.45% |
| Median Days to Purchase | 7 |
| 90th Percentile Days to Purchase | 12 |
| Users with Adjacent-Stage Date Inversions | 3,296 |
| Complete Six-Stage Ordered Paths | 0 |

**Business Interpretation**

Although 627 users have observed purchase events, no user completes the entire strict chronological path in the supplied records.

This inconsistency highlights an event sequencing and source-quality problem, not proof that no purchases occurred.

The correct next step is to investigate instrumentation, event timestamps, and missing intermediate activity before interpreting funnel losses as user abandonment.

**Skills Demonstrated:** SQL window functions, temporal analysis, customer segmentation, funnel analytics, Python validation, and event-level data quality assessment.

**Project Resources**

[📖 Case Study](05_User_Journey_Analytics/README.md) | [💻 SQL Analysis](05_User_Journey_Analytics/SQL/analysis.sql) | [📊 Results](05_User_Journey_Analytics/Results) | [📄 Offline Report](05_User_Journey_Analytics/REPORT.html)

---

## 🛠️ Technical Skills & Tools

| Category | Technologies & Competencies |
|---|---|
| Programming | Python, SQL |
| Data Analysis | pandas, exploratory analysis, descriptive statistics |
| Databases | SQLite, relational joins, indexes, query execution plans |
| Data Preparation | Data cleaning, schema validation, normalization, transformations |
| Statistical Methods | Hypothesis testing, confidence intervals, conversion-rate comparison |
| Business Analytics | KPI development, revenue analysis, funnel analysis, segmentation |
| Data Quality | Integrity checks, anomaly investigation, numerical reconciliation |
| Excel | Formula-based summaries, recalculation validation, source-linked metrics |
| Business Intelligence | Power BI model inspection, DAX verification preparation, Tableau Hyper extracts |
| Reporting | HTML analytical reports, CSV outputs, technical documentation |
| Testing | Python unittest, integration checks, GitHub Actions |
| Reproducibility | Git, GitHub, pinned dependencies, SHA-256 evidence manifests |

### Core SQL Competencies

- Data filtering, sorting, and aggregation
- `INNER JOIN` and `LEFT JOIN`
- `GROUP BY`, `HAVING`, and conditional aggregation
- Common Table Expressions (CTEs)
- Window functions and rankings
- Date-based analysis
- Conversion and retention-related metric calculations
- Null and division-by-zero handling
- Relational integrity validation
- Local query-plan inspection

All active portfolio SQL queries use SQLite-compatible syntax.

### Core Python Competencies

- Importing and validating CSV datasets
- DataFrame-based cleaning and transformation
- Independent verification of SQL results
- Statistical calculations
- Automated report generation
- Reproducible pipelines
- Data quality diagnostics
- Automated unit and integration testing

---

## 🔄 End-to-End Data Analytics Workflow

Each project follows a consistent, repeatable analytical process.

**01 — Define the Business Problem**

Identify the decision to support, analytical questions, required KPIs, and constraints affecting interpretation.

↓

**02 — Inspect and Validate Source Data**

Review source schemas, row counts, required fields, keys, types, relationships, and known limitations.

↓

**03 — Clean and Transform**

Apply documented type normalization and data transformations while preserving the original source files.

↓

**04 — Execute SQL Analysis**

Load cleaned records into SQLite, run named queries, and export query-level results.

↓

**05 — Verify with Python**

Independently recalculate selected metrics, validate relationships, and check results against expected definitions.

↓

**06 — Interpret the Results**

Evaluate business implications, statistical uncertainty, data quality, and competing explanations.

↓

**07 — Generate Reporting Evidence**

Produce CSV outputs, offline analytical reports, validation records, and SHA-256 manifests.

↓

**08 — Communicate Recommendations**

Translate findings into clear recommendations while distinguishing observed evidence from hypotheses requiring further testing.

### Data Pipeline Architecture

**Raw CSV → Data Contracts → Cleaning & Transformation → SQLite → SQL Analytics → Python Reconciliation → Results & Reports → Validation Evidence**

The workflow is locally reproducible and does not depend on paid cloud resources or an external database service.

---

## ✅ Data Quality, Testing & Validation

Reliable analysis requires more than queries that run successfully.

This portfolio incorporates structured testing and validation so that results can be traced, reproduced, and challenged.

### Validation Framework

| Validation Area | Implementation |
|---|---|
| Schema Integrity | Required columns and supported data types |
| Missing Values | Required-field checks |
| Key Integrity | Duplicate declared-key detection |
| Referential Integrity | Broken relationship and orphan-record checks |
| Data Quality | Repeated-row, date, and source-anomaly diagnostics |
| Metric Reconciliation | SQL-to-Python comparisons |
| Statistical Correctness | Interval calculations and inference boundary tests |
| Chronological Integrity | Event ordering and eligible-stage transitions |
| Query Execution | Executable named SQL result generation |
| Source Traceability | SHA-256 file manifests |
| Regression Testing | Saved numerical results and automated test execution |

### Documented Test Coverage

- **93 runtime validation checks** across five projects.
- **35 unit and integration tests** covering statistical edge cases, source contracts, relational integrity, chronological handling, SQL calculations, and evidence consistency.
- GitHub Actions workflow for execution, test runs, and numerical output-drift checks.
- Independent metric reconciliation using pandas.
- Current-run manifests linking outputs to input data and analysis code.

**Validation boundary:** Passing technical tests does not establish the correctness of every business assumption, causal interpretation, native dashboard visualization, or external business decision.

### Reproducibility and Evidence

Each project includes source records, executable analysis, exported outputs, and supporting evidence.

Key files include:

- `Results/validation.json` — Validation results.
- `Results/quality.json` — Source quality and limitation diagnostics.
- `Results/query_plans.json` — SQLite query-plan information.
- `Results/manifest.json` — File hashes and execution provenance.
- `Results/*.csv` — Named analytical query outputs.
- `REPORT.html` — Offline analytical report.

---

## 📊 Business Intelligence & Native Workbook Verification

This repository also contains legacy BI workbooks, Excel summaries, and a dedicated native-file verification package.

The verification process explicitly distinguishes source inspection, numerical testing, formula recalculation, and full native application acceptance.

### BI Asset Verification Matrix

| Asset | Documented Verification | Remaining Limitation |
|---|---|---|
| Five Excel summaries | Corrected formulas and source-aligned results with recalculation evidence | Microsoft Excel execution is not claimed |
| Three Tableau Hyper extracts | 18 source/result tables verified by extract readback | Tableau Desktop visual refresh and acceptance not completed |
| Two legacy Power BI models | 19 independently calculated measure baselines and DAX verification queries | Power BI Desktop DAX execution not completed |
| Five legacy BI dashboards | Embedded data sources inspected | Legacy sources differ from canonical analysis datasets |
| Canonical reports | SQL/Python results and offline HTML reports | Separate from legacy native dashboard visuals |

### Why This Matters

One important finding of the workbook audit is that the existing Power BI and Tableau dashboards use different datasets from the canonical project analyses.

Rather than presenting incompatible dashboard screenshots as proof of the current metrics, the portfolio preserves the original assets and documents their limitations.

The verification package provides:

- Native workbook source audits
- Excel formula recalculation evidence
- Tableau Hyper extract validation
- Power BI model and DAX measure baselines
- Source-to-result reconciliation documentation
- Procedures for completing remaining Desktop acceptance checks

**Current status:** Source inspection and the documented machine-verification stages are distinct from fully completed native Power BI Desktop and Tableau Desktop validation. The latter has not been claimed.

**Explore the Evidence:**

[📘 Native Workbook Verification](verification/native/README.md) | [🔎 Workbook Audit](verification/native/workbook_audit.json) | [📊 Excel Recalculation Evidence](verification/native/excel_calc_verification.json)

---

## 💻 Reproduce the Portfolio

### Requirements

- Python 3.12
- Git
- Compatible operating system: Windows, macOS, or Linux
- No paid BI license, cloud subscription, or external database required for the core analysis

### Step 1 — Clone the Repository

`git clone https://github.com/JamieChristian22/data-analyst-portfolio.git`

`cd data-analyst-portfolio`

### Step 2 — Create a Virtual Environment

`python -m venv .venv`

Activate on macOS/Linux:

`source .venv/bin/activate`

Activate on Windows PowerShell:

`.venv\Scripts\Activate.ps1`

### Step 3 — Install Dependencies

`python -m pip install -r requirements.txt`

### Step 4 — Execute All Five Projects

`python -m portfolio.run`

This regenerates the clean datasets, local SQLite databases, analytical results, validation records, and offline reports.

### Step 5 — Run Automated Tests

`python -m unittest discover -s tests -v`

### Step 6 — Execute One Project

For example, run only the A/B testing project:

`python -m portfolio.run --project 02_AB_Test_Feature_Impact`

### Step 7 — Review the Results

Open the repository's `index.html` locally to access the report directory, or open the corresponding project's `REPORT.html`.

GitHub may display HTML source rather than the rendered report. Download or clone the repository and open the files locally for the intended offline viewing experience.

For more detailed troubleshooting, see the [Reproduction Runbook](docs/RUNBOOK.md).

---

## 📂 Repository Structure

| Directory / File | Purpose |
|---|---|
| `01_SaaS_Product_Analytics_StreamFlow/` | SaaS activation, subscription revenue, and onboarding analysis |
| `02_AB_Test_Feature_Impact/` | A/B testing and statistical inference |
| `03_Ecommerce_Product_Analytics/` | Ecommerce funnel and merchandise analysis |
| `04_Amazon_Marketplace_Analytics/` | Marketplace revenue quality and seller performance |
| `05_User_Journey_Analytics/` | Ordered customer journeys and event-quality diagnostics |
| `portfolio/` | Shared data validation, processing, SQL, statistics, and reporting modules |
| `tests/` | Automated unit and integration tests |
| `docs/` | Methodology, execution guidance, and interview documentation |
| `verification/native/` | Native workbook audits and validation artifacts |
| `scripts/` | Additional verification and supporting utilities |
| `requirements.txt` | Python dependency specifications |
| `index.html` | Local report navigation |
| `README.md` | Main portfolio documentation |

### Standard Project Components

Each case study provides:

- Original data inputs and regenerated cleaned data
- SQL analysis scripts
- Python execution entry point
- KPI definitions and data documentation
- Saved analytical results
- Data quality evidence
- Automated validation records
- Analytical case study
- Offline HTML report

This organization allows individual projects to be explored separately while sharing a consistent analytical framework.

---

## 🧠 Analytical Judgment & Business Decision-Making

A central goal of this portfolio is to demonstrate the ability to recognize when apparently useful metrics are unreliable or incomplete.

| Analytical Challenge | Decision Taken | Business Value |
|---|---|---|
| Missing stable customer identifiers | Excluded unsupported customer RFM claims | Prevents misleading customer segmentation |
| Revenue not reconciling to price × quantity | Reported discrepancies without inventing fee assumptions | Protects financial reporting integrity |
| Out-of-order customer events | Separated observed stage reach from valid ordered paths | Avoids misinterpreting tracking errors as abandonment |
| Experiment assignment details unavailable | Reported statistical findings with explicit assumptions | Prevents overconfident rollout conclusions |
| Legacy dashboard datasets differ | Preserved assets and documented source mismatches | Avoids presenting unsupported dashboard evidence |
| Duplicate records without stable event IDs | Preserved and quantified repeated rows | Avoids deleting potentially legitimate activity |
| Unsupported projected business outcomes | Focused on measured findings and future validation | Maintains evidence-based reporting |

**Guiding principle:** An accurate analytical limitation is more valuable than an unsupported business conclusion.

---

## 🎯 How This Portfolio Applies to Real Data Analyst Work

These projects represent skills commonly used to support business decisions across several functions.

**Product Analytics**

Evaluate user behavior, onboarding, activation, retention-related indicators, and feature experiments.

**Business Intelligence & Reporting**

Create defined KPIs, reconcile datasets, prepare reporting outputs, and validate analytical measures.

**Revenue & Operations Analysis**

Investigate financial discrepancies, monitor performance, evaluate concentration, and identify reporting risks.

**Marketing & Ecommerce Analytics**

Measure conversion, segment customer behavior, assess checkout friction, and evaluate channel performance.

**Data Quality & Analytics Engineering Support**

Validate incoming records, maintain traceable transformations, test metric definitions, and produce repeatable analytical outputs.

The emphasis is on skills demonstrated in the repository rather than claims of enterprise production experience.

---

## 📚 Documentation & Supporting Evidence

| Resource | Description |
|---|---|
| [Methodology & Limitations](docs/METHODOLOGY.md) | Source assumptions, statistical interpretation, data contracts, and analytical boundaries |
| [Reproduction Runbook](docs/RUNBOOK.md) | Setup, project execution, troubleshooting, and output descriptions |
| [Interview Walkthrough](docs/INTERVIEW_GUIDE.md) | Project explanations and interview discussion guidance |
| [Upgrade Record](docs/UPGRADE_NOTES.md) | Documented portfolio improvements |
| [Native Workbook Verification](verification/native/README.md) | Excel, Tableau, and Power BI evidence and remaining verification requirements |
| [Portfolio Report Index](index.html) | Entry point for offline project reports |

---

## 🔎 Important Project Limitations

To support transparent interpretation:

1. All five projects use supplied simulated datasets, not live customer or production information.
2. Revenue currency codes are not supplied; revenue values are presented in dataset units.
3. Observational relationships do not independently establish causation.
4. The A/B testing analysis depends on independence and assignment assumptions that cannot be fully confirmed from supplied metadata.
5. User-journey sequencing problems limit conclusions about true behavioral abandonment.
6. Legacy BI assets and canonical analytical datasets are not interchangeable.
7. Native Desktop refresh, DAX execution, and complete dashboard visual acceptance remain separate from the documented machine checks.

These limitations are intentionally disclosed so readers can evaluate the results accurately.

---

## 🤝 Connect With Me

I'm interested in opportunities where I can apply SQL, Python, business analysis, data visualization, and problem-solving to help organizations understand their data and make informed decisions.

My professional interests include:

**Data Analyst • Junior Data Analyst • Business Intelligence Analyst • Reporting Analyst • Business Data Analyst • Operations Analyst**

I value analytical accuracy, continuous learning, practical problem-solving, and clear communication between technical and business stakeholders.

📧 **Email:** [Jamiechristian331@gmail.com](mailto:Jamiechristian331@gmail.com)

💼 **LinkedIn:** [linkedin.com/in/jamiechristian2](https://www.linkedin.com/in/jamiechristian2/)

💻 **GitHub:** [github.com/JamieChristian22](https://github.com/JamieChristian22)

---

### 📌 Portfolio Summary

**Five projects. Reproducible SQL and Python analysis. Documented technical validation. Clear business questions and evidence-based recommendations.**

This portfolio demonstrates not just how to calculate metrics, but how to validate, interpret, explain, and responsibly use them.

**Built and maintained by Jamie Christian.**
