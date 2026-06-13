from pathlib import Path


def extract_text(file_path: str) -> str:
    """
    Reads a text file and returns its contents.

    Args:
        file_path (str): Path to the text file.

    Returns:
        str: Text inside the file.
    """

    path = Path(file_path)

    # Check if the file exists
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check if it is a .txt file
    if path.suffix.lower() != ".txt":
        raise ValueError("Only .txt files are supported right now.")

    # Read the file
    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text