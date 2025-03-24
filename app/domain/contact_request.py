from pydantic import BaseModel, EmailStr

class ContactRequest(BaseModel):

    """
    Schema for collecting user contact information when requesting
    to speak with a human representative.

    Attributes:
        full_name (str): The full name of the user.
        email (EmailStr): The user's email address (validated).
        phone_number (str): The user's phone number.
    """

    full_name: str
    email: EmailStr
    phone_number: str
