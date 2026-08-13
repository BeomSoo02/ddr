from pathlib import Path

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / "gilsaegim-standalone.html"

st.set_page_config(
    page_title="길새김 | 운송 현장 안내",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      .stApp { background: #f5f7f8; }
      [data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      footer { display: none !important; }
      .block-container {
        max-width: 1600px;
        padding: 0.35rem 0.5rem 0.5rem;
      }
      iframe[title="streamlit.components.v1.html"] {
        border: 0;
        border-radius: 16px;
        background: #f5f7f8;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.is_file():
    st.error("앱 화면 파일을 찾을 수 없습니다: gilsaegim-standalone.html")
    st.stop()

st.iframe(HTML_FILE, height=1040)
