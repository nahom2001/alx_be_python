from simple_calculator import SimpleCalculator    
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        result = self.calc.add(self, -2, 1)
        self.assertEqual(result, -1)

    def test_subtraction(self):
        result = self.calc.subtract(self, -2, 1)
        self.assertEqual(result, -3)

    def test_multiply(self):
        result = self.calc.multiply(self, -2, -1)
        self.assertEqual(result, 2)

    def test_divide(self):
        result = self.calc.divide(self, 5, 2)
        self.assertEqual(result, 2.5)
