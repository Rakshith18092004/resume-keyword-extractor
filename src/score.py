
from collections import Counter


def calculate_match(resume_keywords, jd_keywords):
    """
    Calculate the percentage of JD keywords found in the resume.
    """

    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)

    matched = resume_set.intersection(jd_set)

    if len(jd_set) == 0:
        return 0

    percentage = (len(matched) / len(jd_set)) * 100

    return round(percentage, 2)


def get_matched_keywords(resume_keywords, jd_keywords):
    """
    Return keywords present in both resume and job description.
    """

    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)

    # Return in alphabetical order for better readability
    return sorted(list(resume_set.intersection(jd_set)))


def get_missing_keywords(resume_keywords, jd_keywords):
    """
    Return the top 10 keywords that are present in the
    job description but missing from the resume.

    Keywords are sorted by:
    1. Frequency in the job description (highest first)
    2. Alphabetically (if frequencies are equal)
    """

    resume_set = set(resume_keywords)

    # Count how many times each keyword appears in the JD
    keyword_counts = Counter(jd_keywords)

    # Keep only keywords that are NOT in the resume
    missing_keywords = {
        keyword: count
        for keyword, count in keyword_counts.items()
        if keyword not in resume_set
    }

    # Sort by frequency (descending), then alphabetically
    sorted_missing = sorted(
        missing_keywords.items(),
        key=lambda item: (-item[1], item[0])
    )

    # Return only the top 10 keyword names
    return [keyword for keyword, _ in sorted_missing[:10]]

