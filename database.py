import sqlite3


class Database:

    def __init__(self, name=None):

        self.conn = None
        self.cursor = None

        if name:
            self.open(name)

    def open(self, name):

        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print("Error connecting to database!")

    def close(self):

        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        self.close()
