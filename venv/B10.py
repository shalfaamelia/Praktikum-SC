import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

st.title('Prediksi Harga Mobil')

st.header("Dataset")
# Open file csv
df1 = pd.read_csv('CarPrice_Assignment.csv')
st.dataframe(df1)

st.write("Grafik Highway-mpg")
chart_highway = pd.DataFrame(df1, columns=["highwaympg"])
st.line_chart(chart_highway)

st.write("Grafik curbweight")
chart_curbweight = pd.DataFrame(df1, columns=["curbweight"])
st.line_chart(chart_curbweight)

st.write("Grafik horsepower")
chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
st.line_chart(chart_horsepower)

# Input nilai dari variable independent
highwaympg = st.number_input('highwaympg', min_value=0, max_value=100, value=30)
curbweight = st.number_input('curbweight', min_value=500, max_value=5000, value=2000)
horsepower = st.number_input('horsepower', min_value=0, max_value=1000, value=150)

if st.button('Prediksi'):
    # Prediksi variabel yang telah diinputkan
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

    # Convert ke string
    harga_mobil_str = np.array(car_prediction)
    harga_mobil_float = float(harga_mobil_str[0])

    # Tampilkan hasil prediksi
    harga_mobil_formatted = f"$ {harga_mobil_float:,.2f}"
    st.text(f"Harga Mobil {harga_mobil_formatted}")