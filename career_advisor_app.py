import streamlit as st
import openai
import os

# Set OpenAI client using environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="CareerMate AI", page_icon="🧠")

st.title("🧠 CareerMate AI – Your Personal Career Advisor")
st.write("Hi there! 👋 I'm CareerMate. Tell me a bit about yourself — what’s your current job or experience, and what are you interested in?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are CareerMate, an expert career advisor that provides helpful, clear, and practical advice based on the user's background and goals."}
    ]

# Display chat messages
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
if prompt := st.chat_input("What would you like help with?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # OpenAI response
        response = c
