-- name: summary
SELECT COUNT(*) AS users, SUM(mrr>0) AS paying_users,
 SUM(mrr) AS snapshot_mrr, SUM(mrr)*12 AS snapshot_arr,
 1.0*SUM(CASE WHEN mrr>0 THEN churned_within_90d ELSE 0 END)/NULLIF(SUM(mrr>0),0) AS paying_churn_label_rate
FROM subscriptions_clean;
-- name: revenue_by_tier
SELECT plan_tier, COUNT(*) AS users, SUM(mrr) AS snapshot_mrr,
 1.0*SUM(mrr)/NULLIF((SELECT SUM(mrr) FROM subscriptions_clean),0) AS mrr_share
FROM subscriptions_clean GROUP BY plan_tier ORDER BY snapshot_mrr DESC;
-- name: onboarding_funnel
WITH s0 AS (SELECT user_id, signup_date AS reached FROM users_clean),
s1 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM events_clean e WHERE e.user_id=p.user_id AND e.event_name='Step 1: Account' AND e.event_date>=p.reached) AS reached FROM s0 p WHERE p.reached IS NOT NULL),
s2 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM events_clean e WHERE e.user_id=p.user_id AND e.event_name='Step 2: Workspace' AND e.event_date>=p.reached) AS reached FROM s1 p WHERE p.reached IS NOT NULL),
s3 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM events_clean e WHERE e.user_id=p.user_id AND e.event_name='Step 3: Integration' AND e.event_date>=p.reached) AS reached FROM s2 p WHERE p.reached IS NOT NULL),
s4 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM events_clean e WHERE e.user_id=p.user_id AND e.event_name='Step 4: First Workflow' AND e.event_date>=p.reached) AS reached FROM s3 p WHERE p.reached IS NOT NULL),
s5 AS (SELECT p.user_id, (SELECT MIN(e.event_date) FROM events_clean e WHERE e.user_id=p.user_id AND e.event_name='Step 5: Invite Team' AND e.event_date>=p.reached) AS reached FROM s4 p WHERE p.reached IS NOT NULL)
SELECT 1 AS step, 'Step 1: Account' AS stage, COUNT(reached) AS users FROM s1
UNION ALL
SELECT 2 AS step, 'Step 2: Workspace' AS stage, COUNT(reached) AS users FROM s2
UNION ALL
SELECT 3 AS step, 'Step 3: Integration' AS stage, COUNT(reached) AS users FROM s3
UNION ALL
SELECT 4 AS step, 'Step 4: First Workflow' AS stage, COUNT(reached) AS users FROM s4
UNION ALL
SELECT 5 AS step, 'Step 5: Invite Team' AS stage, COUNT(reached) AS users FROM s5 ORDER BY step;

-- name: power_user_association
WITH activity AS (
 SELECT u.user_id, COUNT(e.user_id) AS workflow_runs
 FROM users_clean u LEFT JOIN events_clean e ON e.user_id=u.user_id
 AND e.event_name='Workflow Run' AND e.event_group='Product'
 AND e.event_date>=u.signup_date AND e.event_date<date(u.signup_date,'+90 days')
 GROUP BY u.user_id)
SELECT CASE WHEN workflow_runs>=20 THEN '20+ runs' ELSE 'Under 20 runs' END AS activity_group,
 COUNT(*) AS paying_users, AVG(1.0*s.churned_within_90d) AS churn_label_rate
FROM activity a JOIN subscriptions_clean s USING(user_id)
WHERE s.mrr>0 GROUP BY activity_group;
