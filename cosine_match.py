def cosine_similarity_sparse(
    sparse_resume,
    resume_magnitude,
    jd_indices,
    jd_magnitude,
):

    if resume_magnitude == 0 or jd_magnitude == 0:
        return 0

    dot_product = sum(
        value
        for index, value in sparse_resume.items()
        if index in jd_indices
    )

    return dot_product / (
        resume_magnitude * jd_magnitude
    )