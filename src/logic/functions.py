import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

# Function registry dictionary
tool_registry: dict[str, Callable[..., Any]] = {}


def register_tool(name: str):
    """Decorator to register a function tool by name.

    Args:
        name (str): The name to register the function under.

    Returns:
        Callable: Decorator for registering the function.

    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        tool_registry[name] = func
        return func

    return decorator


def get_tool(name: str) -> Callable[..., Any]:
    """Retrieve a registered function tool by name.

    Args:
        name (str): The name of the registered function.

    Returns:
        Callable: The registered function.

    """
    return tool_registry[name]


# --- Function Tool Stubs ---


@register_tool("get_professional_experience")
def get_professional_experience() -> str:
    """Retrieve the full professional experience markdown content.

    Returns:
        str: The full content of experience.md.

    """
    exp_path = Path("data/experience.md")
    if not exp_path.exists():
        raise FileNotFoundError(f"File not found: {exp_path}")
    with exp_path.open("r", encoding="utf-8") as f:
        return f.read()


@register_tool("get_education")
def get_education() -> list[dict[str, Any]]:
    """Retrieve the full education.json content as a Python object.

    Returns:
        list[dict[str, Any]]: List of education entries.

    """
    edu_path = Path("data/education.json")
    if not edu_path.exists():
        raise FileNotFoundError(f"File not found: {edu_path}")
    try:
        with edu_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load education data: {e}")


@register_tool("get_skills")
def get_skills() -> list[dict[str, Any]]:
    """Retrieve the full skills.json content as a Python object.

    Returns:
        list[dict[str, Any]]: List of skills.

    """
    skills_path = Path("data/skills.json")
    if not skills_path.exists():
        raise FileNotFoundError(f"File not found: {skills_path}")
    try:
        with skills_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load skills data: {e}")


@register_tool("get_user_data")
def get_user_data() -> dict[str, Any]:
    """Retrieve the full user_data.json content as a Python object.

    Returns:
        dict[str, Any]: User profile data.

    """
    user_path = Path("data/user_data.json")
    if not user_path.exists():
        raise FileNotFoundError(f"File not found: {user_path}")
    try:
        with user_path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load user data: {e}")


@register_tool("get_resume_summary")
def get_resume_summary() -> str:
    """Retrieve the full professional summary markdown content.

    Returns:
        str: The full content of summary.md.

    """
    summary_path = Path("data/summary.md")
    if not summary_path.exists():
        raise FileNotFoundError(f"File not found: {summary_path}")
    with summary_path.open("r", encoding="utf-8") as f:
        return f.read()
