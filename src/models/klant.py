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
