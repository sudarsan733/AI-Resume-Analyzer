# 🚀 AI Resume Analyzer

## 🎯 Project Goal

Build an AI/NLP-based web application that analyzes a user's **resume against a job description** and provides a **match score, skill analysis, and improvement suggestions**.

## ⚙️ How It Works

```text
Resume PDF + Job Description
            ↓
      Text Extraction
            ↓
      NLP Processing
            ↓
TF-IDF + Cosine Similarity
            ↓
      Skill Extraction
            ↓
         Analysis
            ↓
Match Score + Missing Skills +
Recommendations
```

TimelineDay:

1: Planning and creating README fileDay 
2: Extract text from the uploaded PDFDay 
3: Clean and preprocess resume/JD textDay 
4: TF-IDF + Cosine Similarity → Match ScoreDay 
5: Skill extraction → Matched & missing skillsDay 
6: Dashboard + charts + suggestions

## ✨ Key Features

- 📄 **Resume Upload** – Upload resumes in PDF format.
- 💼 **Job Description Input** – Analyze the resume against a specific job description.
- 🎯 **Match Score** – Calculate how well the resume matches the job requirements.
- ✅ **Matched Skills** – Identify skills present in both the resume and job description.
- ❌ **Missing Skills** – Highlight important skills missing from the resume.
- 📊 **Visual Dashboard** – Display analysis results using interactive charts and metrics.
- 💡 **Improvement Suggestions** – Provide recommendations to improve resume relevance.
- 🤖 **NLP-Based Analysis** – Use text processing and similarity techniques for resume analysis.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Streamlit** | Web application interface |
| **Scikit-learn** | TF-IDF vectorization and cosine similarity |
| **NLP** | Text preprocessing and analysis |
| **Pandas** | Data processing |
| **Plotly** | Interactive data visualization |
| **PyPDF** | Resume PDF text extraction |
