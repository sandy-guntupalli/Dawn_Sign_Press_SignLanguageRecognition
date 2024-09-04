import streamlit as st
from styles import page_setup,page_with_webcam_video

st.markdown(page_setup(), unsafe_allow_html=True)


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

def main():
    st.markdown("""
    <style>
    body {
        background-color: #89CDD3;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(set_font_style(), unsafe_allow_html=True)
    
    st.markdown(page_setup(), unsafe_allow_html=True)
    st.write("Credits and Acknowledgements\n\nChicago Fingerspelling in the Wild Data Sets - videos of deaf signers used to train model\nSinglingo - base to create UI")


if __name__ == "__main__":
    main()



