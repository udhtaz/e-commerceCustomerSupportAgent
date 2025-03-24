from app.agents.conversation_agent import create_conversational_agent, memory_instance

agent = create_conversational_agent()

def get_chat_response(user_input: str) -> dict:
    """
    Generate a response from the conversational agent.

    Args:
        user_input (str): The message input from the user.

    Returns:
        dict: A dictionary with the response from the agent.
    """

    result = agent({"input": user_input})

    output = result.get("output", "Agent responded without a final output.")

    return {"response": {"output": output}}


def clear_chat_history() -> dict:
    """
    Clears the in-memory conversation history.

    Returns:
        dict: A confirmation message.
    """
    
    memory_instance.clear()

    return {"message": "Chat history cleared."}
