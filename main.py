from dataOperations.getData import get_data, split_dataset
from dataOperations.cleanData import clean_data
from dataOperations.wordCloud import generate_cloud
from Classifiers.Models import trained_model, accurcy, compare_predictions

# get sample data
data = get_data('data/alexa_reviews.csv')

# prepare data
cleaned_data = clean_data(data)

# # split dataset
dataset_split = split_dataset(cleaned_data['verified_reviews'], cleaned_data["rating"])



# 4 -chmura słów
generate_cloud(cleaned_data['verified_reviews'])



# 5 - przewidywanie oceny
# train model
classifiers = ["LinearSVC", "DecisionTreeClassifier", "AdaBoost"]
for classifier in classifiers:
    model = trained_model(dataset_split['X_train'], dataset_split["Y_train"], classifier)
    accurcy(model, dataset_split['X_test'], dataset_split["Y_test"])


reviews = ["Echo sounds so good!",
           "I love this product"]

compare_predictions(reviews, classifiers, cleaned_data)
