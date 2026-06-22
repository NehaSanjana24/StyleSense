import streamlit as st
import json
import os

DATA_FILE = "data/outfits.json"


def load_outfits():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_outfits(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def admin_page():

    st.title("🛠 Admin Panel")

    outfits = load_outfits()

    st.subheader("➕ Add New Outfit")

    with st.form("add_outfit"):

        gender = st.selectbox("Gender", ["Male", "Female"])

        style = st.selectbox(
            "Style",
            [
                "Casual",
                "Formal",
                "Streetwear",
                "Minimalist"
            ]
        )

        occasion = st.selectbox(
            "Occasion",
            [
                "College",
                "Office",
                "Party",
                "Travel"
            ]
        )

        budget = st.selectbox(
            "Budget",
            [
                "Low",
                "Medium",
                "High"
            ]
        )

        top = st.text_input("Top")

        bottom = st.text_input("Bottom")

        shoes = st.text_input("Shoes")

        accessory = st.text_input("Accessory")

        tip = st.text_area("Styling Tip")

        image = st.text_input(
            "Image Path",
            "assets/casual.jpg"
        )

        submitted = st.form_submit_button("Add Outfit")

        if submitted:

            outfits.append(
                {
                    "gender": gender,
                    "style": style,
                    "occasion": occasion,
                    "budget": budget,
                    "top": top,
                    "bottom": bottom,
                    "shoes": shoes,
                    "accessory": accessory,
                    "tip": tip,
                    "image": image
                }
            )

            save_outfits(outfits)

            st.success("Outfit Added!")

            st.rerun()

    st.divider()

    st.subheader("📋 Existing Outfits")

    for i, outfit in enumerate(outfits):

        col1, col2 = st.columns([5, 1])

        with col1:

            st.write(
                f"**{outfit['top']}** • "
                f"{outfit['style']} • "
                f"{outfit['occasion']}"
            )

        with col2:

            if st.button("🗑", key=f"delete_{i}"):

                outfits.pop(i)

                save_outfits(outfits)

                st.rerun()