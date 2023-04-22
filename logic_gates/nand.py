""" A NAND logic gate created from perceptrons. """

from typing import Tuple
from neurons.perceptron import Perceptron


class NAND(Perceptron):
    """ The NAND gate as an extension of the Perceptron class. """

    def __init__(self) -> None:
        """ Define a NAND gate. """
        super().__init__([-2, -2], -3)

    def compute(self, inputs: Tuple[1 | 0, 1 | 0]) -> 1 | 0:
        """ Compute the value of the NAND gate.

        Parameters:
        inputs (Tuple[1 | 0, 1 | 0]): 2 inputs, each being 0 or 1.

        Returns:
        0 if the input is (1, 1), 1 otherwise.
        """
        return super().compute(inputs)
