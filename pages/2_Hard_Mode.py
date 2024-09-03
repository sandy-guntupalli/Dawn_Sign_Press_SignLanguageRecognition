import streamlit as st
from styles import page_setup,page_with_webcam_video

st.set_page_config(page_title="Hard Mode")

# Check if 'page' exists in session state, if not, initialize it
if "page" not in st.session_state:
    st.session_state["page"] = "hardpage"

st.session_state["page"] = "hardpage"

def set_font_style():
    return """
    <style>
        /* Apply Century Gothic font to the whole app */
        * {
            font-family: 'Century Gothic', sans-serif;
        }
        
        /* Specific styling for the title */
        .st-bd h1 {
            font-family: 'Century Gothic', sans-serif;
        }
    </style>
    """

st.markdown(
    """
    <style>
    .stApp {
        background-color: #89CDD3;  /* Light blue background */
    }
    </style>
    """,
    unsafe_allow_html=True)
    
st.markdown(set_font_style(), unsafe_allow_html=True)

st.markdown(page_setup(), unsafe_allow_html=True)
