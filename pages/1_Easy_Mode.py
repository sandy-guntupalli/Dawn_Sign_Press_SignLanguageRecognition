import streamlit as st
import time
import datetime
from components import progress_bar,update_video
from styles import page_setup,page_with_webcam_video
from streamlit_webrtc import webrtc_streamer
from webcam import video_frame_callback

st.set_page_config(page_title="Easy Mode")
print(datetime.datetime.now())
# Check if 'page' exists in session state, if not, initialize it
if "pages" not in st.session_state or st.session_state["pages"]!='easypage':
    st.session_state["pages"] = 'easypage'

    
st.markdown(page_setup(), unsafe_allow_html=True)
st.markdown(page_with_webcam_video(), unsafe_allow_html=True)

if "alphabet" not in st.session_state:
    st.session_state["alphabet"] = 0

ALPHABET_LIST = {
    0:"A",
    1:"B",
    2:"C",
    3:"D",
    4:"E",
    5:"F",
    6:"G",
    7:"H",
    8:"I",
    9:"J",
    10:"K",
    11:"L",
    12:"M",
    13:"N",
    14:"O",
    15:"P",
    16:"Q",
    17:"R",
    18:"S",
    19:"T",
    20:"U",
    21:"V",
    22:"W",
    23:"X",
    24:"Y",
    25:"Z"
}

NUM_ALPHABETS = len(ALPHABET_LIST)

# Element struction
col1, col2 = st.columns([0.5, 0.5])
with col1:
    video_placeholder = st.empty()  # to display video
    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
        unsafe_allow_html=True,
    )
with col2:
    # Stream webcam feed
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback, 
                    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})
    
index = 0
right_arrow_placeholder = st.empty()
if st.button("NEXT", key="right_arrow"):
    video_placeholder.empty()  # Clear the previous video
    time.sleep(0.5)  # Small delay to prevent rapid updates
    # WORD_LIST[current_word_index] # Aroosh          

    # Aroosh

    print(st.session_state["alphabet"])

    st.session_state["alphabet"] = ( st.session_state["alphabet"] + 1 ) % NUM_ALPHABETS
    index += 1
    time.sleep(1)

    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
        unsafe_allow_html=True,
    )
left_arrow_placeholder = st.empty()
if st.button("BACK", key="left_arrow"):
    video_placeholder.empty()
    # WORD_LIST[current_word_index] # Aroosh          

    # Aroosh

    print(st.session_state["alphabet"])

    st.session_state["alphabet"] = ( st.session_state["alphabet"] - 1 ) % NUM_ALPHABETS
    index -= 1

    time.sleep(1)

    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
        unsafe_allow_html=True,
    )
shuffle_placeholder = st.empty()
#if st.button("SHUFFLE", key="shuffle"):
#    video_placeholder.empty()


matched_placeholder = st.empty()

# creating the progress bar
prob = 0
progress_bar_placeholder = st.empty()

while True and st.session_state.page == "easypage":
    time.sleep(5)
    #if cap is not None or cap.isOpened():
    #    ret, frame = cap.read()
    #else:
    #    st.write("loading")

    #if ret:

    charachter = ALPHABET_LIST[st.session_state["alphabet"]]
    #frame, prob = prediction_model(frame,charachter)

    #webcam_placeholder.image(frame, channels="BGR")

    #progress_bar_placeholder.markdown(
    #    progress_bar(prob),
    #    unsafe_allow_html=True,
    #)

    #prob = 100

    #if prob == 100:
    #    st.balloons()


        

