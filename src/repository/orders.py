from src.models.models import Orders
from src.repository.base_repository import BaseRepository


class OrdersRepository(BaseRepository):
    def __init__(self, engine):
        super().__init__(engine, Orders)
