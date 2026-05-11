def print_vocabulary(vocabulary):

    print("\nVocabulary:\n")

    for index, skill in enumerate(vocabulary):

        print(index, skill)


def print_idf(idf):

    print("\nIDF Values:\n")

    for skill, value in idf.items():

        print(skill, round(value, 4))