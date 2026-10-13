# KPI lineage and business rules

SQL dialect: SQLite 3.25+; tested runtime recorded in the manifest. Each result name maps to a named section in `SQL/analysis.sql`. Additional statistical estimates are computed in `portfolio/metrics.py` and reconciled in `portfolio/run.py`.

| Metric | Calculation / denominator | Result file | Interpretation |
| --- | --- | --- | --- |
| snapshot_mrr | SUM(mrr), all supplied subscription rows | summary.csv | Snapshot only; not verified active MRR. |
| snapshot_arr | 12 × snapshot_mrr | summary.csv | Annualization, not recognized revenue. |
| paying_churn_label_rate | SUM(churned label where mrr > 0) / COUNT(mrr > 0) | summary.csv | Free rows excluded; label is not independently reconstructed. |
| ordered onboarding | Unique users reaching all preceding steps on/after signup, in nondecreasing date order | onboarding_funnel.csv | Same-day ties allowed; earliest eligible retry used. |
| power-user association | 20+ Workflow Run events in [signup, signup+90 days), compared within paying users | power_user_association.csv | Includes zero-activity users in comparison; correlation only. |
