from sqlalchemy import create_engine
from src.db.database import Database
from src.etl.extract import Extract
from src.etl.load import Load
from src.etl.transform import Transform
from src.repository.categories import CategoriesRepository
from src.repository.customers import CustomersRepository
from src.repository.orders import OrdersRepository
from src.repository.products import ProductsRepository

DB_PATH = "data/db/store.db"
DB_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DB_URL)

db = Database(db_url=DB_URL)

db.create_tables()

extract = Extract()
data = extract.extract_data("data/raw/retail_data.csv")
transform = Transform(data=data)
load = Load()

categories_repository = CategoriesRepository(engine=engine)
customers_repository = CustomersRepository(engine=engine)
products_repository = ProductsRepository(engine=engine)
orders_repository = OrdersRepository(engine=engine)


categories = transform.create_categories()
load.load(categories_repository, categories)

customers = transform.create_customers()
load.load(customers_repository, customers)

products = transform.create_products(categories_repository)
load.load(products_repository, products)

orders = transform.create_orders(customers_repository, products_repository)
load.load(orders_repository, orders)
