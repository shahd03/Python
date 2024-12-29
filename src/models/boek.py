#boek.py
class Boek:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar

    def opslaan(self, conn):
        """
        Slaat een boek op in de database.

        Args:
            conn (sqlite3.Connection): De verbinding met de database.
        """
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO boeken (titel, auteur, jaar) VALUES (?, ?, ?)", 
                (self.titel, self.auteur, self.jaar)
            )
            conn.commit()
            print("Boek succesvol opgeslagen.")
        except Exception as e:
            print(f"Fout bij het opslaan van het boek: {e}")
