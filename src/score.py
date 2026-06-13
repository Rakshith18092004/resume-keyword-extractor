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

    return list(resume_set.intersection(jd_set))


def get_missing_keywords(resume_keywords, jd_keywords):
    """
    Return keywords that are in the job description
    but missing from the resume.
    """

    resume_set = set(resume_keywords)
    jd_set = set(jd_keywords)

    return list(jd_set - resume_set)