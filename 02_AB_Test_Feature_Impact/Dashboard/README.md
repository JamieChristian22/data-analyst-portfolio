# Native dashboard status

The original PBIX/TWBX in this folder uses a different dataset from the canonical CSV analysis. Its embedded model/extract was inspected; it is preserved as a separate-data legacy asset. It is not certified as a refreshed view of `Data/clean/`.

See [the native verification report](../../verification/native/README.md) for exact source populations, formulas, native-engine evidence and remaining Desktop checks.

For Tableau projects, `Validated_Analysis.hyper` is a source-aligned replacement extract whose 18 tables across the three projects were compared cell by cell through Tableau Hyper. It is a data source, not a completed Tableau dashboard. Use individual Results tables for separate visuals; do not join aggregate tables to raw facts.

For Power BI projects, `verification/native/<project>/verify_legacy_measures.dax` tests the existing legacy model against independent baselines from its own embedded data. DAX execution and Desktop visual acceptance remain open.
