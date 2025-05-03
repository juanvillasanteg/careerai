# from logic import session_manager, message_handler

# session_manager.init_session()

# user_input = st.chat_input("Say something...")

# if user_input:
#     response = message_handler.handle_user_message(user_input)
#     st.chat_message("assistant").write(response)

import time

import streamlit as st
from ui.chat import render_chat
from ui.profile import render_profile_sidebar, render_profile_expander
from ui.utils import clear_chat_history
from typing import Dict, List

def run_careerai_app():
    """Main function to run the CareerAI Streamlit app."""
    # Streamlit Page Configuration
    st.set_page_config(
        page_title="CareerAI - An interactive Resume",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            "Get help": "https://github.com/juanvillasanteg/careerai",
            "Report a bug": "https://github.com/juanvillasanteg/careerai",
            "About": """
                ## CareerAI
                ### Powered using GPT-4o-mini

                **GitHub**: https://github.com/juanvillasanteg

                Some information about the app and how to use it.
            """,
        },
    )

    with st.sidebar:
        render_profile_sidebar(clear_chat_callback=clear_chat_history)

    st.title("💬 CareerAI")
    st.caption("🚀 A Streamlit chatbot powered by LLMs")

    render_profile_expander()

    if "messages" not in st.session_state:
        st.session_state["messages"] = [
            {"role": "assistant", "content": "Ask about my professional experience!"},
        ]

    render_chat(st.session_state["messages"])

if __name__ == "__main__":
    run_careerai_app()
