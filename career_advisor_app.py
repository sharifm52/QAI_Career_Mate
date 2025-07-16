import streamlit as st
import openai
import os

# Initialize OpenAI client with your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit page settings
st.set_page_config(page_title="CareerMate AI", page_icon="🧠")

st.title("🧠 CareerMate AI – Your Personal Career Advisor")
st.write("Hi there! 👋 I'm CareerMate. Tell me a bit about yourself — what’s your current job or experience, and what are you interested in?")

# Start or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are CareerMate, an expert career advisor that provides helpful, clear, and practical advice based on the user's background and goals."}
    ]

# Display past messages
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["content"])

# User input box
if prompt := st.chat_input("What would you like help with?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    try:
        # Call OpenAI's GPT model
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
        st.chat_message("assistant").write(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error("Something went wrong. Please check your API key or try again later.")
        st.exception(e)
