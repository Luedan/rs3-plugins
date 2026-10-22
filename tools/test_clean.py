import re

def clean_text_sample(text):
    text = re.sub(r'<br\s*/?>', ' ', text, flags=re.I)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

print(clean_text_sample("Hello<br>World"))
print(clean_text_sample("Hello<br />World"))
