import pandas as pd
from sqlalchemy import create_engine

# Step 1: Extract data
raw_data = pd.read_csv("data/raw_sales_data.csv")
print("Raw Data:")
print(raw_data.head())

# Step 2: Transform data (cleaning)
raw_data.drop_duplicates(inplace=True)
raw_data['Amount'] = raw_data['Amount'].fillna(0)  # Replace missing amounts with 0
raw_data['Customer_ID'] = raw_data['Customer_ID'].fillna("UNKNOWN")  # Fill missing Customer_ID
raw_data['Order_Date'] = pd.to_datetime(raw_data['Order_Date'])  # Ensure proper datetime format

print("Cleaned Data:")
print(raw_data.head())

# Save cleaned data
raw_data.to_csv("data/cleaned_sales_data.csv", index=False)

# Step 3: Load data into SQLite database
engine = create_engine("sqlite:///outputs/sales_data.db")
raw_data.to_sql("sales", engine, if_exists="replace", index=False)
print("Data loaded into SQLite database 'sales_data.db'")

# Query the database
query = """
SELECT Product, SUM(Amount) as Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC;
"""
result = pd.read_sql(query, engine)
print("Query Results:")
print(result)
