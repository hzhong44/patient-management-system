from models.DAO import DAO
from models.filter import Filter


class Patient:
    def __init__(self, row: list[str]) -> None:
        self.first_name = row[1]
        self.middle_name = row[2]
        self.last_name = row[3]
        self.dob = row[4]
        self.status = row[5]
        self.address = row[6]
        self.other = row[6]

    def get_other(self, other):
        # json representation
        pass


class PatientDAO(DAO):
    def __init__(self) -> None:
        super().__init__("patients",
                         ["id", "first_name", "middle_name", "last_name", "dob", "status", "address", "other"],
                         "id")

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

    def create_patients_table(self) -> None:
        create_patients_table = f''' CREATE TABLE IF NOT EXISTS patients_{self.env} (
                                               id integer PRIMARY KEY,
                                               first_name text NOT NULL,
                                               middle_name text,
                                               last_name text NOT NULL,
                                               dob text NOT NULL,
                                               status text NOT NULL,
                                               address text,
                                               other text);'''
        self.create_table(create_patients_table)

    def get_patients_list(self) -> list[list[str]]:
        return self.select_all(self.name)

    def search(self, filter: Filter) -> list[list[str]]:
        return self.select_query(filter.construct())

    def search_first_name(self, first_name: str) -> list[list[str]]:
        return self.filter_query(self.name, "first_name", first_name)

    def search_last_name(self, last_name: str) -> list[list[str]]:
        return self.filter_query(self.name, "last_name", last_name)

    def filter_status(self) -> list[list[str]]:
        pass

    def text_search(self, keyword: str) -> list[list[str]]:
        # todo: text search on keyword? multiple keywords?
        patients = self.get_patients_list()
        results = []
        for patient in patients:
            if keyword in ' '.join(patient):
                results.append(patient)
        return results

    def update(self, id: int, patient: list[str]):
        update_patient = f'''UPDATE {self.table_name} 
                                    SET first_name = ?,
                                    middle_name = ?,
                                    last_name = ?,
                                    dob = ?,
                                    status = ?,
                                    address = ?,
                                    other = ?
                                    WHERE id = {id};'''
        c = self.conn.cursor()
        c.execute(update_patient, patient)
        self.conn.commit()
