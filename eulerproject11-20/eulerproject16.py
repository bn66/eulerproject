"""
Euler Project Problem #16
Power digit sum
http://projecteuler.net/problem=16
"""

def power_sum(a, n):
    """Literal and straightforward solution for Problem #16. Prints
    sum of the digits of number 'a' to the 'n'th exponent. 
    O(n)
    """
    list = map(int, str(a ** n))
    ans = sum(list)
    print ans

# tests
power_sum(2,1000)