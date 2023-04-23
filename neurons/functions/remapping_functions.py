""" A set of remapping functions and their derivatives useful in defining various neurons. """

import numpy as np


class Remapping:
    """ Define functions used in artificial neurons. """

    def logistic(self, inputs):
        """ Define the logistic function. """

        return 1.0 / (1.0 + np.exp(-inputs))

    def logistic_derivative(self, inputs):
        """ Define the first derivative of the logistic function (logistic prime). """

        return self.logistic(inputs) * (1.0 - self.logistic(inputs))
