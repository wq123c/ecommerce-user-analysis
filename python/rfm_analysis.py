import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/Online Retail.csv",encoding="gbk")
# print(df.dtypes)

df["InvoiceDate"] = pd.to_datetime(
    df["InvoiceDate"]
)
# 确定分析日期
analysis_date = pd.Timestamp("2012-01-01")

# 新增销售额字段
df["Sales"] = df["Quantity"] * df["UnitPrice"]

# 删除空用户
df = df.dropna(
    subset=["CustomerID"]
)

# 删除退款订单
df = df[df["Quantity"] > 0]

# 删除异常价格
df = df[df["UnitPrice"] > 0]

# R（最近消费时间）
R = (
    analysis_date -
    df.groupby("CustomerID")["InvoiceDate"]
    .max()
).dt.days

# F（消费频次）
F = (
    df.groupby("CustomerID")["InvoiceNo"]
    .nunique()
)

# M（消费金额）
M = (
    df.groupby("CustomerID")["Sales"]
    .sum()
)

rfm = pd.concat(
    [R, F, M],
    axis=1
)

rfm.columns = [
    "Recency",
    "Frequency",
    "Monetary"
]

print(rfm.head())

# RFM评分
rfm["R_score"] = pd.qcut(
    rfm["Recency"],
    5,
    labels=[5,4,3,2,1]
)

rfm["F_score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1,2,3,4,5]
)

rfm["M_score"] = pd.qcut(
    rfm["Monetary"],
    5,
    labels=[1,2,3,4,5]
)

rfm["RFM_Score"] = (
    rfm["R_score"].astype(str)
    + rfm["F_score"].astype(str)
    + rfm["M_score"].astype(str)
)

# print(rfm.head())

def user_level(row):

    if (
        int(row["R_score"]) >= 4
        and int(row["F_score"]) >= 4
        and int(row["M_score"]) >= 4
    ):
        return "High Value"

    elif int(row["R_score"]) >= 4:
        return "Potential"

    elif int(row["R_score"]) <= 2 and int(row["F_score"]) <= 2:
        return "Sleeping"

    else:
        return "Normal"


rfm["UserType"] = rfm.apply(
    user_level,
    axis=1
)

# 统计人数
user_distribution = (
    rfm["UserType"]
    .value_counts()
)

# 绘制RFM饼图
plt.figure(figsize=(10,6))

user_distribution.sort_values().plot(
    kind="barh"
)

plt.title("RFM User Segmentation")
plt.xlabel("Number of Users")
plt.ylabel("User Type")

plt.tight_layout()

plt.savefig(
    "../images/rfm_analysis_bar.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

rfm.to_excel(
    "../data/rfm_users.xlsx"
)

user_distribution.to_excel(
    "../data/rfm_summary.xlsx"
)

rfm.to_excel(
    "../data/rfm_users.xlsx"
)