import logging
from typing import Any

from llama_index.core.agent import ReActAgent
from llama_index.core.prompts import PromptTemplate
from llama_index.core.tools import FunctionTool
from llama_index.llms.openai import OpenAI

from logic.query_engine import query_resume

# Set up logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def get_llm() -> Any:
    """Initialize and return the OpenAI LLM instance."""
    return OpenAI(model="gpt-4o")


def get_agent_prompt() -> PromptTemplate:
    """Return the custom ReAct system prompt for CareerAI."""
    react_system_header_str = """
You are CareerAI, an AI assistant representing a professional's career.
You have access to a powerful search tool that can retrieve any information from the resume database.

Always reason step by step, and use the search tool when you need specific details.
Respond in a professional, helpful, and concise manner.

## Tools

You have access to a wide variety of tools. You are responsible for using the tools in any sequence you deem appropriate to complete the task at hand.
This may require breaking the task into subtasks and using different tools to complete each subtask.

You have access to the following tools:
{tool_desc}


## Output Format

Please answer in the same language as the question and use the following format:

```
Thought: The current language of the user is: (user's language). I need to use a tool to help me answer the question.
Action: tool name (one of {tool_names}) if using a tool.
Action Input: the input to the tool, in a JSON format representing the kwargs (e.g. {{"input": "hello world", "num_beams": 5}})
```

Please ALWAYS start with a Thought.

NEVER surround your response with markdown code markers. You may use code markers within your response if you need to.

Please use a valid JSON format for the Action Input. Do NOT do this {{'input': 'hello world', 'num_beams': 5}}.

If this format is used, the tool will respond in the following format:

```
Observation: tool response
```

You should keep repeating the above format till you have enough information to answer the question without using any more tools. At that point, you MUST respond in one of the following two formats:

```
Thought: I can answer without using any more tools. I'll use the user's language to answer
Answer: [your answer here (In the same language as the user's question)]
```

```
Thought: I cannot answer the question with the provided tools.
Answer: [your answer here (In the same language as the user's question)]
```

## Current Conversation

Below is the current conversation consisting of interleaving human and assistant messages.
"""
    return PromptTemplate(react_system_header_str)


def get_resume_agent() -> ReActAgent:
    """Create and return the CareerAI ReActAgent with the query engine tool."""
    llm = get_llm()
    prompt = get_agent_prompt()
    # Wrap the query_resume function as a FunctionTool
    tools = [
        FunctionTool.from_defaults(
            query_resume,
            name="search_resume",
            description="Searches the resume database for relevant information. Use this tool for any question about the candidate's experience, education, skills, or background.",
        ),
    ]
    agent = ReActAgent.from_tools(
        tools=tools,
        llm=llm,
        system_prompt=prompt,
        verbose=True,
    )
    logger.info("Resume agent created with ReActAgent and query engine tool.")
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
        logger.warning("No user message found in conversation history.")
        return "No user message found."
    logger.info("Agent received user message: %s", latest_user_message)
    try:
        chat_response = agent.chat(latest_user_message)
    except Exception as e:
        logger.error("Agent failed to generate response: %s", e, exc_info=True)
        return f"Agent error: {e}"

    # Log the response and metadata
    logger.info(
        "Agent response: %s",
        getattr(chat_response, "response", str(chat_response)),
    )
    if hasattr(chat_response, "tool_calls") and chat_response.tool_calls:
        for call in chat_response.tool_calls:
            logger.info(
                "Tool called: %s with args: %s and kwargs: %s",
                getattr(call, "tool_name", None),
                getattr(call, "tool_args", None),
                getattr(call, "tool_kwargs", None),
            )
    if hasattr(chat_response, "metadata"):
        logger.info("Metadata: %s", chat_response.metadata)
    if hasattr(chat_response, "sources"):
        logger.info("Sources: %s", chat_response.sources)

    return (
        chat_response.response
        if hasattr(chat_response, "response")
        else str(chat_response)
    )
