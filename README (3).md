# 🚀 AI Resume Analyzer

An end-to-end AI/ML project that analyzes a PDF resume against a job description.

## Features
- 📄 PDF resume upload
- 💼 Job description input
- 🎯 Resume–job match score
- 🧠 TF-IDF + Cosine Similarity
- ✅ Matched skills
- ❌ Missing skills
- 💡 Improvement recommendations
- 📊 Streamlit dashboard
- 🧹 Dataset cleaning and dataset-driven skill vocabulary

## Workflow
```text
resume_data.csv
      ↓
Data Cleaning
      ↓
cleaned_resume_data.csv + skills.csv
      ↓
Resume PDF + Job Description
      ↓
Text Extraction + Cleaning
      ↓
TF-IDF + Cosine Similarity
      ↓
Skill Matching
      ↓
Score + Missing Skills + Recommendations
```

## Setup

```bash
python -m venv venv
```

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/data_cleaning.py
streamlit run app.py
```

If activation is blocked:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate.ps1
```

## Project Structure

```text
AI-Resume-Analyzer/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── resume_data.csv
│   ├── cleaned_resume_data.csv
│   └── skills.csv
├── src/
│   ├── data_cleaning.py
│   ├── pdf_parser.py
│   ├── text_processing.py
│   ├── skill_extractor.py
│   ├── matcher.py
│   └── recommender.py
└── assets/
```

## Dataset

The provided `resume_data.csv` contains 9,544 records and resume/job-related fields, including skills, positions, job position, required skills, responsibilities, and `matched_score`.

The cleaning pipeline normalizes column names, removes duplicate rows, normalizes relevant text fields, converts `matched_score` to numeric form, and extracts a unique skill vocabulary from skill-related columns.

## GitHub

```bash
git init
git add .
git commit -m "Build AI Resume Analyzer"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```
