import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel

from agents.conversation_agent import create_conversational_agent

app = FastAPI(
    title="E-Commerce Support Chatbot",
    description="A LangChain-based chatbot for order status, return policies, and human rep requests.",
    version="1.0.0",
)

agent = create_conversational_agent()

class UserMessage(BaseModel):
    message: str

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


