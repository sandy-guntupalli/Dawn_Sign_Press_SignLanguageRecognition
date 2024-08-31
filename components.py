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
    if st.session_state["page"]=="easypage":
       gif_url = f"https://www.lifeprint.com/asl101/fingerspelling/abc-gifs/{character.lower()}.gif"
    
        return f"""
        <div class="video-wrapper">
        <img src="{gif_url}" width="350" height="290" style="transform: scale(1.75); border-radius: 1rem;">
        </div>
        """
