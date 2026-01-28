# Complete data analysis pipeline with charts using matplotlib

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

# DATA CLEANING
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# DATA ANALYSIS
# 1. Total sales by product
sales_by_product = df.groupby("Product")["Total_Sales"].sum()
# 2. Sales trend over time
sales_over_time = df.groupby("Date")["Total_Sales"].sum()

# VISUALIZATION 1: BAR CHART
plt.figure()
sales_by_product.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig("visualizations/sales_by_product.png")
plt.close()

# VISUALIZATION 2: LINE CHART
plt.figure()
sales_over_time.plot(kind="line")
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales (₹)")
plt.tight_layout()
plt.savefig("visualizations/sales_trend.png")
plt.close()

# FINAL METRICS
total_sales = df["Total_Sales"].sum()
best_selling_product = sales_by_product.idxmax()
highest_sale = df["Total_Sales"].max()
lowest_sale = df["Total_Sales"].min()

# OUTPUT
print("E-COMMERCE SALES ANALYSIS REPORT")
print("--------------------------------")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Best Selling Product: {best_selling_product}")
print(f"Highest Single Sale: ₹{highest_sale:,.2f}")
print(f"Lowest Single Sale: ₹{lowest_sale:,.2f}")
print("\nCharts saved in the 'visualizations' folder.")
print("Analysis completed successfully!")
