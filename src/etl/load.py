from typing import Any, List
import pandas as pd
from sqlalchemy import create_engine

from src.repository.base_repository import BaseRepository


class Load:
    def __init__(
        self,
    ):
        pass

    def load(self, repository: BaseRepository, items: List[Any]):
        repository.create_many(items)
