class Filter:
    """Convert to search criteria to SQL"""

    def __init__(self, table: str) -> None:
        # recursively construct filter
        self.params: dict[str, list[str]] = {}
        self.table = table
        self.query_type = "AND"

    def add_criteria(self, col: str, crit: str) -> None:
        if col in self.params:
            self.params[col].append(crit)
        else:
            self.params[col] = [crit]

    def construct(self) -> str:
        """construct AND search condition"""
        # sql = f"SELECT * FROM {self.table} WHERE "
        # for col, crits in self.params.items():
        #     sql += " OR ".join(f"{col}='{crit}'" for crit in crits)
        #     sql += " AND"
        # return sql.rstrip(" AND") + ";"
        # print(sql + " AND ".join(" OR ".join(f"{col}='{crit}'" for crit in self.params[col]) for col in self.params.keys()))

        # todo: can use IN (a, b, c) syntax instead of OR
        return f"SELECT * FROM {self.table} WHERE " + " AND ".join(
            " OR ".join(f"{col}='{crit}'" for crit in self.params[col]) for col in self.params.keys())
