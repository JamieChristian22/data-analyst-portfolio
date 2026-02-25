# 01 SaaS Product Analytics StreamFlow

## Dashboard
**Included dashboard file:** `Product Analytics Dashboard | StreamFlow (Simulated SaaS).twbx`  
> This project includes raw + cleaned CSVs that match the dashboard’s model (tables + fields).  
> Connect the CSVs to rebuild / refresh visuals in Power BI or Tableau.

## Executive Summary
This analysis is **tied directly** to the included dashboard. The dataset structure mirrors the dashboard data model and supports the same KPI calculations and visual breakdowns.

## What’s In This Folder
- `Dashboard/` — the actual dashboard file
- `Data/raw/` — raw CSV exports (messy/realistic inputs)
- `Data/clean/` — cleaned CSVs used for analysis + dashboard refresh
- `Docs/Dashboard_Field_Mapping.md` — exactly which CSV fields power which dashboard visuals/KPIs
- `Docs/Data_Dictionary.md` — definitions, business rules, and KPI formulas
- `SQL/` + `Python/` — analysis scripts (queries + notebooks-style python)

## How To Rebuild / Refresh The Dashboard With These CSVs
1. Open the dashboard in Power BI (`.pbix`) or Tableau (`.twbx`)
2. Replace the data source connections with the CSVs in `Data/clean/`
3. Validate KPIs using `Docs/Data_Dictionary.md`
4. Confirm visuals using `Docs/Dashboard_Field_Mapping.md`

## Deliverables (Recruiter-Friendly)
- Dashboard file ✅
- Raw + cleaned datasets ✅
- Data dictionary + field-to-visual mapping ✅
- SQL + Python analysis ✅


## Advanced SQL (Complex Queries)
This project includes **complex, production-style SQL** (CTEs, window functions, Pareto, funnel, cohort-style logic) in:
- `SQL/advanced_queries.sql`

Open that file to see:
- Funnel / stage conversion calculations
- Revenue concentration (Pareto / cumulative share)
- Segment-level lift and guardrails (A/B)
- Seller concentration + stockout impact (marketplace)
- Time-to-convert percentiles (journey)


## Challenges & Tradeoffs

- **Data Quality Issues:** Raw datasets contained missing values, duplicates, and inconsistent formats that required cleaning and validation.
- **Assumptions:** Some metrics (e.g., churn proxy, conversion attribution) were derived using business assumptions due to lack of full tracking data.
- **Data Granularity Limits:** Certain dashboards required aggregation, limiting deep drill-down analysis in some cases.
- **Simulated Data Constraints:** While realistic, datasets are simulated and may not capture all real-world edge cases.
- **Performance vs Accuracy:** Balancing query performance with complex calculations (window functions, joins) required optimization tradeoffs.
- **Tool Limitations:** Differences between Power BI, Tableau, SQL dialects, and Excel required adaptation of logic across tools.
