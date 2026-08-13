import base64
import time
from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / "gilsaegim-standalone.html"
SPLASH_FILE = APP_DIR / "splash.png"

st.set_page_config(
    page_title="길새김 | 운송 현장 안내",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp {
            background: #f5f7f8;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        footer {
            display: none !important;
        }

        .block-container {
            max-width: 1600px;
            padding: 0.35rem 0.5rem 0.5rem;
        }

        iframe {
            border: 0;
            border-radius: 16px;
            background: #f5f7f8;
        }

        .splash-wrap {
            position: fixed;
            inset: 0;
            z-index: 999999;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
            background: #f6f7f8;
        }

        .splash-wrap img {
            width: 100vw;
            height: 100vh;
            object-fit: contain;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.is_file():
    st.error("gilsaegim-standalone.html 파일을 찾을 수 없습니다.")
    st.stop()

if "splash_seen" not in st.session_state and SPLASH_FILE.is_file():
    splash_data = base64.b64encode(SPLASH_FILE.read_bytes()).decode("ascii")

    st.markdown(
        f"""
        <div class="splash-wrap">
            <img
                src="data:image/png;base64,{splash_data}"
                alt="길새김 시작 화면"
            >
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.session_state.splash_seen = True
    time.sleep(1.8)
    st.rerun()

st.iframe(HTML_FILE, height=1040)
