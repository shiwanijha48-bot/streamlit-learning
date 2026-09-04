import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# Gemini client
client = genai.Client(api_key=api_key)

# -------------------------
# Session State
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# UI
# -------------------------
st.title("AI Chatbot")
st.write("Ask me anything!")

# show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#  user input
question = st.chat_input("Enter your Question")
# when user sends message
if question:
    # show user message
    with st.chat_message("user"):
        st.markdown(question)
    # save user message
    st.session_state.messages.append({
        "role" :"user",
        "content":question
    })
    # get AI respoense
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            chat_history = []
            for message in st.session_state.messages:
                chat_history.append({
                    "role":message["role"],
                    "parts":[{"text":message["content"]}]
                })
            try:
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=chat_history)
                answer= response.text
                st.markdown(answer)
                
                # save AI response
                st.session_state.messages.append({
                    "role":"assistant",
                    "content":answer})
            except Exception as e:
                 st.error("Something went wrong. Please try again later.")
