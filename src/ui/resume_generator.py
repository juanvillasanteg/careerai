"""Resume Generator UI Component for CareerAI."""

import streamlit as st

st.title("📄 Resume Generator")
st.write("Generate a complete professional resume from your profile data.")

# Resume template selection
st.subheader("Resume Options")
col1, col2 = st.columns(2)

with col1:
    template = st.selectbox(
        "Select Template",
        options=["modern", "classic", "minimal", "creative"],
        index=0,
        help="Choose the visual style for your resume",
    )

with col2:
    include_image = st.checkbox(
        "Include Profile Image",
        value=True,
        help="Generate and include a professional profile image",
    )

# Color theme options
color_theme = st.selectbox(
    "Color Theme",
    options=["Blue (Default)", "Green", "Purple", "Red", "Monochrome"],
    index=0,
    help="Choose the color scheme for your resume",
)

# Generate button
if st.button("Generate Resume", type="primary"):
    with st.spinner("Generating your professional resume..."):
        # Convert color theme to format expected by generator
        color_map = {
            "Blue (Default)": "blue",
            "Green": "green",
            "Purple": "purple",
            "Red": "red",
            "Monochrome": "monochrome",
        }
        color = color_map.get(color_theme, "blue")


def initialize_resume_state():
    """Initialize session state variables for the resume generator if they don't exist."""
    if "resume_generated" not in st.session_state:
        st.session_state.resume_generated = False

    if "generated_resume_html" not in st.session_state:
        st.session_state.generated_resume_html = ""
