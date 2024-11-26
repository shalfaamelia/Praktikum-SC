import streamlit as st

st.checkbox("yes")

st.button("Click")

st.radio("Pick your gender", ["Male", "Female"])

st.selectbox("Pick your gender", ["Male", "Female"])

selected_planet = st.selectbox(
    "choose a planet",
    ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"],
    index=0,
    placeholder="Choose an option"
)

mark_options = ["Bad", "Good", "Excellent"]
selected_mark = st.select_slider(
    "Pick a mark", 
    options=mark_options, 
    value="Good"
)

st.slider("Pick a number", min_value=0, max_value=50, value=9)