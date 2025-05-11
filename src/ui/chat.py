"""Chat UI Component for CareerAI."""

import streamlit as st

from logic.backend_interface import get_ai_response
from ui.profile import render_profile_expander

st.title("💬 CareerAI")
st.caption("🚀 A Streamlit chatbot powered by LLMs")
render_profile_expander()
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Ask about my professional experience!",
        },
    ]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Thinking..."):
        message_placeholder = st.empty()
        response = get_ai_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
