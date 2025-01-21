from src.models.models import Categories
from src.repository.base_repository import BaseRepository


class CategoriesRepository(BaseRepository):
    def __init__(self, engine):
        super().__init__(engine, Categories)
