import streamlit as st
from datetime import date 

st.title("Age Calculator")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!") 

dob = st.date_input("Enter your date of birth:",min_value=date(1900,1,1),max_value=date.today())

if dob:
    today = date.today()
    age = today.year - dob.year
    if(today.month < dob.month or (today.month == dob.month and today.day < dob.day)):
        age = age - 1
    st.write(f"{name} you are {age} years old.")    