from fastapi import APIRouter, Body
from langchain.schema import OutputParserException
from app.api.schemas.schemas import UserMessage
from app.agents.conversation_agent import create_conversational_agent, memory_instance

chat_router = APIRouter(tags=["Chat"])
agent = create_conversational_agent()

@chat_router.post("/chat", summary="Chat Endpoint", description="Endpoint for sending messages to the chatbot.")
def chat(user_message: UserMessage = Body(...)):

    """
    Handles incoming user messages and returns the chatbot's response.

    This endpoint sends the user's input to the LangChain conversational agent,
    which uses ReAct-style reasoning to decide whether to respond directly or call a tool.
    The result is parsed and returned to the frontend in a structured format.

    Args:
        user_message (UserMessage): The message sent by the user, validated by a Pydantic schema.

    Returns:
        dict: A JSON response containing either the chatbot's final answer or a relevant error message.
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


@chat_router.post("/clear-chat", summary="Clear Chat History", description="Clears the in-memory conversation history.")
def clear_chat():
    
    """
    Clears the current conversation history stored in memory.

    This endpoint is useful for resetting the agent’s memory between interactions
    to avoid context carryover from previous chats.

    Returns:
        dict: A message confirming that the chat history was successfully cleared.
    """
    
    memory_instance.clear()
    return {"message": "Chat history cleared."}