"""
Euler Project Problem #5
Smallest Multiple
http://projecteuler.net/problem=5
"""

def PrimeTest(number):
    """This function takes the Brute Force method for testing primes.
    It will return True or False.
    O(n)
    """
    # Initialize bounds. Factors meet at the square root of a number.
    limit = number ** 0.5
    i = 2
    if number == 1: # Exception
        print "One is special"
        return False
    while i <= limit: # Division tests
        if number % i == 0:
            return False
        elif number % i != 0:
            i += 1
    if i > limit:
        return True

def MultipleCalc(number):
    """This function calculates the lowest common multiple of numbers
    from 1 to 'number.'
    O(n^2)
    """
    answer = 1
    for i in range(1, number + 1):
        if answer % i == 0: # Already divisble
            continue
        elif PrimeTest(i): # Prime case
            answer *= i
        elif answer % i != 0: # All other cases
            answer *= i / (answer % i)
    print """The lowest number that is divisible by all numbers
    from 1 to %d is %d
    """ % (number, answer)