from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Categories(Base):

    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)

    products = relationship("Products", back_populates="categories")


class Customers(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String, nullable=False)
    customer_email = Column(String, nullable=False)

    orders = relationship("Orders", back_populates="customers")


class Orders(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    order_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    shipping_address = Column(String, nullable=False)

    products = relationship("Products", back_populates="orders")
    customers = relationship("Customers", back_populates="orders")


class Products(Base):

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"))

    categories = relationship("Categories", back_populates="products")
