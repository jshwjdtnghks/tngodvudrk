import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🎵 Ultimate 감정 음악 추천기",
    page_icon="🎧",
    layout="centered"
)

# 감정별 음악 데이터 (곡명, 유튜브 영상 ID, 아티스트)
music_recommendations = {
    "😊 기쁨": [
        ("BTS - Dynamite", "gdZLi9oWNZg", "BTS"),
        ("Pharrell Williams - Happy", "ZbZSe6N_BXs", "Pharrell Williams"),
        ("Katy Perry - Firework", "QGJuMBdaqIw", "Katy Perry"),
    ],
    "😢 슬픔": [
        ("Adel
