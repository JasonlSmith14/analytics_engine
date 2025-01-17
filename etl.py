import pandas as pd
import sqlite3

customers = pd.read_csv('data/customers.csv')
products = pd.read_csv('data/products.csv')
orders = pd.read_csv('data/orders.csv')
order_details = pd.read_csv('data/order_details.csv')

conn = sqlite3.connect("sql/store.db")

customers.to_sql("Customers", conn, if_exists='append', index=False)
products.to_sql("Products", conn, if_exists='append', index=False)
orders.to_sql("Orders", conn, if_exists='append', index=False)
order_details.to_sql("OrderDetails", conn, if_exists='append', index=False)
