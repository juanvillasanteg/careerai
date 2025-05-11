import streamlit as st

from ui.profile import render_profile_sidebar
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

    # Define pages using st.Page
    chat_page = st.Page("ui/chat.py", title="Chat", icon=":material/chat:")
    resume_generator_page = st.Page(
        "ui/resume_generator.py",
        title="Resume with Image",
        icon=":material/description:",
    )

    pg = st.navigation(
        [
            chat_page,
            resume_generator_page,
        ],
    )
    pg.run()


if __name__ == "__main__":
    run_careerai_app()  # TODO: run with asyncio asyncio.run()
