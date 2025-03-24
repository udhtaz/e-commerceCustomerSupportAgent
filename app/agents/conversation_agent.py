import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
# from langchain.prompts.chat import SystemMessagePromptTemplate

from app.utils.prompts import REACT_SYSTEM_PROMPT
from app.infrastructure.tools.human_rep_tool import HumanRepTool
from app.infrastructure.tools.order_status_tool import OrderStatusTool
from app.infrastructure.tools.policies_tool import ReturnPolicyTool
from app.config import settings

# Shared memory instance
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def create_conversational_agent():

    """
    Creates and returns a LangChain-powered conversational agent configured 
    with the ReAct framework and equipped with memory, tools, and a system prompt.

    Features:
    - Uses the OpenAI GPT-4o model with deterministic output (temperature=0).
    - Incorporates a robust ReAct-style system prompt to guide reasoning and tool usage.
    - Loads OpenAI API key from environment variables via `dotenv`.
    - Includes three tools:
        1. OrderStatusTool: For checking order status using an order ID.
        2. ReturnPolicyTool: For responding to queries about return/refund policies.
        3. HumanRepTool (with input validation): For escalating to human representatives.

    Returns:
        An initialized LangChain agent with memory and defined tools ready for conversational use.
    """    

    load_dotenv()

    # Prepare LLM with environment config
    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=settings.OPENAI_API_KEY,
        model_name="gpt-4o",
    )

    # Instantiate tools
    order_tool = OrderStatusTool()
    human_rep_tool = HumanRepTool()
    policy_tool = ReturnPolicyTool()

    # Add basic input validation for human contact info
    def safe_human_rep_tool(input_text: str) -> str:
        if input_text.strip().lower() == "full name, email, phone number":
            return (
                "It seems like you haven’t provided your actual contact details. "
                "Please share your full name, email, and phone number."
            )
        return human_rep_tool.run(input_text)

    # Tool definitions
    tools = [
        Tool(name=order_tool.name, func=order_tool.run, description=order_tool.description),
        Tool(name=human_rep_tool.name, func=safe_human_rep_tool, description=human_rep_tool.description),
        Tool(name=policy_tool.name, func=policy_tool.run, description=policy_tool.description),
    ]

    # Create the agent with memory, tools, and system prompt
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        system_message=REACT_SYSTEM_PROMPT
    )

    return agent

# Expose memory instance for clearing
memory_instance = memory
