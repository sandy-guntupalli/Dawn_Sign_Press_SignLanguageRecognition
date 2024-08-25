import streamlit as st


def main():
    st.sidebar.title("ASL AI " + ":i_love_you_hand_sign:")
    st.sidebar.markdown("---")

    # Create custom navigation buttons for both "About" and "Model"
    selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])

if __name__ == "__main__":
    main()

