from pathlib import Path
from PyPDF2 import PdfReader


def extract_text(file_path: str) -> str:
    """
    Extract text from a TXT or PDF file.

    Args:
        file_path (str): Path to the input file.

    Returns:
        str: Extracted text from the file.
    """

    path = Path(file_path)

    # Check if file exists
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Handle TXT files
    if path.suffix.lower() == ".txt":
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    # Handle PDF files
    elif path.suffix.lower() == ".pdf":
        reader = PdfReader(path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    # Unsupported file type
    else:
        raise ValueError("Only .txt and .pdf files are supported.")