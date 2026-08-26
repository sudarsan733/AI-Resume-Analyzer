from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text, job_description):
    if not str(resume_text).strip() or not str(job_description).strip():
        return 0.0
    matrix = TfidfVectorizer(stop_words="english", ngram_range=(1,2)).fit_transform([resume_text, job_description])
    return round(float(cosine_similarity(matrix[0:1], matrix[1:2])[0][0]) * 100, 2)

def get_fit_label(score):
    return "Strong Match" if score >= 75 else "Moderate Match" if score >= 50 else "Low Match"
