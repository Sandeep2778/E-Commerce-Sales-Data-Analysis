import pandas as pd
import numpy as np

df = pd.read_csv("dataset/ecommerce.csv")

print("Dataset Loaded Successfully!")

print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nData Exploration Completed Successfully!")


print("\n========== DATA CLEANING ==========")

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df = df.drop_duplicates()

df["Date"] = pd.to_datetime(df["Date"])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicate Records After Cleaning:")
print(df.duplicated().sum())

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nCleaned Dataset:")
print(df.head())

df.to_csv("dataset/cleaned_ecommerce.csv", index=False)

print("\nData Cleaning Completed Successfully!")




print("\n========== SALES ANALYSIS ==========")

total_revenue = df["Total_Sales"].sum()
print("\nTotal Revenue:", total_revenue)

total_orders = df["Order_ID"].nunique()
print("Total Orders:", total_orders)

total_products_sold = df["Quantity"].sum()
print("Total Products Sold:", total_products_sold)

average_order_value = total_revenue / total_orders
print("Average Order Value:", average_order_value)

top_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
print("Best Selling Product:", top_product)

product_sales = df.groupby("Product")["Total_Sales"].sum()
print("\nProduct Wise Sales:")
print(product_sales)

category_sales = df.groupby("Category")["Total_Sales"].sum()
print("\nCategory Wise Sales:")
print(category_sales)

city_sales = df.groupby("City")["Total_Sales"].sum()
print("\nCity Wise Sales:")
print(city_sales)

payment_analysis = df["Payment"].value_counts()
print("\nPayment Method Analysis:")
print(payment_analysis)

monthly_sales = df.groupby(df["Date"].dt.month)["Total_Sales"].sum()
print("\nMonthly Sales:")
print(monthly_sales)

print("\nSales Analysis Completed Successfully!")




import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

print("\n========== DATA VISUALIZATION ==========")

# 1. Product Wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(10, 5))
product_sales.sort_values().plot(kind="bar", color="skyblue")
plt.title("Product Wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/product_sales.png")
plt.show()


# 2. Category Wise Sales
category_sales = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Wise Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("graphs/category_sales.png")
plt.show()


# 3. City Wise Sales
city_sales = df.groupby("City")["Total_Sales"].sum()

plt.figure(figsize=(9, 5))
city_sales.sort_values().plot(kind="bar", color="orange")
plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("graphs/city_sales.png")
plt.show()


# 4. Monthly Sales
monthly_sales = df.groupby(df["Date"].dt.month)["Total_Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o", color="green")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("graphs/monthly_sales.png")
plt.show()


# 5. Payment Method Analysis
payment_sales = df.groupby("Payment")["Total_Sales"].sum()

plt.figure(figsize=(8, 5))
payment_sales.plot(kind="bar", color="purple")
plt.title("Payment Method Analysis")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("graphs/payment_analysis.png")
plt.show()


print("\nAll Graphs Created Successfully!")
