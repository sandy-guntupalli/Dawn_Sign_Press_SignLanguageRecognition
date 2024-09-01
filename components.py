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
        <div style="text-align: center;">
        <img src="{gif_url}" alt="Sign language gif" style="width: 350px; height: 290px;">
        </div>
        """
