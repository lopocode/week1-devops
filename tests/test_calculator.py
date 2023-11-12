import unittest
from src.calculator import add, sub, mul, div  # Replace 'calculator_module' with the actual name of your Python file

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        assert add(1,1) == 0

    def test_sub(self):
        self.assertEqual(sub(4, 2), 2)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1, -1), 0)

    def test_mul(self):
        self.assertEqual(mul(3, 2), 6)
        self.assertEqual(mul(-1, 2), -2)
        self.assertEqual(mul(0, 10), 0)

    def test_div(self):
        self.assertEqual(div(8, 4), 2)
        self.assertEqual(div(9, 3), 3)
        self.assertRaises(ZeroDivisionError, div, 5, 0)

if __name__ == '__main__':
    unittest.main()
