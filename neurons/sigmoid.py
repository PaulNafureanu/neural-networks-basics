""" Sigmoid Neuron - a modern artificial neuron. """

from typing import List, Callable


class Sigmoid:
    """
    The Sigmoid Class.

    It is used for manipulations of data inputs using a weight list and a bias value.
    """

    def __init__(self, weights: List[float], bias: float) -> None:
        """
        Define the sigmoid.

        Please make sure that the size of the weight list will be the same as the size of the input list.
        """
        self.weights = weights
        self.bias = bias
        self.input_size = len(weights)

    def compute(self, inputs: List[float], remapper: Callable) -> float:
        """ Compute the value of the sigmoid. 

        Parameters:
        inputs (List[float]): the inputs of our neuron is a number between 0 and 1 inclusive.
        The size of the input list should be the same as the size of the weight list.
        remapper (Callable): a remapping function used to resize the sigmoid's output.

        Returns: A floating number depending on which remapping function is being used.
        """

        output: float = 0
        for index in range(self.input_size):
            output += (self.weights[index]*inputs[index] + self.bias)

        return remapper(output)
