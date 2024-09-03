import streamlit as st
from styles import page_setup,page_with_webcam_video

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
st.write("DawnSign has long been recognized as an industry leader in ASL learning, consistently setting the standard for excellence. As we continue to evolve and innovate, we are now expanding into the Sign Recognition space, driven by our commitment to harnessing cutting-edge technology for the benefit of ASL learners everywhere. Our mission is to continue leading in the Ed-Tech ASL space through technological advancements that enhance education and make ASL more accessible to all. As ASL continues to be one of the fastest-growing languages in the United States, with over 500,000 people using it as their primary means of communication, we are committed to bridging the communication gap and fostering inclusivity between Deaf and hearing communities. With an estimated 2-3 out of every 1,000 children born in the U.S. being deaf or hard of hearing, the need for accessible ASL education has never been greater. By advancing Sign Recognition technology, we aim to make ASL learning more intuitive, engaging, and widely accessible, ensuring that both Deaf and hearing individuals can connect and communicate effectively. Sign Recognition technology is significantly improving ASL learning by providing an interactive and personalized experience for learners. It offers real-time feedback on signing accuracy, allowing users to correct mistakes instantly and progress more quickly. This technology also makes ASL learning more accessible by enabling self-paced study, which is particularly beneficial for those without access to in-person instruction. By integrating advanced AI, Sign Recognition enhances the learning process, making it more engaging, efficient, and tailored to individual needs, ultimately leading to greater fluency and confidence in using ASL.")

