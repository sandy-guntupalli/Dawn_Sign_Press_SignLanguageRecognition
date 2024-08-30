import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

# Stream webcam feed
#webrtc_streamer(key="example", video_frame_callback=video_frame_callback, 
                 #rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

def video_frame_callback(frame: av.VideoFrame) -> av.VideoFrame:
    # Convert frame to a NumPy array
    img = frame.to_ndarray(format="bgr24")
    
    # Flip the video horizontally 
    img = img[:, ::-1, :]

    # Convert the frame back to av.VideoFrame
    return av.VideoFrame.from_ndarray(img, format="bgr24")
