import streamlit as st

def clear_chat_history():
    """
    Clear the chat history in the session state.
    """
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"},
    ]
