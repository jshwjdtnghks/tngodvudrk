import streamlit as st
import random

# 페이지 설정
st.set_page_config(
    page_title="감정 음악 추천기 🎧",
    page_icon="🎵",
    layout="centered"
)

# CSS 스타일 (더 세련되고 감성적이게)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    body {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: #e0e0e0;
        font-family: 'Montserrat', sans-serif;
    }
    .title {
        font-size: 56px;
        font-weig
