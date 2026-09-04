import streamlit as st

st.title("AI Chatbot")
st.write("Ask me anything!")

question = st.text_input("Enter your Question")
if st.button("Ask AI"):
    if question:
        st.write("You asked:", question)
    else:
        st.warning("Please enter your question.")
