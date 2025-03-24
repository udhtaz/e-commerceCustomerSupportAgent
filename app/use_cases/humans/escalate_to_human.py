import csv

class EscalateToHumanUseCase:

    """
    Use case for handling escalation requests to human representatives.

    This class is responsible for validating and storing user-provided contact information 
    when they request to speak with a human representative.
    """

    def execute(self, contact_info: str) -> str:

        """
        Processes the contact info provided by the user and saves it to a CSV file.

        Args:
            contact_info (str): A comma-separated string containing the user's 
                                full name, email, and phone number.

        Returns:
            str: A confirmation message or an error message if input is invalid.

        Example:
            >>> use_case = EscalateToHumanUseCase()
            >>> use_case.execute("Jane Doe, jane@example.com, 1234567890")
            "Your request has been noted. A human rep will reach out shortly."
        """

        parts = [x.strip() for x in contact_info.split(",")]
        if len(parts) != 3:
            return "Invalid input. Use: Full Name, Email, Phone Number"

        with open("data/contact_info.csv", "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(parts)

        return "Your request has been noted. A human rep will reach out shortly."
