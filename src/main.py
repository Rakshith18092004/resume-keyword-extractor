from extract import extract_text
from keywords import extract_keywords
from score import (
    calculate_match,
    get_matched_keywords,
    get_missing_keywords,
)


def main():
    # Read files
    resume_text = extract_text("data/sample_resume.txt")
    jd_text = extract_text("data/sample_jd.txt")

    # Extract keywords
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    # Calculate results
    match_percentage = calculate_match(resume_keywords, jd_keywords)
    matched = get_matched_keywords(resume_keywords, jd_keywords)
    missing = get_missing_keywords(resume_keywords, jd_keywords)

    # Display
    print("Match Percentage:", match_percentage, "%")
    print()
    print("Matched Keywords:")
    print(matched)
    print()
    print("Missing Keywords:")
    print(missing)


if __name__ == "__main__":
    main()