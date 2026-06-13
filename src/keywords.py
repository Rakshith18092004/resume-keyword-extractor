import re


def extract_keywords(text: str) -> list:
    """
    Extract words from text and convert them to lowercase.
    """

    # Find all words
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    return words