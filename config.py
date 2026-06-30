import os

try:
    import streamlit as st
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    MODEL_NAME = st.secrets.get("MODEL_NAME", "llama-3.3-70b-versatile")

except Exception:
    
    from dotenv import load_dotenv
    load_dotenv()

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")