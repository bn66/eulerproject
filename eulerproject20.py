"""
Euler Project Problem #20
Factorial Digit Sum
http://projecteuler.net/problem=20
"""
from math import factorial

def factorial_sum(number):
    """Returns the sum of the digits in the factorial of 'number'.
    Converts factorial to a string to break into digits, then back to
    integers to sum
    O(n)
    """
    answer = sum([int(a) for a in list(str(factorial(number)))])
    return answer
    
# tests
factorial_sum(10)
factorial_sum(100)