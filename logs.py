# logs.py
import streamlit as st

if "logs" not in st.session_state:
    st.session_state["logs"] = []

def log_message(message):
    from datetime import datetime
    timestamp = datetime.now().strftime("%H:%M:%S")
    full_msg = f"[{timestamp}] {message}"
    st.session_state["logs"].insert(0, full_msg)

def get_logs():
    return "\n".join(st.session_state["logs"])

def clear_logs():
    st.session_state["logs"] = []
