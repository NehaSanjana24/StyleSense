import streamlit as st
from utils.recommendations import recommend
from components.outfit_card import outfit_card

def outfit_page():

    st.title("👗 AI Outfit Recommender")
    st.write("Upload your photo and get personalized outfit recommendations.")

    st.divider()

    uploaded = st.file_uploader(
        "Upload your photo",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded:
        st.image(uploaded, width=250)

    col1, col2 = st.columns(2)

    with col1:
        gender = st.radio(
            "Gender",
            ["Female", "Male"],
            horizontal=True
        )

        style = st.selectbox(
            "Style",
            [
                "Casual",
                "Formal",
                "Streetwear",
                "Minimalist"
            ]
        )

    with col2:
        occasion = st.selectbox(
            "Occasion",
            [
                "College",
                "Office",
                "Party",
                "Travel"
            ]
        )

        budget = st.select_slider(
            "Budget",
            ["Low", "Medium", "High"]
        )

    st.write("")

    if st.button("✨ Generate Recommendations", use_container_width=True):

      results = recommend(
        gender,
        style,
        occasion,
        budget
    )

    st.success("Top Outfit Recommendations")

    for index, (score, outfit) in enumerate(results):
        outfit_card(score, outfit, index)