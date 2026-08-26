import re

def clean_text(text):
    text = str(text or "").lower()
    text = re.sub(r"[^a-z0-9+#.\\s]", " ", text)
    return re.sub(r"\\s+", " ", text).strip()
