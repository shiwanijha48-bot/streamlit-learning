import streamlit as st

st.title("Chai Maker App")

if st.button("Make chai"):
    st.success("Your chai is being nrewed")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala added to your chai")

tea_type = st.radio("Pick your chai base:", ["milk", "water", "almond milk"])
st.write(f"sleected base : {tea_type}")

flavour = st.selectbox("choose flavour:", ["adrak", "kesar", "tulsi"])
st.write(f"selected flavour:  {flavour}")

sugar = st.slider("sugar level", 0, 10, 2)
st.write(f"selected sugar level {sugar}")

cups = st.number_input("how many cups", min_value = 1, max_value = 10, step = 1)
st.write(f"selected sugar level {cups}")

name = st.text_input("enter your name")
name = st.text_input("enter your name")
if name:
    st.write(f"Welcome, {name}! your chai is on the way")

dob = st.date_input("Select your date of birth")
st.write(f"your date of birth is {dob}")
