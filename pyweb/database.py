import sqlite3


class Database():
    @staticmethod
    def create_db():
        conn = sqlite3.connect('banco.db')
        with open('schema.sql') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

    @staticmethod
    def get_connection():
        conn = sqlite3.connect('banco.db')
        return conn


if __name__ == '__main__':
    Database.create_db()
