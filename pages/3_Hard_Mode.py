import streamlit as st

st.set_page_config(page_title="Hard Mode")

# Check if 'page' exists in session state, if not, initialize it
if "page" not in st.session_state:
    st.session_state["page"] = "hardpage"

st.session_state["page"] = "hardpage"
