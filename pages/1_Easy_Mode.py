import streamlit as st
import cv2
import time
import sqlite3
import datetime
from components import progress_bar,update_video
from styles import page_setup,page_with_webcam_video

st.set_page_config(page_title="Easy Mode")
print(datetime.datetime.now())

# Check if 'page' exists in session state, if not, initialize it
if "page" not in st.session_state or st.session_state["page"]!='easypage':
    cv2.destroyAllWindows()
    st.session_state["page"] = 'easypage'
    cap = cv2.VideoCapture(cv2.CAP_DSHOW)

conn = sqlite3.connect("signlingo.db")
c = conn.cursor()

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
    16:"R",
    17:"S",
    18:"T",
    19:"U",
    20:"V",
    21:"W",
    22:"X",
    23:"Y",
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
    webcam_placeholder = st.empty()  # to display webcam

matched_placeholder = st.empty()

# creating the progress bar
prob = 0
progress_bar_placeholder = st.empty()

while True and st.session_state.page == "learnpage":

    if cap is not None or cap.isOpened():
        ret, frame = cap.read()
    else:
        st.write("loading")

    if ret:

        charachter = ALPHABET_LIST[st.session_state["alphabet"]]
        frame, prob = prediction_model(frame,charachter)

        webcam_placeholder.image(frame, channels="BGR")

        progress_bar_placeholder.markdown(
            progress_bar(prob),
            unsafe_allow_html=True,
        )

        if prob == 100:
            st.balloons()

            video_placeholder.empty()
            # WORD_LIST[current_word_index] # Aroosh
            try:
                c.execute(
                    """INSERT INTO Alphabet (username, letter) VALUES (?, ?)""",
                    (current_user["username"], charachter),
                )
                print("added_letter")
                conn.commit()
                pass
            except Exception as e:
                print(e)            

            # Aroosh

            print(st.session_state["alphabet"])

            st.session_state["alphabet"] = ( st.session_state["alphabet"] + 1 ) % NUM_ALPHABETS

            time.sleep(2)

            video_placeholder.markdown(
                update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
                unsafe_allow_html=True,
            )

cap.release()
cv2.destroyAllWindows()
conn.close()
