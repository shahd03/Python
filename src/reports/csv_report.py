import csv
import sqlite3

def generate_csv_report(filename, table_name, conn):
    """
    Genereert een CSV-rapport voor boeken of klanten.

    Args:
        filename (str): De naam van het CSV-bestand.
        table_name (str): De naam van de tabel ('boeken' of 'klanten').
        conn (sqlite3.Connection): Een verbinding met de SQLite-database.

    Returns:
        None
    """
    # Valideer of de tabelnaam geldig is
    valid_tables = ["boeken", "klanten"]
    if table_name not in valid_tables:
        raise ValueError(f"Onbekende tabelnaam: '{table_name}'. Gebruik 'boeken' of 'klanten'.")

    # Haal gegevens op uit de opgegeven tabel
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Controleer of er gegevens zijn
        if not rows:
            print(f"Geen gegevens gevonden in de tabel '{table_name}'.")
            return

        # Hardcoded kolomnamen per tabel
        if table_name == "boeken":
            columns = ["ID", "Titel", "Auteur", "Jaar"]
        elif table_name == "klanten":
            columns = ["ID", "Naam", "Email"]

        # Schrijf kolomnamen en rijen naar CSV
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(columns)  # Schrijf kolomnamen
            writer.writerows(rows)    # Schrijf gegevens
        print(f"Rapport succesvol opgeslagen als {filename}.")

    except sqlite3.Error as e:
        print(f"Databasefout bij het ophalen van gegevens: {e}")
    except Exception as e:
        print(f"Er is een onverwachte fout opgetreden: {e}")
