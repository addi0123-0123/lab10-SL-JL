# https://github.com/addi0123-0123/lab10-SL-JL.git
# Partner 1: Skylar Liu
# Partner 2: Jeffrey Li

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

# First example
def square_root(a):
    try:
        return math.sqrt(a)
    except:
        raise ValueError
    
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b
def logarithm(a, b):
    if b > 0 and b != 1 and a > 0:
        return math.log(b,a)
    raise ValueError
def exp(a, b):
    return a ** b