""" Testing different gates, components (classes) and computations (functions). """

from logic_gates.circuit_examples.adder2bits import Adder2Bits
from logic_gates.nand_gate import NAND
from logic_gates.and_gate import AND
from logic_gates.nor_gates import NOR
from logic_gates.or_gate import OR
from logic_gates.xnor_gate import XNOR
from logic_gates.xor_gate import XOR


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

    def run_nor_gate_tests(self):
        """ Testing the NOR gate. """

        gate = NOR()
        print("NOR (0, 0): ", gate.compute((0, 0)))
        print("NOR (1, 0): ", gate.compute((1, 0)))
        print("NOR (0, 1): ", gate.compute((0, 1)))
        print("NOR (1, 1): ", gate.compute((1, 1)))

    def run_xor_gate_tests(self):
        """ Testing the XOR gate. """

        gate = XOR()
        print("XOR (0, 0): ", gate.compute((0, 0)))
        print("XOR (1, 0): ", gate.compute((1, 0)))
        print("XOR (0, 1): ", gate.compute((0, 1)))
        print("XOR (1, 1): ", gate.compute((1, 1)))

    def run_xnor_gate_tests(self):
        """ Testing the XNOR gate. """

        gate = XNOR()
        print("XNOR (0, 0): ", gate.compute((0, 0)))
        print("XNOR (1, 0): ", gate.compute((1, 0)))
        print("XNOR (0, 1): ", gate.compute((0, 1)))
        print("XNOR (1, 1): ", gate.compute((1, 1)))

    def run_all_gates(self):
        """ Testing all the logic gates. """

        self.run_nand_gate_tests()
        self.run_and_gate_tests()
        self.run_or_gate_tests()
        self.run_nor_gate_tests()
        self.run_xor_gate_tests()
        self.run_xnor_gate_tests()

    def run_adder2bits_tests(self):
        """ Testing the 2 bit Adder circuit. """

        adder = Adder2Bits()
        print("Adder2Bits (0, 0): ", adder.compute((0, 0)))
        print("Adder2Bits (0, 1): ", adder.compute((0, 1)))
        print("Adder2Bits (1, 0): ", adder.compute((1, 0)))
        print("Adder2Bits (1, 1): ", adder.compute((1, 1)))
