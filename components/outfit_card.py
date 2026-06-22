import streamlit as st
from utils.favorites import save_favorite


def outfit_card(score, outfit, index):

    st.markdown(f"""
    <div style="
        background:rgba(255,255,255,.08);
        padding:25px;
        border-radius:20px;
        margin-bottom:20px;
        border:1px solid rgba(255,255,255,.15);
    ">
        <h2>⭐ Match Score: {score}%</h2>

        <p><b>👕 Top:</b> {outfit['top']}</p>

        <p><b>👖 Bottom:</b> {outfit['bottom']}</p>

        <p><b>👟 Shoes:</b> {outfit['shoes']}</p>

        <p><b>👜 Accessories:</b> {outfit['accessory']}</p>

        <p>💡 {outfit['tip']}</p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.image(outfit["image"], use_container_width=True)

    with col2:
        if st.button("❤️ Save Outfit", key=f"save_{index}"):
            save_favorite(outfit)
            st.success("Saved!")