import streamlit as st
import random

# 🎨 페이지 설정
st.set_page_config(
    page_title="감정 음악 추천기 🎧",
    page_icon="🎵",
    layout="centered"
)

# 🖌️ 기본 스타일 + 추천 박스 꾸미기
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

    .music-box {
        background-color: #1e1e1e;
        padding: 30px;
        border-radius: 15px;
        margin-top: 40px;
        text-align: center;
        border: none;
        box-shadow: 0 4px 20px rgba(0, 224, 255, 0.2);
        transition: transform 0.3s ease;
    }

    .music-box:hover {
        transform: scale(1.02);
    }

    .music-box h3 {
        color: #00e0ff;
        font-size: 26px;
        margin-bottom: 20px;
    }

    .music-link {
        display: inline-block;
        padding: 12px 24px;
        background-color: #00e0ff;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        text-decoration: none;
        font-size: 18px;
        transition: background-color 0.2s ease;
    }

    .music-link:hover {
        background-color: #00c0e0;
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

# 🎶 음악 추천 리스트 (감정별 5곡씩)
music_recommendations = {
    "😊 기쁨": [
        ("BTS - Dynamite", "https://www.youtube.com/watch?v=gdZLi9oWNZg"),
        ("Pharrell Williams - Happy", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
        ("Red Velvet - Power Up", "https://www.youtube.com/watch?v=5eAalHA1bAc"),
        ("Katy Perry - Firework", "https://www.youtube.com/watch?v=QGJuMBdaqIw"),
        ("TWICE - Dance The Night Away", "https://www.youtube.com/watch?v=Fm5iP0S1z9w")
    ],
    "😢 슬픔": [
        ("Adele - Someone Like You", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
        ("김광석 - 너무 아픈 사랑은 사랑이 아니었음을", "https://www.youtube.com/watch?v=zXEK9xYrQ8U"),
        ("IU - 사랑이 지나가면", "https://www.youtube.com/watch?v=xROz7MhbZmg"),
        ("Sam Smith - I'm Not The Only One", "https://www.youtube.com/watch?v=nCkpzqqog4k"),
        ("이문세 - 옛사랑", "https://www.youtube.com/watch?v=ugVs4m9EAYA")
    ],
    "😡 화남": [
        ("Linkin Park - Numb", "https://www.youtube.com/watch?v=kXYiU_JCYtU"),
        ("Eminem - Lose Yourself", "https://www.youtube.com/watch?v=_Yhyp-_hX2s"),
        ("방탄소년단 - RUN", "https://www.youtube.com/watch?v=wKYSYj5xaQk"),
        ("Imagine Dragons - Believer", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Stray Kids - MANIAC", "https://www.youtube.com/watch?v=OvioeS1ZZ7o")
    ],
    "😌 평온": [
        ("IU - 밤편지", "https://www.youtube.com/watch?v=BzYnNdJhZQw"),
        ("Lauv - I Like Me Better", "https://www.youtube.com/watch?v=B3eAMGXFw1o"),
        ("적재 - 나랑 같이 걸을래", "https://www.youtube.com/watch?v=HcwK8IWcV6I"),
        ("Honne - Day 1", "https://www.youtube.com/watch?v=TM9G8IVvDnE"),
        ("볼빨간사춘기 - 여행", "https://www.youtube.com/watch?v=9dwfhJZORm4")
    ],
    "😱 불안": [
        ("Coldplay - Fix You", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
        ("이수 - My Way", "https://www.youtube.com/watch?v=wDJzYRrPZ_k"),
        ("Billie Eilish - Everything I Wanted", "https://www.youtube.com/watch?v=EgBJmlPo8Xw"),
        ("자우림 - 스물다섯, 스물하나", "https://www.youtube.com/watch?v=GhKZtg0p26M"),
        ("Alan Walker - Faded", "https://www.youtube.com/watch?v=60ItHLz5WEA")
    ]
}

# 🎯 추천 결과 출력
if selected_emotion:
    music = random.choice(music_recommendations[selected_emotion])
    st.markdown(f"""
        <div class="music-box">
            <h3>🎵 추천 음악</h3>
            <a href="{music[1]}" class="music-link" target="_blank">{music[0]}</a>
        </div>
    """, unsafe_allow_html=True)
