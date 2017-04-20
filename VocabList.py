def get_vocab_list():
    """
    Used the Vocabulary list form the Stanford's Coursera ML course assignment
    :return: list of words with indexes loaded from vocab.txt
    """
    f = open(r"Resources/vocab.txt")
    vocab_list = {}
    for line in f.read().split('\n'):
        if len(line) != 0:
            temp = line.split("\t")
            vocab_list[temp[1]] = int(temp[0]) - 1
    return vocab_list
