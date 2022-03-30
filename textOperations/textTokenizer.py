from prepareText.cleanText import clean_text
from prepareText.removeStopwords import remove_stopwords
from prepareText.stemWords import stem_words


def text_tokenizer(data: str) -> list:
    clean_data = clean_text(data)
    stem_data = stem_words(clean_data)
    without_stopwords = remove_stopwords(stem_data)
    final_list = [word for word in without_stopwords if len(word) > 3]
    return final_list
