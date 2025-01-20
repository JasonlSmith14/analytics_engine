from src.db.database import Database

DB_PATH = "data/db/store.db"

db = Database(db_url=f"sqlite:///{DB_PATH}")

db.create_tables()



