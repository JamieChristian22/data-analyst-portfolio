# Reproduction and troubleshooting runbook

## Setup

Use Python 3.12. In the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m portfolio.run
python -m unittest discover -s tests -v
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1`.

For a single project, pass `--project 02_AB_Test_Feature_Impact`. For an alternate source tree, use `--root /absolute/path/to/repository`. The per-project `Python/analysis.py` entry points also work from any working directory. No credentials, external database, cloud account or paid software are required for the verified workflow.

## Outputs

- `Data/clean/`: normalized datasets, regenerated from immutable raw files.
- `Results/*.csv`: one table for every named SQL query.
- `Results/additional_metrics.json`: experiment statistics or supplementary estimates.
- `Results/quality.json`: row counts, repeated-row diagnostics, source limitations and hashes.
- `Results/validation.json`: successful execution/reconciliation checks.
- `Results/query_plans.json`: local SQLite query plans.
- `Results/manifest.json`: source, code and result hashes plus actual dependency versions.
- `REPORT.html`: standalone, offline report. Download/open locally; GitHub's file viewer shows HTML source.
- `build/`: recreated local SQLite databases and overall run summary; excluded from git.

## Failures

| Failure | Response |
| --- | --- |
| Missing dependency | Activate the environment and install the pinned requirements. |
| Schema/null/type failure | Locate the source column, confirm contract with source owner, fix or explicitly version the policy. |
| Duplicate declared key / orphan | Investigate source extraction and relationship grain. Do not silently deduplicate. |
| SQL/Python mismatch | Compare populations, filters, windows, join multiplicity, units and null treatment. |
| Result checksum mismatch | Rebuild results from the current code and sources; investigate unexpected edits. |
| BI totals differ | Use Docs/Dashboard_Reconciliation.md; check embedded data and filters before presenting. |

A nonzero run invalidates success evidence for the failed project and can leave partial outputs. Rerun successfully before consumption. To test determinism, hash result files, rerun with the same environment and compare the hashes. Software-version metadata can differ across environments; CSV metric comparisons are the CI drift gate.

## CI

The GitHub Actions workflow builds all projects, runs tests, checks numerical output drift and uploads evidence. Local test success is recorded separately from remote CI. Do not describe a remote workflow as passing until GitHub reports completion for the relevant commit.
