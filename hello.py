import streamlit as st
import pandas as pd
import numpy as np


# Wedding budget planner for the region of Southern France 
st.title("Wedding Budget Planner for the Region of Southern France")

# Filter to allow the user to narrow down their options
st.subheader("Filter")
number_of_guests = st.slider("Number of guests", 0, 500)
type_of_accommodation = st.selectbox("Type of accommodation", ["Hotel", "Villa", "Castle"])
type_of_catering = st.selectbox("Type of catering", ["Sit-down dinner", "Buffet", "Family-style"])
type_of_entertainment = st.selectbox("Type of entertainment", ["Live band", "DJ", "Karaoke"])
type_of_decor = st.selectbox("Type of decor", ["Simple", "Elegant", "Extravagant"])

# Selector of the number of days for the wedding
st.subheader("Number of days")
number_of_days = st.slider("Number of days for the wedding", 0, 30)

# Maximum and minimum budget
st.subheader("Budget")
maximum_budget = st.number_input("Maximum budget", 0, 100000)
minimum_budget = st.number_input("Minimum budget", 0, maximum_budget)

# OpenAI API connection
st.subheader("OpenAI API")
openAI_connect = st.checkbox("Connect to OpenAI API for budget advice")

if openAI_connect:
    st.text("Connecting to OpenAI API...")
    # Connect to OpenAI API
    # Retrieve budget advice
    st.text("Retrieving budget advice...")
    st.text("Budget advice: Spend wisely and get the most value for your money.")  # dummy advice 

st.success("Done!")  # when the user is done creating the budget plan 
st.button("Save budget plan")  # save the budget plan
