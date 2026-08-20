import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("🚀 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with a job description."
)

resume = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "💼 Enter the Job Description"
)

if resume and job_description:
    st.success("Resume and Job Description received successfully!")