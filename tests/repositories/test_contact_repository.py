import os
import csv
from app.infrastructure.repositories.contact_repository import ContactRepository
from app.domain.contact_request import ContactRequest

def test_save_contact_request(tmp_path):
    """
    Test that a contact request is correctly written to the CSV file.
    """

    # Arrange
    test_csv = tmp_path / "test_contacts.csv"
    repo = ContactRepository()
    repo.FILE_PATH = str(test_csv)  # Override path for test safety

    contact = ContactRequest(
        full_name="John Doe",
        email="johndoe@example.com",
        phone_number="+1234567890"
    )

    # Act
    repo.save(contact)

    # Assert
    with open(test_csv, newline='', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)

    assert len(rows) == 1
    assert rows[0] == ["John Doe", "johndoe@example.com", "+1234567890"]
