#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import RidgeCV
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# x1 * x2 + a = y1
a = 2
x1 = np.float32(range(5, 100, 2))
x2 = np.float32(range(15, 110, 2))
y = x1 * x2 + 2

test_x1 = np.float32(range(111, 180, 3))
test_x2 = np.float32(range(121, 190, 3))
test_y = test_x1 * test_x2 + 2

# Use separate values as input for training
model = SVR(kernel='linear')
model.fit(np.float32(zip(x1, x2)), y)
pred_y = model.predict(np.float32(zip(test_x1, test_x2)))
r2 = r2_score(test_y, pred_y)
print r2

# Use the multiply result as input for training
model2 = SVR(kernel='rbf')
x3 = x1 * x2
model2.fit(x3.reshape(-1, 1), y)
test_x3 = test_x1 * test_x2
pred_y2 = model2.predict(test_x3.reshape(-1, 1))
r2_2 = r2_score(test_y, pred_y2)
print r2_2

# plt.scatter(test_x3, test_y, color='darkorange', label='data')
# plt.plot(test_x3, pred_y2, color='navy', lw=2, label='RBF model')
# plt.show()


# x1 + b * x2 + c = y1 + y2
b = 2
c = 3
