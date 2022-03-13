from matplotlib import pyplot as plt
from wordcloud import WordCloud
from prepareText.getDataCSV import get_data_csv
from prepareText.cleanText import clean_text
from prepareText.removeStopwords import remove_stopwords
from prepareText.bagOfWords import bag_of_words

# prepare data
data = get_data_csv('dataFiles/True.csv')
data = clean_text(data)
data = remove_stopwords(data)
data_list = data.split(' ')

# bag of words
data_set = set(data_list)
data_dict = bag_of_words(data_set, data_list)

# generate word cloud
wc = WordCloud()
wc.generate_from_frequencies(data_dict)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()



