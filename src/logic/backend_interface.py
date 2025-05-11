"""Backend interface for CareerAI.

Connects the UI to the backend ReActAgent, which uses a retrieval-augmented generation (RAG) pipeline with Qdrant and a query engine.
"""

from agents.resume_agent import agent_respond


def get_ai_response(messages: list[dict[str, str]]) -> str:
    """Get a response from the backend AI agent using the ReActAgent and query engine.

    Args:
        messages (List[Dict[str, str]]): The conversation history.

    Returns:
        str: The AI agent's response.

    """
    return agent_respond(messages)
