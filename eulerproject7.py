"""
Euler Project Problem #7
10001st Prime
http://projecteuler.net/problem=7
"""
import eulerproject5
import math

def find_prime(nth):
    """This function builds a list of primes until the 'nth' prime is
    found. It uses eulerproject5.PrimeTest to test for primality. It
    works off the fact that, except 2 and 3, only numbers 6 +/- 1 need
    to be checked for primality. This was an effort to (simply) reduce
    calcuations.
    O(n^1.5)
    """
    PrimeList = [2, 3]  # Initialize first two primes
    i = 5
    j = 7
    while len(PrimeList) < nth:  # Loop until found
        if eulerproject5.PrimeTest(i):  # If it's a prime, add to list
            PrimeList.append(i)
        if eulerproject5.PrimeTest(j):  # If it's a prime, add to list
            PrimeList.append(j)
        i += 6
        j += 6
        

    print PrimeList[-1]

def find_prime_se(nth):
    """This function uses the Sieve of Eratosthenes to create a list
    of primes. In the end, the nth prime is printed with 'True'.
    At http://en.wikipedia.org/wiki/Prime_number_theorem , the amount of 
    primes under an 'x' amount of numbers are available. The line was 
    fit to a log-log plot and offset to over-estimate the upper bound.
    O(n^1.5)
    """
    
    # Initialize variables with linear approximation
    # y = 1.1022 * x + 1.5 for log-log plot. '1.5' can act as an offset
    upper_bound = int(math.exp(math.log(nth) * 1.1022 + 1.5))
    search_bound = int(upper_bound ** 0.5)  # Sieve limits
    
    # Sets were preferred because of O(1) search time
    full_list = set()  # Set of numbers for Sieve 
    multiples = set()  # Prevents overlap calcuations
    for i in xrange(2, upper_bound): 
        full_list.add(i)
    
    i = 2  # Number, will go until search_bound is reached
    j = 2  # Multiplier counter
    
    # Calculations
    while i < search_bound:
        while j * i < upper_bound:
            if j * i not in multiples:  # Check set
                multiples.add(j * i)
                full_list.discard(j * i)  # Sieving out
                j += 1
            else:
                j += 1
        if j * i >= upper_bound:
            j = 2  # Reset        
        i += 1
    
    # Get the answer
    answers = []
    for i in full_list:
        if len(answers) == nth:
            print answers[nth - 1]
            return True
        else:
            answers.append(i)

# time testing
import time    

tic = time.clock()    
find_prime_se(10001)
toc = time.clock()
print toc - tic

tic = time.clock()
find_prime(100001)
toc = time.clock()
print toc - tic