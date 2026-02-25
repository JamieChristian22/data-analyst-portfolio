-- User Journey — Advanced SQL Pack

-- 1) Stage-to-stage conversion (funnel) with window functions
WITH stage_users AS (
  SELECT
    journey_stage,
    COUNT(DISTINCT user_id) AS users
  FROM journey_events_clean
  GROUP BY journey_stage
),
ordered AS (
  SELECT
    journey_stage,
    users,
    CASE journey_stage
      WHEN 'Landing' THEN 1
      WHEN 'Browse' THEN 2
      WHEN 'Product View' THEN 3
      WHEN 'Add to Cart' THEN 4
      WHEN 'Checkout' THEN 5
      WHEN 'Purchase' THEN 6
      WHEN 'Signup' THEN 7
      ELSE 999
    END AS stage_order
  FROM stage_users
),
calc AS (
  SELECT
    journey_stage,
    users,
    stage_order,
    LAG(users) OVER (ORDER BY stage_order) AS prior_stage_users
  FROM ordered
)
SELECT
  journey_stage,
  users,
  prior_stage_users,
  1.0*users/NULLIF(prior_stage_users,0) AS stage_to_stage_conversion
FROM calc
ORDER BY stage_order;

-- 2) Checkout drop-off by segment (returning vs new, device, source)
WITH reached AS (
  SELECT
    u.traffic_source,
    u.device,
    u.is_returning,
    SUM(CASE WHEN e.journey_stage='Checkout' THEN 1 ELSE 0 END) AS checkout_events,
    SUM(CASE WHEN e.journey_stage='Purchase' THEN 1 ELSE 0 END) AS purchase_events
  FROM users_clean u
  LEFT JOIN journey_events_clean e ON e.user_id = u.user_id
  GROUP BY u.traffic_source, u.device, u.is_returning
)
SELECT
  traffic_source,
  device,
  is_returning,
  checkout_events,
  purchase_events,
  1.0*purchase_events/NULLIF(checkout_events,0) AS checkout_to_purchase_rate,
  1.0 - (1.0*purchase_events/NULLIF(checkout_events,0)) AS checkout_dropoff_rate
FROM reached
ORDER BY checkout_dropoff_rate DESC;

-- 3) Time-to-convert (days from first_seen to purchase) with percentiles
WITH first_seen AS (
  SELECT user_id, CAST(first_seen_date AS DATE) AS first_seen_date
  FROM users_clean
),
purchase AS (
  SELECT user_id, MIN(CAST(event_date AS DATE)) AS purchase_date
  FROM journey_events_clean
  WHERE journey_stage='Purchase'
  GROUP BY user_id
),
ttc AS (
  SELECT
    f.user_id,
    (purchase_date - first_seen_date) AS days_to_purchase
  FROM first_seen f
  JOIN purchase p ON p.user_id = f.user_id
)
SELECT
  AVG(days_to_purchase) AS avg_days_to_purchase,
  PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY days_to_purchase) AS p50_days,
  PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY days_to_purchase) AS p90_days
FROM ttc;