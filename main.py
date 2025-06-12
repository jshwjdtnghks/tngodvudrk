import streamlit as st
import random

st.set_page_config(page_title="심플 감정 음악 추천기", page_icon="🎵", layout="centered")

# 감정별 곡 리스트 많이 넣기 (곡명, 유튜브 ID, 아티스트)
music_recommendations = {
    "😊 기쁨": [
        ("BTS - Dynamite", "gdZLi9oWNZg", "BTS"),
        ("Pharrell Williams - Happy", "ZbZSe6N_BXs", "Pharrell Williams"),
        ("Katy Perry - Firework", "QGJuMBdaqIw", "Katy Perry"),
        ("Bruno Mars - Uptown Funk", "OPf0YbXqDm0", "Bruno Mars"),
        ("Taylor Swift - Shake It Off", "nfWlot6h_JM", "Taylor Swift"),
        ("Mark Ronson - Valerie", "4HLY1NTe04M", "Mark Ronson"),
    ],
    "😢 슬
