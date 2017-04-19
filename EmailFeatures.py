import numpy as np


def extract_features(word_indices, vocab_list_len):
    """
    :param word_indices: indices of words in an email
    :param vocab_list_len: length of vocab list
    :return:
    """
    features = np.zeros((vocab_list_len, 1), dtype=int)
    for index in word_indices:
        features[index, 0] = 1
    return features

print(extract_features([1, 4, 6], 8))
