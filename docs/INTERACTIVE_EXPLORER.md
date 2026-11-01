# Interactive Analytics Explorer — Source and Validation

Open [the standalone explorer](../demo/analytics-explorer.html) in your browser after downloading the file, or view it through a static site that serves HTML. The app runs **entirely offline**, uses no external network calls or third-party JavaScript, and requires no Power BI, Tableau or cloud account.

## What it shows

The explorer embeds aggregate results from these files:
- [SaaS onboarding](../01_SaaS_Product_Analytics_StreamFlow/Results/onboarding_funnel.csv) — time-ordered onboarding reach
- [Experiment summary](../02_AB_Test_Feature_Impact/Results/variant_summary.csv) — observed session conversion and guardrails
- [Ecommerce funnel](../03_Ecommerce_Product_Analytics/Results/funnel_by_segment.csv) — session-level conversion/abandonment by device and channel
- [Marketplace categories](../04_Amazon_Marketplace_Analytics/Results/category_performance.csv) — recorded category revenue and units
- [User journey reach](../05_User_Journey_Analytics/Results/stage_reach.csv) — *unordered* event-stage reach, not the strict chronological funnel

These CSVs are themselves derived from supplied simulated portfolio datasets, with independently checked Python/SQL reconciliations. **The explorer is a snapshot of repository results, not a live data feed or a native BI product.** It does not show raw user/session records.

## How to use

1. Select one of the five projects.
2. Choose a metric appropriate to that project.
3. Search for a group or segment, then change the sort order and number of visible rows.
4. Open the linked source CSV and compare values. Bars start at zero; the numeric labels preserve original units.
5. Review the project README, validation.json, quality.json and assumptions before interpreting the result.

## Verification and maintenance

Run `python -m unittest discover -s tests -v` in the repository root. `tests/test_explorer.py` loads the embedded JSON, compares the entire aggregate dataset **field by field** to each CSV, checks that all five related validation reports are passing, and checks the basic accessible/offline UI structure. If any CSV changes, regenerate the embedded snapshot from the updated result CSVs and re-run the tests before publishing.

`python -m portfolio.run` refreshes canonical SQL results, reconciliation evidence, reports and SHA-256 manifests. Run it before unit tests if source code or raw data change. The CI workflow executes both steps and records the results.

## Data and statistical limitations

- Results use simulated datasets, not actual business or customer outcomes.
- A/B testing assumes independent sessions and does not verify assignment randomization or real-world causal impact.
- Marketplace recorded revenue is not automatically GMV, orders or commission revenue.
- Journey stage reach is *not* the same as the six-step ordered funnel; some source timestamps violate expected sequence.
- Legacy native Power BI/Tableau workbooks are audited separately and may use different underlying datasets.
