import streamlit as st
import time
from typing import List, Dict

def render_chat(messages: List[Dict[str, str]]) -> None:
    """
    Render the chat interface.

    Args:
        messages (List[Dict[str, str]]): List of message dicts with 'role' and 'content'.
    """
    for msg in messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        with st.spinner("Thinking..."):
            message_placeholder = st.empty()
            time.sleep(1.5)
            response = (
                "This is a placeholder response."  # Replace with backend/AI call later
            )
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
