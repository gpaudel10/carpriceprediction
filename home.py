import streamlit as st

def home_app():
    st.title("Car Prediction app")
    st.image("data/welcome.jpg")
    st.text("""
        This web app allows a user to predict the prices of a car based on their engine size, horse power,dimensions and the drive wheel type. """
    )