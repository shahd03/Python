import sqlite3

def create_tables():
    with sqlite3.connect("mijn_database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS boeken (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titel TEXT NOT NULL,
            auteur TEXT NOT NULL,
            jaar INTEGER
        )
        """)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS klanten (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naam TEXT NOT NULL,
            email TEXT
        )
        """)
if __name__ == "__main__":
    create_tables()
