# Streamlit UI for predicting diamond prices
import streamlit as st
import pandas as pd
import joblib

# Load the exported pipeline
model = joblib.load("DiamondPrediction.pkl")

st.title("💎Diamond Price Prediction✨")
st.markdown("## ⬇Enter the Diamond details ⬇")

# Feature Inputs : carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y','z'
carat = st.number_input("Carat",min_value=0.2, max_value=2.7, value=0.7)
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ['E', 'I', 'J', 'H', 'F', 'G', 'D'])
clarity = st.selectbox("Clarity", ['SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF'])
depth = st.number_input("Depth" , min_value=55.0, max_value=70.0, value=61.7)
table = st.number_input("Table", min_value=50.0, max_value=65.0, value=57.2)
x = st.number_input("Length (x)", min_value=3.0, max_value=10.0, value=5.0)
y = st.number_input("Width (y)", min_value=3.0, max_value=10.0, value=5.0)
z = st.number_input("Depth (z)", min_value=1.0, max_value=6.0, value=3.0)

# Create a DataFrame for the input data
input_data = pd.DataFrame({
    "carat": [carat],
    "cut": [cut],
    "color": [color],
    "clarity": [clarity],
    "depth": [depth],
    "table": [table],
    "x": [x],
    "y": [y],
    "z": [z]
})

if st.button("🔍Predict Price"):
    prediction = model.predict(input_data)
    
    
    st.success(f"💲The Predicted Price: {prediction[0]} 💲")



