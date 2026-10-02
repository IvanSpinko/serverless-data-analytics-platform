1. Total revenue
SELECT
    SUM(total_amount) AS total_revenue
FROM "sales_analytics_db"."processed";


2. Revenue by country
SELECT
    country,
    SUM(total_amount) AS revenue
FROM "sales_analytics_db"."processed"
GROUP BY country
ORDER BY revenue DESC;


3. Revenue by product
SELECT
    product,
    SUM(total_amount) AS revenue
FROM "sales_analytics_db"."processed"
GROUP BY product
ORDER BY revenue DESC;


4. Orders by country
SELECT
    country,
    COUNT(*) AS orders
FROM "sales_analytics_db"."processed"
GROUP BY country
ORDER BY orders DESC;


5. Average order value
SELECT
    AVG(total_amount) AS average_order_value
FROM "sales_analytics_db"."processed";