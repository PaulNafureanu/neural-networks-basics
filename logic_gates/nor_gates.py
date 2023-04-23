""" A NOR logic gate created from perceptrons. """

from typing import Tuple
from neurons.perceptron import Perceptron


class NOR(Perceptron):
    """ The NOR gate as an extension of the Perceptron class. """

    def __init__(self) -> None:
        """ Define a NOR gate. """
        super().__init__([-1, -1], -1)

    def compute(self, inputs: Tuple[1 | 0, 1 | 0]) -> 1 | 0:
        """ Compute the value of the NOR gate.

        Parameters:
        inputs (Tuple[1 | 0, 1 | 0]): 2 inputs, each being 0 or 1.

        Returns:
        1 if the input is (0, 0), 0 otherwise.
        """
        return super().compute(inputs)
