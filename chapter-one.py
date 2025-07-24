import streamlit as st

st.title("Hello, Programmer!")
st.subheader("Welcome to your Streamlit app.")
st.text("Welcome to first interacctive app")
st.write("Choose your fav. programming language")

language = st.selectbox(
    "Programming Language: ",["java", "python", "c++", "javascript", "c#", "go", "ruby"])
st.write(f"You selected: {language}")
st.success("You have successfully selected your favorite programming language!  ")