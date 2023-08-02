import csv
import os
import sqlite3
from sqlite3 import Error

db_file = "/../sqlite.db"


class Database:
    def __init__(self, file: str, env: str) -> None:
        self.db = os.path.join(os.getcwd() + file)
        self.conn = None
        self.env = env

    def add_users(self, users: list[list[str]]) -> None:
        if self.conn is not None:
            insert_users_sql = f'''
            INSERT INTO users_{self.env} (email, password) 
            VALUES (?, ?);
            '''
            c = self.conn.cursor()
            c.executemany(insert_users_sql, users)
            self.conn.commit()
        else:
            print("Connection error")

    def add_patients(self, patients: list[list[str]]) -> None:
        if self.conn is not None:
            insert_patients_sql = f'''
            INSERT INTO patients_{self.env} (first_name, middle_name, last_name, dob, status, address, other) 
            VALUES (?, ?, ?, ?, ?, ?, ?);
            '''
            c = self.conn.cursor()
            c.executemany(insert_patients_sql, patients)
            self.conn.commit()
        else:
            print("Connection error")

    def create_connection(self) -> None:
        try:
            conn = sqlite3.connect(self.db)
            self.conn = conn
        except Error as e:
            print(e)

    def get_connection(self) -> sqlite3.Connection:
        return self.conn

    def create_table(self, create_table_sql: str) -> None:
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
            self.conn.commit()
        except Error as e:
            print(e)

    def cleanup_rows(self):
        c = self.conn.cursor()
        c.execute(f"DELETE FROM patients_{self.env};", f"DELETE FROM users_{self.env};")

    def drop_tables(self) -> None:
        if self.conn is not None:
            c = self.conn.cursor()
            c.execute(f"DROP TABLE IF EXISTS users_{self.env};")
            c.execute(f"DROP TABLE IF EXISTS patients_{self.env};")
            self.conn.commit()
        else:
            print(f"Error: could not connect to database at {self.db}")

    def create_tables(self) -> None:
        create_patients_table = f''' CREATE TABLE IF NOT EXISTS patients_{self.env} (
                                               id integer PRIMARY KEY,
                                               first_name text NOT NULL,
                                               middle_name text,
                                               last_name text NOT NULL,
                                               dob text NOT NULL,
                                               status text NOT NULL,
                                               address text,
                                               other text
                                           );'''

        create_users_table = f''' CREATE TABLE IF NOT EXISTS users_{self.env} (
                                                   email text PRIMARY KEY,
                                                   password text NOT NULL
                                               ); '''

        if self.conn is not None:
            self.create_table(create_users_table)
            self.create_table(create_patients_table)
        else:
            print(f"Error: could not connect to database at {self.db}")

    def execute_query(self) -> str:
        pass

    def filter_query(self, table: str, column: str, value: str) -> list:
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {table}_{self.env} WHERE {column} = {value};")
        return c.fetchall()

    def load_data(self, file: str, table: str) -> None:
        """Load data into table from csv file"""
        with open(file, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)[1:]  # header row

        if table == "users":
            self.add_users(data)
        elif table == "patients":
            self.add_patients(data)
        else:
            print(f"Error: invalid table specified {table}")

    def multi_filter_query(self, table: str, column: str, values: list[str]) -> list:
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {table}_{self.env} WHERE {column} in {values};")
        return c.fetchall()

    def select_all(self, table: str) -> list:
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM {table}_{self.env}")
        return c.fetchall()


if __name__ == '__main__':
    db = Database(db_file, "test")
    db.create_connection()
    db.create_tables()
    # drop_tables(create_connection(db_file))
