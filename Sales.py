
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("train.csv")
print(df.head())
print(df.isnull().sum())
#Total sales
total_sales = df['Sales'].sum()
print("Total Sales:", total_sales)
#Sales by category
category_sales = df.groupby('Category')['Sales'].sum()
print(category_sales)
#Plot sales by category
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
#Top-selling products
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)
print("Top Products:",top_products)
for i, (product, sales) in enumerate(top_products.items(), start=1):
    print(f"{i}. {product} - {sales}")
#Sale by region
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.show()
# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
# Monthly sales
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
#Customer Segment
segment_sales = df.groupby('Segment')['Sales'].sum()
segment_sales.plot(kind='bar')
plt.title("Sales by Customer Segment")
plt.show()
#Location Analysis
state_sales = df.groupby('State')['Sales'].sum().sort_values(ascending=False).head(10)
state_sales.plot(kind='bar')
plt.title("Top 10 States by Sales")
plt.show()
#Sub-Category
subcat_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
subcat_sales.plot(kind='bar')
plt.title("Sales by Sub-Category")
plt.show()