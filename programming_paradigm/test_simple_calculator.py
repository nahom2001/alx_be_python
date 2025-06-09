from simple_calculator import SimpleCalculator    
import unittest


class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = SimpleCalculator.add(self, -2, 1)
        self.assertEqual(result, -1)

    def test_subtract(self):
        result = SimpleCalculator.subtract(self, -2, 1)
        self.assertEqual(result, -3)

    def test_multiply(self):
        result = SimpleCalculator.multiply(self, -2, -1)
        self.assertEqual(result, 2)

    def test_divide(self):
        result = SimpleCalculator.divide(self, 5, 2)
        self.assertEqual(result, 2.5)
