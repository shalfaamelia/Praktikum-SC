import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pickle

# Load dataset
df_mobil = pd.read_csv("CarPrice_Assignment.csv")

# Streamlit Title
st.title("Car Price Prediction and Visualization")

# Display dataset
st.subheader("Dataset Overview")
st.write(df_mobil)

# Check for missing values
missing_values = df_mobil.isnull().sum()
st.subheader("Missing Values")
st.write(missing_values)

# Dataset statistics
statistics = df_mobil.describe()
st.subheader("Dataset Statistics")
st.write(statistics)

# Data types
data_types = df_mobil.dtypes
st.subheader("Data Types")
st.write(data_types)

# Visualization 1: Car Price Distribution
st.subheader("Car Price Distribution")
fig, ax = plt.subplots(figsize=(10, 4))
sns.histplot(df_mobil['price'], kde=True, color='blue', ax=ax)
ax.set_xlabel('Price')
st.pyplot(fig)

# Visualization 2: Car Name Distribution
st.subheader("Car Name Distribution")
car_counts = df_mobil['CarName'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
car_counts.plot(kind="bar", color='green', ax=ax)
ax.set_title("Car Name Distribution")
ax.set_xlabel("Car Name")
ax.set_ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig)

# Visualization 3: Top 10 Car Names
st.subheader("Top 10 Car Names")
top_10_cars = car_counts.head(10)
st.write(top_10_cars)

fig, ax = plt.subplots(figsize=(10, 6))
top_10_cars.plot(kind="bar", color='skyblue', ax=ax)
ax.set_title("Top 10 Car Names Distribution")
ax.set_xlabel("Car Name")
ax.set_ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig)

# Visualization 4: Word Cloud of Car Names
st.subheader("Word Cloud of Car Names")
car_names = " ".join(df_mobil['CarName'])
wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(car_names)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
ax.set_title("Word Cloud of Car Names", fontsize=16)
st.pyplot(fig)

# Visualization 5: Scatter Plot - Highway MPG vs Price
st.subheader("Highway MPG vs Price")
fig, ax = plt.subplots()
ax.scatter(df_mobil['highwaympg'], df_mobil['price'], color='orange', alpha=0.7)
ax.set_xlabel('Highway MPG')
ax.set_ylabel('Price')
ax.set_title('Highway MPG vs Price')
st.pyplot(fig)

# Linear Regression Model
X = df_mobil[['highwaympg', 'curbweight', 'horsepower']]
y = df_mobil['price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model_regresi = LinearRegression()
model_regresi.fit(X_train, y_train)

# Predict using the model
model_regresi_pred = model_regresi.predict(X_test)

# Visualization 6: Actual vs Predicted Prices
st.subheader("Actual vs Predicted Prices")
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X_test['highwaympg'], y_test, label='Actual Prices', color='blue', alpha=0.6)
ax.scatter(X_test['highwaympg'], model_regresi_pred, label='Predicted Prices', color='red', alpha=0.6)
ax.set_xlabel('Highway MPG')
ax.set_ylabel('Price')
ax.legend()
ax.set_title("Actual vs Predicted Prices")
st.pyplot(fig)

# Predict price for a specific input
X_new = np.array([[32, 2338, 75]])  # Example input
harga_X = model_regresi.predict(X_new)
harga_X_int = int(round(harga_X[0]))
st.subheader(f"Predicted Price for input [Highway MPG: 32, Curb Weight: 2338, Horsepower: 75]:")
st.write(f"${harga_X_int}")

# Evaluate the model
mae = mean_absolute_error(y_test, model_regresi_pred)
mse = mean_squared_error(y_test, model_regresi_pred)
rmse = np.sqrt(mse)

st.subheader("Model Evaluation")
st.write(f"Mean Absolute Error (MAE): {mae:.2f}")
st.write(f"Mean Squared Error (MSE): {mse:.2f}")
st.write(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# Save the model
filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi, open(filename, 'wb'))
st.write(f"Model saved as {filename}")