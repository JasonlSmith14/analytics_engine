from src.models.models import Products
from src.repository.base_repository import BaseRepository


class ProductsRepository(BaseRepository):
    def __init__(self, engine):
        super().__init__(engine, Products)
