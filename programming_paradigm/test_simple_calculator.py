from simple_calculator import SimpleCalculator    
import unittest


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()
    def test_add(self):
        result = self.calculator.add(self, -2, 1)
        self.assertEqual(result, -1)

    def test_subtract(self):
        result = self.calculator.subtract(self, -2, 1)
        self.assertEqual(result, -3)

    def test_multiply(self):
        result = self.calculator.multiply(self, -2, -1)
        self.assertEqual(result, 2)

    def test_divide(self):
        result = self.calculator.divide(self, 5, 2)
        self.assertEqual(result, 2.5)
