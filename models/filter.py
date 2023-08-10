from collections import defaultdict


class Clause:
    """Convert to AND or OR clause of search terms"""

    def __init__(self, table: str, type: str) -> None:
        # recursively construct filter
        self.criteria: dict[str, list[str]] = defaultdict(list)
        self.table = table
        self.type = type

    def add_criteria(self, col: str, crit: str) -> None:
        if col in self.criteria:
            self.criteria[col].append(crit)
        else:
            self.criteria[col] = [crit]

    def construct(self) -> str:
        """construct AND search condition"""
        # todo: can use IN (a, b, c) syntax instead of OR]
        clause = []
        for col, crit_list in self.criteria.items():
            for crit in crit_list:
                if isinstance(crit, str):
                    clause.append(f"'{col}'='{crit}'")
                else:  # nested clause
                    clause.append(crit.construct())
            clause.append(f" {self.type} ")

        return ''.join(clause).rstrip(f" {self.type} ")  # remove trailing " AND "


class Filter:
    """Convert to search criteria to SQL"""

    def __init__(self, table: str) -> None:
        # recursively construct filter
        self.criteria: dict[str, list[str]] = defaultdict(list)
        self.table = table

    def add_criteria(self, col: str, crit: str) -> None:
        self.criteria[col].append(crit)

    def construct(self) -> str:
        """construct AND search condition"""
        # todo: can use IN (a, b, c) syntax instead of OR
        return f"SELECT * FROM {self.table} WHERE " + f" AND ".join(
            " OR ".join(f"{col}='{crit}'" for crit in self.criteria[col]) for col in self.criteria.keys())
