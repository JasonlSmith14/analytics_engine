from sqlalchemy.orm import Session
from typing import List, Dict, Any


class BaseRepository:
    def __init__(self, engine, table):
        self.engine = engine
        self.table = table

    def create_single(self, item):
        with Session(self.engine) as session:
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

    def create_many(self, items: List):
        with Session(self.engine) as session:
            session.add_all(items)
            session.commit()
            return items

    def read_many(self, filters: Dict[str, Any] = None):
        with Session(self.engine) as session:
            query = session.query(self.table)
            if filters:
                query = query.filter_by(**filters)
            return query.all()

    def update_many(self, filters: Dict[str, Any], updates: Dict[str, Any]):
        with Session(self.engine) as session:
            items = session.query(self.table).filter_by(**filters).all()
            if items:
                for item in items:
                    for key, value in updates.items():
                        setattr(item, key, value)
                session.commit()
                return True
            return False

    def delete_many(self, filters: Dict[str, Any]):
        with Session(self.engine) as session:
            items = session.query(self.table).filter_by(**filters).all()
            if items:
                for item in items:
                    session.delete(item)
                session.commit()
                return True
            return False
