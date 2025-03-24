import os
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

if not os.path.exists(TEMPLATES_DIR):
    raise RuntimeError(f"Templates directory not found: {TEMPLATES_DIR}")

jinja_templates = Jinja2Templates(directory=TEMPLATES_DIR)