# Source data dictionary

All inputs are supplied **simulated** CSVs. Currency codes, generation seed, source owner and extraction timestamps were not supplied. The upgrade does not invent them. Raw bytes are preserved and hashed in `Results/manifest.json`.

## Contract conventions

All listed columns are required and non-null. Numeric fields must be finite and nonnegative; IDs and unit/seat counts must be positive. Binary fields accept 0/1 or true/false and normalize to 0/1. Dates parse as YYYY-MM-DD. Text is trimmed. Unknown columns, duplicate declared primary keys and orphan references fail the pipeline. Repeated event/fact rows without stable IDs are counted and preserved.

## users

Rows: **6,000**. Declared primary key: **user_id**. Source: `Data/raw/users_raw.csv`; output: `Data/clean/users_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `user_id` | integer | Dataset-local user identifier; not shared across projects. |
| `first_seen_date` | date | Recorded first observation date; not necessarily acquisition date. |
| `traffic_source` | text | Supplied user traffic-source category. |
| `device` | text | Source device category; category vocabulary differs by project. |
| `is_returning` | binary | Supplied returning-user flag; lookback definition unavailable. |
## journey_events
Rows: **17,354**. Declared primary key: **none supplied**. Source: `Data/raw/journey_events_raw.csv`; output: `Data/clean/journey_events_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `user_id` | integer | Dataset-local user identifier; not shared across projects. |
| `event_date` | date | Day-level event date; no timestamp or event identifier is available. |
| `journey_stage` | text | Source stage label; Signup is excluded from the ordered commerce path. |
| `stage_order` | integer | Source ordinal; describes nominal stage order, not verified event chronology. |
