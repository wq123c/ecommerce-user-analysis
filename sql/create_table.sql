-- 创建数据库
CREATE DATABASE ecommerce;

-- 使用数据库
USE ecommerce;

-- 创建表
CREATE TABLE online_retail (
  InvoiceNo VARCHAR (20),
  StockCode VARCHAR (20),
  Description TEXT,
  Quantity INT,
  InvoiceDate VARCHAR (50),
  UnitPrice DECIMAL (10, 2),
  CustomerID VARCHAR (20),
  Country VARCHAR (50)
);

-- 创建清洗后的表
CREATE TABLE retail_clean AS SELECT
  *
FROM
  online_retail
WHERE
  CustomerID IS NOT NULL
  AND CustomerID != ''
  AND Quantity > 0
  AND UnitPrice > 0;
  
-- 创建“带标准时间”的新表
CREATE TABLE retail_final AS SELECT
  InvoiceNo,
  StockCode,
  Description,
  Quantity,
  STR_TO_DATE(InvoiceDate, '%Y/%m/%d %H:%i') AS InvoiceDate,
  UnitPrice,
  CustomerID,
  Country
FROM
  retail_clean;
  
-- 创建 RFM 表
CREATE TABLE rfm AS SELECT
  CustomerID,
  DATEDIFF('2011-12-10', MAX(InvoiceDate)) AS R,
  COUNT(DISTINCT InvoiceNo) AS F,
  ROUND(SUM(Quantity * UnitPrice), 2) AS M
FROM
  retail_final
GROUP BY
  CustomerID;