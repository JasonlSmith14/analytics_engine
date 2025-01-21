import pandas as pd
from sqlalchemy import create_engine


class Load:
    def __init__(
        self,
        db_url: str,
    ):
        self.db_url = db_url
        self.engine = create_engine(self.db_url, echo=True)
        
    def load(self, data: pd.DataFrame, table_name: str):
        with self.engine.connect() as conn:
            data.to_sql(table_name, conn, if_exists="append", index=False)
