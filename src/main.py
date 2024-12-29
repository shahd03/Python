import sqlite3
from models.boek import Boek
from models.klant import Klant

def setup_database():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS boeken (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titel TEXT NOT NULL,
                auteur TEXT NOT NULL,
                jaar INTEGER NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS klanten (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                naam TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE
            );
        """)
        conn.commit()
        print("Database en tabellen zijn correct ingesteld.")

def main():
    # Zorg ervoor dat de database en tabellen goed zijn ingesteld voordat we verder gaan
    setup_database()

    with sqlite3.connect("database.db") as conn:
        while True:
            print("\nMenu:")
            print("1. Voeg een boek toe")
            print("2. Bekijk alle boeken")
            print("3. Voeg een klant toe")
            print("4. Bekijk alle klanten")
            print("5. Sluit programma")
            keuze = input("Kies een optie: ")

            if keuze == "1":
                try:
                    titel = input("Titel: ")
                    auteur = input("Auteur: ")
                    jaar = int(input("Jaar: "))
                    boek = Boek(titel, auteur, jaar)
                    boek.opslaan(conn)
                    print("Boek toegevoegd.")
                except ValueError:
                    print("Fout: Het jaar moet een geldig getal zijn.")
                except sqlite3.Error as e:
                    print(f"Fout bij het opslaan van het boek: {e}")

            elif keuze == "2":
                try:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM boeken")
                    boeken = cursor.fetchall()
                    if boeken:
                        for row in boeken:
                            print(row)
                    else:
                        print("Geen boeken gevonden.")
                except sqlite3.Error as e:
                    print(f"Databasefout: {e}")

            elif keuze == "3":
                naam = input("Naam: ")
                email = input("E-mail: ")
                try:
                    klant = Klant(naam, email)
                    klant.opslaan(conn)
                    print("Klant toegevoegd.")
                except sqlite3.Error as e:
                    print(f"Databasefout: {e}")

            elif keuze == "4":
                try:
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM klanten")
                    klanten = cursor.fetchall()
                    if klanten:
                        for row in klanten:
                            print(row)
                    else:
                        print("Geen klanten gevonden.")
                except sqlite3.Error as e:
                    print(f"Databasefout: {e}")

            elif keuze == "5":
                print("Programma afgesloten.")
                break

            else:
                print("Ongeldige keuze. Probeer opnieuw.")

if __name__ == "__main__":
    main()
