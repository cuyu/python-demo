#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Implement a simple linear binary classier f = a * x + b * y + c
# Refer to http://karpathy.github.io/neuralnets/
#
# vector -> label
# ---------------
# [1.2, 0.7] -> +1
# [-0.3, 0.5] -> -1
# [-3, -1] -> +1
# [0.1, 1.0] -> -1
# [3.0, 1.1] -> -1
# [2.1, -3] -> +1


class LinearClassier(object):
    def __init__(self):
        self.a = 1.0
        self.b = 1.0
        self.c = 1.0

    def train_v1(self, data_set, learning_rate=0.01, steps=100):
        """
        :param data_set: a list of tuple, the first of the tuple is the feature vector, the second is the label
        :param learning_rate: the learning rate
        :param steps: how many rounds for training
        """
        for _ in range(steps):
            for feature, label in data_set:
                if self.predict(feature) * label < 0:
                    if label < 0:
                        self.a -= learning_rate * feature[0]
                        self.b -= learning_rate * feature[1]
                        self.c -= learning_rate * 1
                    else:
                        self.a += learning_rate * feature[0]
                        self.b += learning_rate * feature[1]
                        self.c += learning_rate * 1

    def train_v2(self, data_set, learning_rate=0.01, steps=100):
        """
        Comparing to v1, we will make the predict value more distinguished
        """
        for _ in range(steps):
            for feature, label in data_set:
                if self.predict(feature) * label < 0 or abs(self.predict(feature)) < 1:
                    if label < 0:
                        self.a -= learning_rate * feature[0]
                        self.b -= learning_rate * feature[1]
                        self.c -= learning_rate * 1
                    else:
                        self.a += learning_rate * feature[0]
                        self.b += learning_rate * feature[1]
                        self.c += learning_rate * 1

    def train_v3(self, data_set, learning_rate=0.01, steps=100):
        """
        Comparing to v2, we will add regularization pull for parameters, make it not too sensitive to some feature point
        """
        for _ in range(steps):
            for feature, label in data_set:
                if self.predict(feature) * label < 0 or abs(self.predict(feature)) < 1:
                    if label < 0:
                        a_grad = -feature[0]
                        b_grad = -feature[1]
                        c_grad = -1
                    else:
                        a_grad = feature[0]
                        b_grad = feature[1]
                        c_grad = 1
                else:
                    a_grad = 0
                    b_grad = 0
                    c_grad = 0
                # Make a, b towards 0
                a_grad -= self.a
                b_grad -= self.b
                self.a += learning_rate * a_grad
                self.b += learning_rate * b_grad
                self.c += learning_rate * c_grad

    def predict(self, feature):
        """
        :param feature: a 2 dimension vector(list)
        :return: confident value
        """
        return self.a * feature[0] + self.b * feature[1] + self.c


if __name__ == '__main__':
    data_set = [
        ([1.2, 0.7], 1),
        ([-0.3, -0.5], -1),
        ([3.0, 0.1], 1),
        ([-0.1, -1.0], -1),
        ([-1.0, 1.1], -1),
        ([2.1, -3.0], 1),
    ]
    classifier = LinearClassier()
    classifier.train_v1(data_set)
    for feature, _ in data_set:
        print(classifier.predict(feature))
    print(classifier.a, classifier.b, classifier.c)
    print('---')
    classifier = LinearClassier()
    classifier.train_v2(data_set)
    for feature, _ in data_set:
        print(classifier.predict(feature))
    print(classifier.a, classifier.b, classifier.c)
    print('---')
    classifier = LinearClassier()
    classifier.train_v3(data_set)
    for feature, _ in data_set:
        print(classifier.predict(feature))
    print(classifier.a, classifier.b, classifier.c)

