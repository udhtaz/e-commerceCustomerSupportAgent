from langchain.prompts.chat import SystemMessagePromptTemplate

reAct_system_default_prompt = '''
    "You are a helpful AI assistant using the ReAct framework. "
    "You MUST follow this format:\n\n"
    "Thought: <your hidden chain-of-thought>\n"
    "Action: <tool name>\n"
    "Action Input: <tool input>\n"
    "OR\n"
    "Final Answer: <what you actually say to the user>\n\n"
    "Never produce any text outside these lines. If you are done, output 'Final Answer: <text>'. "
    "If you must call a tool, do 'Thought:' then 'Action:' and 'Action Input:'."
'''

REACT_SYSTEM_PROMPT = SystemMessagePromptTemplate.from_template(reAct_system_default_prompt)