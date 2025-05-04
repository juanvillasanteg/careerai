import time

import streamlit as st

from logic.backend_interface import get_ai_response


def render_chat(messages: list[dict[str, str]]) -> None:
    """Render the chat interface.

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
            time.sleep(1.5)  # sleep to simulate backend call

            response = get_ai_response(st.session_state.messages)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.chat_message("assistant").write(response)
