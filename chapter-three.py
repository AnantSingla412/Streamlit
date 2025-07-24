import streamlit as st 

st.title("chai Taste Poll")

col1,col2 = st.columns(2)

with col1:
    st.header("Masala chai")
    vote1 = st.button("Vote for Masala chai")

with col2:
    st.header("adrak chai")
    vote2 = st.button("Vote for adrak chai")

if vote1:
    st.success("Thank you for voting masala chai!")
elif vote2:
    st.success("Thank you for voting adrak chai!")

name = st.sidebar.text_input("Enter your name:")
tea = st.sidebar.selectbox(
    "Select your favorite tea:", ["Masala chai", "adrak chai", "Lemon chai", "Green tea", "Black tea"])
st.sidebar.write(f"Hello {name}, you selected {tea} as your favorite tea!")    
