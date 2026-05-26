import streamlit as st
from chat_agent import customer_reply

st.set_page_config(
    page_title="BawahTech Consulting Support",
    page_icon="🛡️",
    layout="centered"
)

col1, col2 = st.columns([1, 4])

with col1:
    st.image("logo.jpeg", width=80)

with col2:
    st.markdown("## BawahTech Consulting")
    st.caption("AI-Powered Customer Support — Cybersecurity · Data Science · AI")

st.divider()

if "history" not in st.session_state:
    st.session_state.history = []

for speaker, message in st.session_state.history:
    if speaker == "Customer":
        with st.chat_message("user"):
            st.write(message)
    else:
        with st.chat_message("assistant"):
            st.write(message)

user_input = st.chat_input("Ask us about cybersecurity, data science or AI...")

if user_input:
    response = customer_reply(user_input)
    st.session_state.history.append(("Customer", user_input))
    st.session_state.history.append(("BawahTech AI", response))
    st.rerun()