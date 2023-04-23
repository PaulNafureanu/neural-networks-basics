""" A XNOR logic gate created from perceptrons. """

from typing import Tuple
from neurons.perceptron import Perceptron


class XNOR(Perceptron):
    """ The XNOR gate as an extension of the Perceptron class. """

    def __init__(self) -> None:
        """ Define a XNOR gate. """

        super().__init__([-1, -1], -2)

    def compute(self, inputs: Tuple[1 | 0, 1 | 0]) -> 1 | 0:
        """ Compute the value of the XNOR gate.

        Parameters:
        inputs (Tuple[1 | 0, 1 | 0]): 2 inputs, each being 0 or 1.

        Returns:
        1 if the input is (1, 1) or (0, 0), 0 otherwise.
        """
        result1 = super().compute(inputs)
        result2 = super().compute((inputs[0], result1))
        result3 = super().compute((inputs[1], result1))
        result4 = super().compute((result2, result3))

        return super().compute((result4, result4))
