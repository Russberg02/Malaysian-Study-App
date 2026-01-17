import streamlit as st

st.set_page_config(page_title="Malaysian Study Hub", layout="wide")

# Simple Sidebar Navigation
st.sidebar.title("📚 Study Menu")
grade = st.sidebar.selectbox("Select Grade", ["Form 1", "Form 2", "Form 3", "Form 4", "Form 5", "Form 6"])

# Placeholder for Subjects (We will expand this later)
subject = st.sidebar.selectbox("Select Subject", ["Bahasa Melayu", "Sejarah", "Mathematics", "Science"])

st.title(f"Welcome to {grade} Study Portal")
st.write(f"You have selected **{subject}**. Content will appear here.")
