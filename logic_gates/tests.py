""" Testing different gates, components (classes) and computations (functions). """

from logic_gates.circuit_examples.adder2bits import Adder2Bits
from logic_gates.nand_gate import NAND
from logic_gates.and_gate import AND
from logic_gates.or_gate import OR


class PrintLogicGatesTests:
    """ Test and print different logic gates and circuits. """

    def run_nand_gate_tests(self):
        """ Testing the NAND gate. """

        gate = NAND()
        print("NAND (0, 0): ", gate.compute((0, 0)))
        print("NAND (1, 0): ", gate.compute((1, 0)))
        print("NAND (0, 1): ", gate.compute((0, 1)))
        print("NAND (1, 1): ", gate.compute((1, 1)))

    def run_and_gate_tests(self):
        """ Testing the AND gate. """

        gate = AND()
        print("AND (0, 0): ", gate.compute((0, 0)))
        print("AND (1, 0): ", gate.compute((1, 0)))
        print("AND (0, 1): ", gate.compute((0, 1)))
        print("AND (1, 1): ", gate.compute((1, 1)))

    def run_or_gate_tests(self):
        """ Testing the OR gate. """

        gate = OR()
        print("OR (0, 0): ", gate.compute((0, 0)))
        print("OR (1, 0): ", gate.compute((1, 0)))
        print("OR (0, 1): ", gate.compute((0, 1)))
        print("OR (1, 1): ", gate.compute((1, 1)))

    def run_adder2bits_tests(self):
        """ Testing the 2 bit Adder circuit. """

        adder = Adder2Bits()
        print("Adder2Bits (0, 0): ", adder.compute((0, 0)))
        print("Adder2Bits (0, 1): ", adder.compute((0, 1)))
        print("Adder2Bits (1, 0): ", adder.compute((1, 0)))
        print("Adder2Bits (1, 1): ", adder.compute((1, 1)))

    def run_all(self):
        """ Testing all the logic gates and circuits. """

        self.run_nand_gate_tests()
        self.run_and_gate_tests()
        self.run_or_gate_tests()
        self.run_adder2bits_tests()
