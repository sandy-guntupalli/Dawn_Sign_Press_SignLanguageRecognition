import streamlit as st
from urls import video_urls

def progress_bar(prog):
    if(prog > 0):
        return f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: {prog}%;">{prog}%</div>
            </div>
            """
    else:
        return f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: {prog}%;"></div>
            </div>
            """

def update_video(charachter):
    if st.session_state["page"]=="easypage":
        return f"""
        <div class="video-wrapper">
        <div class="text-overlay">
            {charachter}
        </div>
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scale(1.75);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div> 
        """
    else:
        return f"""
        <div class="video-wrapper">
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scale(1.75);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div>
        """


def right_click():
    video_placeholder.empty()
    # WORD_LIST[current_word_index] # Aroosh          

    # Aroosh

    print(st.session_state["alphabet"])

    st.session_state["alphabet"] = ( st.session_state["alphabet"] + 1 ) % NUM_ALPHABETS

    time.sleep(1)

    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
        unsafe_allow_html=True,
    )

def left_click():
    video_placeholder.empty()
    # WORD_LIST[current_word_index] # Aroosh          

    # Aroosh

    print(st.session_state["alphabet"])

    st.session_state["alphabet"] = ( st.session_state["alphabet"] - 1 ) % NUM_ALPHABETS

    time.sleep(1)

    video_placeholder.markdown(
        update_video(ALPHABET_LIST[st.session_state["alphabet"]]),
        unsafe_allow_html=True,
    )
