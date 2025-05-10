# from logic import session_manager, message_handler

# session_manager.init_session()

# user_input = st.chat_input("Say something...")

# if user_input:
#     response = message_handler.handle_user_message(user_input)
#     st.chat_message("assistant").write(response)


import streamlit as st

from ui.chat import render_chat
from ui.profile import render_profile_expander, render_profile_sidebar
from ui.utils import clear_chat_history


def run_careerai_app():
    """Run the CareerAI Streamlit app."""
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

    # Static profile data (replace with dynamic load in future)
    static_profile = {
        "name": "Juan Villasante",
        "title": "AI Engineer | Data Scientist",
        "location": "Remote | Global",
        "summary": "Experienced in AI, ML, and data-driven product development.",
    }
    with st.sidebar:
        render_profile_sidebar(
            clear_chat_callback=clear_chat_history,
            profile_data=static_profile,
        )

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
