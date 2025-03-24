from fastapi import APIRouter, Request
from app.core.templates import jinja_templates

pages_router = APIRouter(tags=["Pages"])

@pages_router.get("/", include_in_schema=False)
def home(request: Request):

    """
    Serves the home page of the chatbot UI.

    This route returns the `index.html` template rendered with the current
    request context. It is typically the entry point to the web-based user interface
    for interacting with the chatbot.

    Args:
        request (Request): The incoming HTTP request object.

    Returns:
        TemplateResponse: The rendered index.html page.
    """

    return jinja_templates.TemplateResponse("index.html", {"request": request})
