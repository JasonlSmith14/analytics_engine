import numpy as np
import pandas as pd

from src.models.models import Categories, Customers, Orders, Products
from src.repository.categories import CategoriesRepository
from src.repository.customers import CustomersRepository
from src.repository.products import ProductsRepository


class Transform:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.cleaning()

    def standardize(self):
        for col in self.data.select_dtypes(include=["object"]):
            self.data[col] = self.data[col].str.capitalize()
            self.data[col] = self.data[col].str.strip()

        return self

    def match_name_email_to_shipping_address(self):
        null_customers = self.data[
            self.data["Customer_Name"].isna() | self.data["Customer_Email"].isna()
        ]

        non_null_customers = self.data[
            ~(self.data["Customer_Name"].isna() | self.data["Customer_Email"].isna())
        ]

        for index, row in null_customers.iterrows():
            matching_record = non_null_customers[
                self.data["Shipping_Address"] == row["Shipping_Address"]
            ].iloc[0]

            if pd.isna(row["Customer_Name"]) and not pd.isna(
                matching_record["Customer_Name"]
            ):
                self.data.at[index, "Customer_Name"] = matching_record["Customer_Name"]

            if pd.isna(row["Customer_Email"]) and not pd.isna(
                matching_record["Customer_Email"]
            ):
                self.data.at[index, "Customer_Email"] = matching_record[
                    "Customer_Email"
                ]

    def cleaning(self):

        cleaned_columns = [column.strip() for column in self.data.columns]
        self.data.columns = cleaned_columns

        self.data.drop_duplicates(inplace=True)
        self.standardize()
        self.data.replace("", np.nan, inplace=True)

        self.match_name_email_to_shipping_address()

        mode_product_name = self.data["Product_Name"].mode()[0]
        self.data["Product_Name"].fillna(mode_product_name, inplace=True)

        self.data["Quantity"] = self.data.apply(
            lambda row: (
                row["Total_Amount"] / row["Price"]
                if pd.isna(row["Quantity"]) and row["Price"] != 0
                else row["Quantity"]
            ),
            axis=1,
        )

        self.data["Order_Date"] = pd.to_datetime(self.data["Order_Date"]).dt.date

    def categories(self):
        return self.data["Category"].drop_duplicates()

    def customers(self):
        return self.data[["Customer_Name", "Customer_Email"]].drop_duplicates()

    def products(self):
        return self.data[["Product_Name", "Price", "Category"]].drop_duplicates()

    def orders(self):
        return self.data

    def create_categories(self):
        categories = []
        for row in self.categories():
            category = Categories(category=row)
            categories.append(category)
        return categories

    def create_customers(self):
        customers = []
        for _, row in self.customers().iterrows():
            customer = Customers(
                customer_name=row["Customer_Name"], customer_email=row["Customer_Email"]
            )
            customers.append(customer)
        return customers

    def create_products(self, categories_repository: CategoriesRepository):
        products = []
        for _, row in self.products().iterrows():
            category = categories_repository.read_single({"category": row["Category"]})
            product = Products(
                product_name=row["Product_Name"],
                price=row["Price"],
                category_id=category.category_id,
            )
            products.append(product)

        return products

    def create_orders(
        self,
        customers_repository: CustomersRepository,
        products_repository: ProductsRepository,
    ):
        orders = []
        for _, row in self.orders().iterrows():
            customer = customers_repository.read_single(
                {
                    "customer_name": row["Customer_Name"],
                    "customer_email": row["Customer_Email"],
                }
            )
            product = products_repository.read_single(
                {
                    "product_name": row["Product_Name"],
                    "price": row["Price"],
                }
            )

            order = Orders(
                order_id=row["Order_ID"],
                product_id=product.product_id,
                customer_id=customer.customer_id,
                quantity=row["Quantity"],
                order_date=row["Order_Date"],
                status=row["Status"],
                total_amount=row["Total_Amount"],
                shipping_address=row["Shipping_Address"],
            )

            orders.append(order)

        return orders
