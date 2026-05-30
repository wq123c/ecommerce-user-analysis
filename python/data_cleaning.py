import pandas as pd

df = pd.read_csv("../data/Online Retail.csv",encoding="gbk")

print(df.head())
print(df.info())

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

print(df.shape)

df.to_csv("../data/clean_data.csv", index=False)