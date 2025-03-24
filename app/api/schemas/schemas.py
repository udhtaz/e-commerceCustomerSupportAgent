from pydantic import BaseModel

class UserMessage(BaseModel):

    """
    Schema for incoming user message in a chat request.

    Attributes:
        message (str): The user's message to the chatbot.
    """

    message: str
