"""
Euler Project Problem #21
-----------
http://projecteuler.net/problem=21
"""

from math import factorial

def factorial_sum(number):
    """Retu----
    O(n)
    """
    answer = sum([int(a) for a in list(str(factorial(number)))])
    return answer
    
# tests
factorial_sum(10)
factorial_sum(100)