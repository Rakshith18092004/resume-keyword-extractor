import re


def extract_keywords(text: str) -> list:
    """
    Extract keywords from text.
    """

    words = [
        word
        for word in re.findall(r"\b[a-zA-Z]+\b", text.lower())
        if len(word) > 2
    ]

    return list(dict.fromkeys(words))