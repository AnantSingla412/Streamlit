import streamlit as st

st.title("Tea Maker app")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!.")

cups = st.number_input("How many cups of tea do you want?", min_value=1, max_value=10, step=1)
st.write(f"You want {cups} cups of tea")

tea_type = st.radio(
    "Select your tea base: ",["Milk","water","Almond Milk","Coconut Milk","Oat Milk"])
st.write(f"You selected: {tea_type}")  

add_masala = st.checkbox("Add Masala") 
if add_masala:
    st.write("Masala will be added to your chai")

flavour = st.selectbox(
    "Select your flavour: ",["Cardamom","Ginger","Mint","Lemon  Zest","Vanilla"])
st.write(f"You selected: {flavour}")

sugar = st.slider(
    "Sugar level(spoon): ", 0, 10, 5)
st.write(f"You selected sugar level: {sugar}")

if st.button("Make chai"):
    st.success(f"{name} your chai is being brewed")



 







