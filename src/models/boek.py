#boek.py
class Boek:
    def __init__(self, titel, auteur, jaar):
        self.titel = titel
        self.auteur = auteur
        self.jaar = jaar

    def opslaan(self, conn):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO boeken (titel, auteur, jaar) VALUES (?, ?, ?)", 
                       (self.titel, self.auteur, self.jaar))
        conn.commit()
