# title TestComplex
# description Unit tests for complex number class
# code
import unittest
from math import sqrt
from ComplexNumber import ComplexNumber


class TestComplexNumber(unittest.TestCase):

    complex_number = ComplexNumber(7, 6)

    def test_mod(self):
        self.assertEqual(self.complex_number.mod(),
                         sqrt(self.complex_number.real ** 2 + self.complex_number.Im ** 2))

    def test_sum(self):
        second_number = ComplexNumber(4, 3)
        sum_result = self.complex_number.sum(second_number)
        self.assertEqual(sum_result.Im, second_number.Im + self.complex_number.Im)
        self.assertEqual(sum_result.real, second_number.real + self.complex_number.real)

    def test_sub(self):
        second_number = ComplexNumber(2, 5)
        sum_result = self.complex_number.sub(second_number)
        self.assertEqual(sum_result.Im, self.complex_number.Im - second_number.Im)
        self.assertEqual(sum_result.real, self.complex_number.real - second_number.real)

    def test_mul(self):
        second_number = ComplexNumber(3, 2)
        sum_result = self.complex_number.mul(second_number)
        self.assertEqual(sum_result.Im,
                         self.complex_number.real * second_number.Im + self.complex_number.Im * second_number.real)
        self.assertEqual(sum_result.real,
                         self.complex_number.real * second_number.real - self.complex_number.Im * second_number.Im)

    def test_comparison(self):
        b = self.complex_number.copy()
        self.assertTrue(self.complex_number, b)


if __name__ == '__main__':
    unittest.main()