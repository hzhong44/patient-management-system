import os

import models.database


class Test:
    def __init__(self, db: str):
        self.db = models.database.Database(db, "test")
        self.db.create_connection()
        self.conn = self.db.get_connection()

    def create_test_tables(self) -> None:
        self.db.create_tables()

    def load_data(self) -> None:
        # load users
        users_file = os.path.join(os.getcwd() + "/data/users")
        self.db.load_data(users_file, "users")

        # load patients
        patients_file = os.path.join(os.getcwd() + "/data/patients")
        self.db.load_data(patients_file, "patients")

    def setup(self) -> None:
        self.create_test_tables()
        self.load_data()

    def teardown(self) -> None:
        self.db.drop_tables()


if __name__ == "__main__":
    db_test = Test(models.database.db_file)
    db_test.setup()
    # db_test_
