# Rebuild and connect

1. Follow the root README to install the pinned Python environment.
2. Run `python -m portfolio.run --project 02_AB_Test_Feature_Impact`. Stop if it exits nonzero.
3. Open `REPORT.html` for the generated analysis report.
4. For Power BI or Tableau, import individual `Results/*.csv` tables or `Data/clean/*.csv`. Use the documented source grain; avoid many-to-many fact joins.
5. Rebuild measures from `KPI_Lineage.md`; do not sum pre-aggregated percentages.
6. Compare headline values, denominators, filters and time windows with `Results/`. Record evidence before marking a workbook reconciled.

Local SQLite database: `build/02_AB_Test_Feature_Impact/analysis.sqlite`. The directory is intentionally excluded from git; the build recreates it.
