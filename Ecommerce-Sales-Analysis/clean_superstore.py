import pandas as pd

# Load data
df = pd.read_csv("D:\\Ecommerce_Sales_Analysis\\data\\superstore.csv")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("/", "_")

# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Check missing values
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("superstore_cleaned.csv", index=False)

print("Dataset cleaned successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

# Remove duplicates
df = df.drop_duplicates()

# Create analysis columns
df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month_name()

# Save cleaned dataset
df.to_csv("superstore_cleaned.csv", index=False)

print("Dataset cleaned successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order_ID"].nunique())
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))
top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)
top_customers = (
    df.groupby("Customer_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)
monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)

print(monthly_sales)
