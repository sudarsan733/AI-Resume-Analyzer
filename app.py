import streamlit as st
from src.pdf_parser import extract_text_from_pdf


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("🚀 AI Resume Analyzer")

st.write(
    "Upload your resume and compare it with a job description."
)

# Resume Upload
resume = st.file_uploader(
    "📄 Upload your Resume",
    type=["pdf"]
)

# Job Description
job_description = st.text_area(
    "💼 Enter the Job Description"
)

# Process Resume
if resume is not None:

    resume_text = extract_text_from_pdf(resume)

    st.success("Resume uploaded and text extracted successfully!")

    with st.expander("📄 View Extracted Resume Text"):
        st.text(resume_text)


# Check both inputs
if resume is not None and job_description:

    st.success(
        "Resume and Job Description received successfully!"
    )