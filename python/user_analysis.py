import pandas as pd

df = pd.read_csv("../data/Online Retail.csv",encoding="gbk")

# 删除CustomerID为空的数据
df = df.dropna(subset=["CustomerID"])

# 删除退货订单
df = df[df["Quantity"] > 0]

# 删除价格异常
df = df[df["UnitPrice"] > 0]

# 转换时间格式
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 新增销售额字段
df["Sales"] = df["Quantity"] * df["UnitPrice"]

# 用户消费分析
# 统计用户消费金额
customer_sales = (
    df.groupby("CustomerID")["Sales"]
    .sum()
    .reset_index()
)

print(customer_sales.head())

# 查看消费最高用户
print(customer_sales.sort_values(
    by="Sales",
    ascending=False
).head(10))

# 复购用户分析
# 统计订单次数
customer_orders = (
    df.groupby("CustomerID")["InvoiceNo"]
    .nunique()
    .reset_index()
)

customer_orders.columns = [
    "CustomerID",
    "OrderCount"
]

print(customer_orders.head())

# 复购用户
repeat_users = customer_orders[
    customer_orders["OrderCount"] > 1
]

print(len(repeat_users))