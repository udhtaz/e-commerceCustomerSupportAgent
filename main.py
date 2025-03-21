import uvicorn
from fastapi import FastAPI, Body
from contextlib import asynccontextmanager

from schemas import UserMessage
from agents.conversation_agent import create_conversational_agent
from setup_db import setup_database

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

@app.post("/chat", summary="Chat Endpoint", description="Endpoint for sending messages to the chatbot.")
def chat(user_message: UserMessage = Body(...)):
    """
    This endpoint receives a user's message and returns the chatbot's response.
    """
    result = agent({"input": user_message.message})
    # result = agent.invoke({"input": user_message.message})
    return {"response": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)