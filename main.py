from process_resumes import process_resumes
from tfidf_resumes import (
    build_vocabulary,
    compute_idf,
    generate_tfidf_vector,
)
from jd_vectors import (
    JOB_DESCRIPTIONS,
    build_jd_vector,
)
from cosine_match import cosine_similarity_sparse
from sanity_checks import (
    print_vocabulary,
    print_idf,
)


def rank_candidates(scores):

    return sorted(
        scores,
        key=lambda x: (-x[1], x[0])
    )[:3]


def main():

    print("\nResume Matching Engine\n")

    resumes = process_resumes()

    all_skills = [
        resume["normalized_skills"]
        for resume in resumes
    ]

    vocabulary, vocab_index = build_vocabulary(all_skills)

    df, idf = compute_idf(all_skills, vocabulary)

    print_vocabulary(vocabulary)

    print_idf(idf)

    tfidf_vectors = []

    for resume in resumes:

        vector = generate_tfidf_vector(
            resume["normalized_skills"],
            vocab_index,
            idf,
        )

        tfidf_vectors.append(vector)

    for jd in JOB_DESCRIPTIONS:

        jd_indices, jd_magnitude = build_jd_vector(
            jd,
            vocab_index,
        )

        scores = []

        for index, resume in enumerate(resumes):

            sparse_vector, magnitude = tfidf_vectors[index]

            similarity = cosine_similarity_sparse(
                sparse_vector,
                magnitude,
                jd_indices,
                jd_magnitude,
            )

            scores.append((
                resume["name"],
                round(similarity, 2),
            ))

        top_candidates = rank_candidates(scores)

        print(f"\n{jd['id']} -- {jd['company']} ({jd['role']})")

        print(
            ", ".join(
                f"{name}({score:.2f})"
                for name, score in top_candidates
            )
        )


if __name__ == "__main__":
    main()