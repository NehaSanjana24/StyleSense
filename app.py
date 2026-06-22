import streamlit as st

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="StyleSense",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================= CSS ================= #

try:
    with open("styles/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )
except FileNotFoundError:
    st.warning("style.css not found.")

# ================= SESSION ================= #

if "favorites" not in st.session_state:
    st.session_state["favorites"] = []

# ================= IMPORT PAGES ================= #

from pages.home import home_page
from pages.outfit import outfit_page
from pages.color_match import color_match_page
from pages.style_guide import style_guide_page
from pages.planner import planner_page
from pages.favorites import favorites_page
from pages.about import about_page

# ================= HEADER ================= #

st.markdown(
    """
    <div class="navbar">
        <div class="logo">👗 StyleSense</div>
        <div class="tagline">Dress Smart. Feel Confident.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ================= NAVIGATION ================= #

page = st.radio(
    "",
    [
        "🏠 Home",
        "👗 Outfit",
        "🎨 Color Match",
        "💡 Style Guide",
        "📅 Planner",
        "❤️ Favorites",
        "ℹ️ About",
    ],
    horizontal=True,
)

st.divider()

# ================= ROUTER ================= #

if page == "🏠 Home":
    home_page()

elif page == "👗 Outfit":
    outfit_page()

elif page == "🎨 Color Match":
    color_match_page()

elif page == "💡 Style Guide":
    style_guide_page()

elif page == "📅 Planner":
    planner_page()

elif page == "❤️ Favorites":
    favorites_page()

elif page == "ℹ️ About":
    about_page()