# Dashboard Field Mapping (Visuals ↔ Data)

Use this file to explain *exactly* how the dashboard visuals are powered by the CSV tables.

## Table: `web_sessions`
**Primary fields:** session_id, session_date, device, channel, added_to_cart, purchased
**KPIs/Visuals supported:**
- Sessions by channel/device
- Funnel: session→cart→purchase
- Cart abandonment rate

## Table: `orders`
**Primary fields:** session_id, session_date, device, channel, sku, category, discount_applied, order_value, units
**KPIs/Visuals supported:**
- Revenue by category
- Top SKUs (Pareto)
- AOV by discount/device
- Units sold trend
