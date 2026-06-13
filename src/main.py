from extract import extract_text
from keywords import extract_keywords

resume_text = extract_text("data/sample_resume.txt")

keywords = extract_keywords(resume_text)

print(keywords)