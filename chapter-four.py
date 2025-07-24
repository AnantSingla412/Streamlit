import streamlit as st
import pandas as pd

st.title("Chai sales Dashboard")

file = st.file_uploader("Upload your sales data (CSV file):", type=["csv"])    

if file:
    
    df = pd.read_csv(file)
    st.subheader("Sales Data")
    st.dataframe(df)

if file:
    st.subheader("Sales Summary")
    st.write(df.describe())

if file:
    cities = df['City'].unique()
    selected_city = st.selectbox("Select a city:", cities)
    city_data = df[df['City'] == selected_city]
    st.dataframe(city_data)