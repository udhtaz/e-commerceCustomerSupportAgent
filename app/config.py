import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_TITLE = "E-Commerce Support Chatbot"
    APP_DESCRIPTION = (
        "An E-Commerce Customer Support Conversational Agent.\n\n"
        "This Agent is capable of:\n"
        "- 📦 Order Status Tracking\n"
        "- 🔄 Return Policies\n"
        "- 👨‍💼 Escalation to Human Representatives"
    )
    VERSION = "1.0.0"
    CONTACT = {
        "name": "Udhtaz",
        "url": "https://github.com/udhtaz/",
        "email": "reachtaye@gmail.com",
    }
    LICENSE_INFO = {
        "name": "Apache License",
        "url": "https://opensource.org/license/apache-2-0"
    }
    TERMS_OF_SERVICE = "https://example.com/tos"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()