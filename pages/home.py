import streamlit as st


def home_page():

    # ================= HERO ================= #

    left, right = st.columns([1.2, 1])

    with left:

        st.markdown("""
        <div class="hero">
            <h1>STYLESENSE</h1>
            <h3>Dress Smart. Feel Confident.</h3>
            <p>
            Discover personalized outfit recommendations
            based on your style, occasion and preferences.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.button("✨ Start Styling", use_container_width=True)

    with right:
        st.image("assets/hero.jpg", use_container_width=True)

    st.write("")
    st.write("")

    # ================= FEATURES ================= #

    st.markdown("## ✨ Why Choose StyleSense?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <h2>👗</h2>
        <h3>Outfit Generator</h3>
        <p>Generate personalized outfits instantly.</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h2>🎨</h2>
        <h3>Color Matcher</h3>
        <p>Find colors that complement your style.</p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h2>💡</h2>
        <h3>Styling Guide</h3>
        <p>Professional fashion advice for every body type.</p>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # ================= TRENDING ================= #

    st.markdown("## 🔥 Trending Styles")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.image("assets/casual.jpg", use_container_width=True)
        st.markdown("### Casual")
        st.write("Comfortable everyday outfits.")

    with t2:
        st.image("assets/formal.jpg", use_container_width=True)
        st.markdown("### Formal")
        st.write("Elegant business and office fashion.")

    with t3:
        st.image("assets/streetwear.jpg", use_container_width=True)
        st.markdown("### Streetwear")
        st.write("Modern urban fashion trends.")

    st.write("")
    st.write("")

    # ================= STATS ================= #

    st.markdown("## 📊 Our Fashion Collection")

    s1, s2, s3 = st.columns(3)

    s1.metric("👗 Outfits", "500+")
    s2.metric("✨ Styles", "30+")
    s3.metric("🎉 Occasions", "20+")

    st.write("")
    st.write("")

    # ================= QUICK ACTIONS ================= #

    st.markdown("## 🚀 Quick Access")

    q1, q2, q3, q4 = st.columns(4)

    with q1:
        st.button("👗 Outfit")

    with q2:
        st.button("🎨 Colors")

    with q3:
        st.button("📅 Planner")

    with q4:
        st.button("❤️ Favorites")