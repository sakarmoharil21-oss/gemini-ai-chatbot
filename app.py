import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    st.error("Gemini API key not found.please configure your env file.")
genai.configure(api_key=GEMINI_API_KEY)

if "chat_session" not in st.session_state:
    model = genai.GenerativeModel("gemini-3.6-flash")
    st.session_state.chat_session = model.start_chat(history=[])

for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

if user_prompt := st.chat_input("Type your message here..."):
    with st.chat_message("user"):
        st.markdown(user_prompt)
    with st.chat_message("assistant"):
        response = st.session_state.chat_session.send_message(user_prompt)
        st.markdown(response.text)