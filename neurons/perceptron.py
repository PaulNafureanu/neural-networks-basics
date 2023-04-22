""" Perceptron Neuron - the first basic artificial neuron. """

from typing import List


class Perceptron:
    """
    The Perceptron Class.

    It is used for basic manipulations of binary input data using a weight list and a threshold value.
    """

    def __init__(self, weights: List[float], threshold: float) -> None:
        """
        Define the perceptron.

        Please make sure that the size of the weight list will be the same as the size of the input list.
        """
        self.weights = weights
        self.threshold = threshold
        self.input_size = len(weights)

    def compute(self, inputs: List[1 | 0]) -> 1 | 0:
        """ Compute the value of the perceptron. 

        Parameters:
        inputs (List[1 | 0]): the inputs of our neuron in binary.
        The size of the input list should be the same as the size of the weight list.

        Returns:
        0 if the sum of the products of weights and inputs is less than or equal with the threshold,
        1 otherwise.
        """
        sum_result: float = 0
        for index in range(self.input_size):
            sum_result += self.weights[index]*inputs[index]
        return 0 if sum_result <= self.threshold else 1
