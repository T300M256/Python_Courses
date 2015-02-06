"""
classFactory: function to return tailored classes
"""

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding fucntion"""
        def __init__(self, data):
            """Uses data and column names to injet atribuites"""
            assert len(data) == len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        def retrieve(self, curs, condition=None):
            # build SQL
            if condition==None:
                sql = "SELECT {0} FROM {1}".format(", ".join(self.cols), self.table)
            else:
                conditions = condition.split()
                sql = "SELECT {0} FROM {1} WHERE {2}".format(", ".join(self.cols), self.table, " AND ".join(conditions))
            curs.execute(sql)
            for r in curs.fetchall():
                yield DataRow(r)

    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow