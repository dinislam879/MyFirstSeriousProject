import sqlite3

class SQLighter:
    def __init__(self, databasename):
        self.connection = sqlite3.connect(databasename)
        self.cursor = self.connection.cursor()
        
    def create_table(self, table):
        self.table = table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER
            )""")
        self.connection.commit()
    def add_info(self, info):
        data2 = self.cursor.execute(f"SELECT id FROM users WHERE id = {info}")
        data = data2.fetchone()
        if data is None:
            self.cursor.execute("INSERT INTO users VALUES (?);",(info,))
            self.connection.commit()
    def get_users(self):
      with self.connection:
        return self.cursor.execute("SELECT `id` FROM `users`").fetchall()



s1 = SQLighter('database.db')
