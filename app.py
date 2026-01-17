import streamlit as st

# Set page configuration
st.set_page_config(page_title="MY Study Hub", page_icon="🇲🇾", layout="wide")

# --- DATA STRUCTURE ---
# This dictionary maps Grade -> Subject -> Chapters
curriculum_data = {
    "Form 1 (KSSM)": {
        "Science": ["Bab 1: Introduction to Scientific Investigation", "Bab 2: Cell as the Basic Unit of Life", "Bab 3: Coordination and Response", "Bab 4: Reproduction"],
        "Sejarah": ["Bab 1: Mengenal Sejarah", "Bab 2: Zaman Air Batu", "Bab 3: Zaman Prasejarah"],
        "Mathematics": ["Bab 1: Nombor Nisbah", "Bab 2: Faktor dan Gandaan", "Bab 3: Kuasa Dua & Punca Kuasa Dua"]
    },
    "Form 4 (KSSM)": {
        "Biology": ["Bab 1: Introduction to Biology", "Bab 2: Cell Biology", "Bab 3: Movement of Substances", "Bab 4: Chemical Composition"],
        "Physics": ["Bab 1: Pengukuran", "Bab 2: Daya dan Gerakan I"],
        "Add Maths": ["Bab 1: Fungsi", "Bab 2: Fungsi Kuadratik", "Bab 3: Sistem Persamaan"]
    },
    "Form 6 (STPM)": {
        "Pengajian Am": ["Bab 1: Kemahiran Belajar", "Bab 2: Malaysia Kekal Berdaulat"],
        "Biology (STPM)": ["Chapter 1: Biological Molecules", "Chapter 2: Organelles and Diversities"],
        "Ekonomi": ["Bab 1: Pengenalan Ekonomi"]
    }
}

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("📚 Study Menu")

# Selection 1: Grade
selected_grade = st.sidebar.selectbox("1. Select Level", list(curriculum_data.keys()))

# Selection 2: Subject (Filtered by Grade)
available_subjects = list(curriculum_data[selected_grade].keys())
selected_subject = st.sidebar.selectbox("2. Select Subject", available_subjects)

# Selection 3: Chapter (Filtered by Subject)
available_chapters = curriculum_data[selected_grade][selected_subject]
selected_chapter = st.sidebar.selectbox("3. Select Chapter", available_chapters)

# --- MAIN CONTENT AREA ---
st.title(f"{selected_subject} ({selected_grade})")
st.divider()

# Displaying Content based on selection
st.header(f"📖 {selected_chapter}")

# This is where you will add your notes or PDF links later
st.info(f"You are now studying **{selected_chapter}**. Below are the resources available for this topic.")

# Example layout for study materials
col1, col2 = st.columns(2)

with col1:
    st.subheader("📝 Key Notes")
    st.write("- Important definitions")
    st.write("- Essential formulas")
    st.write("- Chapter summary")

with col2:
    st.subheader("🎥 Video Tutorial")
    # You can link YouTube videos here
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Example link

st.success("Tip: Use the sidebar to switch between subjects or forms!")
