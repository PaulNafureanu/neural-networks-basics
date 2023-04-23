""" A XOR logic gate created from perceptrons. """

from typing import Tuple
from neurons.perceptron import Perceptron


class XOR(Perceptron):
    """ The XOR gate as an extension of the Perceptron class. """

    def __init__(self) -> None:
        """ Define a XOR gate. """

        super().__init__([-1, -1], -2)

    def compute(self, inputs: Tuple[1 | 0, 1 | 0]) -> 1 | 0:
        """ Compute the value of the XOR gate.

        Parameters:
        inputs (Tuple[1 | 0, 1 | 0]): 2 inputs, each being 0 or 1.

        Returns:
        1 if the input is (1, 0) or (0, 1), 0 otherwise.
        """
        result1 = super().compute(inputs)
        result2 = super().compute((inputs[0], result1))
        result3 = super().compute((inputs[1], result1))

        return super().compute((result2, result3))
