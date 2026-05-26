import os
import streamlit as st
from groq import Groq
from chat_prompt import build_prompt

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=api_key)

def customer_reply(user_message):
    prompt = build_prompt(user_message)
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        max_tokens=200
    )
    return response.choices[0].message.content