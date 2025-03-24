import os
import sqlite3
import uvicorn
from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request
from contextlib import asynccontextmanager
from langchain.schema import OutputParserException

from app.config import settings
from app.setup_db import setup_database
from app.agents.conversation_agent import create_conversational_agent, memory_instance
from app.api.schemas.schemas import UserMessage
from app.api.routes.chat import chat_router
from app.api.routes.orders import orders_router
from app.api.routes.pages import pages_router
from app.core.assets import static_files
from app.core.templates import jinja_templates

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    setup_database()
    yield

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.VERSION,
    contact=settings.CONTACT,
    license_info=settings.LICENSE_INFO,
    terms_of_service=settings.TERMS_OF_SERVICE,
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=db_lifespan,
)

# Serve static files
app.mount("/static", static_files, name="static")

# Agent instance
agent = create_conversational_agent()

# Routers
app.include_router(chat_router, tags=["Chat"])
app.include_router(orders_router, tags=["Orders"])
app.include_router(pages_router, include_in_schema=False)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
