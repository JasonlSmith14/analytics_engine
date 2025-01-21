from src.db.database import Database
from src.etl.extract import Extract
from src.etl.load import Load
from src.etl.transform import Transform

DB_PATH = "data/db/store.db"
DB_URL = f"sqlite:///{DB_PATH}"

db = Database(db_url=DB_URL)

db.create_tables()

extract = Extract()
data = extract.extract_data("data/raw/retail_data.csv")

transform = Transform(data=data)
categories = transform.standardize().categories()

load = Load(DB_URL)
load.load(categories, "categories")
