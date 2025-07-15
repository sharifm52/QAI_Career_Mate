import streamlit as st
import openai

# Enter your OpenAI API key here or set as environment variable
openai.api_key = st.secrets["OPENAI_API_KEY"]

system_prompt = """
You are a friendly and practical career advisor AI called CareerMate. 
You ask users about their interests, job background, and goals, then suggest career paths, 
learning resources, or next steps. Be non-judgmental and supportive.
"""

st.set_page_config(page_title="CareerMate AI", page_icon="🧠")
st.title("🧠 CareerMate AI – Your Personal Career Advisor")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt},
        {"role": "assistant", "content": "Hi there! 👋 I'm CareerMate. Tell me a bit about yourself — what’s your current job or experience, and what are you interested in?"}
    ]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=st.session_state.messages
    )
    reply = response.choices[0].message.content

    with st.chat_message("assistant"):
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
