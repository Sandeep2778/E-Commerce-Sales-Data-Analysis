import pandas as pd
import numpy as np
import os

# Random data generation
np.random.seed(42)

products = [
    "Laptop", "Mobile", "Headphones",
    "Shoes", "T-Shirt", "Watch",
    "Tablet", "Keyboard"
]

categories = {
    "Laptop": "Electronics",
    "Mobile": "Electronics",
    "Headphones": "Electronics",
    "Shoes": "Fashion",
    "T-Shirt": "Fashion",
    "Watch": "Accessories",
    "Tablet": "Electronics",
    "Keyboard": "Electronics"
}

prices = {
    "Laptop": 45000,
    "Mobile": 18000,
    "Headphones": 2000,
    "Shoes": 2500,
    "T-Shirt": 800,
    "Watch": 1500,
    "Tablet": 15000,
    "Keyboard": 1200
}

n = 200

product_list = np.random.choice(products, n)

df = pd.DataFrame({
    "Order_ID": range(1001, 1001+n),
    "Date": pd.date_range(
        "2026-01-01", periods=n, freq="D"
    ),
    "Product": product_list,
    "Category": [categories[p] for p in product_list],
    "Quantity": np.random.randint(1, 5, n),
    "Price": [prices[p] for p in product_list],
    "City": np.random.choice(
        ["Delhi", "Mumbai", "Jaipur", "Gurgaon", "Pune"], n
    ),
    "Payment": np.random.choice(
        ["UPI", "Credit Card", "Cash", "Debit Card"], n
    )
})

# Create dataset folder if needed
os.makedirs("dataset", exist_ok=True)

# Save CSV file
df.to_csv("dataset/ecommerce.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("Total records:", len(df))


print("E-Commerce Project Started!")

print("Dataset Created Successfully!")

print("Program Completed!")