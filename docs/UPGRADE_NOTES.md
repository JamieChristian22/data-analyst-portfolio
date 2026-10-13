# Upgrade record

## Scope

Rebuilt the analysis layer for all five existing projects, preserving all ten original raw CSVs and every original BI/Excel/image asset. The upgrade is based on main commit `5887f7940282859197689b60e41be3e5a8287724`.

## What changed

- Replaced placeholder Python scripts with per-project entry points into a shared executable pipeline.
- Consolidated active SQL in named, executable SQLite query sections. The old `advanced_queries.sql` paths now direct readers to the canonical executable file.
- Added typed contracts, relationship validation, conservative cleaning and visible source-quality diagnostics.
- Corrected customer/session identity misuse, funnel eligibility and temporal order, paying-user churn denominator, market revenue labels and experiment uncertainty.
- Replaced unsupported outcomes with computed findings and explicitly conditional recommendations.
- Added case studies, offline HTML reports with source-driven charts, source dictionaries, KPI lineage, native-workbook reconciliation checklists, query plans and content hashes.
- Added unit/integration tests and a CI workflow that runs the complete analysis and checks numerical result drift.
- Corrected the LinkedIn profile link.

## Evidence

The local full build processed 121,366 rows and passed 93 validation/reconciliation checks. Thirty unit/integration tests passed. Evidence manifests record the actual environment and source/code/output hashes. Remote CI status must be read from GitHub for the relevant commit; it is not inferred from local execution.

## Meaningful discoveries

- SaaS event inputs have 481 exact-repeat rows with no stable event ID. They remain preserved and disclosed.
- Marketplace inputs have 140 exact-repeat rows and 9,019 revenue-vs-price×units discrepancies. They are not silently repaired.
- Journey inputs contain 3,296 users with adjacent-stage date inversions. Unordered purchase reach and ordered-path completion answer different questions; the latter is not presented as validated customer abandonment.
- The top-20% ecommerce SKU share is 31.42%, not the previous 68% claim.
- The experiment's observed relative conversion lift is 16.33%, with an absolute lift of 3.24 percentage points and a 95% difference interval of 1.77–4.71 points under stated assumptions.

## Remaining limits

Native Power BI/Tableau/Excel refresh and internal-measure reconciliation have not been performed. Source generation, accounting semantics and experiment assignment metadata were not supplied. No production deployment, real commercial impact, independent external review or guaranteed hiring outcome is claimed.

## Native verification update

Added an audit of all ten original workbooks, corrected all five Excel summaries, verified their formulas in Artifact Tool and desktop Calc, and added source-cell perturbation evidence. Built three replacement Tableau Hyper sources with 18 cell-verified tables. Decoded both PBIX models and supplied 19 independent measure baselines with DAX queries. All five legacy native dashboards were confirmed to use different source datasets; this mismatch remains explicit and is not converted into a passing certification. See the latest validation record and native evidence report.
