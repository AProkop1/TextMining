from nltk.stem import PorterStemmer


def stem_words(input: str) -> list:
    porter = PorterStemmer()
    input_list = list(input.split(" "))
    output_list = []
    for word in input_list:
        output_list.append(porter.stem(word))
    return output_list
