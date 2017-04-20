from sklearn.svm import SVC
import numpy as np


def train_classifier(X, y):
    clf = SVC()
    clf.fit(X, y)
    return clf

# clf = train_classifier(np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]]), np.array([1, 1, 2, 2]))
# print(clf.predict([[2, 2], [-1, -2]]))
