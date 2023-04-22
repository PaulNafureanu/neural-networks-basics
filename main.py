""" The main entry point of the application. """

from neurons.perceptron import Perceptron

p1 = Perceptron([3, 3, 4], 5)
print(p1.compute([1, 1, 0]))
