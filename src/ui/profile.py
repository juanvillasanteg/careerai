import streamlit as st


def render_profile_sidebar():
    """Render the profile/overview sidebar panel.

    Args:
        clear_chat_callback (Callable): Function to clear chat history.
        profile_data (Optional[dict]): Static or loaded profile data for display.

    """
    with st.expander("**About**"):
        st.markdown(
            """
            This is a simple Streamlit app that uses a large language model (LLM) to answer questions about my professional experience.
            """,
        )
        st.markdown(
            """
            **Name:** Juan Villasante  
            **Title:** AI Engineer | Data Scientist  
            **Location:** Remote | Global  
            **Summary:** Experienced in AI, ML, and data-driven product development.
            """,
        )
        st.markdown(
            """
            ### Instructions
            - Ask me anything about my professional experience.
            - I will respond with relevant information.
            """,
        )

    linkedin = "https://raw.githubusercontent.com/juanvillasanteg/careerai/dev/src/ui/assets/linkedin.gif"
    github = "https://raw.githubusercontent.com/juanvillasanteg/careerai/dev/src/ui/assets/github.gif"
    st.sidebar.caption(
        f"""
        <div style='display: flex; align-items: center;'>
            <a href = 'https://linkedin.com/in/juan-villasante'><img src='{linkedin}' style='width: 35px; height: 35px; margin-right: 25px;'></a>
            <a href = 'https://github.com/juanvillasanteg'><img src='{github}' style='width: 35px; height: 35px; margin-right: 25px;'></a>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_profile_expander():
    """Render the profile/overview expander panel."""
    with st.expander("**📖 How to Use CareerAI**"):
        st.markdown("""
            Hi everyone! 👋
            This is a simple Streamlit app that uses a large language model (LLM) to answer questions about my professional experience.
            You can ask me anything about my professional experience, and I will respond with relevant information.
            I hope you find this app useful!
            If you have any questions or feedback, please feel free to reach out to me directly [here](https://github.com/juanvillasanteg)
        """)
