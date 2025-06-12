import streamlit as st
import random

st.set_page_config(
    page_title="🎵 감정 음악 추천기",
    page_icon="🎧",
    layout="centered"
)

music_recommendations = {
    "😊 기쁨": [
        ("BTS - Dynamite", "gdZLi9oWNZg", "BTS"),
        ("Pharrell Williams - Happy", "ZbZSe6N_BXs", "Pharrell Williams"),
        ("Katy Perry - Firework", "QGJuMBdaqIw", "Katy Perry"),
    ],
    "😢 슬픔": [
        ("Adele - Someone Like You", "hLQl3WQQoQ0", "Adele"),
        ("김광석 - 너무 아픈 사랑은 사랑이 아니었음을", "zXEK9xYrQ8U", "김광석"),
        ("Sam Smith - Stay With Me", "pB-5XG-DbAA", "Sam Smith"),
    ],
    "😡 화남": [
        ("Linkin Park - Numb", "kXYiU_JCYtU", "Linkin Park"),
        ("Eminem - Lose Yourself", "_Yhyp-_hX2s", "Eminem"),
        ("Imagine Dragons - Believer", "7wtfhZwyrcc",
