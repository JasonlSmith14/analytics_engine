import pandas as pd
from random import choice, randint
from datetime import datetime

# Create Customers Data
customers_data = {
    "CustomerID": range(1, 11),
    "Name": [
        "Alice",
        "Bob",
        "Charlie",
        "David",
        "Eve",
        "Frank",
        "Grace",
        "Hannah",
        "Ivy",
        "Jack",
    ],
    "Email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@example.com",
        "david@example.com",
        "eve@example.com",
        "frank@example.com",
        "grace@example.com",
        "hannah@example.com",
        "ivy@example.com",
        "jack@example.com",
    ],
    "JoinDate": [datetime(2023, 1, randint(1, 28)) for _ in range(10)],
}
customers_df = pd.DataFrame(customers_data)

# Create Products Data
products_data = {
    "ProductID": range(1, 6),
    "Name": ["Laptop", "Phone", "Tablet", "Headphones", "Charger"],
    "Price": [1000, 500, 300, 50, 20],
}
products_df = pd.DataFrame(products_data)

# Create Orders Data (Linking to Customers)
orders_data = {
    "OrderID": range(1, 21),
    "CustomerID": [choice(customers_df["CustomerID"]) for _ in range(20)],
    "OrderDate": [datetime(2023, 3, randint(1, 28)) for _ in range(20)],
}
orders_df = pd.DataFrame(orders_data)

# Create OrderDetails Data (Linking to Orders and Products)
order_details_data = {
    "OrderDetailID": range(1, 21),
    "OrderID": [choice(orders_df["OrderID"]) for _ in range(20)],
    "ProductID": [choice(products_df["ProductID"]) for _ in range(20)],
    "Quantity": [randint(1, 5) for _ in range(20)],
    "TotalPrice": lambda x: (
        x["Quantity"] * products_df.loc[x["ProductID"] - 1, "Price"]
        if isinstance(x, pd.Series)
        else 0
    ),
}
order_details_df = pd.DataFrame(order_details_data)

# Calculate TotalPrice correctly
order_details_df["TotalPrice"] = order_details_df.apply(
    lambda x: x["Quantity"] * products_df.loc[x["ProductID"] - 1, "Price"], axis=1
)

# Save DataFrames to CSV
customers_df.to_csv("data/customers.csv", index=False)
products_df.to_csv("data/products.csv", index=False)
orders_df.to_csv("data/orders.csv", index=False)
order_details_df.to_csv("data/order_details.csv", index=False)

# Print the DataFrames to verify
print("Customers DataFrame:")
print(customers_df)
print("\nProducts DataFrame:")
print(products_df)
print("\nOrders DataFrame:")
print(orders_df)
print("\nOrderDetails DataFrame:")
print(order_details_df)

print(
    "\nCSV files have been saved: customers.csv, products.csv, orders.csv, order_details.csv."
)
