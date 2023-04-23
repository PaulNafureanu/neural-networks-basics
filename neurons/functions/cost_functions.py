""" A set of cost functions and their derivatives useful in defining various gradient descent / backpropagation algorithms. """

import numpy as np


class CostFunctions:
    """ Define functions used in gradient descent / backpropagation algorithms. """

    def quadratic_cost(self, length: int, network_outputs, desired_outputs):
        """ Define the quadratic cost function. 

        Parameters:
        length (int): the total length of training inputs.
        network_outputs: A list of vectors where each vector is the actual output vector from the network for each input.
        desired_outputs: A list of vectors where each vector is the desired output vector for the network for each input.
        """

        error_sum: int = 0
        for index in range(length):
            error_sum += (np.abs(desired_outputs[index] -
                          network_outputs[index])**2)

        return (1.0 / (2.0 * length)) * error_sum

    def quadratic_cost_derivative(self):
        """ Define the first derivative of the quadratic cost function (quadratic cost prime). """
