from pathlib import Path
import pandas as pd
import ast, re
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

def normalize_text(value):
    if value is None:
        return ""
    if not isinstance(value, (list, tuple, dict)) and pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value).lower()).strip()

def parse_list(value):
    if pd.isna(value): return []
    try:
        parsed = ast.literal_eval(str(value))
        items = parsed if isinstance(parsed, list) else [parsed]
    except (ValueError, SyntaxError):
        items = re.split(r"[,;|/]", str(value))
    result = []
    for item in items:
        item = normalize_text(item).strip("[]'\" ")
        if item and item not in {"none", "nan", "n/a", "na"}:
            result.append(item)
    return result

def main():
    raw = DATA / "resume_data.csv"
    df = pd.read_csv(raw)
    original = df.shape
    df.columns = (df.columns.astype(str).str.replace("\ufeff", "", regex=False)
                  .str.strip().str.lower().str.replace(r"[^a-z0-9]+", "_", regex=True).str.strip("_"))
    df = df.drop_duplicates().copy()

    relevant = ["career_objective","skills","related_skils_in_job","positions",
                "responsibilities","role_positions","certification_skills",
                "job_position_name","educational_requirements",
                "experiencere_requirement","responsibilities_1","skills_required"]
    for col in relevant:
        if col in df.columns:
            df[col] = df[col].apply(normalize_text)

    if "matched_score" in df.columns:
        df["matched_score"] = pd.to_numeric(df["matched_score"], errors="coerce").clip(0, 1)

    vocab = set()
    for col in ["skills","related_skils_in_job","certification_skills","skills_required"]:
        if col in df.columns:
            for value in df[col]:
                vocab.update(parse_list(value))

    df.to_csv(DATA / "cleaned_resume_data.csv", index=False)
    pd.DataFrame(sorted(vocab), columns=["skill"]).to_csv(DATA / "skills.csv", index=False)
    print("Cleaning completed")
    print("Original shape:", original)
    print("Cleaned shape:", df.shape)
    print("Unique skills:", len(vocab))

if __name__ == "__main__":
    main()
