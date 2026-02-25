# Dashboard Field Mapping (Visuals ↔ Data)

Use this file to explain *exactly* how the dashboard visuals are powered by the CSV tables.

## Table: `users`
**Primary fields:** user_id, signup_date, country, acquisition_channel, plan_tier
**KPIs/Visuals supported:**
- Signups trend by date
- Users by country
- Acquisition channel mix
- Users by plan tier

## Table: `events`
**Primary fields:** user_id, event_date, event_group, event_name
**KPIs/Visuals supported:**
- Onboarding funnel (Step 1–5)
- Feature usage over time
- Active users trend

## Table: `subscriptions`
**Primary fields:** user_id, plan_tier, mrr, seats, completed_step2, churned_within_90d, first_payment_date
**KPIs/Visuals supported:**
- MRR/ARR by tier
- Churn rate by tier
- Step 2 completion vs churn
- Enterprise revenue concentration
