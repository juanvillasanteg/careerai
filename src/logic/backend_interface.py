"""Backend interface for CareerAI.

Defines the interface for connecting the UI to backend logic (mock or real).
"""


def get_ai_response(messages: list[dict[str, str]]) -> str:
    """Get a response from the backend AI agent (mock for now).

    Args:
        messages (List[Dict[str, str]]): The conversation history.

    Returns:
        str: The AI agent's response.

    """
    # Reason: This is a placeholder for backend logic. Replace with real agent call later.
    return "This is a placeholder response from the backend interface."
