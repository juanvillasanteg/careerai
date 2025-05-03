import time

import streamlit as st

# TODO: configure logging
# logging.basicConfig(level=logging.INFO)

# Streamlit Page Configuration
st.set_page_config(
    page_title="CareerAI - An interactive Resume",
    # page_icon="imgs/avatar_streamly.png",
    layout="wide",
    initial_sidebar_state="auto",  # "expanded", "auto" or "collapsed"
    menu_items={
        "Get help": "https://github.com/juanvillasanteg/careerai",  # change this paths to icon paths
        "Report a bug": "https://github.com/juanvillasanteg/careerai",
        "About": """
            ## CareerAI
            ### Powered using GPT-4o-mini

            **GitHub**: https://github.com/juanvillasanteg

            Some information about the app and how to use it.
        """,
    },
)


# esta function puede ser extraida a un archivo utils.py
def clear_chat_history():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I assist you today?"},
    ]


with st.sidebar:
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

    st.sidebar.button("Clear Chat History", on_click=clear_chat_history)


st.title("💬 CareerAI")  # TODO: Replace the icon with a logo of the app
st.caption("🚀 A Streamlit chatbot powered by LLMs")

with st.expander("**📖 How to Use CareerAI**"):
    st.markdown("""
                    Hi everone! 👋
                    This is a simple Streamlit app that uses a large language model (LLM) to answer questions about my professional experience.
                    You can ask me anything about my professional experience, and I will respond with relevant information.
                    I hope you find this app useful!
                    If you have any questions or feedback, please feel free to reach out to me directly [here]https://github.com/juanvillasanteg)
                    """)


if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Ask about my professional experience!"},
    ]

for msg in st.session_state.messages:
    # TODO: avatar can be customized with a custom image or icon
    st.chat_message(msg["role"]).markdown(msg["content"])


if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})

    st.chat_message("user").write(prompt)

    # with st.chat_message("assistant"):
    with st.spinner("Thinking..."):
        message_placeholder = st.empty()
        time.sleep(3)
        # function to retrieve response from LLM
        # response = get_response(prompt)  # Replace with actual LLM call
        response = "This is a placeholder response."  # Replace with actual LLM call
        # response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        # message_placeholder.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)
