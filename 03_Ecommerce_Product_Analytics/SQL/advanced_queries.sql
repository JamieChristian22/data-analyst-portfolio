-- Ecommerce — Advanced SQL Pack

-- 1) Funnel metrics by device/channel (session→cart→purchase)
WITH f AS (
  SELECT
    device,
    channel,
    COUNT(*) AS sessions,
    SUM(added_to_cart) AS carts,
    SUM(purchased) AS purchases
  FROM web_sessions_clean
  GROUP BY device, channel
)
SELECT
  device,
  channel,
  sessions,
  carts,
  purchases,
  1.0*carts/NULLIF(sessions,0) AS cart_rate,
  1.0*purchases/NULLIF(sessions,0) AS conversion_rate,
  1.0*purchases/NULLIF(carts,0) AS cart_to_purchase_rate,
  1.0 - (1.0*purchases/NULLIF(carts,0)) AS cart_abandonment_rate
FROM f
ORDER BY conversion_rate DESC;

-- 2) Pareto SKU analysis (top 20% SKUs share of revenue)
WITH sku_rev AS (
  SELECT
    sku,
    SUM(order_value) AS revenue
  FROM orders_clean
  GROUP BY sku
),
ranked AS (
  SELECT
    sku,
    revenue,
    SUM(revenue) OVER () AS total_revenue,
    ROW_NUMBER() OVER (ORDER BY revenue DESC) AS rn,
    COUNT(*) OVER () AS sku_count,
    SUM(revenue) OVER (ORDER BY revenue DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cum_revenue
  FROM sku_rev
),
top20 AS (
  SELECT *
  FROM ranked
  WHERE rn <= CEIL(0.20 * sku_count)
)
SELECT
  (SELECT SUM(revenue) FROM top20) / NULLIF((SELECT SUM(revenue) FROM sku_rev),0) AS revenue_share_top_20pct_skus,
  (SELECT COUNT(*) FROM top20) AS num_top_skus,
  (SELECT COUNT(*) FROM sku_rev) AS total_skus;

-- 3) Discount effectiveness: AOV + units (with confound controls via stratification)
WITH agg AS (
  SELECT
    device,
    category,
    discount_applied,
    COUNT(*) AS orders,
    AVG(order_value) AS aov,
    AVG(units) AS avg_units
  FROM orders_clean
  GROUP BY device, category, discount_applied
)
SELECT *
FROM agg
ORDER BY device, category, discount_applied;

-- 4) RFM-lite: identify high value customers (requires customer_id; if absent, use session_id proxy)
-- If your model includes customer_id, replace session_id with customer_id.
WITH r AS (
  SELECT
    session_id AS customer_id,
    MAX(CAST(session_date AS DATE)) AS last_purchase_date,
    COUNT(*) AS frequency,
    SUM(order_value) AS monetary
  FROM orders_clean
  GROUP BY session_id
),
scored AS (
  SELECT
    customer_id,
    last_purchase_date,
    frequency,
    monetary,
    NTILE(5) OVER (ORDER BY last_purchase_date DESC) AS r_score,
    NTILE(5) OVER (ORDER BY frequency DESC) AS f_score,
    NTILE(5) OVER (ORDER BY monetary DESC) AS m_score
  FROM r
)
SELECT
  customer_id,
  r_score, f_score, m_score,
  (r_score+f_score+m_score) AS rfm_total,
  frequency, monetary, last_purchase_date
FROM scored
ORDER BY rfm_total DESC
FETCH FIRST 100 ROWS ONLY;