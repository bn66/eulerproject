"""
Euler Project Problem #3
Largest Prime Factor
http://projecteuler.net/problem=3
"""

def PrimeFactorization(number):
    """All numbers can be represenated by the product of primes.
    The answer to this problem will be the last entry of the output.
    The first divisible number will always be prime.
    O(n)
    """
    PrimeFactors = [] # initialize list
    i = 2 # start with a non trivial divisor
    while number > 1: # find other primes
        if number % i == 0: # found one
            PrimeFactors.append(i)
            number /= i # reduce by divisor
        else:
            i += 1 # let's keep trying
    if number == 1: # reduced as much as possible
        print PrimeFactors
        print "The greatest prime divisor is %d" % PrimeFactors[-1]
        
def product(list):
    """Returns the product of every item in a list
    O(n)
    """
    product = 1
    for i in list:
        product *= i
    return product
        
def product_reduce(list):
    """Returns the product of every item in a list. Uses reduce.
    O(n)
    """
    
    return reduce(lambda x, y: x * y, list)

# Tests
"""
# PrimeFactorization(600851475143)
# print Product([1, 2, 3, 4]) # test
"""