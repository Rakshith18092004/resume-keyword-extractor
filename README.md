# Resume Keyword Extractor

A Python-based command-line application that compares a resume with a job description and identifies matching and missing keywords.

## Problem Statement

Recruiters and Applicant Tracking Systems (ATS) often filter resumes based on the presence of relevant keywords from a job description. Manually comparing a resume against a job posting is time-consuming and error-prone. This project automates the process by extracting keywords from both documents, calculating a match percentage, and highlighting missing skills or terms.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Rakshith18092004/resume-keyword-extractor.git
cd resume-keyword-extractor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the project

```bash
python src/main.py --resume data/sample_resume.txt --jd data/sample_jd.txt
```

## Usage Examples

### Sample Input

Resume:

```
John Doe

Skills:
Python
Git
SQL
Machine Learning
```

Job Description:

```
Python Developer

Required Skills:
Python
Git
SQL
Machine Learning
Docker
Communication
Problem Solving
```

### Sample Output

```
==================================================
         Resume Keyword Analysis
==================================================

Match Percentage : 27.78%

Matched Keywords
--------------------
git
learning
machine
python
sql

Missing Keywords
--------------------
applications
build
collaborate
communication
databases
develop
developer
docker
models
problem

==================================================

Report successfully saved to output/report.txt
```

## Screenshots / Demo

## Screenshots / Demo

![Application Output](data\Output.png)

## Approach

The project is implemented in Python using a modular design. `extract.py` handles text extraction from TXT and PDF files using PyPDF2. `keywords.py` extracts keywords using regular expressions, removes stopwords, filters unnecessary words, and removes duplicates. `score.py` compares the extracted keywords from the resume and job description to calculate the match percentage and identify missing keywords. The command-line interface is implemented using `argparse`, allowing users to provide different resume and job description files without modifying the source code.

## Known Limitations

* Lemmatization is not currently implemented, so plural and singular forms are treated as different words.
* Noun phrase extraction is not supported.
* OCR is not available for scanned PDF documents containing images instead of selectable text.
* Keyword matching is based on exact word comparison and does not consider semantic similarity or synonyms.
