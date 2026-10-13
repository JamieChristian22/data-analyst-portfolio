# Source data dictionary

All inputs are supplied **simulated** CSVs. Currency codes, generation seed, source owner and extraction timestamps were not supplied. The upgrade does not invent them. Raw bytes are preserved and hashed in `Results/manifest.json`.

## Contract conventions

All listed columns are required and non-null. Numeric fields must be finite and nonnegative; IDs and unit/seat counts must be positive. Binary fields accept 0/1 or true/false and normalize to 0/1. Dates parse as YYYY-MM-DD. Text is trimmed. Unknown columns, duplicate declared primary keys and orphan references fail the pipeline. Repeated event/fact rows without stable IDs are counted and preserved.

## web_sessions

Rows: **25,000**. Declared primary key: **session_id**. Source: `Data/raw/web_sessions_raw.csv`; output: `Data/clean/web_sessions_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `session_id` | integer | Unique session identifier; never a substitute for a stable customer ID. |
| `session_date` | date | Day-level session observation date. |
| `device` | text | Source device category; category vocabulary differs by project. |
| `channel` | text | Session acquisition channel. |
| `added_to_cart` | binary | Binary indicator that the session added a cart item. |
| `purchased` | binary | Binary indicator that the session purchased. |
## orders
Rows: **3,037**. Declared primary key: **session_id**. Source: `Data/raw/orders_raw.csv`; output: `Data/clean/orders_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `session_id` | integer | Unique session identifier; never a substitute for a stable customer ID. |
| `session_date` | date | Day-level session observation date. |
| `device` | text | Source device category; category vocabulary differs by project. |
| `channel` | text | Session acquisition channel. |
| `sku` | text | Product SKU identifier; one SKU per supplied order row. |
| `category` | text | Source product category. |
| `discount_applied` | binary | Binary observed discount flag, not a randomized treatment. |
| `order_value` | number | Recorded order value; refunds, taxes and shipping treatment unavailable. |
| `units` | integer | Units on the supplied single-row order. |
