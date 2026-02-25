# Dashboard Field Mapping (Visuals ↔ Data)

Use this file to explain *exactly* how the dashboard visuals are powered by the CSV tables.

## Table: `users`
**Primary fields:** user_id, first_seen_date, traffic_source, device, is_returning
**KPIs/Visuals supported:**
- Users by source/device
- Returning user share
- Cohorts by first_seen_date

## Table: `journey_events`
**Primary fields:** user_id, event_date, journey_stage, stage_order
**KPIs/Visuals supported:**
- Journey funnel drop-off by stage
- Stage-to-stage conversion
- Time-to-convert distribution
