# Source data dictionary

All inputs are supplied **simulated** CSVs. Currency codes, generation seed, source owner and extraction timestamps were not supplied. The upgrade does not invent them. Raw bytes are preserved and hashed in `Results/manifest.json`.

## Contract conventions

All listed columns are required and non-null. Numeric fields must be finite and nonnegative; IDs and unit/seat counts must be positive. Binary fields accept 0/1 or true/false and normalize to 0/1. Dates parse as YYYY-MM-DD. Text is trimmed. Unknown columns, duplicate declared primary keys and orphan references fail the pipeline. Repeated event/fact rows without stable IDs are counted and preserved.

## ab_sessions

Rows: **12,000**. Declared primary key: **session_id**. Source: `Data/raw/ab_sessions_raw.csv`; output: `Data/clean/ab_sessions_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `session_id` | integer | Unique session identifier; never a substitute for a stable customer ID. |
| `session_date` | date | Day-level session observation date. |
| `variant` | text | Experiment arm: Control or Variant B; allocation metadata unavailable. |
| `device` | text | Source device category; category vocabulary differs by project. |
| `source` | text | Experiment traffic-source category. |
| `converted` | binary | Binary conversion indicator per session. |
| `engagement_score` | number | Synthetic engagement score; measurement scale is not independently specified. |
| `bounce` | binary | Binary bounce indicator per session. |
| `revenue` | number | Recorded revenue in dataset currency units; accounting treatment is not supplied. |
