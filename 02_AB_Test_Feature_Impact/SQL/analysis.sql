-- name: variant_summary
SELECT variant,COUNT(*) AS sessions,SUM(converted) AS conversions,
 AVG(1.0*converted) AS conversion_rate,AVG(1.0*bounce) AS bounce_rate,
 AVG(engagement_score) AS mean_engagement,SUM(revenue) AS revenue,
 AVG(revenue) AS revenue_per_session
FROM ab_sessions_clean GROUP BY variant ORDER BY variant;
-- name: segment_conversion
SELECT device, source, variant, COUNT(*) AS sessions,SUM(converted) AS conversions,
 AVG(1.0*converted) AS conversion_rate
FROM ab_sessions_clean GROUP BY device,source,variant ORDER BY device,source,variant;
-- name: daily_assignment
SELECT session_date, variant,COUNT(*) AS sessions,SUM(converted) AS conversions
FROM ab_sessions_clean GROUP BY session_date,variant ORDER BY session_date,variant;
