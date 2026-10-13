# 📊 Data Analyst Portfolio | Jamie Christian

**Five reproducible business analyses • SQL • Python • Data quality • Statistical judgment**

[![Validate analysis](https://github.com/JamieChristian22/data-analyst-portfolio/actions/workflows/validate.yml/badge.svg)](https://github.com/JamieChristian22/data-analyst-portfolio/actions/workflows/validate.yml)

[LinkedIn](https://www.linkedin.com/in/jamiechristian2/) · [GitHub](https://github.com/JamieChristian22) · [Email](mailto:Jamiechristian331@gmail.com)

I use SQL and Python to turn business questions into traceable metrics, test data assumptions, and explain what a result can—and cannot—support. This portfolio uses **supplied simulated datasets**, with source limitations made explicit. It does not claim real client outcomes or production deployment.

## Start here

| Project | Business question | Verified finding | Explore |
| --- | --- | --- | --- |
| SaaS activation | Where does onboarding lose eligible users? | 698 paying users; 21.06% supplied churn-label rate among paying users | [Case study](01_SaaS_Product_Analytics_StreamFlow/README.md) · [SQL](01_SaaS_Product_Analytics_StreamFlow/SQL/analysis.sql) |
| A/B experiment | Is conversion higher, and how uncertain is the difference? | 19.84% → 23.08%; +3.24 percentage points; 95% interval +1.77 to +4.71 points | [Case study](02_AB_Test_Feature_Impact/README.md) · [SQL](02_AB_Test_Feature_Impact/SQL/analysis.sql) |
| Ecommerce | Where is funnel friction and merchandise concentration? | 12.15% session conversion; 64.24% cart abandonment; top 20% of SKUs contribute 31.42% of revenue | [Case study](03_Ecommerce_Product_Analytics/README.md) · [SQL](03_Ecommerce_Product_Analytics/SQL/analysis.sql) |
| Marketplace | Can recorded revenue be reconciled and seller exposure measured? | 1,830,085.36 recorded revenue; 9,019 rows differ from price × units | [Case study](04_Amazon_Marketplace_Analytics/README.md) · [SQL](04_Amazon_Marketplace_Analytics/SQL/analysis.sql) |
| User journey | Does stage reach agree with a valid chronological path? | 627 observed purchasers; 3,296 users have adjacent-stage date inversions | [Case study](05_User_Journey_Analytics/README.md) · [SQL](05_User_Journey_Analytics/SQL/analysis.sql) |

All numerical findings come from the included data and saved outputs. A/B inference assumes independent sessions; assignment metadata are unavailable. Revenue values use unspecified dataset currency units. Journey sequencing issues prevent a valid business-abandonment interpretation of the strict funnel.

## Run the full portfolio

Python **3.12**; no cloud subscription, database server, credentials or paid BI license required.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m portfolio.run
python -m unittest discover -s tests -v
```

Windows PowerShell: use `.venv\Scripts\Activate.ps1` to activate. See the [runbook](docs/RUNBOOK.md) for single-project execution and troubleshooting.

After running, open [index.html](index.html) locally for the report directory, or open a project's `REPORT.html`. GitHub displays HTML source; download the repository to view these offline reports. Read project READMEs directly on GitHub for the same findings.

## Evidence, not just screenshots

- **121,366 source rows across 10 CSVs** processed without altering raw source bytes.
- **93 run-time checks** covering contracts, relationships, query execution and independent metric reconciliation.
- **35 unit/integration tests** covering inference boundaries, bad data, temporal ordering, SQL edge cases and evidence integrity.
- Named executable SQLite queries export result tables. Independent pandas calculations reconcile headline metrics, ordered funnels and selected advanced calculations.
- SHA-256 manifests link results to source files, analysis code and actual software versions.
- GitHub Actions repeats execution and tests and checks numerical output drift. The badge reports remote CI status; local success does not imply a remote run has passed.

## Analytical decisions that matter

| Issue | Decision |
| --- | --- |
| Repeated events without event IDs | Preserve and quantify them; do not invent deduplication keys. |
| Missing stable customer IDs | Remove customer RFM claims rather than substitute session IDs. |
| Marketplace revenue differs from price × units | Report the discrepancy and preserve recorded revenue; no invented fee model. |
| Out-of-order journey dates | Separate unordered stage reach from ordered-path eligibility. |
| Incomplete experiment metadata | Report uncertainty and assumptions; no real rollout authorization. |
| Unsupported projected business impact | Replace with computed findings and recommendations for validation. |

## Existing BI and Excel assets

Native-file inspection found that all five legacy Power BI/Tableau dashboards use **different source datasets** from the canonical CSV analysis. These dashboards and their images remain preserved, with the mismatch documented rather than hidden.

The five Excel summaries have been corrected, formatted and checked against canonical data. Three source-aligned Tableau Hyper extracts provide 18 verified source/result tables. For the two legacy Power BI models, 19 independently calculated measure baselines and executable DAX Query View tests are included. **Power BI Desktop DAX evaluation and Tableau Desktop refresh/render are not claimed as completed.**

See the [native workbook verification report](verification/native/README.md), [machine-readable audit](verification/native/workbook_audit.json), and [Excel recalculation evidence](verification/native/excel_calc_verification.json).

## Technical organization

```text
portfolio/       Shared contracts, cleaning, statistics, SQL execution and reporting
tests/           Statistical, data-contract and SQL integration tests
docs/            Methodology, reproduction runbook and interview walkthrough
01_.../          SaaS activation and revenue quality
02_.../          Experiment inference and guardrails
03_.../          Ecommerce funnel and SKU concentration
04_.../          Marketplace revenue reconciliation and seller concentration
05_.../          Ordered journey and source chronology diagnostics
```

Each project contains immutable raw inputs, regenerated clean inputs, executable SQL, a Python entry point, source dictionaries, KPI lineage, query results, evidence manifests, a case study and an offline report. Local SQLite databases are recreated under the ignored `build/` directory.

[Methodology and limitations](docs/METHODOLOGY.md) · [Reproduction runbook](docs/RUNBOOK.md) · [Interview walkthrough](docs/INTERVIEW_GUIDE.md) · [Upgrade record](docs/UPGRADE_NOTES.md)
