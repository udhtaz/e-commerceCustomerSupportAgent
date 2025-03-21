import uvicorn
from fastapi import FastAPI, Body
from contextlib import asynccontextmanager
import sqlite3

from schemas import UserMessage
from agents.conversation_agent import create_conversational_agent, memory_instance
from setup_db import setup_database

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

# @app.on_event("startup")
# def startup_event():
#     setup_database()  

@asynccontextmanager
async def db_lifespan(app: FastAPI):
    setup_database()  
    yield 

app = FastAPI(
    title="E-Commerce Support Chatbot",
    description="A LangChain-based chatbot for order status, return policies, and human rep requests.",
    version="1.0.0",
    lifespan=db_lifespan
)


# Initialize LangChain agent
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
    result = agent({"input": user_message.message})
    # result = agent.invoke({"input": user_message.message})
    return {"response": result}

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