import sqlite3
from typing import List



class SqliteConnection:
    """
    Here we establish connections to the sqlite database
    then we create the database schema
    we create methods for fetching and insertion into the created
    sqlite3 database
    """

    DATABASE_PATH = 'api.sqlite3'

    def __init__(self) -> None:
        """
        This give us a direct connetion to the database
        """
        self.connection = sqlite3.connect(database=self.DATABASE_PATH)
        self.cursor = self.connection.cursor()
        

    def schema_defination(self, table_name, **kwargs) -> None:
        """
        A generic method to create a table in the database
        """
        # name: str
        # age: int
        # address: str
        # gender: str
        # email: str
        # phone_number: str
        # create a table

        _columns = kwargs.keys()
        # ['age', 'address', 'name', 'email']
        columns = tuple(_columns)
        #TODO:: Fix accessing the column names dynamically
        command = f"create table {table_name}(name, age, gender, address, email, phone_number)"
        self.cursor.execute(command)
        
    def insertion(self, table_name, **kwargs) -> None:
        """
        Inserting data to the specified method
        """
        _columns = kwargs.keys()
        # ['age', 'address', 'name', 'email']
        columns = tuple(_columns)
        command = f"INSERT OR REPLACE INTO {table_name} VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(command, (kwargs['name'],
                             str(kwargs['age']),
                             kwargs['gender'],
                               kwargs['address'],
                                 kwargs['email'],
                                   kwargs['phone_number']))
    def select(self, limit: int = None) -> List:
        """
        Select data from the database with limit
        when limit is None, we select all the data
        """
        selected_users = []
        raw_db = self.cursor.execute("select * from users")
        for row in raw_db:
            selected_users.append(row)

        return selected_users

    def close(self) -> None:
        """
        To safely closed the open connection to the sqlite db
        """
        self.connection.close()
