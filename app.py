import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('model_real.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Title of the app
st.title('Real Estate Price Prediction')

# Input fields for user to enter data
st.header('Enter the details of the property:')

# Create input fields for each feature
transaction_date = st.number_input('Transaction Date (e.g., 2012.916667)', min_value=2012.0, max_value=2014.0, value=2013.0)
house_age = st.number_input('House Age (e.g., 32.0)', min_value=0.0, max_value=100.0, value=32.0)
distance_to_mrt = st.number_input('Distance to Nearest MRT Station (e.g., 84.87882)', min_value=0.0, max_value=10000.0, value=84.87882)
num_convenience_stores = st.number_input('Number of Convenience Stores (e.g., 10)', min_value=0, max_value=50, value=10)
latitude = st.number_input('Latitude (e.g., 24.98298)', min_value=24.0, max_value=25.0, value=24.98298)
longitude = st.number_input('Longitude (e.g., 121.54024)', min_value=121.0, max_value=122.0, value=121.54024)

# Create a DataFrame from the input data
input_data = pd.DataFrame({
     'No': [0], 
    'X1 transaction date': [transaction_date],
    'X2 house age': [house_age],
    'X3 distance to the nearest MRT station': [distance_to_mrt],
    'X4 number of convenience stores': [num_convenience_stores],
    'X5 latitude': [latitude],
    'X6 longitude': [longitude]
})

# Predict button
if st.button('Predict Price'):
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.success(f'Predicted House Price of Unit Area: {prediction[0]:.2f}')