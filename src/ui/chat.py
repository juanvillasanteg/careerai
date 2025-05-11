"""Chat UI Component for CareerAI."""

import streamlit as st
from streamlit_chat import message

from logic.backend_interface import get_ai_response
from ui.profile import render_profile_expander


def clear_chat() -> None:
    """Clear the chat history in session state."""
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Ask about my professional experience!",
        },
    ]


st.title("💬 CareerAI")
st.caption("🚀 A Streamlit chatbot powered by LLMs")
render_profile_expander()
st.button("Clear Chat", on_click=clear_chat)

if "messages" not in st.session_state:
    clear_chat()

# Display chat history using streamlit-chat's message component
for i, msg in enumerate(st.session_state["messages"]):
    if msg["role"] == "user":
        message(
            msg["content"],
            is_user=True,
            key=f"user_{i}",
            avatar_style="fun-emoji",
            seed="George",
        )
    else:
        message(
            msg["content"],
            is_user=False,
            key=f"assistant_{i}",
            avatar_style="bottts-neutral",
            seed="Brooklynn",
        )

if prompt := st.chat_input("Type your message..."):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    message(
        prompt,
        is_user=True,
        key=f"user_{len(st.session_state['messages'])}",
        avatar_style="fun-emoji",
        seed="George",
    )
    with st.spinner("Thinking..."):
        response = get_ai_response(st.session_state["messages"])
    st.session_state["messages"].append({"role": "assistant", "content": response})
    message(
        response,
        is_user=False,
        key=f"assistant_{len(st.session_state['messages'])}",
        avatar_style="bottts-neutral",
        seed="Brooklynn",
    )
