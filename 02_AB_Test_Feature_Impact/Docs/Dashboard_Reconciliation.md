# Workbook reconciliation status

| Layer | Status | Evidence |
| --- | --- | --- |
| SQL and independent Python headline metrics | Passed | Results/validation.json |
| Corrected Excel formulas and source-cell perturbations | Passed | ../../verification/native/excel_formula_verification.json |
| Desktop Calc recalculation | See engine evidence | ../../verification/native/excel_calc_verification.json |
| Original Power BI/Tableau source alignment | Mismatch | ../../verification/native/workbook_audit.json |
| Replacement Hyper source data (Tableau projects) | Passed cell-level readback | ../../verification/native/tableau_extract_verification.json |
| Legacy Power BI DAX measures | Baselines and queries supplied; execution not run | ../../verification/native/ |
| Power BI/Tableau Desktop refresh and visual acceptance | Not run | Requires the native application |

The original BI dashboards are separate-data artifacts. An automatic refresh cannot make them equivalent to the canonical analysis because their source schemas, populations and metric definitions differ. For Tableau, rebuild the visual source from `Dashboard/Validated_Analysis.hyper`; for Power BI, import the actual canonical tables and implement the definitions in `KPI_Lineage.md`.

The Excel source sheets match the canonical clean CSVs. All summary expectations, formulas, perturbations, and actual recalculated outputs are recorded in the evidence directory. Calc is not Microsoft Excel; engine labels must remain accurate.

For legacy Power BI, the generated DAX tests compare its existing measures with expectations derived from its own embedded model. Passing those tests would verify that model's unfiltered measures, not prove alignment to unrelated CSV datasets or correctness of every filtered visual.
