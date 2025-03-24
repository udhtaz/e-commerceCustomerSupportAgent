import csv

def save_contact_info(name: str, email: str, phone: str) -> str:
    """
    Saves user contact information to a CSV file for follow-up by a human representative.

    Args:
        name (str): The user's full name.
        email (str): The user's email address.
        phone (str): The user's phone number.

    Returns:
        str: A confirmation message or an error message.
    """
    
    try:
        with open("data/contact_info.csv", "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([name, email, phone])
        return "Your request has been noted. A human representative will contact you soon."
    
    except Exception as e:
        return f"Error saving contact info: {str(e)}"
