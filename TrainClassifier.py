from sklearn.svm import SVC
import numpy as np


def train_classifier(X, y, C):
    """
    :param X: features, shape (n_samples, n_features)
    :param y: shape (n_samples,)
    :return:
    """
    clf = SVC(C=C, kernel='linear', class_weight='balanced')
    clf.fit(X, y)
    return clf

# clf = train_classifier(np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]]), np.array([1, 1, 2, 2]))
# print(clf.predict([[2, 2], [-1, -2]]))
