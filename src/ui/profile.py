import streamlit as st

def render_profile_sidebar(clear_chat_callback):
    """
    Render the profile/overview sidebar panel.

    Args:
        clear_chat_callback (Callable): Function to clear chat history.
    """
    st.title("CareerAI")
    st.caption("🚀 A Streamlit chatbot powered by LLMs")
    st.markdown(
        """
        ### About
        This is a simple Streamlit app that uses a large language model (LLM) to answer questions about my professional experience.
        """,
    )
    st.markdown(
        """
        ### Instructions
        - Ask me anything about my professional experience.
        - I will respond with relevant information.
        """,
    )
    st.sidebar.button("Clear Chat History", on_click=clear_chat_callback)

def render_profile_expander():
    """
    Render the profile/overview expander panel.
    """
    with st.expander("**📖 How to Use CareerAI**"):
        st.markdown("""
            Hi everyone! 👋
            This is a simple Streamlit app that uses a large language model (LLM) to answer questions about my professional experience.
            You can ask me anything about my professional experience, and I will respond with relevant information.
            I hope you find this app useful!
            If you have any questions or feedback, please feel free to reach out to me directly [here](https://github.com/juanvillasanteg)
        """)
