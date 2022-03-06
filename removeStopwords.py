import nltk
from nltk.corpus import stopwords


def remove_stopwords(input: str):
    eng_stopwords = set(stopwords.words('english'))
    input_list = list(input.split(" "))
    input_without_stopwords = [word.lower() for word in input_list if not word in eng_stopwords]
    return ' '.join([str(word) for word in input_without_stopwords])

