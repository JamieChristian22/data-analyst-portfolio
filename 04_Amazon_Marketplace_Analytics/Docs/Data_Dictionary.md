# Source data dictionary

All inputs are supplied **simulated** CSVs. Currency codes, generation seed, source owner and extraction timestamps were not supplied. The upgrade does not invent them. Raw bytes are preserved and hashed in `Results/manifest.json`.

## Contract conventions

All listed columns are required and non-null. Numeric fields must be finite and nonnegative; IDs and unit/seat counts must be positive. Binary fields accept 0/1 or true/false and normalize to 0/1. Dates parse as YYYY-MM-DD. Text is trimmed. Unknown columns, duplicate declared primary keys and orphan references fail the pipeline. Repeated event/fact rows without stable IDs are counted and preserved.

## listings

Rows: **1,800**. Declared primary key: **listing_id**. Source: `Data/raw/listings_raw.csv`; output: `Data/clean/listings_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `listing_id` | integer | Listing identifier; join sales to listings on this field. |
| `seller_id` | integer | Seller identifier; multiple listings can belong to one seller. |
| `category` | text | Source product category. |
| `price` | number | Supplied listing/unit price snapshot. |
| `rating` | number | Listing rating on a 0–5 scale. |
| `in_stock` | binary | Undated binary listing stock snapshot; not historical inventory. |
## sales
Rows: **24,000**. Declared primary key: **none supplied**. Source: `Data/raw/sales_raw.csv`; output: `Data/clean/sales_clean.csv`.
| Column | Type | Definition |
| --- | --- | --- |
| `sale_date` | date | Day-level recorded sale date. |
| `listing_id` | integer | Listing identifier; join sales to listings on this field. |
| `units_sold` | integer | Recorded units per sale row; sale/order ID is unavailable. |
| `seller_id` | integer | Seller identifier; multiple listings can belong to one seller. |
| `price` | number | Supplied listing/unit price snapshot. |
| `rating` | number | Listing rating on a 0–5 scale. |
| `in_stock` | binary | Undated binary listing stock snapshot; not historical inventory. |
| `category` | text | Source product category. |
| `revenue` | number | Recorded revenue in dataset currency units; accounting treatment is not supplied. |
