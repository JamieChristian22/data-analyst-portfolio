-- name: summary
SELECT COUNT(*) AS sessions,SUM(added_to_cart) AS cart_sessions,SUM(purchased) AS purchases,
 AVG(1.0*purchased) AS conversion_rate,
 1.0-SUM(1.0*purchased)/NULLIF(SUM(added_to_cart),0) AS cart_abandonment_rate,
 (SELECT SUM(order_value) FROM orders_clean) AS revenue,
 (SELECT AVG(order_value) FROM orders_clean) AS average_order_value
FROM web_sessions_clean;
-- name: funnel_by_segment
SELECT device,channel,COUNT(*) AS sessions,SUM(added_to_cart) AS carts,SUM(purchased) AS purchases,
 AVG(1.0*purchased) AS conversion_rate,
 1.0-SUM(1.0*purchased)/NULLIF(SUM(added_to_cart),0) AS cart_abandonment_rate
FROM web_sessions_clean GROUP BY device,channel ORDER BY conversion_rate DESC;
-- name: sku_pareto
WITH revenue AS (SELECT sku,SUM(order_value) AS revenue FROM orders_clean GROUP BY sku),
 ranked AS (SELECT *,ROW_NUMBER() OVER(ORDER BY revenue DESC,sku) AS rank,
 COUNT(*) OVER() AS sku_count,SUM(revenue) OVER() AS total_revenue,
 SUM(revenue) OVER(ORDER BY revenue DESC,sku ROWS UNBOUNDED PRECEDING) AS cumulative_revenue FROM revenue)
SELECT *, cumulative_revenue/NULLIF(total_revenue,0) AS cumulative_share,
 (rank<=(sku_count+4)/5) AS in_top_20_percent FROM ranked ORDER BY rank;
-- name: discount_association
SELECT device,category,discount_applied,COUNT(*) AS orders,AVG(order_value) AS average_order_value,AVG(1.0*units) AS average_units
FROM orders_clean GROUP BY device,category,discount_applied ORDER BY device,category,discount_applied;
