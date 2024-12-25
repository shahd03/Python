import sqlite3
from models.boek import Boek

def main():
    with sqlite3.connect("mijn_database.db") as conn:
        while True:
            print("1. Voeg een boek toe")
            print("2. Bekijk alle boeken")
            print("3. Sluit programma")
            keuze = input("Kies een optie: ")

            if keuze == "1":
                titel = input("Titel: ")
                auteur = input("Auteur: ")
                jaar = int(input("Jaar: "))
                boek = Boek(titel, auteur, jaar)
                boek.opslaan(conn)
                print("Boek toegevoegd.")
            elif keuze == "2":
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM boeken")
                for row in cursor.fetchall():
                    print(row)
            elif keuze == "3":
                break
            else:
                print("Ongeldige keuze.")

if __name__ == "__main__":
    main()
