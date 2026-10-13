# Interview walkthrough

## A concise opening

“I built five analyses around product activation, experimentation, ecommerce, marketplace revenue and user journeys. Each starts with supplied simulated CSVs, validates source contracts, executes SQLite queries and exports results. I independently reconcile headline calculations in Python and keep source hashes and test evidence. The most useful part was finding where the initial business claims exceeded what the data could support.”

## Explain one project in five minutes

1. Name the stakeholder question and the decision it supports.
2. State the source grain, join keys and observation window.
3. Open one SQL query and explain its denominator, join cardinality and edge cases.
4. Open the matching Results CSV and validation checks.
5. Give the supported finding, a recommended next action and the strongest limitation.

## Questions to practice

**Why didn't you remove every duplicate?** There are no stable IDs for SaaS events or marketplace sale records. Identical rows may represent repeat events. I preserve them and report the repeat count, while failing duplicate primary keys in tables where uniqueness is declared.

**How did you verify the SQL?** All queries execute against databases built from supplied CSVs. Independent pandas calculations reconcile headline metrics, ordered funnels and selected advanced metrics. Fixture tests also check retries, out-of-order events, empty denominators and rounding.

**What did you change in the funnel?** Counting users at each stage alone does not establish a valid path. I added sequential eligibility and date constraints, including valid retries. Source chronology problems are surfaced rather than relabeled as customer abandonment.

**What does experiment lift mean?** Absolute lift is treatment rate minus control rate; relative lift divides that change by the control rate. I report uncertainty and the assumptions that session-level data cannot verify.

**Why no RFM?** There is no stable customer ID. Treating a session as a customer would misrepresent purchase frequency and retention.

**How do you handle a failed refresh?** The process exits nonzero and invalidates prior success evidence. I inspect the failing contract or reconciliation, resolve the source or documented business rule, then rerun. I do not adjust source values to make a test pass.

**What remains before operational use?** Verified upstream provenance, stakeholder-approved definitions, true transaction/event IDs, appropriate observation windows, security/access design, scheduling and monitored refreshes. Legacy BI files also need native-tool reconciliation.

## Do not overclaim

Describe this as reproducible simulated analysis. Do not claim employment at Amazon, real client revenue improvements, a production deployment or native workbook refresh you did not perform. Be ready to explain and edit the code yourself before listing a technique as an interview strength.
