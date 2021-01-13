import operator
from numpy import linalg as LA
import numpy as np


class Knn:


    def __init__(self, k, p, train):
        self.k = k
        self.p = p
        self.train = train


    def run_knn(self, test):
        labels = []
        for point in test:
            maj = 0
            distances = []
            for i in range(self.train.shape[0]):
                distances.append(
                    (LA.norm((self.train[i, 0]-point[0], 
                            self.train[i, 1]-point[1]), self.p),
                    self.train[i, 2]))
            distances.sort(key=operator.itemgetter(0),reverse=False)
            knn_distances = distances[0:self.k]
            maj = sum(label for dist,label in knn_distances)
            label = 1 if maj >= 0 else -1
            labels.append(label)
        return labels
        

    def compute_error(self, predicts, data):
        return 1 - np.sum(data == predicts) / len(data)
       