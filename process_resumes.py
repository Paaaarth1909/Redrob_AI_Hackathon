from skill_normalizer import normalize_skills


RESUMES = [
    {
        "id": "01",
        "name": "Arjun Sharma",
        "skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning",
    },
    {
        "id": "02",
        "name": "Priya Nair",
        "skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS",
    },
    {
        "id": "03",
        "name": "Rahul Gupta",
        "skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates",
    },
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
     "background": "Data Science Intern . Wipro 2024"}
]


def process_resumes():

    normalized_resumes = []

    for resume in RESUMES:

        normalized = normalize_skills(resume["skills"])

        resume["normalized_skills"] = normalized

        normalized_resumes.append(resume)

    return normalized_resumes