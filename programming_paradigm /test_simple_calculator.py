import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):
    """
    Test Cases for the Simple Calculator.
    """
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(5,5), 10)
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1,1), 0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,2), 3)
        self.assertEqual(self.calc.subtract(3,2), 1)
        self.assertEqual(self.calc.subtract(-1,1), -2)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,2), 10)
        self.assertEqual(self.calc.multiply(4,3), 12)
        self.assertEqual(self.calc.multiply(1,2), 2)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(5,5), 1)
        self.assertIsNone(self.calc.divide(10,0))

if __name__ == '__main__':
    unittest.main()

# if the main fuction Raised Zero Divison Error we do this:
    # with self.assertRaises(ZeroDivisionError):
    #     SimpleCalculator().divide(10,0)
    # or assert.assertraises(ZeroDivisionError,SimpleCalculator().divide, 10,0)
