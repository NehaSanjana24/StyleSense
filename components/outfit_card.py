import streamlit as st
from utils.favorites import save_favorite


def outfit_card(score, outfit, index):

    left, right = st.columns([1, 2])

    with left:
        st.image(outfit["image"], use_container_width=True)

    with right:

        st.subheader(f"⭐ Match Score: {score}%")

        st.write(f"👕 **Top:** {outfit['top']}")
        st.write(f"👖 **Bottom:** {outfit['bottom']}")
        st.write(f"👟 **Shoes:** {outfit['shoes']}")
        st.write(f"👜 **Accessories:** {outfit['accessory']}")

        st.success(outfit["tip"])

        if st.button(
            "❤️ Save Outfit",
            key=f"save_{index}_{outfit['top']}"
        ):
            save_favorite(outfit)
            st.success("Added to Favorites!")

    st.divider()