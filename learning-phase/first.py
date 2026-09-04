import streamlit as st
st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interative app")
st.write("Choose your fav variety of chai")


chai = st.selectbox("Your fav chai:", ["Mashala Chai", "Adrak Chai", "Tulsi Chai"])
st.write(f"You choose {chai}. Excellent Choice!")
st.success(f"Your {chai} has been breawed!")
