import os

from models.database import Database
from dotenv import load_dotenv

load_dotenv()


class DAO(Database):
    def __init__(self, name: str, columns: list[str], pkey: str) -> None:
        super().__init__(os.getenv("db_file"), os.getenv("env"))
        self.create_connection()
        self.name = name
        self.table_name = name + "_" + self.env
        self.columns = columns
        self.pkey = pkey
