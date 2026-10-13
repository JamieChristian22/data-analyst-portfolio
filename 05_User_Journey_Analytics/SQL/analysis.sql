-- name: summary
SELECT COUNT(*) AS users,
 (SELECT COUNT(DISTINCT user_id) FROM journey_events_clean WHERE journey_stage='Purchase') AS purchasers,
 1.0*(SELECT COUNT(DISTINCT user_id) FROM journey_events_clean WHERE journey_stage='Purchase')/NULLIF(COUNT(*),0) AS observed_purchase_rate
FROM users_clean;
-- name: ordered_funnel
WITH s0 AS (SELECT user_id, first_seen_date AS reached FROM users_clean),
s1 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM journey_events_clean e WHERE e.user_id=p.user_id AND e.journey_stage='Landing' AND e.event_date>=p.reached) AS reached FROM s0 p WHERE p.reached IS NOT NULL),
s2 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM journey_events_clean e WHERE e.user_id=p.user_id AND e.journey_stage='Browse' AND e.event_date>=p.reached) AS reached FROM s1 p WHERE p.reached IS NOT NULL),
s3 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM journey_events_clean e WHERE e.user_id=p.user_id AND e.journey_stage='Product View' AND e.event_date>=p.reached) AS reached FROM s2 p WHERE p.reached IS NOT NULL),
s4 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM journey_events_clean e WHERE e.user_id=p.user_id AND e.journey_stage='Add to Cart' AND e.event_date>=p.reached) AS reached FROM s3 p WHERE p.reached IS NOT NULL),
s5 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM journey_events_clean e WHERE e.user_id=p.user_id AND e.journey_stage='Checkout' AND e.event_date>=p.reached) AS reached FROM s4 p WHERE p.reached IS NOT NULL),
s6 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM journey_events_clean e WHERE e.user_id=p.user_id AND e.journey_stage='Purchase' AND e.event_date>=p.reached) AS reached FROM s5 p WHERE p.reached IS NOT NULL)
SELECT 1 AS step, 'Landing' AS stage, COUNT(reached) AS users FROM s1
UNION ALL
SELECT 2 AS step, 'Browse' AS stage, COUNT(reached) AS users FROM s2
UNION ALL
SELECT 3 AS step, 'Product View' AS stage, COUNT(reached) AS users FROM s3
UNION ALL
SELECT 4 AS step, 'Add to Cart' AS stage, COUNT(reached) AS users FROM s4
UNION ALL
SELECT 5 AS step, 'Checkout' AS stage, COUNT(reached) AS users FROM s5
UNION ALL
SELECT 6 AS step, 'Purchase' AS stage, COUNT(reached) AS users FROM s6 ORDER BY step;

-- name: returning_user_conversion
WITH p AS (SELECT DISTINCT user_id FROM journey_events_clean WHERE journey_stage='Purchase')
SELECT u.is_returning,COUNT(*) AS users,COUNT(p.user_id) AS purchasers,1.0*COUNT(p.user_id)/COUNT(*) AS purchase_rate
FROM users_clean u LEFT JOIN p USING(user_id) GROUP BY u.is_returning ORDER BY u.is_returning;
-- name: time_to_purchase
SELECT u.user_id,MIN(e.event_date) AS first_purchase_date,
 julianday(MIN(e.event_date))-julianday(u.first_seen_date) AS days_to_purchase
FROM users_clean u JOIN journey_events_clean e USING(user_id)
WHERE e.journey_stage='Purchase' AND e.event_date>=u.first_seen_date
GROUP BY u.user_id ORDER BY u.user_id;
-- name: stage_reach
SELECT journey_stage,COUNT(DISTINCT user_id) AS users FROM journey_events_clean GROUP BY journey_stage ORDER BY users DESC;
