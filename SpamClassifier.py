import numpy as np
import ReadFile
import ProcessEmail
import EmailFeatures
import VocabList
import TrainClassifier

print("loading emails")
emails = ReadFile.read_files(r"Resources\lingspam_public\bare\part1")
print("read emails")

vocab_list = VocabList.get_vocab_list()
print("vocab list loaded")

features = np.zeros((len(emails), len(vocab_list)))
i = 0
for email in emails:
    # print(email)
    content = open(email, 'r').read()
    word_indices = ProcessEmail.process(content, vocab_list)
    features[i] = EmailFeatures.extract_features(word_indices, len(vocab_list)).transpose()
    i += 1
print("features loaded")

# saving the features to a text file - features.txt
# to avoid doing the same work again and again for testing
file = open("features.txt", 'w')
for row in features:
    for num in row:
        file.write(str(num) + " ")
    file.write("\n")


# training_set_size = int((4 * len(emails)) / 5)
