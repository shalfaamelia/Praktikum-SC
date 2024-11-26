import streamlit as st

st.number_input("Pick a number", min_value=0, max_value=100, value=1)

st.text_input("Email address")

st.date_input("Travelling date")

st.time_input("School time")

st.text_area("Description")

st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])

st.color_picker("Choose your favourite color", value="#800080")