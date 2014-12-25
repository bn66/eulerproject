"""
Euler Project Problem #10
Summation of primes
http://projecteuler.net/problem=10
"""
import eulerproject5

def compile_primes(nth):
    """This function builds a list of primes under 'nth'.
    It uses eulerproject5.PrimeTest to test for primality. It
    works off the fact that, except 2 and 3, only numbers 6 +/- 1 need
    to be checked for primality. This was an effort to (simply) reduce
    calcuations.
    This function borrows heavily from the structure in eulerproject7.
    O(n^1.5)
    """
    PrimeList = [2, 3]  # Initialize first two primes
    i = 5
    j = 7
    # Loop until done
    while i < nth:
        if eulerproject5.PrimeTest(i):  # If it's a prime, add to list
            PrimeList.append(i)
        if eulerproject5.PrimeTest(j):  # If it's a prime, add to list
            PrimeList.append(j)
        i += 6
        j += 6
        
    answer = sum(PrimeList)
    print "The sum of all numbers under %d is %d" % (nth, answer)

def compile_primes_se(nth):
    """This function uses the Sieve of Eratosthenes to create a list
    of primes under 'nth'.
    This function borrows heavily from the structure in eulerproject7.
    O(n^1.5)
    """
    
    # Initialize variables
    upper_bound = int(nth)
    search_bound = int(upper_bound ** 0.5) + 1 # Sieve limits
    
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
    
    answer = sum(full_list)
    print "The sum of all numbers under %d is %d" % (nth, answer)

# time testing
import time    

tic = time.clock()    
compile_primes_se(2E6)
toc = time.clock()
print toc - tic

tic = time.clock()
compile_primes(2E6)
toc = time.clock()
print toc - tic