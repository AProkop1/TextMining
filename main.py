from cleanText import clean_text
from removeStopwords import remove_stopwords


input1 = 'Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku. Lorem ipsum dolor sit amet, consectetur; adipiscing elit.' \
        'Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In' \
        'eu risus.or :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) ' \
        'Mauris ;( egestas erat quam, :-< ut <p>'

input2 = 'This is a day in a year when we all'

print(clean_text(input1))
print(remove_stopwords(input2))

