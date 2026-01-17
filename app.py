import streamlit as st
from data import curriculum_data

# Page Setup
st.set_page_config(page_title="MY Study Hub", page_icon="📚", layout="wide")

# Custom CSS for a better look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stSelectbox label { font-weight: bold; color: #1E3A8A; }
    </style>
    """, unsafe_allow_stdio=True)

# --- SIDEBAR ---
st.sidebar.image("https://img.icons8.com/clouds/200/education.png")
st.sidebar.title("Syllabus Navigator")

# Grade Selection
grade = st.sidebar.selectbox("🎯 Choose Grade", list(curriculum_data.keys()))

# Subject Selection
available_subjects = list(curriculum_data[grade].keys())
subject = st.sidebar.selectbox("📖 Choose Subject", available_subjects)

# Chapter Selection
available_chapters = curriculum_data[grade][subject]
chapter = st.sidebar.selectbox("📑 Choose Chapter", available_chapters)

# --- MAIN CONTENT ---
st.title(f"{subject}")
st.write(f"**Level:** {grade} | **Topic:** {chapter}")
st.divider()

# Creating Tabs for different types of content
tab1, tab2, tab3 = st.tabs(["📝 Study Notes", "🎥 Video Tutorial", "🎯 Quiz"])

with tab1:
    st.header(f"Notes: {chapter}")
    
    # Example logic for showing diagrams based on subject
    if "Cell" in chapter:
        st.info("Visualizing the building blocks of life...")
        
    elif "Force" in chapter or "Motion" in chapter:
        st.info("Applying Newton's Laws...")
        
    elif "Market Equilibrium" in chapter:
        
    elif "Redox" in chapter:
        

    st.write("Detailed notes for this chapter are currently being updated. Please check back soon!")
    st.button("Download PDF Version")

with tab2:
    st.header("Related Video")
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Placeholder

with tab3:
    st.header("Quick Knowledge Check")
    st.write("Test your understanding of this topic.")
    q1 = st.radio("Have you completed the exercises for this chapter?", ["Not yet", "In Progress", "Completed"])
    if q1 == "Completed":
        st.balloons()
