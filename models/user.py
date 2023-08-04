import os

from models.DAO import DAO
from models.filter import Filter


class UserDAO(DAO):
    def __init__(self):
        super().__init__("users", ["email", "password"], "email")

    def create_user_table(self) -> None:
        create_users_table = f''' CREATE TABLE IF NOT EXISTS users_{self.env} (
                                        email text PRIMARY KEY,
                                        password text NOT NULL); '''
        self.create_table(create_users_table)

    def login(self, email: str, password: str) -> bool:
        # todo: passwords should be encrypted
        filter = Filter(self.table_name)
        filter.add_criteria("email", email)
        filter.add_criteria("password", password)
        print(self.get_connection())
        print(self.db)
        print(os.getcwd())
        return len(self.select_query(filter.construct())) == 1

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

    def change_password(self, email: str, old: str, new: str) -> bool:
        if self.login(email, old):
            self.update(email, new)
        else:
            print("Error: incorrect email or old password")

    def update(self, email: str, password: str) -> None:
        update_user = f'''UPDATE {self.table_name} SET password='{password}' WHERE email = {email};'''
        c = self.conn.cursor()
        c.execute(update_user)
        self.conn.commit()
