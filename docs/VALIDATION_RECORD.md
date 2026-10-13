# Validation record

## Core analysis

- Five complete workflows processed 121,366 source rows.
- 93 source, relationship, execution and reconciliation checks passed.
- 35 unit/integration tests passed, including rejecting forged PASS flags, missing/duplicate metrics and nonfinite values in imported Power BI evidence.
- Original raw CSVs and original Power BI/Tableau/image assets remain unchanged.

## Excel repair and verification

- Corrected the SaaS churn formula to use paying accounts and normalized boolean flags to numeric 0/1.
- Expanded and formatted all five summaries with source-linked calculations and definitions.
- All ten Excel source sheets match their canonical CSVs.
- All 23 summary formulas match independently calculated expectations in Artifact Tool and LibreOffice Calc.
- All five workbooks passed source-cell perturbation tests in both engines.
- Calc test copies had formula caches removed before opening, establishing recalculation rather than inspection of preexisting cached answers.
- All five summary views were rendered and visually inspected. Source sheets were preserved and value-checked.
- Microsoft Excel itself was not executed.

## Tableau

- All three original Hyper extracts opened through Tableau's native engine.
- Three new source-aligned Hyper files contain 18 source/result tables. Every table was read back and compared cell by cell.
- These new extracts are data sources, not rebuilt Tableau workbooks. Tableau Desktop refresh, rendering and interactive filter behavior have not been tested.

## Power BI

- Both original PBIX files were decoded, including actual embedded tables, DAX measures, Power Query, relationships and report-page inventory.
- Nineteen independent measure baselines and DAX Query View verification queries were generated.
- Power BI Desktop DAX execution, refresh and visual acceptance were not performed.

## Material finding

All five original native BI dashboards use different datasets from the canonical analysis. They are not certified as refreshed views of the canonical CSVs. The audit distinguishes this mismatch from data-engine readability and numerical checks.

See verification/native/SUMMARY.json for current evidence counts and verification/native/README.md for reproduction and remaining steps. Remote GitHub CI remains unexecuted because the integration denied branch creation. HTML browser review remains unperformed; Excel summary image review is complete.
