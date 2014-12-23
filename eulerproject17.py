"""
Euler Project Problem #17
Power digit sum
http://projecteuler.net/problem=17
"""

def power_sum(a, n):
    """Lit
    """
    list = map(int, str(a ** n))
    ans = sum(list)
    print ans

# tests
# power_sum(2,1000)