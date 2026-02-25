# Dashboard Field Mapping (Visuals ↔ Data)

Use this file to explain *exactly* how the dashboard visuals are powered by the CSV tables.

## Table: `listings`
**Primary fields:** listing_id, seller_id, category, price, rating, in_stock
**KPIs/Visuals supported:**
- Listings by category
- Average rating distribution
- Stockout rate
- Price bands vs performance

## Table: `sales`
**Primary fields:** sale_date, listing_id, units_sold, seller_id, price, rating, in_stock, category, revenue
**KPIs/Visuals supported:**
- Revenue trend
- Revenue by seller (top sellers)
- Sales vs rating
- Stockouts impact on revenue
