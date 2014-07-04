"""
Euler Project Problem #6
Sum Square Difference
http://projecteuler.net/problem=6
"""

def SumSquareDif(number):
    """Brute Force calculation of the difference of the sum of the
    squares of natural numbers and the square of the sum of natural
    numbers.
    O(n)
    """
    
    # Sum of the squares
    sum_square = []  
    for i in xrange(1, number + 1):
        sum_square.append(i*i)
    small = sum(sum_square)
    print small
    
    # Square the sum
    square_sum = []  
    large = 0
    for i in xrange(1, number + 1):
        large += i
    large *= large
    print large
    
    # Answer
    print large - small
    
def SumSquareDifSF(n):
    """Uses Summation Formulas for the calculation of the difference
    of the sum of the squares of natural numbers and the square of
    the sum of natural numbers.
    O(1)
    """
    
    # Sum of the squares
    small =  n*(n + 1)*(2*n + 1) / 6
    print small
    
    # Square the sum
    large = n * (n + 1) / 2
    large *= large
    print large
    
    # Answer
    print large - small
    
    
SumSquareDifSF(100)
