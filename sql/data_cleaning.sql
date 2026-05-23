-- 查看 CustomerID 缺失情况
SELECT
  COUNT(*) AS null_customer
FROM
  online_retail
WHERE
  CustomerID IS NULL
  OR CustomerID = '';
  
-- 查看数量 <= 0 的数据
SELECT
  *
FROM
  online_retail
WHERE
  Quantity <= 0
  LIMIT 20;
  
-- 查看价格 <= 0 的数据
SELECT
  *
FROM
  online_retail
WHERE
  UnitPrice <= 0
  LIMIT 20;