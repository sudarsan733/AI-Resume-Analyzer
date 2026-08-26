from pathlib import Path
import pandas as pd
import re
ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "data" / "skills.csv"

def load_skills():
    if not SKILLS.exists():
        raise FileNotFoundError("Run: python src/data_cleaning.py")
    return sorted(pd.read_csv(SKILLS)["skill"].dropna().astype(str).str.lower().str.strip().unique(), key=len, reverse=True)

def extract_skills(text):
    text = str(text).lower()
    found = []
    for skill in load_skills():
        if re.search(r"(?<!\\w)" + re.escape(skill) + r"(?!\\w)", text):
            found.append(skill)
    return sorted(set(found))
