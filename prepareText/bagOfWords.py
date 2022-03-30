def bag_of_words(data_set: set, data_list: list) -> dict:
    j = 0
    data_dict = {}
    for word in data_set:
        for i in data_list:
            if word == i:
                j += 1
        data_dict[word] = j
    return data_dict
