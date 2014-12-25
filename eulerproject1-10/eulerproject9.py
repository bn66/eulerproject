"""
Euler Project Problem #9
Special Pythagorean Triplet
http://projecteuler.net/problem=9
"""

import eulerproject3

def pythagorean_triplet_product(abc_sum):
    """This function takes a number 'abc_sum' as an argument. It finds 
    set(s) of pythagorean triplets that add up to 'abc_sum'. It will
    also print the product of the three triplets.
    'a' is essentially a lower bound. 'b' is between.
    'c' is essentially an upper bound.
    O(n^2)
    """
    
    for a in range(1, int(abc_sum / 3)):  # Lower bound, a
        for b in range(a + 1, int((abc_sum - a) / 2 + 1)):  # between, b
            c = abc_sum - a - b
            if a ** 2 + b ** 2 == c ** 2:  # Is a pythagorean triplet
                answer = eulerproject3.product([a, b, c]) # product
                print """%d, %d, %d are a pythagorean triple. Their
                    product is %d.
                    """ % (a, b, c, answer)
                return True
            else:
                continue
    print "No answer"
    
def whole_test(number):
    """Tests if a number is a whole number. Returns True or False
    O(1)
    """
    if number % 1 == 0:
        return True # Is a whole number
    else:
        return False
    
    
    
# Tests
pythagorean_triplet_product(1000)

# output pythagorean triplets
# 