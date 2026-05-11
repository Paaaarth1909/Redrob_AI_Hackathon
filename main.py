
import math


RESUMES = [
    {"id": "01", "name": "Arjun Sharma",
     "skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning",
     "background": "TCS Intern . BITS Pilani CSE 2024"},
    {"id": "02", "name": "Priya Nair",
     "skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS",
     "background": "Freelance Web Developer . VIT IT 2024"},
    {"id": "03", "name": "Rahul Gupta",
     "skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates",
     "background": "Infosys SDE Intern . IIT Delhi 2023"},
    {"id": "04", "name": "Sneha Patel",
     "skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib",
     "background": "IISc Research Assistant . IIIT Hyderabad AI 2024"},
    {"id": "05", "name": "Vikram Singh",
     "skills": "C++, Algoritms, Data Structure, competitive programming, python",
     "background": "Google SWE Intern . IIT Bombay 2024"},
    {"id": "06", "name": "Ananya Krishnan",
     "skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD",
     "background": "Full Stack Developer . NIT Trichy 2022"},
    {"id": "07", "name": "Karan Mehta",
     "skills": "Python, Sklearn, XGboost, feature engineering, SQL, tableau",
     "background": "Data Analyst . Delhi University 2023"},
    {"id": "08", "name": "Deepika Rao",
     "skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma",
     "background": "Samsung Android Intern . NSIT 2024"},
    {"id": "09", "name": "Aditya Kumar",
     "skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest",
     "background": "Frontend SDE . Flipkart / IIIT Bangalore"},
    {"id": "10", "name": "Meera Iyer",
     "skills": "python, R, statistics, ML, regression, clustering, Power-BI",
     "background": "Data Science Intern . Wipro 2024"},
]

JOB_DESCRIPTIONS = [
    {"id": "JD-1", "company": "Kakao (Seoul)", "role": "ML Engineer",
     "required_skills": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization",
     "preferred_skills": "NLP, BERT, Feature Engineering, Statistics"},
    {"id": "JD-2", "company": "Naver (Seongnam)", "role": "Backend Engineer",
     "required_skills": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes",
     "preferred_skills": "REST API, CI/CD, Redis"},
    {"id": "JD-3", "company": "Line (Seoul)", "role": "Frontend Engineer",
     "required_skills": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS",
     "preferred_skills": "Node.js, GraphQL, Redux, Jest, AWS"},
]

SKILL_ALIASES = {
    "python": "python", "pyhton": "python",
    "java": "java",
    "javascript": "javascript", "javascrpit": "javascript", "js": "javascript",
    "typescript": "typescript", "typescrpit": "typescript",
    "c++": "cpp", "cpp": "cpp",
    "r": "r", "kotlin": "kotlin",
    "machinelearning": "machine_learning", "machine learning": "machine_learning",
    "ml": "machine_learning", "sklearn": "machine_learning",
    "deeplearning": "deep_learning", "deep learning": "deep_learning",
    "deep-learning": "deep_learning",
    "tensorflow": "tensorflow", "pytorch": "pytorch", "keras": "keras",
    "nlp": "nlp", "bert": "bert", "xgboost": "xgboost",
    "feature engineering": "feature_engineering",
    "statistics": "statistics", "stats": "statistics",
    "regression": "regression", "clustering": "clustering",
    "data-viz": "data_visualization", "data visualization": "data_visualization",
    "data viz": "data_visualization", "matplotlib": "data_visualization",
    "tableau": "data_visualization", "power-bi": "data_visualization",
    "power bi": "data_visualization", "powerbi": "data_visualization",
    "pandas": "pandas", "numpy": "numpy",
    "react": "react", "reacts": "react", "reactjs": "react",
    "vue": "vue", "vue.js": "vue", "vuejs": "vue",
    "redux": "redux", "tailwind": "tailwind",
    "html/css": "html_css", "html css": "html_css", "html": "html_css", "css": "html_css",
    "jest": "jest", "graphql": "graphql",
    "node.js": "nodejs", "nodejs": "nodejs", "node js": "nodejs",
    "flask": "flask",
    "spring boot": "spring_boot", "springboot": "spring_boot",
    "rest api": "rest_api", "rest": "rest_api", "restapi": "rest_api",
    "microservices": "microservices",
    "sql": "sql", "mysql": "mysql", "mysq": "mysql",
    "postgresql": "postgresql", "postgres": "postgresql",
    "mongodb": "mongodb", "redis": "redis",
    "docker": "docker",
    "kubernetes": "kubernetes", "kubernates": "kubernetes", "k8s": "kubernetes",
    "ci/cd": "ci_cd", "cicd": "ci_cd", "ci cd": "ci_cd",
    "aws": "aws",
    "android": "android", "firebase": "firebase",
    "algorithms": "algorithms", "algoritms": "algorithms",
    "data structure": "data_structures", "data structures": "data_structures",
    "competitive programming": "competitive_programming",
    "ui/ux": "ui_ux", "ui ux": "ui_ux", "figma": "figma",
}

