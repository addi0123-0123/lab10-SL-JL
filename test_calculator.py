import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(7, 3), 21)
        self.assertEqual(mul(0, 9), 0)
        self.assertAlmostEqual(mul(0.5, 7.2), 3.6)

    def test_divide(self): # 3 assertions
        self.assertAlmostEqual(div(6, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)
        self.assertAlmostEqual(div(1, 2), 0.5)
    ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(0, 5), 5)
        self.assertEqual(hypotenuse(6, 8), 10)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-16)
        self.assertAlmostEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(9), 3)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()