# Resume Matching Engine

This project was developed for the Redrob AI Campus Hackathon.  
The objective of the system is to compare candidate resumes with multiple job descriptions and rank the most suitable candidates using TF-IDF and Cosine Similarity.

The entire implementation is written in pure Python without using external machine learning or data science libraries.

---

# Overview

The Resume Matching Engine processes noisy resume skill data, normalizes the skills using alias mapping, generates TF-IDF vectors for resumes, creates binary vectors for job descriptions, and calculates similarity scores to determine the best candidate matches.

The workflow follows all constraints and formulas provided in the official hackathon problem statement.

---

# Technologies Used

- Python 3
- Standard Python Libraries
  - `math`

No external libraries such as:
- NumPy
- Pandas
- Scikit-learn

were used in this project.

---

# Core Concepts Used

## Skill Normalization

The dataset contains:
- spelling mistakes
- inconsistent formatting
- multiple variations of the same skill

Examples:
- `Pyhton` → `python`
- `Reactjs` → `react`
- `Deep-learning` → `deep_learning`

The normalization pipeline:
- converts skills to lowercase
- trims spaces
- applies alias mapping
- removes unknown skills
- removes duplicates while preserving order

---

# TF-IDF Implementation

The TF-IDF calculation was implemented manually using the formulas provided in the hackathon sheet.

## Term Frequency (TF)

```math
TF = 1 / total_unique_skills
```

## Inverse Document Frequency (IDF)

```math
IDF(skill) = ln(total_resumes / document_frequency)
```

## TF-IDF Formula

```math
TF-IDF = TF × IDF
```

The vectors are generated efficiently by storing only meaningful skill values.

---

# Cosine Similarity

Cosine Similarity is used to measure how closely a resume matches a job description.

```math
Cosine(A,B) = (A · B) / (|A||B|)
```

A higher score indicates a stronger match between the resume and the JD.

---

# Workflow

## Step 1 — Skill Normalization

- Split raw skills using commas
- Convert skills to lowercase
- Apply alias mapping
- Remove duplicates
- Ignore unknown skills

## Step 2 — Vocabulary Construction

- Build a shared vocabulary from normalized resume skills
- Sort vocabulary alphabetically

## Step 3 — TF-IDF Vector Generation

- Calculate TF manually
- Calculate IDF manually
- Generate TF-IDF vectors for resumes

## Step 4 — Job Description Vectors

- Normalize JD skills
- Create binary vectors using the same vocabulary

## Step 5 — Similarity Calculation

- Compute cosine similarity between resumes and JDs

## Step 6 — Candidate Ranking

- Rank candidates based on similarity score
- Break ties alphabetically
- Return Top 3 candidates for each JD

---

# Optimizations Used

| Component | Optimization |
| --- | --- |
| Skill Mapping | Direct dictionary lookup |
| Duplicate Removal | Order-preserving deduplication |
| Vocabulary Access | Indexed lookup |
| Similarity Calculation | Sparse vector comparison |
| TF-IDF Computation | Efficient single-pass calculation |

---

# Project Structure

```bash
resume-matching-engine/
│
├── main.py
├── cosine_match.py
├── jd_vectors.py
├── process_resumes.py
├── sanity_checks.py
├── skill_normalizer.py
└── tfidf_resumes.py
```

---

# Running the Project

No installation steps are required apart from Python.

Run the project using:

```bash
python resume_matcher.py
```

---

# Sample Output

```text
JD-1 — Kakao (ML Engineer)
Sneha Patel(0.57), Karan Mehta(0.53), Arjun Sharma(0.40)

JD-2 — Naver (Backend Engineer)
Rahul Gupta(0.81), Ananya Krishnan(0.28), Deepika Rao(0.19)

JD-3 — Line (Frontend Engineer)
Aditya Kumar(0.67), Priya Nair(0.58), Ananya Krishnan(0.35)
```

---

# Key Learnings

This project helped in understanding:
- Data preprocessing
- Text normalization
- TF-IDF implementation
- Cosine similarity
- Ranking systems
- Efficient Python programming

---

# Notes

- The project was implemented completely from scratch.
- No external ML or Data Science libraries were used.
- All constraints and formulas from the official hackathon problem statement were followed.

---

# Author

Parthsaarthie Sharma  
Redrob AI Campus Hackathon Participant