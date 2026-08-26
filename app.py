import streamlit as st
import plotly.graph_objects as go
from src.pdf_parser import extract_text_from_pdf
from src.text_processing import clean_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_match_score, get_fit_label
from src.recommender import generate_recommendations

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")
st.title("🚀 AI Resume Analyzer")
st.caption("Analyze a PDF resume against a job description using NLP and the provided dataset.")

resume_file = st.file_uploader("📄 Upload Resume", type=["pdf"])
job_description = st.text_area("💼 Paste Job Description", height=220)

if st.button("🔍 Analyze Resume", type="primary", use_container_width=True):
    if not resume_file or not job_description.strip():
        st.warning("Upload a PDF resume and enter a job description.")
        st.stop()
    try:
        with st.spinner("Analyzing..."):
            resume_text = extract_text_from_pdf(resume_file)
            if not resume_text.strip():
                st.error("No readable text found. Use a text-based PDF.")
                st.stop()

            resume = clean_text(resume_text)
            job = clean_text(job_description)
            score = calculate_match_score(resume, job)
            resume_skills = extract_skills(resume)
            job_skills = extract_skills(job)
            matched = sorted(set(resume_skills) & set(job_skills))
            missing = sorted(set(job_skills) - set(resume_skills))

        a,b,c,d = st.columns(4)
        a.metric("🎯 Match Score", f"{score}%")
        b.metric("🏷️ Job Fit", get_fit_label(score))
        c.metric("✅ Matched Skills", len(matched))
        d.metric("❌ Missing Skills", len(missing))

        fig = go.Figure(go.Indicator(mode="gauge+number", value=score, number={"suffix":"%"}, title={"text":"Resume–Job Match"}, gauge={"axis":{"range":[0,100]}}))
        fig.update_layout(height=280)
        st.plotly_chart(fig, use_container_width=True)

        left, right = st.columns(2)
        with left:
            st.subheader("✅ Matched Skills")
            st.write(", ".join(matched) if matched else "No matched skills detected.")
        with right:
            st.subheader("❌ Missing Skills")
            st.write(", ".join(missing) if missing else "No missing skills detected.")

        st.subheader("💡 Recommendations")
        for tip in generate_recommendations(score, missing, matched):
            st.write("- " + tip)

        with st.expander("View Extracted Resume Text"):
            st.text(resume_text)
    except FileNotFoundError as e:
        st.error(str(e))
