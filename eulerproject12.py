"""
Euler Project Problem #12
Highly divisible triangular number
http://projecteuler.net/problem=12
"""

import eulerproject3

def triangular_divisors(divisors):
    """The 'nth' triangular number is made by the summation of all
    natural numbers from 1 to 'nth'. This function will find the 'nth'
    triangular number with at least 'divisors' number of divisors.
    Triangular numbers can be calculated using summation formulas.
    O(n^1.5)
    """
    
    # nth prime
    i = 1
    
    # While the 'nth' prime has under the amount of divisors we want
    while len(factorize_half(i * (i + 1) / 2)) < divisors / 2:
        i += 1
    print """Triangular number %d is %d. This number has at least %d
            divisors.""" % (i, (i * (i + 1) / 2), divisors)
    
def factorize_half(number):
    """This function compiles the first half of factors for a given
    'number'. When it has reached the limit, it will return the half
    list of factors
    O(n^0.5)
    """
    
    # Initialize variables. Factors meet at the square root of a number.
    limit = number ** 0.5
    factors = [1]
    i = 2
    
    while i <= limit: # Division tests
        if number % i == 0:
            factors.append(i)
            i += 1
        elif number % i != 0:
            i += 1
    
    if i > limit:
        return factors
 
# Tests 
triangular_divisors(500)
    
# optimize factorization?