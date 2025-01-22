from typing import List
from src.models.models import Categories
from src.repository.base_repository import BaseRepository


class CategoriesRepository(BaseRepository):
    def __init__(self, engine):
        super().__init__(engine, Categories)

    def create_single(self, item: Categories):
        return super().create_single(item)

    def read_single(self, filters) -> Categories:
        return super().read_single(filters)

    def create_many(self, items: List[Categories]):
        return super().create_many(items)

    def read_many(self, filters=None) -> List[Categories]:
        return super().read_many(filters)
