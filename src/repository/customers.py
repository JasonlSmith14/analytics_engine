from src.models.models import Customers
from src.repository.base_repository import BaseRepository


class CustomersRepository(BaseRepository):
    def __init__(self, engine):
        super().__init__(engine, Customers)
