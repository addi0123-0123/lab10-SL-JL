import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3, True)
        self.assertEqual(add(1, -2), -1, True)
        self.assertEqual(add(1, 0), 1, True)
        self.assertEqual(add(0, 0), 0, True)
        self.assertEqual(add(0, 0), 1, False)
        self.assertEqual(add(-1, -1), -2, True)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(1, 2), 1, False)
        self.assertEqual(sub(2, 1), 1, True)
        self.assertEqual(sub(1, -2), -1, False)
        self.assertEqual(sub(1, 0), 0, False)
        self.assertEqual(sub(0, 0), 0, True)
        self.assertEqual(sub(0, 0), 1, False)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        self.assertRaises(div(0,5), ZeroDivisionError)
        self.assertRaises(div(5, 0), ZeroDivisionError)
        self.assertRaises(div(0, 0), ZeroDivisionError)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,8), 3, True)
        self.assertEqual(log(2, 8), 2, False)
        self.assertEqual(log(2, 16), 2, False)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertEqual(log(0, 16), ValueError)
        self.assertEqual(log(16, 0), ValueError)
        self.assertEqual(log(-2, 16), ValueError)
        self.assertEqual(log(2, -16), ValueError)
        self.assertEqual(log(2, 1), ValueError)
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()