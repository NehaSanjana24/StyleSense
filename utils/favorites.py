import streamlit as st


def initialize_favorites():
    if "favorites" not in st.session_state:
        st.session_state["favorites"] = []


def save_favorite(outfit):
    initialize_favorites()

    if outfit not in st.session_state["favorites"]:
        st.session_state["favorites"].append(outfit)


def get_favorites():
    initialize_favorites()
    return st.session_state["favorites"]


def remove_favorite(index):
    initialize_favorites()

    if 0 <= index < len(st.session_state["favorites"]):
        st.session_state["favorites"].pop(index)