import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import SystemMessagePromptTemplate

from tools.order_status_tool import OrderStatusTool
from tools.human_rep_tool import HumanRepTool
from tools.policies_tool import ReturnPolicyTool

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

def create_conversational_agent():
    """Create and return a LangChain conversational agent with a strong ReAct-style prompt."""
    
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

    system_prompt_content = (
        "You are a helpful AI assistant using the ReAct framework. "
        "You MUST follow this format:\n\n"
        "Thought: <your hidden chain-of-thought>\n"
        "Action: <tool name>\n"
        "Action Input: <tool input>\n"
        "OR\n"
        "Final Answer: <what you actually say to the user>\n\n"
        "Never produce any text outside these lines. If you are done, output 'Final Answer: <text>'. "
        "If you must call a tool, do 'Thought:' then 'Action:' and 'Action Input:'.\n"
    )

    system_prompt = SystemMessagePromptTemplate.from_template(system_prompt_content)

    llm = ChatOpenAI(
        temperature=0,
        openai_api_key=openai_api_key,
        model_name="gpt-4o",
    )

    order_tool = OrderStatusTool()
    human_rep_tool = HumanRepTool()
    policy_tool = ReturnPolicyTool()

    def safe_human_rep_tool(input_text: str) -> str:
        if input_text.strip().lower() == "full name, email, phone number":
            return (
                "It seems like you haven’t provided your actual contact details. "
                "Please share your full name, email, and phone number."
            )
        return human_rep_tool.run(input_text)

    tools = [
        Tool(name=order_tool.name, func=order_tool.run, description=order_tool.description),
        Tool(name=human_rep_tool.name, func=safe_human_rep_tool, description=human_rep_tool.description),
        Tool(name=policy_tool.name, func=policy_tool.run, description=policy_tool.description),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        memory=memory,
        system_message=system_prompt 
    )

    return agent

memory_instance = memory