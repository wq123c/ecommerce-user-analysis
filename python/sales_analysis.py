import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("../data/clean_data.csv")

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 日销售趋势分析
daily_sales = (
    df.groupby(df["InvoiceDate"].dt.date)["Sales"]
    .sum()
    .reset_index()
)

daily_sales.to_excel(
    "../data/daily_sales.xlsx",
    index=False
)

plt.figure(figsize=(12,6))

plt.plot(
    daily_sales["InvoiceDate"],
    daily_sales["Sales"]
)

plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    "../images/daily_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# 月销售趋势分析
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

monthly_sales.to_excel(
    "../data/monthly_sales.xlsx",
    index=False
)

plt.figure(figsize=(12,6))

plt.plot(
    monthly_sales["Month"].astype(str),
    monthly_sales["Sales"]
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    "../images/monthly_sales_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

# TOP10商品分析
top_products = (
    df.groupby("Description")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_products.to_excel(
    "../data/top_products.xlsx"
)

plt.figure(figsize=(12,8))

top_products.plot(
    kind="barh"
)

plt.title("Top 10 Products")
plt.xlabel("Quantity")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    "../images/top10_products.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()
