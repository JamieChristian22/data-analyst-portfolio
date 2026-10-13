# Methodology, source limits and analytical decisions

## Source provenance

The ten original CSVs were already in the repository at commit `5887f7940282859197689b60e41be3e5a8287724`. They are simulated portfolio data. No source-generation script, seed, external data license, experiment assignment log, event ID or currency code was provided. Raw data are preserved byte-for-byte. The repository MIT license covers the repository as provided; this upgrade does not claim third-party ownership or an independently verified upstream license.

## Pipeline and trust boundary

Raw CSV → schema/type/range/key validation → clean CSV → SQLite tables → named SQL queries → result CSVs → independent pandas reconciliation → statistical estimates → case study and HTML report → SHA-256 evidence manifest.

The runner fails on null required values, invalid dates/booleans, nonfinite or out-of-contract numbers, unexpected schema, duplicate declared keys, broken relationships and metric disagreements. It invalidates old success evidence before starting a project. A failed run may leave partial result files: consumers must require both a current manifest and passing validation, and must rerun after fixing the source. Do not use an old HTML report after a failed run.

Cleaning is intentionally conservative. Type normalization and trimming are permitted. There is no fabricated dirty dataset. Duplicate event and sales rows without stable event IDs are retained because repeated legitimate activity cannot be distinguished from ingestion duplicates. Exact-repeat counts are published. Source anomalies and missing context remain visible in `quality.json`.

## SQL portability and performance

All active SQL targets SQLite 3.25+ rather than mixing warehouse dialects. Use Python 3.12 with the pinned environment. The runner creates primary/foreign-key lookup indexes and records `EXPLAIN QUERY PLAN` for each query. This demonstrates the local execution plan, not warehouse-scale performance or a production benchmark. SQLite date functions operate on normalized ISO dates. `NULLIF` makes empty denominators undefined rather than zero.

## Statistical interpretation

The experiment's primary comparison is overall session conversion. Report absolute lift in percentage points, relative lift as a ratio, a 95% Newcombe-Wilson difference interval, and a two-sided pooled two-proportion z-test. The sample-ratio diagnostic tests an explicitly assumed 50:50 allocation. Segment analysis and guardrail metrics are exploratory; there is no familywise multiple-testing adjustment. Session independence, intended allocation and absence of sequential peeking cannot be verified. A small p-value is not permission to launch a real feature from simulated data.

## Funnels and chronology

Stage reach counts users with an event, independent of prior steps. An ordered funnel requires each user to have every preceding stage at an eligible date and uses the earliest eligible retry. Day-level ties are allowed. Source stage ordinals do not repair event timestamps. The journey data contain date-order inversions; strict path loss must be interpreted as a tracking/synthetic-data diagnostic, not automatically as checkout abandonment. Signup is reported separately instead of requiring signup after purchase.

## Business claims

No projected revenue benefit is presented as realized revenue. No causal retention, inventory or discount impact is inferred from observational segments. Customer RFM is omitted because stable customer IDs are absent. Marketplace sales rows are not orders, and recorded revenue is not platform commission revenue. Churn is a supplied label, not an independently reconstructed lifecycle metric. These limits are part of the analysis and interview story.

## Validation scope

Thirty-five unit/integration tests cover statistical boundaries, known Wilson interval values, arm-swap symmetry, invalid contracts, duplicate policies, orphan relationships, chronological retry handling, zero denominators, top-20% SKU rounding and source/output integrity. The full run adds per-project checks and independently reconciles headline metrics, ordered funnels and selected advanced metrics. Not every segmented output is independently reimplemented; all named SQL queries are executed. Native workbook inspection, Excel repair/recalculation and Hyper data-source verification are recorded under verification/native. Power BI/Tableau Desktop refresh and visual acceptance remain separate gates.
