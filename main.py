import streamlit as st
import random

# 🎨 페이지 설정
st.set_page_config(
    page_title="감정 음악 추천기 🎧",
    page_icon="🎵",
    layout="centered"
)

# 🖌️ 기본 스타일 적용
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Helvetica Neue', sans-serif;
        background-color: #121212;
        color: white;
    }

    .title {
        font-size: 48px;
        color: #00e0ff;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 20px;
        color: #cccccc;
        text-align: center;
        margin-bottom: 30px;
    }

    .emotion-btn {
        display: inline-block;
        margin: 10px;
        padding: 12px 24px;
        background-color: #1f1f1f;
        border-radius: 8px;
        border: 1px solid #00e0ff;
        color: white;
        cursor: pointer;
        font-size: 18px;
        text-align: center;
        transition: background-color 0.3s, transform 0.2s;
    }

    .emotion-btn:hover {
        background-color: #00e0ff;
        color: black;
        transform: scale(1.05);
    }

    .music-box {
        background-color: #1f1f1f;
        padding: 25px;
        border-radius: 12px;
        margin-top: 40px;
        text-align: center;
        border: 1px solid #00e0ff;
    }

    a {
        color: #00ffff;
        font-weight: bold;
        font-size: 20px;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)

# 📝 제목
st.markdown('<div class="title">🎧 감정 기반 음악 추천기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">지금 당신의 기분에 어울리는 음악은 무엇일까요?</div>', unsafe_allow_html=True)

# 🎭 감정 선택
st.markdown("---")
st.subheader("💭 현재 기분을 선택해 주세요")

emotions = {
    "😊 기쁨": "happy",
    "😢 슬픔": "sad",
    "😡 화남": "angry",
    "😌 평온": "calm",
    "😱 불안": "anxious"
}

selected_emotion = None
cols = st.columns(len(emotions))

for i, (label, key) in enumerate(emotions.items()):
    with cols[i]:
        if st.button(label, key=key):
            selected_emotion = label

# 🎶 음악 추천 리스트
music_recommendations = {
    "😊 기쁨": [
        ("BTS - Dynamite", "https://www.youtube.com/watch?v=gdZLi9oWNZg"),
        ("Pharrell Williams - Happy", "https://www.youtube.com/watch?v=ZbZSe6N_BXs")
    ],
    "😢 슬픔": [
        ("Adele - Someone Like You", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("김광석 - 너무 아픈 사랑은 사랑이 아니었음을", "https://www.youtube.com/watch?v=zXEK9xYrQ8U")
    ],
    "😡 화남": [
        ("Linkin Park - Numb", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
        ("Eminem - Lose Yourself", "https://www.youtube.com/watch?v=_Yhyp-_hX2s")
    ],
    "😌 평온": [
        ("IU - 밤편지", "https://www.youtube.com/watch?v=BzYnNdJhZQw"),
        ("Lauv - I Like Me Better", "https://www.youtube.com/watch?v=B3eAMGXFw1o")
    ],
    "😱 불안": [
        ("Coldplay - Fix You", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
        ("이수 - My Way", "https://www.youtube.com/watch?v=wDJzY
