import operator
from numpy import linalg as LA
import numpy as np


class Knn:


    def __init__(self, k, p, data):
        self.k = k
        self.p = p
        self.data = data


    def run_knn(self, train):
        labelling = []
        for point in train:
            maj = 0
            distances = []
            for i in range(self.data.shape[0]):
                distances.append(
                    (LA.norm((self.data[i, 0]-point[0], 
                            self.data[i, 1]-point[1]), self.p),
                    self.data[i, 2]))
            distances.sort(key=operator.itemgetter(0),reverse=False)
            knn_distances = distances[0:self.k]
            maj = sum(v for k, v in knn_distances)
            label = 1 if maj >= 0 else -1
            labelling.append(label)
        return labelling
        

    def compute_error(self, predicts, data):
        return 1 - np.sum(data == predicts) / len(data)
       