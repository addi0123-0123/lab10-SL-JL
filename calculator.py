"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a/b
def log(a, b):
    if b > 0 and b != 1 and a > 0:
        return math.log(b,a)
    raise ValueError
def exp(a, b):
    return a ** b

print(log(2,6))




