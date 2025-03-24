import csv
from app.domain.contact_request import ContactRequest

class ContactRepository:

    """
    Repository for saving contact requests to a CSV file.
    
    Attributes:
        FILE_PATH (str): Path to the CSV file where contact information is stored.
    """

    FILE_PATH = "data/contact_info.csv"

    def save(self, contact: ContactRequest):

        """
        Save a contact request to the CSV file.

        Args:
            contact (ContactRequest): An object containing the user's full name, email, and phone number.
        """

        with open(self.FILE_PATH, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([contact.full_name, contact.email, contact.phone_number])
