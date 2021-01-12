from sklearn.model_selection import train_test_split
import numpy as np


class HcBodyTemperature:


    def __init__(self, file):
        self.data = np.loadtxt(file)
        self.data[:, [2, 1]] = self.data[:, [1, 2]]
        gender = self.data[:, 2]
        gender[gender == 2] = -1
        self.data[:, 2] = gender
        

    def shuffle_data(self):
        train = self.data[:, [0, 1]]
        test = self.data[:, 2]
        return train_test_split(train, test, test_size=0.5)