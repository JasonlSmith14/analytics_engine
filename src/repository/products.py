from src.models.models import Categories, Products
from src.repository.base_repository import BaseRepository
from src.repository.categories import CategoriesRepository


class ProductsRepository(BaseRepository):
    def __init__(self, engine):
        self.engine = engine
        super().__init__(self.engine, Products)

    def read_single(self, filters) -> Products:
        return super().read_single(filters)

    def create_single(self, categories_item: Categories, products_item: Products):
        category_item = CategoriesRepository(self.engine).read_single(
            {"category": categories_item.category}
        )
        category_id = category_item.category_id
        products_item.category_id = category_id
        return super().create_single(products_item)
