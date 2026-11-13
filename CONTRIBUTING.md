# Contributing to the Data Analyst Portfolio

Thanks for helping make these **synthetic-data analytics examples** easier to understand, validate, and reproduce. Contributions should improve educational usefulness while preserving documented evidence and limitations.

## Useful contributions

- Fix a broken link, confusing explanation, or accessibility problem.
- Add a small, reproducible analytics test or an edge case with clear expected behavior.
- Improve a KPI definition, method explanation, or an input-to-output trace.
- Improve documentation for the [offline analytics explorer](demo/analytics-explorer.html).

For larger changes, [open an issue](https://github.com/JamieChristian22/data-analyst-portfolio/issues) before doing substantial work. Check existing issues and pull requests to avoid duplication.

## Local verification

Use Python 3.12 and a fresh local clone. The portfolio run regenerates reports and derived outputs, so review file changes before committing.

```bash
git clone https://github.com/JamieChristian22/data-analyst-portfolio.git
cd data-analyst-portfolio
python -m pip install -r requirements.txt
python -m portfolio.run
python -m unittest discover -s tests -v
```

For platform-specific environment setup and detailed instructions, use the [README reproducibility section](README.md#-reproduce-the-portfolio) and [runbook](docs/RUNBOOK.md).

## Pull request checklist

1. Keep the change narrow and describe the analytics or documentation problem it solves.
2. Document source and licensing for any new asset; prefer small first-party synthetic fixtures.
3. Report tests **actually run** and any limitations; do not claim passing tests if they were not executed.
4. Keep metric definitions consistent with their source CSVs and existing validation checks.
5. Explain whether the change alters calculations, reports, or only documentation.
6. Link the relevant issue if one exists.

## Data rights and privacy

The repository includes simulated scenarios, but some tracked asset provenance remains **unverified**; see [reviewer guidance](REVIEWER_GUIDE.md). Do not add real customer records, passwords, keys, restricted datasets, or externally sourced assets without appropriate permission and attribution. Do not present modeled impacts as verified business outcomes.

Submission does not guarantee acceptance. Respect any repository security and community policies.

[Back to repository overview](README.md)
