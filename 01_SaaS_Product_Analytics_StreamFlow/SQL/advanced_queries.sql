-- StreamFlow SaaS — Advanced SQL Pack
-- Notes:
-- - Uses ANSI SQL with common warehouse functions.
-- - DATE_TRUNC / DATEDIFF syntax varies by engine (Postgres/Snowflake/BigQuery). Adjust as needed.

-- 1) Onboarding funnel by step (unique users)
WITH onboarding AS (
  SELECT DISTINCT user_id, event_name
  FROM events_clean
  WHERE event_group = 'Onboarding'
),
steps AS (
  SELECT user_id,
         MAX(CASE WHEN event_name = 'Step 1: Account' THEN 1 ELSE 0 END) AS s1,
         MAX(CASE WHEN event_name = 'Step 2: Workspace' THEN 1 ELSE 0 END) AS s2,
         MAX(CASE WHEN event_name = 'Step 3: Integration' THEN 1 ELSE 0 END) AS s3,
         MAX(CASE WHEN event_name = 'Step 4: First Workflow' THEN 1 ELSE 0 END) AS s4,
         MAX(CASE WHEN event_name = 'Step 5: Invite Team' THEN 1 ELSE 0 END) AS s5
  FROM onboarding
  GROUP BY user_id
),
counts AS (
  SELECT
    SUM(s1) AS step1_users,
    SUM(CASE WHEN s1=1 AND s2=1 THEN 1 ELSE 0 END) AS step2_users,
    SUM(CASE WHEN s1=1 AND s2=1 AND s3=1 THEN 1 ELSE 0 END) AS step3_users,
    SUM(CASE WHEN s1=1 AND s2=1 AND s3=1 AND s4=1 THEN 1 ELSE 0 END) AS step4_users,
    SUM(CASE WHEN s1=1 AND s2=1 AND s3=1 AND s4=1 AND s5=1 THEN 1 ELSE 0 END) AS step5_users
  FROM steps
)
SELECT * FROM counts;

-- 2) Churn risk uplift: Step 2 completion vs churn (by tier)
WITH base AS (
  SELECT
    s.user_id,
    s.plan_tier,
    s.completed_step2,
    s.churned_within_90d
  FROM subscriptions_clean s
),
agg AS (
  SELECT
    plan_tier,
    completed_step2,
    COUNT(*) AS users,
    AVG(CASE WHEN churned_within_90d THEN 1 ELSE 0 END) AS churn_rate_90d
  FROM base
  GROUP BY plan_tier, completed_step2
),
pivot AS (
  SELECT
    plan_tier,
    MAX(CASE WHEN completed_step2=1 THEN churn_rate_90d END) AS churn_step2_yes,
    MAX(CASE WHEN completed_step2=0 THEN churn_rate_90d END) AS churn_step2_no
  FROM agg
  GROUP BY plan_tier
)
SELECT
  plan_tier,
  churn_step2_yes,
  churn_step2_no,
  (churn_step2_no - churn_step2_yes) AS churn_rate_uplift_points
FROM pivot
ORDER BY churn_rate_uplift_points DESC;

-- 3) Power users: top percentile by workflow runs within 90 days of signup (window function)
WITH signup AS (
  SELECT user_id, CAST(signup_date AS DATE) AS signup_date
  FROM users_clean
),
runs AS (
  SELECT
    e.user_id,
    COUNT(*) AS workflow_runs_90d
  FROM events_clean e
  JOIN signup u ON u.user_id = e.user_id
  WHERE e.event_group='Product'
    AND e.event_name='Workflow Run'
    AND CAST(e.event_date AS DATE) BETWEEN u.signup_date AND (u.signup_date + INTERVAL '90' DAY)
  GROUP BY e.user_id
),
ranked AS (
  SELECT
    user_id,
    workflow_runs_90d,
    NTILE(10) OVER (ORDER BY workflow_runs_90d DESC) AS decile
  FROM runs
)
SELECT
  decile,
  COUNT(*) AS users,
  AVG(workflow_runs_90d) AS avg_runs
FROM ranked
GROUP BY decile
ORDER BY decile;

-- 4) Revenue concentration (Pareto) — cumulative share by tier and by user (window)
WITH rev AS (
  SELECT user_id, plan_tier, COALESCE(mrr,0) * 12 AS arr
  FROM subscriptions_clean
),
user_rank AS (
  SELECT
    user_id,
    plan_tier,
    arr,
    SUM(arr) OVER () AS total_arr,
    SUM(arr) OVER (ORDER BY arr DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_arr
  FROM rev
)
SELECT
  user_id,
  plan_tier,
  arr,
  cum_arr / NULLIF(total_arr,0) AS cumulative_arr_share
FROM user_rank
ORDER BY arr DESC
FETCH FIRST 200 ROWS ONLY;