import streamlit as st
import time
from components import progress_bar,update_video
from styles import page_setup,page_with_webcam_video
from streamlit_webrtc import webrtc_streamer
from webcam import video_frame_callback

st.set_page_config(page_title="Easy Mode")
# Check if 'page' exists in session state, if not, initialize it
if "pages" not in st.session_state or st.session_state["pages"]!='easypage':
    st.session_state["pages"] = 'easypage'

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
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)

if "alphabet_index" not in st.session_state:
    st.session_state["alphabet_index"] = 0

# Define the alphabet list
ALPHABET_LIST = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# Element struction
col1, col2 = st.columns([0.5, 0.5])
with col1:
    video_placeholder = st.empty()  # to display video
    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet_index"]]),
        unsafe_allow_html=True,)
with col2:
    # Stream webcam feed
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback, 
                    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})
 
right_arrow_placeholder = st.empty()
if st.button("NEXT", key="right_arrow_placeholder"):
    video_placeholder.empty()  # Clear the previous video
    #time.sleep(0.5)  # Small delay to prevent rapid updates
    # WORD_LIST[current_word_index] # Aroosh          

    # Aroosh

    print(st.session_state["alphabet_index"])

    st.session_state["alphabet_index"] = ( st.session_state["alphabet_index"] + 1 ) % len(ALPHABET_LIST)
    time.sleep(1)

    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet_index"]]),
        unsafe_allow_html=True,
    )
left_arrow_placeholder = st.empty()
if st.button("BACK", key="left_arrow_placeholder"):
    video_placeholder.empty()
    # WORD_LIST[current_word_index] # Aroosh          

    # Aroosh

    print(st.session_state["alphabet_index"])

    st.session_state["alphabet_index"] = ( st.session_state["alphabet_index"] - 1 ) % len(ALPHABET_LIST)

    time.sleep(1)

    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet_index"]]),
        unsafe_allow_html=True,
    )

shuffle_placeholder = st.empty()
#if st.button("SHUFFLE", key="shuffle"):
#    video_placeholder.empty()


matched_placeholder = st.empty()

# creating the progress bar
prob = 0
progress_bar_placeholder = st.empty()

while True and st.session_state.pages == "easypage":
    time.sleep(.1)
    charachter = ALPHABET_LIST[st.session_state["alphabet_index"]]


    #progress_bar_placeholder.markdown(
    #    progress_bar(prob),
    #    unsafe_allow_html=True,
    #)

    #prob = 100

    #if prob == 100:
    #    st.balloons()


        

