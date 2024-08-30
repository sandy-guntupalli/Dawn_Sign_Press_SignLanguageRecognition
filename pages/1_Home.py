import streamlit as st

# Check if 'page' exists in session state, if not, initialize it
if "page" not in st.session_state:
    st.session_state["page"] = "homepage"

st.session_state["page"] = "homepage"
