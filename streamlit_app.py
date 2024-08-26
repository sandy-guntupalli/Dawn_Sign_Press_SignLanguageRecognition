import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    mirrored = img[:, ::-1, :]

    return av.VideoFrame.from_ndarray(mirrored, format="bgr24")

def main():
    st.sidebar.title("ASL AI :i_love_you_hand_sign:")
    st.sidebar.markdown("---")

    # Create custom navigation buttons
    selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])
    st.title("Webcam Live Feed")
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback, rtc_configuration={ "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    })

if __name__ == "__main__":
    main()
