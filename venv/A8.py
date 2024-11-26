import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set judul aplikasi
st.title("Web Display with Image, Dataset, and Graph")

# Sidebar untuk menu
menu = st.sidebar.selectbox("Select Page", ["Home", "Dataset", "Graph"])

# Fungsi untuk menampilkan gambar
def display_image(image_path):
    st.image(image_path, use_container_width=True)

# Fungsi untuk menampilkan dataset
def display_dataset(csv_path):
    df = pd.read_csv(csv_path)
    st.write(df)

# Fungsi untuk menampilkan grafik batang
def display_bar_graph(csv_path):
    df = pd.read_csv(csv_path)
    plt.figure(figsize=(10, 5))
    df.plot(kind='bar', x='Inches', y='Price (Euro)', legend=False)
    plt.title('Screen Size vs Price')
    plt.xlabel('Screen Size (Inches)')
    plt.ylabel('Price (Euro)')
    st.pyplot(plt)

# Menampilkan konten sesuai dengan menu yang dipilih
if menu == "Home":
    st.header("Welcome to the Home Page")
    display_image(r"C:\xampp\htdocs\Praktikum SC\venv\Web surfing on laptop.jpg")
    display_dataset(r"C:\xampp\htdocs\Praktikum SC\venv\laptop_price.csv")
    display_bar_graph(r"C:\xampp\htdocs\Praktikum SC\venv\laptop_price.csv")

elif menu == "Dataset":
    st.header("Dataset")
    display_dataset(r"C:\xampp\htdocs\Praktikum SC\venv\laptop_price.csv")

elif menu == "Graph":
    st.header("Screen Size VS Price")
    display_bar_graph(r"C:\xampp\htdocs\Praktikum SC\venv\laptop_price.csv")