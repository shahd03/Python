import csv

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
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")  # Gegevens ophalen
    rows = cursor.fetchall()

    # Hardcoded kolomnamen per tabel
    if table_name == "boeken":
        columns = ["ID", "Titel", "Auteur", "Jaar"]
    elif table_name == "klanten":
        columns = ["ID", "Naam", "Email"]
    else:
        raise ValueError("Onbekende tabelnaam. Gebruik 'boeken' of 'klanten'.")

    # Schrijf kolomnamen en rijen naar CSV
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(columns)  # Schrijf kolomnamen
        writer.writerows(rows)    # Schrijf gegevens
    print(f"Rapport opgeslagen als {filename}.")
