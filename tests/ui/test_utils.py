import pytest
import streamlit as st
from ui.utils import clear_chat_history

def test_clear_chat_history():
    st.session_state["messages"] = [
        {"role": "user", "content": "Hi!"},
        {"role": "assistant", "content": "Hello!"},
    ]
    clear_chat_history()
    assert st.session_state["messages"] == [
        {"role": "assistant", "content": "How may I assist you today?"},
    ]
