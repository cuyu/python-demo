#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Another way to implement a simple neural network, using modular.
"""
import math


class Unit(object):
    def __init__(self, value, gradient=None):
        self.value = value
        self.gradient = gradient


class Gate(object):
    def __init__(self):
        self.utop = None

    def _set_utop_gradient(self):
        """
        Should only called by backward function
        Set the utop gradient to 1.0 if it is the start of backward chain
        """
        if self.utop and self.utop.gradient is None:
            self.utop.gradient = 1.0

    @property
    def value(self):
        return self.utop.value

    @value.setter
    def value(self, new_value):
        self.utop.value = new_value

    @property
    def gradient(self):
        return self.utop.gradient

    @gradient.setter
    def gradient(self, new_value):
        self.utop.gradient = new_value


class AddGate(Gate):
    def __init__(self):
        super(AddGate, self).__init__()
        self.u0 = None
        self.u1 = None

    def forward(self, u0, u1):
        """
        :param u0: <Unit> instance
        :param u1: <Unit> instance

        u0 --- [      ]
               [ Gate ] --- utop
        u1 --- [      ]
        """
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(self.u0.value + self.u1.value)
        return self.utop

    def backward(self):
        self._set_utop_gradient()
        self.u0.gradient = 1 * self.utop.gradient
        self.u1.gradient = 1 * self.utop.gradient


class MultiplyGate(Gate):
    def __init__(self):
        super(MultiplyGate, self).__init__()
        self.u0 = None
        self.u1 = None

    def forward(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(self.u0.value * self.u1.value)
        return self.utop

    def backward(self):
        """
        Use the chain rule, assume f as the final output:
        d(f)/d(u0) = d(f)/d(utop) * d(utop)/d(u0)
                   = utop.gradient * u1.value
        """
        self._set_utop_gradient()
        self.u0.gradient = self.u1.value * self.utop.gradient
        self.u1.gradient = self.u0.value * self.utop.gradient


class SigmoidGate(Gate):
    def __init__(self):
        super(SigmoidGate, self).__init__()
        self.u0 = None

    def forward(self, u0):
        self.u0 = u0
        self.utop = Unit(1 / (1 + math.exp(-self.u0.value)))
        return self.utop

    def backward(self):
        self._set_utop_gradient()
        self.u0.gradient = self.u0.value * (1 - self.u0.value) * self.utop.gradient


class ReLUGate(Gate):
    def __init__(self):
        super(ReLUGate, self).__init__()
        self.u0 = None

    def forward(self, u0):
        self.u0 = u0
        self.utop = Unit(max(0, self.u0.value))
        return self.utop

    def backward(self):
        """
        Here, we define the derivative at x=0 to 0
        Refer to https://www.quora.com/How-do-we-compute-the-gradient-of-a-ReLU-for-backpropagation
        """
        self._set_utop_gradient()
        if self.u0.value > 0:
            self.u0.gradient = 1 * self.utop.gradient
        else:
            self.u0.gradient = 0 * self.utop.gradient


class LinearNetwork(Gate):
    """
    A LinearNetwork: it takes 5 Units (x,y,a,b,c) and outputs a single Unit:
        f(x, y) = a * x + b * y + c
    So we need two MultiplyGate and two AddGate here

    From outside of the network, we can assume the whole network as a gate, which has 5 inputs and 1 output
    So we inherit the <Gate> class here
    """

    def __init__(self):
        super(LinearNetwork, self).__init__()
        self.a = Unit(1.0)
        self.b = Unit(1.0)
        self.c = Unit(1.0)
        self.multi_gate0 = MultiplyGate()
        self.multi_gate1 = MultiplyGate()
        self.add_gate0 = AddGate()
        self.add_gate1 = AddGate()

    def forward(self, x, y):
        self.multi_gate0.forward(self.a, x)
        self.multi_gate1.forward(self.b, y)
        self.add_gate0.forward(self.multi_gate0, self.multi_gate1)
        self.utop = self.add_gate1.forward(self.add_gate0, self.c)
        return self.utop

    def backward(self):
        self._set_utop_gradient()
        self.add_gate1.backward()
        self.add_gate0.backward()
        self.multi_gate1.backward()
        self.multi_gate0.backward()


class LinearClassifier(object):
    def __init__(self):
        self.network = LinearNetwork()

    def train(self, data_set, learning_rate=0.01, steps=100):
        """
        :param data_set: a list of tuple, the first of the tuple is the feature vector, the second is the label
        :param learning_rate: the learning rate
        :param steps: how many rounds for training
        """
        for _ in range(steps):
            for feature, label in data_set:
                utop = self.network.forward(*[Unit(k) for k in feature])
                if label > 0 and utop.value < 1:
                    pull = 1
                elif label < 0 and utop.value > -1:
                    pull = -1
                else:
                    pull = 0
                # Set the gradient of final unit and then backward to get the direction (gradient) of corresponding parameters
                # We can also set the pull (i.e. gradient) more/less than 1 to make the adjust more efficient
                self.network.gradient = pull
                self.network.backward()
                self.network.a.value += learning_rate * self.network.a.gradient
                self.network.b.value += learning_rate * self.network.b.gradient
                self.network.c.value += learning_rate * self.network.c.gradient

    def predict(self, x, y):
        return self.network.forward(Unit(x), Unit(y)).value


class SingleNeuralNetwork(Gate):
    """
    SingleNeuralNetwork, a.k.a. a Neuro of NeuralNetwork
    The formula is:
        f(x, y) = max(0, a * x + b * y + c)
    We can just think as it put the output of a <LinearNetwork> into a <ReLU> Gate
    """

    def __init__(self):
        super(SingleNeuralNetwork, self).__init__()
        self.linear_network = LinearNetwork()
        self.relu_gate = ReLUGate()
        self.a = self.linear_network.a
        self.b = self.linear_network.b
        self.c = self.linear_network.c

    def forward(self, x, y):
        self.linear_network.forward(x, y)
        self.utop = self.relu_gate.forward(self.linear_network)
        return self.utop

    def backward(self):
        self._set_utop_gradient()
        self.relu_gate.backward()
        self.linear_network.backward()


class NeuralNetwork(Gate):
    """
    A neural network consist of two <SingleNeuralNetwork>
    The formula is:
        f(x, y) = a1 * n1 + a2 * n2 + d
    where n1, n2 is the output of <SingleNeuralNetwork>, just as simple as apply the LinearNetwork to the <SingleNeuralNetwork>
    """

    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.neuro0 = SingleNeuralNetwork()
        self.neuro1 = SingleNeuralNetwork()
        self.linear_network = LinearNetwork()

    def forward(self, x, y):
        self.neuro0.forward(x, y)
        self.neuro1.forward(x, y)
        self.utop = self.linear_network.forward(self.neuro0, self.neuro1)
        return self.utop

    def backward(self):
        self._set_utop_gradient()
        self.linear_network.backward()
        self.neuro0.backward()
        self.neuro1.backward()


if __name__ == '__main__':
    data_set = [
        ([1.2, 0.7], 1),
        ([-0.3, -0.5], -1),
        ([3.0, 0.1], 1),
        ([-0.1, -1.0], -1),
        ([-1.0, 1.1], -1),
        ([2.1, -3.0], 1),
    ]
    classifier = LinearClassifier()
    classifier.train(data_set)
    for feature, _ in data_set:
        print(classifier.predict(*feature))
