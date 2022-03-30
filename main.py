from sklearn.feature_extraction.text import CountVectorizer
from textOperations.textTokenizer import text_tokenizer
from prepareText.getDataCSV import get_data_csv

data = get_data_csv('dataFiles/True.csv', 'title')
data = [data]

# Liczebnościowa
vectorizer = CountVectorizer(tokenizer=text_tokenizer)
X_transform = vectorizer.fit_transform(data)
print(vectorizer.get_feature_names_out())
print(X_transform.toarray())
