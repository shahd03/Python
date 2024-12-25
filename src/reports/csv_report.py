import csv

def generate_csv_report(filename, conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM boeken")
    rows = cursor.fetchall()

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Titel", "Auteur", "Jaar"])
        writer.writerows(rows)
    print(f"Rapport opgeslagen als {filename}.")
