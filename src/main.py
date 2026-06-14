import argparse

# Import functions from other modules
from extract import extract_text
from keywords import extract_keywords
from score import (
    calculate_match,
    get_matched_keywords,
    get_missing_keywords,
)


def main():
    # ------------------------------------------
    # Step 1: Create a command-line argument parser
    # This allows the user to provide file paths
    # while running the program.
    # Example:
    # python src/main.py --resume resume.pdf --jd job.txt
    # ------------------------------------------
    parser = argparse.ArgumentParser(
        description="Resume Keyword Extractor"
    )

    # Accept resume file path from the user
    parser.add_argument(
        "--resume",
        required=True,
        help="Path to the resume file (.txt or .pdf)"
    )

    # Accept job description file path from the user
    parser.add_argument(
        "--jd",
        required=True,
        help="Path to the job description file (.txt)"
    )

    # Read the values passed through the command line
    args = parser.parse_args()

    # ------------------------------------------
    # Step 2: Extract text from both files
    # extract_text() automatically handles
    # TXT and PDF files.
    # ------------------------------------------
    resume_text = extract_text(args.resume)
    jd_text = extract_text(args.jd)

    # ------------------------------------------
    # Step 3: Extract keywords from the text
    # Converts text into useful keywords by
    # removing duplicates and short words.
    # ------------------------------------------
    resume_keywords = extract_keywords(resume_text)
    jd_keywords = extract_keywords(jd_text)

    # ------------------------------------------
    # Step 4: Compare resume and job description
    # ------------------------------------------

    # Calculate overall match percentage
    match_percentage = calculate_match(resume_keywords, jd_keywords)

    # Find keywords present in both files
    matched = get_matched_keywords(resume_keywords, jd_keywords)

    # Find keywords missing from the resume
    missing = get_missing_keywords(resume_keywords, jd_keywords)

    # ------------------------------------------
    # Step 5: Display the results
    # ------------------------------------------
    print("Match Percentage:", match_percentage, "%")
    print()

    print("Matched Keywords:")
    print(matched)
    print()

    print("Missing Keywords:")
    print(missing)


# Start the program from here
if __name__ == "__main__":
    main()