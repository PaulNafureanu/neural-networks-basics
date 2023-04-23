""" A 2 bit Adder class made of NAND gates. """

from typing import Tuple
from logic_gates.nand_gate import NAND


class Adder2Bits:
    """ Define a 2 bit Adder """

    def compute(self, inputs: Tuple[1 | 0, 1 | 0]) -> Tuple[1 | 0, 1 | 0]:
        """ Computing the sum of two bits. 

        Parameters:
        inputs (Tuple[1 | 0, 1 | 0]): two bits input.

        Returns:
        (sum_bit, carry_bit): a tuple of the form (Tuple[1 | 0, 1 | 0]).
        """
        nand_gate = NAND()

        result1 = nand_gate.compute(inputs)
        result2 = nand_gate.compute((inputs[0], result1))
        result3 = nand_gate.compute((inputs[1], result1))

        sum_bit = nand_gate.compute((result2, result3))
        carry_bit = nand_gate.compute((result1, result1))

        return (sum_bit, carry_bit)
