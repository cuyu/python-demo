#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implement a simple neural network which has two inputs and one hidden layer with two nodes and two outputs.
We use logistic function as the activation function for each hidden node.
Refer to: https://mattmazur.com/2015/03/17/a-step-by-step-backpropagation-example/
"""
import math
import numpy as np


def sigmoid(x):
    """
    logistic sigmoid function
    """
    return 1 / (1 + math.exp(-x))


def variance_loss(y, y_hat):
    loss = 0
    for i in range(len(y)):
        loss += pow(y[i] - y_hat[i], 2)

    loss = loss / len(y)
    return loss


def single_hidden_layer(X, y, node_number=2, learning_rate=0.05, steps=1000):
    # Append a const 1 to X so that we do not calculate the const b individually
    X = np.append(X, [1])
    # # # The Forward Pass # # #
    # Init Wi, Bi with zeros
    Wi = np.zeros([node_number, len(X)])
    Wo = np.zeros([len(y), node_number])
    for s in range(steps):
        hidden_out = []
        for i in range(node_number):
            input_i = sum(X * Wi[i])
            hidden_out.append(sigmoid(input_i))
        hidden_out = np.float32(hidden_out)

        # Init Wo, Bo with zeros, the output node number equals to y
        y_hat = []
        for i in range(len(y)):
            o = sum(hidden_out * Wo[i])
            y_hat.append(sigmoid(o))
        y_hat = np.float32(y_hat)
        print('y_hat:', y_hat)

        loss = variance_loss(y, y_hat)

        # # # The Backwards Pass # # #
        # Calculate the loss gradient for each w in output layer
        d_Wi = np.zeros([node_number, len(X)])
        d_Wo = np.zeros([len(y), node_number])
        for i in range(len(y)):
            # loss对y_hat[i]求偏导
            d_total_output_i = y_hat[i] - y[i]
            # As we use a liner function (y=x) as the activation function for output layer, the derivative is const 1
            d_output_hidden_i = y_hat[i] * (1 - y_hat[i])
            for j in range(node_number):
                d_net_Wo_j = hidden_out[j]
                d_Wo[i][j] = d_total_output_i * d_output_hidden_i * d_net_Wo_j

        # Calculate the loss gradient for each w in hidden layer
        for i in range(node_number):
            # total_error对hidden_out_i求偏导等于total_error_i对hidden_out_i偏导之和
            d_total_hidden_i = 0
            for w in Wo:
                d_total_hidden_i += w[i]
            # The partial derivative of the logistic function is the output multiplied by 1 minus the output
            d_hidden_net_i = hidden_out[i] * (1 - hidden_out[i])
            for j in range(len(X)):
                d_net_wi_j = X[j]
                d_Wi[i][j] = d_total_hidden_i * d_hidden_net_i * d_net_wi_j

        # Adjust each weight using the calculated gradient
        for i in range(len(y)):
            for j in range(node_number):
                Wo[i][j] -= learning_rate * d_Wo[i][j]
        for i in range(node_number):
            for j in range(len(X)):
                Wi[i][j] -= learning_rate * d_Wi[i][j]

    return loss

if __name__ == '__main__':
    X = np.float32([0.05, 0.1])
    y = np.float32([0.01, 0.99])
    loss = single_hidden_layer(X, y, node_number=2, learning_rate=0.5, steps=10000)
    print(loss)
