from typing import Any

from llama_index.core.agent import FunctionCallingAgent
from llama_index.core.prompts import PromptTemplate
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI

from logic.functions import tool_registry


# Agent prompt template from PLANNING.md
def get_agent_prompt() -> PromptTemplate:
    """Return the agent prompt template for CareerAI."""
    return PromptTemplate(
        """
You are CareerAI, an AI assistant representing a Juan Villasante professional's career.
You have access to the following functions:
- get_professional_experience(): Call when asked about work history, jobs, roles, or responsibilities
- get_education(): Call when asked about education, degrees, schools, or academic background
- get_user_data(): Call when asked about personal information, contact details, or location
- get_resume_summary(): Call when asked for an overview or summary of qualifications
- get_skills(): Call when asked about skills, technologies, or competencies

When responding:
1. If the question maps to available functions, call them to get accurate information
2. If a question doesn't map to any function, politely explain that you don't have that specific information
3. Maintain a conversational, helpful tone throughout the interaction
4. If a function fails, inform the user there was an issue retrieving that information
""",
    )


def get_llm() -> Any:
    """Initialize and return the OpenAI LLM instance."""
    # The OpenAI class will use the OPENAI_API_KEY from the environment
    return OpenAI(model="gpt-4o")


# gpt-4o
# gpt-4.1-nano-2025-04-14


def get_resume_agent() -> FunctionCallingAgent:
    """Create and return the CareerAI LlamaIndex agent."""
    llm = get_llm()
    prompt = get_agent_prompt()
    # Wrap each function in tool_registry as a FunctionTool
    tools = [FunctionTool.from_defaults(fn) for fn in tool_registry.values()]
    agent = FunctionCallingAgent.from_tools(
        tools=tools,
        llm=llm,
        system_prompt=prompt,
    )
    return agent


def agent_respond(messages: list[dict[str, str]]) -> str:
    """Get a response from the CareerAI agent given conversation history.

    Args:
        messages (List[Dict[str, str]]): The conversation history.

    Returns:
        str: The agent's response.

    """
    agent = get_resume_agent()
    # Extract the latest user message (string)
    latest_user_message = ""
    for m in reversed(messages):
        if m.get("role") == "user":
            latest_user_message = m.get("content", "")
            break
    if not latest_user_message:
        return "No user message found."
    chat_response = agent.chat(latest_user_message)

    # Log the response
    print("Chat response:", chat_response)
    if hasattr(chat_response, "tool_calls"):
        print("Tool calls:", chat_response.tool_calls)
    elif hasattr(chat_response, "metadata"):
        print("Metadata:", chat_response.metadata)
    elif hasattr(chat_response, "sources"):
        print("Sources:", chat_response.sources)

    return (
        chat_response.response
        if hasattr(chat_response, "response")
        else str(chat_response)
    )
