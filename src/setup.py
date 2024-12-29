#setup.py
import sqlite3

def setup_database():
    # Maak verbinding met de database
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        
        # Maak de boeken tabel als deze nog niet bestaat
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS boeken (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titel TEXT NOT NULL,
                auteur TEXT NOT NULL,
                jaar INTEGER NOT NULL
            );
        """)

        # Maak de klanten tabel als deze nog niet bestaat
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS klanten (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        
        # Bevestig de wijzigingen
        conn.commit()
        print("Database en tabellen zijn correct ingesteld.")

# Roep deze functie aan bij het opstarten van je programma
setup_database()
