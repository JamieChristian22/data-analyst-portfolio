# Source data dictionary

All inputs are supplied **simulated** CSVs. Currency codes, generation seed, source owner and extraction timestamps were not supplied. The upgrade does not invent them. Raw bytes are preserved and hashed in `Results/manifest.json`.

## Contract conventions

All listed columns are required and non-null. Numeric fields must be finite and nonnegative; IDs and unit/seat counts must be positive. Binary fields accept 0/1 or true/false and normalize to 0/1. Dates parse as YYYY-MM-DD. Text is trimmed. Unknown columns, duplicate declared primary keys and orphan references fail the pipeline. Repeated event/fact rows without stable IDs are counted and preserved.

## users

Rows: **1,500**. Declared primary key: **user_id**. Source: `Data/raw/users_raw.csv`; output: `Data/clean/users_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `user_id` | integer | Dataset-local user identifier; not shared across projects. |
| `signup_date` | date | Recorded signup date; start of onboarding/activity observation. |
| `country` | text | Country code as supplied; no geographic enrichment. |
| `acquisition_channel` | text | Supplied acquisition attribution category. |
| `plan_tier` | text | Supplied plan category: Free, Starter, Pro or Enterprise. |
## subscriptions
Rows: **1,500**. Declared primary key: **user_id**. Source: `Data/raw/subscriptions_raw.csv`; output: `Data/clean/subscriptions_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `user_id` | integer | Dataset-local user identifier; not shared across projects. |
| `plan_tier` | text | Supplied plan category: Free, Starter, Pro or Enterprise. |
| `mrr` | number | Supplied monthly recurring revenue snapshot in dataset currency units. |
| `seats` | integer | Supplied subscription seat count. |
| `completed_step2` | binary | Supplied Step 2 completion flag, checked against event presence. |
| `churned_within_90d` | binary | Supplied binary outcome label; lifecycle events and cohort cutoff are unavailable. |
| `first_payment_date` | date | Supplied payment date, including free-plan records; not independent proof of a paid subscription. |
## events
Rows: **29,175**. Declared primary key: **none supplied**. Source: `Data/raw/events_raw.csv`; output: `Data/clean/events_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `user_id` | integer | Dataset-local user identifier; not shared across projects. |
| `event_date` | date | Day-level event date; no timestamp or event identifier is available. |
| `event_group` | text | Source event grouping (Onboarding or Product). |
| `event_name` | text | Named source event, including onboarding steps and Workflow Run. |
