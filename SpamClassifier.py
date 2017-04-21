import numpy as np
import ReadEmails
import ProcessEmail
import EmailFeatures
import VocabList
import TrainClassifier
import random
import CheckPredictions

print("loading emails")
emails = ReadEmails.read_emails(r"Resources\lingspam_public\bare")
random.shuffle(emails)
print("read emails")

vocab_list = VocabList.get_vocab_list()
print("vocab list loaded")

features = np.zeros((len(emails), len(vocab_list)))
y = np.zeros((len(emails)))
i = 0
for email in emails:
    print(email.path)
    content = open(email.path, 'r').read()
    word_indices = ProcessEmail.process(content, vocab_list)
    features[i] = EmailFeatures.extract_features(word_indices, len(vocab_list)).transpose()
    y[i] = email.is_spam
    i += 1
print("features loaded")

# saving the features to a text file - features.txt
# to avoid doing the same work again and again for testing
# file features.txt shape(no_of_samples, 1 + no_of_features)
# first column contains is_spam -> 1(if yes) 0(if no), rest of th columns contain the features
i = 0
file = open("features.txt", 'w')
for row in features:
    file.write(str(y[i]) + " ")
    i += 1
    for num in row:
        file.write(str(num) + " ")
    file.write("\n")
print("file written")

# reading features from file into the feature vector.
print("reading features")
file = open("features.txt", 'r')
file = file.read()
i = 0
for line in file.split("\n"):
    # print(len(line))
    j = 0
    flag = True
    for word in line.split(" "):
        if flag and len(word) > 0:
            y[i] = float(word)
            flag = False
        elif len(word) > 0:
            features[i, j] = float(word)
            j += 1
    i += 1
print("features read")

training_set_size = int((4 * len(emails)) / 5)

X_train = features[0:training_set_size]
y_train = y[0:training_set_size]

# print("training classifier")
# clf = TrainClassifier.train_classifier(X_train, y_train)
# print("classifier trained")
X_test = features[training_set_size:]
y_test = y[training_set_size:]

# print(CheckPredictions.F1_Score(clf, X_test, y_test))


# code for checking values of C v/s F1 Score
# 0.02
for i in np.arange(0.01, 1, 0.01):
    clf = TrainClassifier.train_classifier(X_train, y_train, i)
    print(CheckPredictions.F1_Score(clf, X_test, y_test))

