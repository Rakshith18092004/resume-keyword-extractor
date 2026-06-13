from extract import extract_text

def main():
    resume_text = extract_text("data/sample_resume.txt")
    print("===== Resume Content =====")
    print(resume_text)

if __name__ == "__main__":
    main()