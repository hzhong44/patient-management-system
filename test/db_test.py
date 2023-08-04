import os

from dotenv import load_dotenv

import models.database
from models.filter import Filter
from models.patient import PatientDAO


class Test:
    def __init__(self, db: str):
        self.db = models.database.Database(db, "test")
        self.db.create_connection()
        self.conn = self.db.get_connection()

    def load_data(self) -> None:
        # load users
        users_file = os.path.join(os.getcwd() + "/data/users")
        self.db.load_data(users_file, "users")

        # load patients
        patients_file = os.path.join(os.getcwd() + "/data/patients")
        self.db.load_data(patients_file, "patients")

    def setup(self) -> None:
        self.db.create_tables()
        self.load_data()

    def teardown(self) -> None:
        self.db.drop_tables()


if __name__ == "__main__":
    load_dotenv()
    db_test = Test(os.getenv("db_file"))
    db_test.teardown()
    db_test.setup()

    # test
    patient = PatientDAO()
    search = Filter("patients_test")
    search.add_criteria("first_name", "Jeffrey")
    search.add_criteria("first_name", "Mary")
    print(patient.search(search))

    # db_test.teardown()
