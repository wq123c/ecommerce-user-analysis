-- 计算每个用户的 R F M
SELECT
  CustomerID,
  DATEDIFF('2011-12-10', MAX(InvoiceDate)) AS R,
  COUNT(DISTINCT InvoiceNo) AS F,
  ROUND(SUM(Quantity * UnitPrice), 2) AS M
FROM
  retail_final
GROUP BY
  CustomerID;
  
-- 计算平均值
SELECT
  AVG(R) AS avg_r,
  AVG(F) AS avg_f,
  AVG(M) AS avg_m
FROM
  rfm;
  
-- 做用户分类
SELECT
  CustomerID,
  CASE
    WHEN R <= 92 THEN
      '高'
    ELSE
      '低'
  END AS R_score,
  CASE
    WHEN F >= 5 THEN
      '高'
    ELSE
      '低'
  END AS F_score,
  CASE
    WHEN M >= 1890 THEN
      '高'
    ELSE
      '低'
  END AS M_score
FROM
  rfm;
  
-- 统计各类用户数量
SELECT
  user_level,
  COUNT(*) AS total_users
FROM
  (
    SELECT
      CustomerID,
      CASE
        WHEN R <= 92
          AND F >= 5
          AND M >= 1890 THEN
          '重要价值用户'
        WHEN R <= 92
          AND F >= 5 THEN
          '重点保持用户'
        WHEN R <= 92
          AND F < 5 THEN
          '潜力用户'
        ELSE
          '普通/流失用户'
      END AS user_level
    FROM
      rfm
  ) t
GROUP BY
  user_level;