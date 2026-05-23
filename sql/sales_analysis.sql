-- 销量最高商品 TOP10
SELECT
  Description,
  SUM(Quantity) AS total_quantity
FROM
  retail_clean
GROUP BY
  Description
ORDER BY
  total_quantity DESC
  LIMIT 10;
  
-- 销售额最高商品 TOP10
SELECT
  Description,
  ROUND(SUM(Quantity * UnitPrice), 2) AS total_sales
FROM
  retail_clean
GROUP BY
  Description
ORDER BY
  total_sales DESC
  LIMIT 10;
  
-- 消费最高用户 TOP10
SELECT
  CustomerID,
  ROUND(SUM(Quantity * UnitPrice), 2) AS total_money
FROM
  retail_clean
GROUP BY
  CustomerID
ORDER BY
  total_money DESC
  LIMIT 10;
  
-- 统计每日销售额
SELECT
  DATE(InvoiceDate) AS order_date,
  ROUND(SUM(Quantity * UnitPrice), 2) AS daily_sales
FROM
  retail_final
GROUP BY
  order_date
ORDER BY
  order_date;
  
-- 每日订单量趋势
SELECT
  DATE(InvoiceDate) AS order_date,
  COUNT(DISTINCT InvoiceNo) AS total_orders
FROM
  retail_final
GROUP BY
  order_date
ORDER BY
  order_date;
  
-- 每日活跃用户趋势
SELECT
  DATE(InvoiceDate) AS order_date,
  COUNT(DISTINCT CustomerID) AS active_users
FROM
  retail_final
GROUP BY
  order_date
ORDER BY
  order_date;
  
-- 客单价分析
SELECT
  ROUND(SUM(Quantity * UnitPrice) / COUNT(DISTINCT InvoiceNo), 2) AS avg_order_value
FROM
  retail_final;
  
-- 复购用户分析 统计复购用户数量
SELECT
  COUNT(*) AS repeat_customers
FROM
  (SELECT CustomerID, COUNT(DISTINCT InvoiceNo) AS order_count FROM retail_final GROUP BY CustomerID HAVING order_count > 1) t;
  
-- 复购率
SELECT
  ROUND((SUM(CASE WHEN order_count > 1 THEN 1 ELSE 0 END) / COUNT(*)) * 100, 2) AS repeat_rate
FROM
  (SELECT CustomerID, COUNT(DISTINCT InvoiceNo) AS order_count FROM retail_final GROUP BY CustomerID) t;
  
-- 月销售趋势
SELECT
  DATE_FORMAT(InvoiceDate, '%Y-%m') AS MONTH,
  ROUND(SUM(Quantity * UnitPrice), 2) AS monthly_sales
FROM
  retail_final
GROUP BY
  MONTH
ORDER BY
  MONTH;