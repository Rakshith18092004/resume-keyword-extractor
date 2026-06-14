import re
from nltk.corpus import stopwords

# Load English stopwords
STOP_WORDS = set(stopwords.words("english"))

# Custom words that are common headings but not useful keywords
IGNORE_WORDS = {
    "required",
    "responsibilities",
    "responsibility",
    "skill",
    "skills",
    "experience",
    "job",
    "role",
}


def extract_keywords(text: str) -> list:
    """
    Extract keywords from text by:
    - converting to lowercase
    - removing stopwords
    - removing custom ignore words
    - removing very short words
    - removing duplicates
    """

    # Extract alphabetic words
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    keywords = []

    for word in words:

        # Ignore very short words
        if len(word) <= 2:
            continue

        # Ignore English stopwords
        if word in STOP_WORDS:
            continue

        # Ignore headings/common words
        if word in IGNORE_WORDS:
            continue

        keywords.append(word)

    # Remove duplicates while preserving order
    return list(dict.fromkeys(keywords))