import math


def build_vocabulary(all_resume_skills):

    vocabulary = sorted({
        skill
        for skills in all_resume_skills
        for skill in skills
    })

    vocab_index = {
        skill: index
        for index, skill in enumerate(vocabulary)
    }

    return vocabulary, vocab_index


def compute_idf(all_resume_skills, vocabulary):

    total_resumes = len(all_resume_skills)

    df = dict.fromkeys(vocabulary, 0)

    for skills in all_resume_skills:

        for skill in set(skills):

            if skill in df:
                df[skill] += 1

    idf = {
        skill: math.log(total_resumes / count)
        for skill, count in df.items()
    }

    return df, idf


def generate_tfidf_vector(skills, vocab_index, idf):

    tf = 1 / len(skills)

    sparse_vector = {}

    magnitude_square = 0

    for skill in skills:

        index = vocab_index[skill]

        value = tf * idf[skill]

        sparse_vector[index] = value

        magnitude_square += value * value

    return sparse_vector, math.sqrt(magnitude_square)