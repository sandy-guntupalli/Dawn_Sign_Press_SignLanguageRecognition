import streamlit as st
from styles import page_setup,page_with_webcam_video

st.set_page_config(page_title="Hard Mode")

# Check if 'page' exists in session state, if not, initialize it
if "page" not in st.session_state:
    st.session_state["page"] = "hardpage"

st.session_state["page"] = "hardpage"

st.markdown(page_setup(), unsafe_allow_html=True)
