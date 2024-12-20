import pandas as pd
import numpy as np

# Simulate sales data
data = {
    "Order_ID": np.arange(1, 101),
    "Product": np.random.choice(["Laptop", "Phone", "Tablet", "Headphones"], 100),
    "Amount": np.random.choice([100, 200, 300, None], 100),
    "Order_Date": pd.date_range(start="2023-01-01", periods=100).tolist(),
    "Customer_ID": np.random.choice(["CUST001", "CUST002", "CUST003", None], 100),
}

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("/Users/adriannavilaysith/etl_pipeline_project/data/raw_sales_data.csv", index=False)

print("Raw sales data saved in 'data/raw_sales_data.csv'")
