import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="🎵 Ultimate 감정 음악 추천기",
    page_icon="🎧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 감정별 데이터: (곡명, 유튜브 영상 ID, 아티스트)
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
        ("Imagine Dragons - Believer", "7wtfhZwyrcc", "Imagine Dragons"),
    ],
    "😌 평온": [
        ("IU - 밤편지", "BzYnNdJhZQw", "IU"),
        ("Lauv - I Like Me Better", "B3eAMGXFw1o", "Lauv"),
        ("Norah Jones - Come Away With Me", "lbjZPFBD6JU", "Norah Jones"),
    ],
    "😱 불안": [
        ("Coldplay - Fix You", "k4V3Mo61fJM", "Coldplay"),
        ("이수 - My Way", "wDJzYRrPZ_k", "이수"),
        ("Billie Eilish - everything i wanted", "WAi8rse3J6Q", "Billie Eilish"),
    ],
}

# 감정별 배경색 + 컬러
emotion_colors = {
    "😊 기쁨": "#FAD02E",
    "😢 슬픔": "#3A5BA0",
    "😡 화남": "#D72631",
    "😌 평온": "#7BC950",
    "😱 불안": "#4A4E69",
}

# CSS 스타일 + 애니메이션
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

body {{
    font-family: 'Montserrat', sans-serif;
    margin: 0; padding: 0;
    background: linear-gradient(135deg, #121212, #1f1f1f);
    color: #eee;
}}

.main > div {{
    padding: 1rem 2rem 3rem 2rem !important;
    max-width: 900px;
    margin: auto;
}}

h1 {{
    font-size: 4rem;
    font-weight: 900;
    color: {emotion_colors["😊 기쁨"]};
    text-align: center;
    margin-bottom: 0.1rem;
    text-shadow: 0 0 10px {emotion_colors["😊 기쁨"]};
}}

h3 {{
    font-weight: 600;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    text-align: center;
}}

.emotion-buttons {{
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 1rem;
    margin-bottom: 2rem;
}}

.emotion-button {{
    font-size: 2.4rem;
    padding: 0.6rem 1.1rem;
    border-radius: 18px;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
    background-color: #222;
    color: #ccc;
    box-shadow: 0 0 8px #000 inset;
    user-select: none;
}}

.emotion-button:hover {{
    color: white;
    box-shadow: 0 0 15px #00fff7;
    transform: scale(1.2);
}}

.emotion-button.selected {{
    color: white;
    background-color: {emotion_colors[selected_emotion] if 'selected_emotion' in locals() else emotion_colors['😊 기쁨']};
    box-shadow: 0 0 25px {emotion_colors[selected_emotion] if 'selected_emotion' in locals() else emotion_colors['😊 기쁨']};
    transform: scale(1.3);
}}

.music-info {{
    background: rgba(0, 0, 0, 0.7);
    border-radius: 25px;
    padding: 20px;
    margin-top: 30px;
    box-shadow: 0 0 30px {emotion_colors[selected_emotion] if 'selected_emotion' in locals() else emotion_colors['😊 기쁨']};
    text-align: center;
    font-weight: 700;
    font-size: 1.8rem;
}}

.music-title {{
    margin-bottom: 0.5rem;
    color: {emotion_colors[selected_emotion] if 'selected_emotion' in locals() else emotion_colors['😊 기쁨']};
    text-shadow: 0 0 10px #fff;
}}

.music-artist {{
    font-weight: 400;
    font-size: 1.3rem;
    margin-bottom: 15px;
    color: #bbb;
}}

.youtube-player {{
    border-radius: 15px;
    box-shadow: 0 0 25px {emotion_colors[selected_emotion] if 'selected_emotion' in locals() else emotion_colors['😊 기쁨']};
    max-width: 100%;
    margin: auto;
}}

.reload-btn {{
    display: block;
    margin: 30px auto 0;
    padding: 12px 30px;
    font-size: 1.3rem;
    font-weight: 700;
    background: linear-gradient(45deg, {emotion_colors[selected_emotion] if 'selected_emotion' in locals() else emotion_colors['😊 기쁨']}, #00fff7);
    color: #111;
    border: none;
    border-radius: 30px;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 0 20px #00fff7;
    user-select: none;
}}

.reload-btn:hover {{
    background: linear-gradient(45deg, #00fff7, {emotion_colors[selected_emotion] if 'selected_emotion' in locals() else emotion_colors['😊 기쁨']});
    box-shadow: 0 0 40px #00fff7;
    transform: scale(1.1);
}}

@media (max-width: 600px) {{
    h1 {{
        font-size: 2.8rem;
    }}
    .emotion-button {{
        font-size: 2rem;
        padding: 0.5rem 1rem;
    }}
    .music-info {{
        font-size: 1.3rem;
    }}
}}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1>🎧 Ultimate 감정 음악 추천기</h1>", unsafe_allow_html=True)
st.markdown("<h3>지금 기분에 딱 맞는 음악을 찾아드립니다!</h3>", unsafe_allow_html=True)

# 감정 선택 버튼 UI (커스텀)
emotion = None
cols = st.columns(len(music_recommendations))

for idx, emo in enumerate(music_recommendations.keys()):
    button_style = """
        style='
        font-size: 2.5rem;
        padding: 0.7rem 1.2rem;
        border-radius: 20px;
        border:none;
        cursor:pointer;
        user-select:none;
        background-color:#222;
        color:#ccc;
        box-shadow: 0 0 8px #000 inset;
        transition: all 0.3s ease;
        '
    """
    if st.button(emo, key=emo):
        emotion = emo

# 기본값 지정
if emotion is None:
    if 'selected_emotion' in st.session_state:
        emotion = st.session_state.selected_emotion
    else:
        emotion = "😊 기쁨"

st.session_state.selected_emotion = emotion

# 컬러 지정
color = emotion_colors[emotion]

# 감정별 배경 색상과 폰트 색 변경 (page body)
st.markdown(f"""
    <style>
        body {{
            background: linear-gradient(135deg, #121212, {color}20);
            color: #eee;
        }}
        h1 {{
            color: {color};
            text-shadow: 0 0 15px {color};
        }}
    </style>
""", unsafe_allow_html=True)

# 음악 추천 기능
if 'selected_song' not in st.session_state or st.session_state.selected_emotion != emotion:
    song = random.choice(music_recommendations[emotion])
    st.session_state.selected_song = song
else:
    song = st.session_state.selected_song

title, video_id, artist = song
thumbnail_url = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

# 음악 정보 및 플레이어 UI
st.markdown(f"""
<div class="music-info">
    <div><strong class="music-title">{title}</strong></div>
    <div class="music-artist">{artist}</div>
    <img src="{thumbnail_url}" alt="thumbnail" width="320" style="border-radius:15px; box-shadow: 0 0 25px {color}; margin-bottom:15px;" />
    <iframe class="youtube-player" width="100%" height="315" src="https://www.youtube.com/embed/{video_id}?autoplay=0&rel=0" 
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
""", unsafe_allow_html=True)

# 다시 듣기 버튼
if st.button("🔄 다시 추천 받기"):
    song = random.choice(music_recommendations[emotion])
    st.session_state.selected_song = song
    st.experimental_rerun()
