from src.text_processing import clean_text
from src.matcher import calculate_match_score
score = calculate_match_score(clean_text("Python SQL Pandas"), clean_text("Python SQL"))
assert 0 <= score <= 100
print("Smoke test passed:", score)