# Pre-compute multi-word alias set once (avoids rebuilding every call)
_MULTI_WORD_SET = frozenset(k for k in SKILL_ALIASES if " " in k)


# ─── STEP 1: SKILL NORMALIZATION ────────────────────────────────────────────────

def normalize_skills(raw_skill_string):
    """
    Multi-stage normalization pipeline:
      1. Tokenize (split on commas, trim, lowercase)
      2. Multi-word phrase matching (exact match against alias set)
      3. Single-token alias mapping
      4. Discard unknown tokens
      5. Deduplicate (preserve first-occurrence order)
    """
    tokens = [t.strip().lower() for t in raw_skill_string.split(",") if t.strip()]

    normalized = []
    for token in tokens:
        # Stage 2 & 3 combined: direct O(1) dict lookup handles both
        # multi-word phrases and single tokens identically
        if token in SKILL_ALIASES:
            normalized.append(SKILL_ALIASES[token])
        # Stage 4: Unknown token — skip

    # Stage 5: Deduplicate preserving order via dict (ordered since Python 3.7+)
    return list(dict.fromkeys(normalized))


# ─── STEP 2: VOCABULARY + INDEX ─────────────────────────────────────────────────

def build_vocabulary(all_resume_skills):
    """Build sorted vocabulary and a reverse index map for O(1) position lookups."""
    vocab = sorted({skill for skills in all_resume_skills for skill in skills})
    index = {skill: i for i, skill in enumerate(vocab)}
    return vocab, index


# ─── STEP 3: TF-IDF (single-pass DF) ────────────────────────────────────────────

def compute_idf_table(all_resume_skills, vocabulary):
    """
    Single-pass DF + IDF computation.
    DF counts how many resumes contain each skill.
    IDF(skill) = ln(N / df). No smoothing.
    """
    n = len(all_resume_skills)
    df = dict.fromkeys(vocabulary, 0)

    # Single pass over resumes to count document frequencies
    for skills in all_resume_skills:
        for skill in set(skills):          # set() avoids double-counting within a resume
            if skill in df:
                df[skill] += 1

    idf = {skill: math.log(n / count) for skill, count in df.items()}
    return df, idf


# ─── STEP 4: SPARSE VECTOR GENERATION ───────────────────────────────────────────

def tfidf_sparse(resume_skills, vocab_index, idf):
    """
    Build a SPARSE TF-IDF representation (dict of index -> value).
    Only stores non-zero entries, cutting memory and speeding up dot products.
    TF = 1 / |unique_skills|
    """
    if not resume_skills:
        return {}, 0.0
    tf = 1.0 / len(resume_skills)
    sparse = {}
    mag_sq = 0.0
    for skill in resume_skills:
        idx = vocab_index.get(skill)
        if idx is not None:
            val = tf * idf[skill]
            sparse[idx] = val
            mag_sq += val * val
    return sparse, math.sqrt(mag_sq)           # return pre-computed magnitude


