from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_PATH = PROJECT_ROOT / "data" / "resume_data.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "cleaned_resume_data.csv"
ROW_LIMIT = 50


def clean_dataset() -> pd.DataFrame:
    """Clean and save the first 50 rows of the bundled resume dataset."""
    df = pd.read_csv(INPUT_PATH, encoding="utf-8-sig")
    df = df.head(ROW_LIMIT).copy()

    print(f"Dataset Shape (first {ROW_LIMIT} rows):")
    print(df.shape)
    # Remove spaces and byte-order marks from column names.
    df.columns = (
        df.columns.str.strip()
        .str.replace("\ufeff", "", regex=False)
        .str.replace("ï»¿", "", regex=False)
    )
    print("\nColumn Names:")
    print(df.columns)
    print("\nMissing Values:")
    print(df.isnull().sum())
    df = df.drop_duplicates()

    text_columns = [
        "skills",
        "positions",
        "responsibilities",
        "job_position_name",
        "skills_required",
    ]
    for column in (column for column in text_columns if column in df.columns):
        df[column] = df[column].fillna("Not Available").astype(str).str.lower().str.strip()

    df.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")
    print("\nCleaning completed successfully!")
    print(f"Saved cleaned data to: {OUTPUT_PATH}")
    print("\nCleaned Dataset Shape:")
    print(df.shape)
    return df


if __name__ == "__main__":
    clean_dataset()
