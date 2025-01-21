from typing import Any, Dict
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, engine, table):
        self.engine = engine
        self.table = table

    def create_single(self, kwargs: Dict[str, Any]):
        with Session(self.engine) as session:
            item = self.table(**kwargs)
            session.add(item)
            session.commit()
            return item

    def read_single(self, filters: Dict[str, Any]):
        with Session(self.engine) as session:
            return session.query(self.table).filter_by(**filters).first()

    def update_single(self, filters: Dict[str, Any], updates: Dict[str, Any]):
        with Session(self.engine) as session:
            item = self.read_single(filters=filters)
            if item:
                for key, value in updates.items():
                    setattr(item, key, value)
                session.commit()
                return True
            return False

    def delete_single(self, filters: Dict[str, Any]):
        with Session(self.engine) as session:
            item = self.read_single(filters=filters)
            if item:
                session.delete(item)
                session.commit()
                return True
            return False

    def create_many(self):
        pass

    def read_many(self):
        pass

    def update_many(self):
        pass

    def delete_many(self):
        pass
