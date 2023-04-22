""" The main entry point of the application. """

from logic_gates.circuit_examples.adder2bits import Adder2Bits
from logic_gates.nand import NAND

gate = NAND()
print(gate.compute((0, 0)))
print(gate.compute((1, 0)))
print(gate.compute((0, 1)))
print(gate.compute((1, 1)))

adder = Adder2Bits()
print(adder.compute((0, 0)))
print(adder.compute((0, 1)))
print(adder.compute((1, 0)))
print(adder.compute((1, 1)))
