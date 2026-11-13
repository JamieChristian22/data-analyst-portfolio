# Small data analytics community tasks — verify, explain, improve

These tasks are suitable for curious analysts and contributors who want to understand a metric before changing it. The project uses simulated data, and some third-party asset provenance requires review. Start with [the offline explorer guide](INTERACTIVE_EXPLORER.md), [runbook](RUNBOOK.md), and [contributing instructions](../CONTRIBUTING.md).

**No paid tools required:** the standalone explorer can run in a browser after the HTML file is downloaded; the Python workflow has the prerequisites in the root README. These tasks are **not paid bounties**.

## Task 1 — Trace one visible KPI to its source

1. Download [analytics-explorer.html](../demo/analytics-explorer.html) to open it locally without Power BI/Tableau or a cloud subscription.
2. Pick **one** displayed metric (for example, a conversion rate, a marketplace category total, or stage reach).
3. Use the [source and validation guide](INTERACTIVE_EXPLORER.md) to locate its CSV input and definition.
4. Explain the numerator, denominator, segmentation and assumptions in plain English. Look for missing qualifications, not just numerical discrepancies.

**Acceptance:** a new reader can reproduce your interpretation from the listed source, and you don't mistake unordered stage reach for a chronological funnel.

## Task 2 — Propose a meaningful data-quality test

1. Read the documented [metric validation rules](../portfolio/metrics.py) and existing [regression tests](../tests/test_metrics.py).
2. Identify **one** missing-value, duplicate, invalid-count or experiment-allocation edge case.
3. Explain the correct expected behavior, with tiny first-party synthetic input.
4. Discuss significant changes in an issue before opening a code PR.

**Acceptance:** the idea is focused, respects original dataset provenance and states the behavior it verifies. Do not claim a test passed unless you ran it.

## Task 3 — Improve the offline reader experience

1. Try [the standalone explorer](../demo/analytics-explorer.html) using keyboard navigation and a small browser viewport.
2. Identify one specific obstacle, ambiguous label, color-only interpretation, or misleading text.
3. Propose a small fix with before/after explanation.

**Acceptance:** preserve the explorer's offline-first nature and avoid third-party network dependencies.

## How to contribute

- Follow [CONTRIBUTING.md](../CONTRIBUTING.md); check [open issues](https://github.com/JamieChristian22/data-analyst-portfolio/issues) and pull requests first.
- Run and report only checks you actually complete. Python 3.12 instructions and the test command are in the contributor guide.
- Avoid sensitive, proprietary or real customer data. Do not add third-party material with unverified redistribution rights.
- Sponsorship is [optional](https://github.com/sponsors/JamieChristian22) and not required to access tasks or submit improvements.
