import cv2
import streamlit as st

def main():
    st.sidebar.title("ASL AI :i_love_you_hand_sign:")
    st.sidebar.markdown("---")

    # Create custom navigation buttons for both "About" and "Model"
    selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])
    st.title("Webcam Live Feed")

    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])

    # Initialize camera
    camera = cv2.VideoCapture(0)
    
    if run:
        while run:
            ret, frame = camera.read()
            if not ret:
                st.error("Failed to capture image")
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)
    else:
        st.write('Stopped')

    # Release the camera when done
    camera.release()

if __name__ == "__main__":
    main()
