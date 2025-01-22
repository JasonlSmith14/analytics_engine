from src.models.models import Customers
from src.repository.base_repository import BaseRepository


class CustomersRepository(BaseRepository):
    def __init__(self, engine):
        super().__init__(engine, Customers)

    def read_single(self, filters) -> Customers:
        return super().read_single(filters)

    def create_single(self, item: Customers):
        return super().create_single(item)
