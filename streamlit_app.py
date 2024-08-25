import streamlit as st
import math

def main():
    st.sidebar.title("ASL AI " + ":i_love_you_hand_sign:")
    st.sidebar.markdown("---")

    # Create custom navigation buttons for both "About" and "Model"
    selected_page = st.sidebar.radio(" ", ["Our Mission", "ASL Detection", "Text to ASL", "Resources"])
    
def page_with_webcam_video() :
    return """
        <style>

        img {
        border-radius: 1rem;
        height:450px;
        width:350px;
        }

        .video-container {
            position: relative;
            width: 100%;
            display: flex; /* Use flexbox */
            justify-content: center; /* Center horizontally */
            align-items: center; /* Center vertically */
            padding: 2rem;
        }

        .video-wrapper {
        background-color: white;
        display: inline-block;
        width: 350px;
        height: 450px;
        overflow: hidden;
        position: relative;
        border-radius: 1rem; 
        align-content : center;
        transform: scaleX(-1);
        }

        .video-wrapper video {
        width: 100%;
        z-index: 1; /* Ensure video is behind text */
        }


        .text-overlay {
            position: absolute; 
            left: 6%;
            bottom: -7%;;
            color: #683aff;
            font-size:150px;
            z-index: 2;
            transform:scaleX(-1);
            text-align: center; /* center the text horizontally */
        }

        .video-wrapperquiz {
        background-color: white;
        width: 250px;
        height: 250px;
        overflow: hidden;
        position: relative;
        border-radius: 1rem;
        display: flex; /* Use flexbox */
        justify-content: center; /* Center horizontally */
        align-items: center; /* Center vertically */
        }

        .letterToFind {
        font-size: 190px;
        color: #ffe090;
        max-height: 20rem;
        text-align : center;
        }

        .progress-text {
        margin-top: 10px;
        text-align: center;
        }

        .progress-container {
        width: 100%;
        height: 2rem; 
        background-color: #683aff;
        border-radius: 5rem;
        position: relative;
        }

        .progress-bar {
        background-color: #ffe090; 
        height: 100%;
        border-radius: 5rem;
        width: 0;
        transition: width 0.3s ease-in-out;
        text-align: center;
        color: #683aff;
        font-size: 20px;
        font-weight: bold;
        line-height: 2rem;
        box-shadow: 10px 0 5px rgba(0, 0, 0, 0.2); /* Adjust values as needed */
        }

        /* quiz question */
        .question-text {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #ffff;
        text-align: center;
        margin-bottom: 20px;
        }

        /* button */
        .st-emotion-cache-11to1yi {
        width: 100%;
        }   

        .st-emotion-cache-1gv5c5a p {
            word-break: break-word;
            margin-bottom: 0px;
            font-size: 25px;
        }
    
        </style>
    """

if __name__ == "__main__":
    main()
    page_with_webcam_video()

