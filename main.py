import uvicorn
from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from contextlib import asynccontextmanager
import sqlite3

from langchain.schema import OutputParserException

from schemas import UserMessage
from agents.conversation_agent import create_conversational_agent, memory_instance
from setup_db import setup_database

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    setup_database()  
    yield 

description = """
An E-Commerce Customer Support Conversational Agent.

This Agent is capable of:
- 📦 Order Status Tracking
- 🔄 Return Policies
- 👨‍💼 Escalation to Human Representatives
"""

app = FastAPI(
    title="E-Commerce Support Chatbot",
    description=description,
    version="1.0.0",
    license_info={"name": "Apache License", "url": "https://opensource.org/license/apache-2-0"},
    contact={
        "name": "Udhtaz",
        "url": "https://github.com/udhtaz/",
        "email": "reachtaye@gmail.com",
    },
    terms_of_service="https://example.com/tos",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=db_lifespan
)

agent = create_conversational_agent()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat", summary="Chat Endpoint", description="Endpoint for sending messages to the chatbot.")
def chat(user_message: UserMessage = Body(...)):
    """
    This endpoint receives a user's message and returns the chatbot's response.
    """
    try:
        result = agent({"input": user_message.message})

        if "output" in result:
            return {"response": {"output": result["output"]}}
        else:
            return {"response": {"output": "Agent responded without a final output."}}
    except OutputParserException as e:

        return {"response": {"output": f"(Parser Error) {str(e)}"}}
    except Exception as e:
        return {"response": {"output": f"An error occurred: {str(e)}"}}

@app.post("/clear-chat", summary="Clear Chat History", description="Clears the in-memory conversation history.")
def clear_chat():
    memory_instance.clear()
    return {"message": "Chat history cleared."}

@app.get("/orders", summary="View all orders", description="Returns all rows in the orders database.")
def get_all_orders():
    conn = sqlite3.connect("data/orders.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    rows = cursor.fetchall()

    column_names = [description[0] for description in cursor.description]
    conn.close()

    return [dict(zip(column_names, row)) for row in rows]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)