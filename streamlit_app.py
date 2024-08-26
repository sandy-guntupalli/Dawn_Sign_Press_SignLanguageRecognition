import cv2
import streamlit as st
import time

def main():
    st.sidebar.title("ASL AI :i_love_you_hand_sign:")
    st.sidebar.markdown("---")

    # Create custom navigation buttons
    selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])
    st.title("Webcam Live Feed")

    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])

    camera = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not camera.isOpened():
        st.error("Could not open the camera.")
        return

    # Small delay to ensure the camera is initialized
    time.sleep(1)

    while run:
        ret, frame = camera.read()
        if not ret:
            st.error("Failed to capture image")
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

    camera.release()
    st.write('Stopped')

if __name__ == "__main__":
    main()
