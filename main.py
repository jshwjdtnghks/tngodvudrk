import streamlit as st
import random

# 🎨 페이지 설정
st.set_page_config(
    page_title="감정 음악 추천기 🎧",
    page_icon="🎵",
    layout="centered"
)

# 🖌️ 스타일
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .title {
        font-size: 48px;
        color: #00e0ff;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #cccccc;
        text-align: center;
    }
    .music-box {
        background-color: #1f1f1f;
        padding: 20px;
        border-radius: 12px;
        margin-top: 30px;
        text-align: center;
    }
    a {
        color: #00ffff;
        font-weight: bold;
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
st.subheader("당신의 현재 감정을 골라주세요 💭")

emotions = ["😊 기쁨", "😢 슬픔", "😡 화남", "😌 평온", "😱 불안"]
selected_emotion = st.selectbox("감정 선택:", emotions)

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
        ("이수 - My Way", "https://www.youtube.com/watch?v=wDJzYRrPZ_k")
    ]
}

# 🎯 추천 버튼
if st.button("음악 추천 받기 🎵"):
    music = random.choice(music_recommendations[selected_emotion])
    st.markdown(f"""
        <div class="music-box">
            <h3>추천 음악:</h3>
            <a href="{music[1]}" target="_blank">{music[0]}</a>
        </div>
    """, unsafe_allow_html=True)
