from src.models.models import Customers, Orders, Products
from src.repository.base_repository import BaseRepository
from src.repository.customers import CustomersRepository
from src.repository.products import ProductsRepository


class OrdersRepository(BaseRepository):
    def __init__(self, engine):
        super().__init__(engine, Orders)

    def create_single(self, orders_item: Orders,customers_item: Customers, products_item: Products):
        customer_item = CustomersRepository(self.engine).read_single(
            {"customer_name": customers_item.customer_name}
        )
        customer_id = customer_item.customer_id
        orders_item.customer_id = customer_id

        product_item = ProductsRepository(self.engine).read_single(
            {"product_name": products_item.product_name}
        )
        product_id = product_item.product_id
        orders_item.product_id = product_id

        return super().create_single(orders_item)

