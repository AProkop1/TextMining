from nltk.stem import PorterStemmer


def stem_words(input: str) -> list:
    porter = PorterStemmer()
    input_list = list(input.split(" "))
    output_list = [porter.stem(word) for word in input_list]
    return output_list
