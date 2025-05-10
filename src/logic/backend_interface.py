"""Backend interface for CareerAI.

Defines the interface for connecting the UI to backend logic (mock or real).
"""

from agents.resume_agent import agent_respond


def get_ai_response(messages: list[dict[str, str]]) -> str:
    """Get a response from the backend AI agent using LlamaIndex.

    Args:
        messages (List[Dict[str, str]]): The conversation history.

    Returns:
        str: The AI agent's response.

    """
    return agent_respond(messages)
