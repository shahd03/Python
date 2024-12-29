#klant.py
class Klant:
    def __init__(self, naam, email):
        """
        Initialiseert een nieuwe klant.

        Args:
            naam (str): De naam van de klant.
            email (str): Het e-mailadres van de klant.
        """
        self.naam = naam
        self.email = email

    def __str__(self):
        """
        Retourneert een stringrepresentatie van de klant.

        Returns:
            str: Een beschrijving van de klant.
        """
        return f"Klant: {self.naam} | Email: {self.email}"

    def to_dict(self):
        """
        Converteert de klant naar een dictionary-representatie.

        Returns:
            dict: Een dictionary met klantinformatie.
        """
        return {
            "naam": self.naam,
            "email": self.email
        }

    def opslaan(self, conn):
        """
        Slaat een klant op in de database.

        Args:
            conn (sqlite3.Connection): De verbinding met de database.
        """
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO klanten (naam, email) VALUES (?, ?)", 
                (self.naam, self.email)
            )
            conn.commit()
            print("Klant succesvol opgeslagen.")
        except Exception as e:
            print(f"Fout bij het opslaan van de klant: {e}")
