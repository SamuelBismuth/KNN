'''
Python version: 3.9
Submitters: Yishay Seroussi 305027948, Samuel Bismuth 342533064.
'''


from data import HcBodyTemperature
from knn import Knn
import numpy as np


ITERATIONS = 100


hc_body_temperature = HcBodyTemperature('data/HC_Body_Temperature.txt')


for k in [1, 3, 5, 7, 9]:
    for p in [1, 2, np.inf]:
        train_error = 0
        test_error = 0
        for iteration in range(ITERATIONS):
            training_features, testing_features, training_labels, testing_labels = hc_body_temperature.shuffle_data()
            train = np.c_[training_features, training_labels]
            knn = Knn(k, p, train)
            test_prediction = knn.run_knn(testing_features)
            test_error += knn.compute_error(test_prediction, testing_labels)
            train_prediction = knn.run_knn(training_features)
            train_error += knn.compute_error(train_prediction, training_labels)
        print('####################################################')
        print('Train -> k: {0}, p: {1}, error: {2}'.format(k, p, train_error/ ITERATIONS))
        print('Test -> k: {0}, p: {1}, error: {2}'.format(k, p, test_error/ ITERATIONS))
        print('####################################################')