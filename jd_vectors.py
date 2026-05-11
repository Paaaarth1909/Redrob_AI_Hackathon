import math

from skill_normalizer import normalize_skills


JOB_DESCRIPTIONS = [
    {
        "id": "JD-1",
        "company": "Kakao (Seoul)",
        "role": "ML Engineer",
        "required_skills":
            "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization",
        "preferred_skills":
            "NLP, BERT, Feature Engineering, Statistics",
    },
    {"id": "JD-2", "company": "Naver (Seongnam)", "role": "Backend Engineer",
     "required_skills": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes",
     "preferred_skills": "REST API, CI/CD, Redis"},
    {"id": "JD-3", "company": "Line (Seoul)", "role": "Frontend Engineer",
     "required_skills": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS",
     "preferred_skills": "Node.js, GraphQL, Redux, Jest, AWS"}
]


def build_jd_vector(jd, vocab_index):

    combined = (
        jd["required_skills"]
        + ", "
        + jd["preferred_skills"]
    )

    normalized = normalize_skills(combined)

    indices = frozenset(
        vocab_index[skill]
        for skill in normalized
        if skill in vocab_index
    )

    magnitude = math.sqrt(len(indices))

    return indices, magnitude