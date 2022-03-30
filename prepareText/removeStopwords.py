import nltk
from nltk.corpus import stopwords


def remove_stopwords(input: list) -> list:
    eng_stopwords = set(stopwords.words('english'))
    input_without_stopwords = [word.lower() for word in input if word not in eng_stopwords]
    return input_without_stopwords
