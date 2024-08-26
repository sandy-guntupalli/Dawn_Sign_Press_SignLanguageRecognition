# import streamlit as st
# from streamlit_webrtc import webrtc_streamer
# import av

# def video_frame_callback(frame):
#     img = frame.to_ndarray(format="bgr24")

#     mirrored = img[:, ::-1, :]

#     return av.VideoFrame.from_ndarray(mirrored, format="bgr24")

# def main():
#     st.sidebar.title("ASL AI :i_love_you_hand_sign:")
#     st.sidebar.markdown("---")

#     # Create custom navigation buttons
#     selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])
#     st.title("Webcam Live Feed")
#     webrtc_streamer(key="example", video_frame_callback=video_frame_callback, rtc_configuration={ "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
#     })

# if __name__ == "__main__":
#     main()

import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

# Global variables for video recording
video_writer = None
recording = False
output_filename = "videos/recorded_video.avi"
fps = 20.0
frame_size = None

if not os.path.exists('videos'):
    os.makedirs('videos')

output_filename = "videos/recorded_video.avi"

def video_frame_callback(frame):
    global video_writer, recording, frame_size

    img = frame.to_ndarray(format="bgr24")
    
    # Flip the video horizontally (mirrored)
    mirrored = img[:, ::-1, :]

    # Initialize the VideoWriter once we know the frame size
    if recording and video_writer is None:
        frame_size = (mirrored.shape[1], mirrored.shape[0])  # (width, height)
        video_writer = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'XVID'), fps, frame_size)

    # Write the frame to the video file if recording
    if video_writer is not None:
        video_writer.write(mirrored)

    return av.VideoFrame.from_ndarray(mirrored, format="bgr24")

def main():
    global recording, video_writer

    st.sidebar.title("ASL AI :i_love_you_hand_sign:")
    st.sidebar.markdown("---")

    # Create custom navigation buttons
    selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])
    st.title("Webcam Live Feed")

    # Add checkbox to start/stop recording
    recording = st.checkbox("Record Video")

    # Display recording status
    if recording:
        st.warning("Recording in progress...")
    else:
        if video_writer is not None:
            video_writer.release()
            video_writer = None
            st.success(f"Video saved as {output_filename}")

    # Stream webcam feed
    webrtc_streamer(key="example", video_frame_callback=video_frame_callback, 
                    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})

if __name__ == "__main__":
    main()