def jd_skill_indices(jd_skills, vocab_index):
    """
    Instead of a full binary vector, return a set of matching vocab indices
    and the magnitude (sqrt of count of matches)).
    """
    indices = frozenset(vocab_index[s] for s in jd_skills if s in vocab_index)
    mag = math.sqrt(len(indices)) if indices else 0.0
    return indices, mag


# ─── STEP 5: SPARSE COSINE SIMILARITY ───────────────────────────────────────────

def cosine_similarity_sparse(sparse_a, mag_a, jd_indices, mag_b):
    """
    Optimised cosine similarity using sparse resume vector and JD index set.
    Only iterates over the resume's non-zero entries (typically 5-7 skills)
    instead of the full 48-element vocabulary.
    """
    if mag_a == 0.0 or mag_b == 0.0:
        return 0.0
    # Dot product: sum resume TF-IDF values where JD also has a 1
    dot = sum(val for idx, val in sparse_a.items() if idx in jd_indices)
    return dot / (mag_a * mag_b)


# ─── STEP 6: RANKING ────────────────────────────────────────────────────────────

def rank_candidates(scores_with_names, top_n=3):
    """Sort desc by score, break ties alphabetically, return top N."""
    ranked = sorted(scores_with_names, key=lambda x: (-x[1], x[0]))
    return ranked[:top_n]


# ─── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    sep = "=" * 80

    print(sep)
    print("RESUME MATCHING ENGINE - REDROB AI CAMPUS HACKATHON")
    print(sep)

    # Step 1: Normalize
    print("\nStep 1: Normalizing resume skills...")
    all_norm_skills = []
    for r in RESUMES:
        r["norm"] = normalize_skills(r["skills"])
        all_norm_skills.append(r["norm"])
    print("[OK] Normalized {} resumes".format(len(RESUMES)))

    # Step 2: Build vocabulary + index
    print("\nStep 2: Building vocabulary...")
    vocab, vocab_index = build_vocabulary(all_norm_skills)
    print("[OK] Vocabulary size: {} unique skills".format(len(vocab)))

    # Step 3: Compute IDF (single-pass DF)
    print("\nStep 3: Calculating TF-IDF...")
    df, idf = compute_idf_table(all_norm_skills, vocab)
    print("[OK] Calculated document frequencies")
    print("[OK] Calculated inverse document frequencies")

    # Step 4: Generate sparse TF-IDF vectors + pre-compute magnitudes
    print("\nStep 4: Generating TF-IDF vectors...")
    resume_vecs = [tfidf_sparse(r["norm"], vocab_index, idf) for r in RESUMES]
    print("[OK] Generated {} TF-IDF vectors".format(len(resume_vecs)))

    # Step 5: Match
    print("\nStep 5: Matching candidates to job descriptions...")
    print("\n" + sep)
    print("RESULTS")
    print(sep)

    for jd in JOB_DESCRIPTIONS:
        combined = jd["required_skills"] + ", " + jd["preferred_skills"]
        jd_skills = normalize_skills(combined)
        jd_idx, jd_mag = jd_skill_indices(jd_skills, vocab_index)

        scores = []
        for i, r in enumerate(RESUMES):
            sparse, mag = resume_vecs[i]
            sim = cosine_similarity_sparse(sparse, mag, jd_idx, jd_mag)
            scores.append((r["name"], round(sim, 2)))

        top3 = rank_candidates(scores)
        formatted = ", ".join("{}({:.2f})".format(name, score) for name, score in top3)

        print("\n{} -- {} ({})".format(jd["id"], jd["company"], jd["role"]))
        print(formatted)

    print("\n" + sep)
    print("[OK] Matching engine completed successfully")
    print(sep)


if __name__ == "__main__":
    main()