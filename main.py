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
        margin-bottom: 1
