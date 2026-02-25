-- A/B Test — Advanced SQL Pack

-- 1) Conversion rate + relative lift with confidence-style summary (by device)
WITH base AS (
  SELECT
    device,
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions,
    SUM(revenue) AS revenue
  FROM ab_sessions_clean
  GROUP BY device, variant
),
rates AS (
  SELECT
    device,
    variant,
    sessions,
    conversions,
    1.0 * conversions / NULLIF(sessions,0) AS conversion_rate,
    1.0 * revenue / NULLIF(sessions,0) AS rev_per_session
  FROM base
),
pivot AS (
  SELECT
    device,
    MAX(CASE WHEN variant='Control' THEN conversion_rate END) AS cr_control,
    MAX(CASE WHEN variant='Variant B' THEN conversion_rate END) AS cr_variant_b,
    MAX(CASE WHEN variant='Control' THEN rev_per_session END) AS rps_control,
    MAX(CASE WHEN variant='Variant B' THEN rev_per_session END) AS rps_variant_b
  FROM rates
  GROUP BY device
)
SELECT
  device,
  cr_control,
  cr_variant_b,
  (cr_variant_b - cr_control) AS abs_lift,
  (cr_variant_b - cr_control) / NULLIF(cr_control,0) AS rel_lift,
  rps_control,
  rps_variant_b,
  (rps_variant_b - rps_control) AS rps_delta
FROM pivot
ORDER BY rel_lift DESC;

-- 2) Guardrail metrics: bounce rate change + engagement distribution (percentiles)
WITH b AS (
  SELECT
    variant,
    COUNT(*) AS sessions,
    AVG(CASE WHEN bounce=1 THEN 1 ELSE 0 END) AS bounce_rate,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY engagement_score) AS p50_engagement,
    PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY engagement_score) AS p90_engagement
  FROM ab_sessions_clean
  GROUP BY variant
)
SELECT * FROM b;

-- 3) Segment heterogeneity: lift by source x device (cube-like rollup)
WITH g AS (
  SELECT
    source,
    device,
    variant,
    COUNT(*) AS sessions,
    SUM(converted) AS conversions
  FROM ab_sessions_clean
  GROUP BY source, device, variant
),
r AS (
  SELECT
    source,
    device,
    variant,
    1.0*conversions/NULLIF(sessions,0) AS cr
  FROM g
),
p AS (
  SELECT
    source,
    device,
    MAX(CASE WHEN variant='Control' THEN cr END) AS cr_control,
    MAX(CASE WHEN variant='Variant B' THEN cr END) AS cr_b
  FROM r
  GROUP BY source, device
)
SELECT
  source,
  device,
  cr_control,
  cr_b,
  (cr_b-cr_control)/NULLIF(cr_control,0) AS rel_lift
FROM p
ORDER BY rel_lift DESC
FETCH FIRST 50 ROWS ONLY;