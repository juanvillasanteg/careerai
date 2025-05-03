import pytest
import streamlit as st
from ui.profile import render_profile_sidebar, render_profile_expander

def dummy_clear():
    st.session_state["cleared"] = True

def test_render_profile_sidebar(monkeypatch):
    st.session_state.clear()
    monkeypatch.setattr(st.sidebar, "button", lambda label, on_click: on_click())
    render_profile_sidebar(clear_chat_callback=dummy_clear)
    assert st.session_state.get("cleared") is True

def test_render_profile_expander():
    # This just checks that the function runs without error
    render_profile_expander()
