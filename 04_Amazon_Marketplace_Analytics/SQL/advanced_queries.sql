-- Amazon Marketplace — Advanced SQL Pack

-- 1) Seller concentration (Top 10 sellers share of revenue)
WITH seller_rev AS (
  SELECT
    seller_id,
    SUM(revenue) AS revenue
  FROM sales_clean
  GROUP BY seller_id
),
ranked AS (
  SELECT
    seller_id,
    revenue,
    SUM(revenue) OVER () AS total_revenue,
    ROW_NUMBER() OVER (ORDER BY revenue DESC) AS rn
  FROM seller_rev
),
top10 AS (
  SELECT * FROM ranked WHERE rn <= 10
)
SELECT
  (SELECT SUM(revenue) FROM top10) / NULLIF((SELECT SUM(revenue) FROM seller_rev),0) AS top10_seller_revenue_share,
  (SELECT SUM(revenue) FROM seller_rev) AS total_revenue;

-- 2) Rating premium: revenue per listing by rating band (window + case)
WITH listing_rev AS (
  SELECT
    l.listing_id,
    l.rating,
    l.category,
    SUM(s.revenue) AS revenue
  FROM listings_clean l
  LEFT JOIN sales_clean s ON s.listing_id = l.listing_id
  GROUP BY l.listing_id, l.rating, l.category
),
banded AS (
  SELECT
    category,
    CASE
      WHEN rating >= 4.5 THEN '4.5–5.0'
      WHEN rating >= 4.0 THEN '4.0–4.49'
      WHEN rating >= 3.5 THEN '3.5–3.99'
      ELSE '<3.5'
    END AS rating_band,
    AVG(revenue) AS avg_rev_per_listing,
    COUNT(*) AS listings
  FROM listing_rev
  GROUP BY category, rating_band
)
SELECT *
FROM banded
ORDER BY category, rating_band;

-- 3) Stockout impact estimate: compare revenue of in-stock vs stockout listings (matched by category and price band)
WITH l AS (
  SELECT
    listing_id,
    category,
    in_stock,
    CASE
      WHEN price < 20 THEN '<$20'
      WHEN price < 50 THEN '$20–$49'
      WHEN price < 100 THEN '$50–$99'
      ELSE '$100+'
    END AS price_band
  FROM listings_clean
),
rev AS (
  SELECT listing_id, SUM(revenue) AS revenue
  FROM sales_clean
  GROUP BY listing_id
),
joined AS (
  SELECT
    l.category,
    l.price_band,
    l.in_stock,
    COALESCE(r.revenue,0) AS revenue
  FROM l
  LEFT JOIN rev r ON r.listing_id = l.listing_id
),
agg AS (
  SELECT
    category,
    price_band,
    in_stock,
    AVG(revenue) AS avg_rev_per_listing,
    COUNT(*) AS listings
  FROM joined
  GROUP BY category, price_band, in_stock
),
pivot AS (
  SELECT
    category,
    price_band,
    MAX(CASE WHEN in_stock=1 THEN avg_rev_per_listing END) AS in_stock_avg,
    MAX(CASE WHEN in_stock=0 THEN avg_rev_per_listing END) AS stockout_avg
  FROM agg
  GROUP BY category, price_band
)
SELECT
  category,
  price_band,
  in_stock_avg,
  stockout_avg,
  (in_stock_avg - stockout_avg) AS avg_rev_lost_per_listing
FROM pivot
ORDER BY avg_rev_lost_per_listing DESC;