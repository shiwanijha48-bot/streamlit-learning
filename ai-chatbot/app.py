import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
# Gemini client
@st.cache_resource
def get_client():
    return genai.Client(api_key=api_key)
client = get_client()

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

# Side bar
with st.sidebar:
    st.title("Settings")

    if st.button(" New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.subheader(" Previous Chats")
    st.write("No previous chats yet.")
    st.divider()
    st.subheader(" Account")

    if st.button(" Sign In"):
        st.info("Login feature coming soon!")



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
                error_message = str(e)
                if "429" in error_message:
                    st.error("API quota exceeded. Please try again later.")
                elif "503" in error_message:
                    st.error("Gemini is temporarily unavailable. Please try again.")
                else:
                    st.error("Something went wrong.")
