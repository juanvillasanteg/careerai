import pytest
import streamlit as st
from ui.chat import render_chat

@pytest.fixture(autouse=True)
def clear_session_state():
    st.session_state.clear()
    yield
    st.session_state.clear()

def test_render_chat_expected(monkeypatch):
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello!"},
        {"role": "user", "content": "Hi!"},
    ]
    # Monkeypatch st.chat_input to simulate user input
    monkeypatch.setattr(st, "chat_input", lambda: None)
    render_chat(st.session_state["messages"])
    assert st.session_state["messages"][0]["content"] == "Hello!"
    assert st.session_state["messages"][1]["content"] == "Hi!"

def test_render_chat_edge_case_empty(monkeypatch):
    st.session_state["messages"] = []
    monkeypatch.setattr(st, "chat_input", lambda: None)
    render_chat(st.session_state["messages"])
    assert st.session_state["messages"] == []

def test_render_chat_failure_case(monkeypatch):
    # Simulate missing 'role' key
    st.session_state["messages"] = [{"content": "No role"}]
    monkeypatch.setattr(st, "chat_input", lambda: None)
    with pytest.raises(KeyError):
        render_chat(st.session_state["messages"])
