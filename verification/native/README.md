# Native workbook verification

This evidence package distinguishes **file inspection**, **data-engine execution**, **formula recalculation**, **Desktop refresh**, and **visual acceptance**. Passing one does not imply the others passed.

## What was found

| Asset | Embedded source | Relationship to the canonical analysis |
| --- | --- | --- |
| SaaS Tableau workbook | 25,000 StreamFlow events with app_open, subscribe and billing-delta fields | Different schema and population from the canonical users/subscriptions/events CSVs |
| A/B Tableau workbook | 12 aggregated experiment rows | Different grain and period from 12,000 canonical session rows |
| Ecommerce Power BI workbook | Customer, order, payment, product and session model | Different schema and grain from canonical web_sessions/orders CSVs |
| Marketplace Power BI workbook | Dimensional model with 85,000 fact_orders rows | Different source from 24,000 canonical sales rows |
| Journey Tableau workbook | 4,066 extracted user-journey records | Different schema and population from canonical users/event-stage CSVs |

These are verified **source mismatches**, not merely “refresh pending.” Do not relabel a legacy screenshot as a chart of the canonical CSV analysis. Legacy native files are preserved for inspection; they have not been silently rewritten to hide the mismatch.

## Delivered evidence

- `original_workbook_audit.json`: first audit, including pre-repair Excel formulas and missing caches. Its initial Hyper attempts document a socket startup failure; the later final audit uses supported TCP transport.
- `workbook_audit.json`: final source/table/formula audit. Tableau extract reads use the native Hyper engine; PBIX data and metadata are decoded with PBIXRay.
- `excel_formula_verification.json`: corrected summary formulas, independent expected values, and source-cell perturbation tests in Artifact Tool.
- `excel_calc_verification.json`: separate desktop Calc recalculation evidence, including cache-cleared inputs and disposable changed-input copies. This is not Microsoft Excel execution.
- `tableau_extract_verification.json`: cell-level readback verification for all 18 tables in the three new `Validated_Analysis.hyper` files.
- Per-Power-BI folders: exported DAX, Power Query, relationships, schema, independently calculated measure expectations, and runnable `verify_legacy_measures.dax` queries. DAX evaluation in Power BI Desktop is **not run** here.
- `previews/`: rendered corrected Excel summary sheets.

## How to complete Power BI Desktop acceptance

1. Open the exact original PBIX identified by the baseline file and SHA-256.
2. Use DAX Query View to execute `verify_legacy_measures.dax`. It evaluates the original model's measures against expectations derived from that same embedded model. It does not compare unrelated CSV datasets.
3. Export the returned table to CSV and run `python scripts/verify_powerbi_export.py --project 03 --csv path/to/export.csv` (use `04` for Marketplace). The verifier checks numbers itself and rejects missing or duplicate metrics and stale PBIX hashes.
4. Inspect relationships, report filters and slicers. Record page-by-page visual checks and a screenshot or PDF after refresh.
5. To instead present the canonical CSV analysis in Power BI, rebuild the native model against its actual canonical tables and metric definitions. The existing native measures are not drop-in equivalents.

## How to use the verified Tableau replacement sources

1. Open `Dashboard/Validated_Analysis.hyper` in Tableau. It contains `Source` tables and separate `Results` tables.
2. Use each Results table as an independent pre-aggregated source for its corresponding visual. Do not join aggregate Results tables to raw facts and multiply totals.
3. Rebuild the workbook visuals using `Docs/KPI_Lineage.md`. An automatic swap into the legacy workbook is unsafe because the columns and populations differ.
4. Compare displayed totals under identical filters to the Results CSVs. Check native calculated fields, tooltips, sorting and filters.
5. Save a new TWBX and capture the refreshed view. Opening and querying the Hyper extract does not establish Tableau Desktop visual acceptance.

## Reproduce machine checks

```bash
python -m pip install -r requirements.txt
python -m pip install -r verification/native/requirements.txt
python scripts/audit_native.py
python scripts/build_tableau_extracts.py
python scripts/powerbi_measure_baselines.py
python -m unittest discover -s tests -v
```

Hyper telemetry is disabled. `use_tcp_port=auto` is the documented local transport option used in this environment. These scripts do not publish files or require access to the cloud accounts referenced by old workbook connections.

## Tool references

- [Tableau Hyper process settings](https://tableau.github.io/hyper-db/docs/hyper-api/hyper_process/)
- [Tableau Hyper read guide](https://tableau.github.io/hyper-db/docs/guides/hyper_file/read/)
- [PBIXRay read-only model extraction](https://github.com/Hugoberry/pbixray)

Native Power BI Desktop and Tableau Desktop refresh/render checks are still required. The evidence package does not declare the entire portfolio 10/10 or manufacture passing native-application results.
