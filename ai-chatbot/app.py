import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEYT")
client = genai.Client(api_key=api_key)


st.title("AI Chatbot")
st.write("Ask me anything!")

question = st.text_input("Enter your Question")
if st.button("Ask AI"):
    if question:
        with st.spinner("Thinking..."):
            response = client.models.generate_content(
                model = "gemini-3.6-flash",
                contents=question
            )
        st.write("You asked:", question)
        st.write(response.text)

    else:
        st.warning("Please enter your question.")
