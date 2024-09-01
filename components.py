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

def update_video(character):
    if st.session_state["pages"]=="easypage":
        #gif_url = f"https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/{character.lower()}.gif"
        #st.image(gif_url, width=350, caption=f"Sign language: {character}")
        return f"""
        <div class="video-wrapper">
        <div class="text-overlay">
            {character}
        </div>
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scale(1.75);">
            <source src="{urls[character]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div> 
        """
