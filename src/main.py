import sqlite3
from models.boek import Boek
from models.klant import Klant

def main():
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
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO klanten (naam, email) VALUES (?, ?)", (naam, email))
                    conn.commit()
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
