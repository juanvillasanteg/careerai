import pytest
import streamlit as st

import ui.chat
from ui.chat import render_chat


@pytest.fixture(autouse=True)
def clear_session_state():
    st.session_state.clear()
    yield
    st.session_state.clear()


def test_render_chat_expected(monkeypatch):
    """Test that messages are correctly displayed in the chat interface."""
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Hi!"},
    ]
    monkeypatch.setattr(st, "chat_input", lambda: None)
    render_chat(st.session_state["messages"])
    assert st.session_state["messages"][0]["content"] == "Hello!"
    assert st.session_state["messages"][1]["content"] == "Hi!"


def test_render_chat_edge_case_empty(monkeypatch):
    """Test handling of an empty message list."""
    st.session_state["messages"] = []
    monkeypatch.setattr(st, "chat_input", lambda: None)
    render_chat(st.session_state["messages"])
    assert st.session_state["messages"] == []


def test_render_chat_failure_case(monkeypatch):
    """Test that messages without a role property raise an error."""
    st.session_state["messages"] = [{"content": "No role"}]
    monkeypatch.setattr(st, "chat_input", lambda: None)
    with pytest.raises(KeyError):
        render_chat(st.session_state["messages"])


def test_chat_backend_interface(monkeypatch):
    """Test that the chat properly calls and handles the backend response."""
    # Start with empty messages
    st.session_state["messages"] = []

    # Mock the input and backend response
    monkeypatch.setattr(st, "chat_input", lambda: "Test backend call")

    monkeypatch.setattr(
        ui.chat,
        "get_ai_response",
        lambda messages: "backend test response",
    )

    render_chat(st.session_state["messages"])

    # Should have two messages: user input and AI response
    assert len(st.session_state["messages"]) == 2
    assert st.session_state["messages"][0]["role"] == "user"
    assert st.session_state["messages"][0]["content"] == "Test backend call"
    assert st.session_state["messages"][1]["role"] == "assistant"
    assert st.session_state["messages"][1]["content"] == "backend test response"
